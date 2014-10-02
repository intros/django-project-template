from django.test import TestCase

from django_mailbox.models import Message
from .models import Person, PersonEmail, Introduction, IntroductionComment, process_message

class ProcessMessage(TestCase):
    fixtures = ['test1.json']
    
    def setUp(self):
        personEmail = PersonEmail.objects.create(email_address='bayuadji@gmail.com',
                                                 person=Person.objects.latest('id'))
    def test_process_intro(self):
        messages = Message.objects.all()
        
        for msg in messages:
            process_message(None, msg)
        
        self.assertEqual(1, Introduction.objects.all().count())
        self.assertEqual(1, IntroductionComment.objects.all().count())
        
