import random
import string

from django.conf import settings
from django.db import models
from django.dispatch import receiver

from django_mailbox.models import Message
from django_mailbox.signals import message_received

from email_reply_parser import EmailReplyParser

from taggit.managers import TaggableManager
#http://alexgaynor.net/2010/may/04/cool-new-django-taggit-api/
from taggit.models import TaggedItemBase

from .custom_fields import NullableCharField
from .email_helpers import  get_delivered_to_addr, get_from_addr, get_to_addrs, get_all_recipients, is_fwd



def gen_short_id():
    length=8
    output = u''
    while len(output) < length:
        output = u"%s%s" % (output, random.choice(string.ascii_letters))
    return output

class Person(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    preferred_email_address = models.EmailField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        if self.user:
            return unicode(self.user)
        return self.preferred_email_address


class PersonEmail(models.Model):
    person = models.ForeignKey(Person)
    email_address = models.EmailField(unique=True)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    extracted_name = models.CharField(max_length=128, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.email_address

    @property
    def printable_name(self):
        if self.first_name and self.last_name:
            return u'%s %s' % (self.first_name, self.last_name)
        if self.extracted_name:
            return self.extracted_name
        return self.email_address


class PersonComment(models.Model):
    person = models.ForeignKey(Person, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(Person)
    comment = models.TextField()
    parent_comment = models.ForeignKey('self',blank=True,null=True,related_name="child_comment_set")

    def __unicode__(self):
        return "Comment about %s recorded on %s" % (self.person, self.created)

#http://alexgaynor.net/2010/may/04/cool-new-django-taggit-api/
class TaggedIntroduction(TaggedItemBase):
    content_object = models.ForeignKey('Introduction')


class Introduction(models.Model):
    email_alias = models.SlugField(max_length=16, unique=True, default=gen_short_id)
    person = models.ForeignKey(Person)
    created = models.DateTimeField(auto_now_add=True)
    from_addr = models.EmailField(verbose_name="Who made this intro? (your email or another person's if this was an intro you received)", null=True, blank=True)
    delivered_to = models.EmailField(null=True, blank=True)
    to_addrs = NullableCharField(max_length=255, null=True, blank=True)
    cc_addrs = NullableCharField(max_length=255, null=True, blank=True)
    subject = NullableCharField(max_length=128, null=True, blank=True)
    message = models.TextField(verbose_name = "Intro Details")
    introduction_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="When did you make this intro?"
        )
    sequence = models.IntegerField(default=None, null=True)
    introducees = models.ManyToManyField(PersonEmail)
    mailbox_message = models.OneToOneField(Message, null=True)

    #http://alexgaynor.net/2010/may/04/cool-new-django-taggit-api/
    tags = TaggableManager(through=TaggedIntroduction)

    def __unicode__(self):
        return "Introduction by %s recorded on %s" % (self.person, self.created)

class IntroductionEmail(models.Model):
    introduction = models.ForeignKey(Introduction)
    email = models.ForeignKey(Message)


class IntroductionComment(models.Model):
    person = models.ForeignKey(Person)
    created = models.DateTimeField(auto_now_add=True)
    introduction = models.ForeignKey(Introduction)
    comment = models.TextField()
    parent_comment = models.ForeignKey('self',blank=True,null=True,related_name="child_comment_set")

    def __unicode__(self):
        return "Introduction comment by %s recorded on %s" % (self.person, self.created)


class IntroductionReminder(models.Model):
    person = models.ForeignKey(Person)
    created = models.DateTimeField(auto_now_add=True)
    introduction = models.ForeignKey(Introduction)
    comment = models.TextField()
    parent_reminder = models.ForeignKey('self',blank=True,null=True,related_name="child_reminder_set")
    requested = models.DateTimeField(null=True, blank=True)
    sent = models.BooleanField(default=True)
    ignore = models.BooleanField(default=True)

    def __unicode__(self):
        return "Introduction reminder by %s scheduled for %s" % (self.person, self.requested)


def process_message_as_follow_up(message):
    # this is a little tricky.  Any message that can be dealt with as a
    # follow-up needs to fit a set of criteria
    # * delivered_to must include the email alias
    # * it should be a reply and not a forward
    # * it shouldn't contain addressees not included in the initial intro
    msg = message.get_email_object()
    delivered_to = get_delivered_to_addr(msg)

    # Is this message part of a chain?
    references = msg.get_all('references', [])
    if len(references) < 1:
        raise Introduction.DoesNotExist('Message %s has no references and is therefore not a followup')

    # TODO: figure out how to store a coherent set of sent/received msg-ids for querying here
    # Which message is it a reply to?
    # We should be able to look this up in the db and see if it is a thread
    # reply_to = msg.get('in-reply-to', None)


    # Is this message a forward?
    if is_fwd(msg):
        raise Introduction.DoesNotExist('Message %s is a forward and probably not followup')

    try:
        email_alias=delivered_to.split("@")[0].split("+")[1]
    except IndexError:
        raise Introduction.DoesNotExist("%s does not appear to represent an existing introduction. Message: %s" % (delivered_to, message.pk))
    # This will raise a DoesNotExist message
    intro = Introduction.objects.get(email_alias=email_alias)
    # If the sender is the user that owns the intro, add it as a comment
    person = PersonEmail.objects.get(msg.get("from").lower().lstrip().rstrip()).person
    if person == intro.person:
        new_comment = IntroductionComment(
            person = person,
            introduction = intro,
            comment = EmailReplyParser.parse_reply(message.text)
        )
        new_comment.save()
    return intro

def process_message_as_new_intro(message):
    msg = message.get_email_object()
    from_addr = get_from_addr(msg)
    delivered_to = get_delivered_to_addr(msg)
    to_addrs = ','.join(get_to_addrs(msg))
    cc_addrs = ','.join(get_to_addrs(msg))
    try:
        person = PersonEmail.objects.get(email_address=from_addr).person
    except PersonEmail.DoesNotExist:
        raise Introduction.DoesNotExist("from address: %s doesn't represent a person in our system.  Message: %s" % (from_addr, message.pk))
    intro = Introduction(person=person,
                        from_addr=from_addr,
                        delivered_to = delivered_to,
                        to_addrs = to_addrs,
                        cc_addrs = cc_addrs,
                        subject = message.subject,
                        message = message.text,
                        mailbox_message = message
                        )
    for name, addr in get_all_recipients(msg):
        if name != '':
            person_email = PersonEmail.objects.get_or_create(
                email_address=addr.lower().lstrip().rstrip(),
            )
        else:
            person_email = PersonEmail.objects.get_or_create(
                email_address=addr.lower().lstrip().rstrip(),
                extracted_name=name
            )
        intro.introducees.add(person_email)
    intro.save()
    return intro


@receiver(message_received)
def process_message(sender, message, **args):
    try:
        intro = process_message_as_follow_up(message)
        print "Processed an introduction followup from %s on intro: %s" % (message.from_header, intro.pk)
    except Introduction.DoesNotExist:
        intro = process_message_as_new_intro(message)
        print "Created an introduction from %s on intro: %s" % (message.from_header, intro.pk)
