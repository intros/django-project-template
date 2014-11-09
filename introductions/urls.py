# urls.py
from django.conf.urls import url, include
from introductions.views import (
    IntroductionView,
    IntroductionCreateView,
    IntroductionDetailView,
    IntroductionListView,
    IntroductionUpdateView,

    IntroductionEmailCreateView,
    IntroductionEmailDetailView,
    IntroductionEmailListView,
    IntroductionEmailUpdateView,

    IntroductionReminderCreateView,
    IntroductionReminderDetailView,
    IntroductionReminderListView,

    PersonCreateView,
    PersonDetailView,
    PersonListView,

    PersonUpdateView,
    PersonEmailCreateView,
    PersonEmailDetailView,
    PersonEmailListView,
    PersonEmailUpdateView,
    
    MailboxListView,
    MailboxDetailView,
    MailboxUpdateView,
    MailboxCreateView
)

urlpatterns = [
    url(r'^$', IntroductionView.as_view(), name="home"),
    url(r'^introduction/$', IntroductionCreateView.as_view(), name="introduction_create"),
    url(r'^introduction/(?P<pk>[0-9]+)/$', IntroductionDetailView.as_view(), name="introduction_detail"),
    url(r'^introductions/$', IntroductionListView.as_view(), name="introduction_list"),
    url(r'^introduction/(?P<pk>[0-9]+)/update/$', IntroductionUpdateView.as_view(), name="introduction_update"),
    url(r'^introduction_email/$', IntroductionEmailCreateView.as_view(), name="introduction_email_create"),
    url(r'^introduction_email/(?P<pk>[0-9]+)/$', IntroductionEmailDetailView.as_view(), name="introduction_email_detail"),
    url(r'^introduction_emails/$', IntroductionEmailListView.as_view(), name="introduction_email_list"),
    url(r'^introduction_email/(?P<pk>[0-9]+)/update/$', IntroductionEmailUpdateView.as_view(), name="introduction_email_update"),
    url(r'^introduction_reminder/$', IntroductionReminderCreateView.as_view(), name="introduction_reminder_create"),
    url(r'^introduction_reminder/(?P<pk>[0-9]+)/$', IntroductionReminderDetailView.as_view(), name="introduction_reminder_detail"),
    url(r'^introduction_reminders/$', IntroductionReminderListView.as_view(), name="introduction_reminder_list"),
    url(r'^person/$', PersonCreateView.as_view(), name="person_create"),
    url(r'^person/(?P<pk>[0-9]+)/$', PersonDetailView.as_view(), name="person_detail"),
    url(r'^persons/$', PersonListView.as_view(), name="person_list"),
    url(r'^person/(?P<pk>[0-9]+)/update/$', PersonUpdateView.as_view(), name="person_update"),
    url(r'^person_email/$', PersonEmailCreateView.as_view(), name="person_email_create"),
    url(r'^person_email/(?P<pk>[0-9]+)/$', PersonEmailDetailView.as_view(), name="person_email_detail"),
    url(r'^person_emails/$', PersonEmailListView.as_view(), name="person_email_list"),
    url(r'^person_email/(?P<pk>[0-9]+)/update/$', PersonEmailUpdateView.as_view(), name="person_email_update"),
    url(r'^mailbox/$', MailboxCreateView.as_view(), name="mailbox_create"),
    url(r'^mailbox/(?P<pk>[0-9]+)/$', MailboxDetailView.as_view(), name="mailbox_detail"),
    url(r'^mailboxs/$', MailboxListView.as_view(), name="mailbox_list"),
    url(r'^mailbox/(?P<pk>[0-9]+)/update/$', MailboxUpdateView.as_view(), name="mailbox_update"),
    url(r'', include('social.apps.django_app.urls', namespace='social'))
]
