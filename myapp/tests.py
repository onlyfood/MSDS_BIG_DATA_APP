from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse

class MyappViewTest(TestCase):
    def test_myapp_view(self):
        response = self.client.get(reverse('myapp'))
        self.assertEqual(response.status_code, 200)

from django.test import TestCase
from django.urls import reverse
from .models import Message

class IntegrationTest(TestCase):

    def test_message_creation_and_display(self):
        # Ensure that there are no messages at the beginning
        self.assertEqual(Message.objects.count(), 0)

        # Post data through the view
        response = self.client.post(reverse('myapp'), {'message': 'Hello, World!'})

        # Ensure that one message was created
        self.assertEqual(Message.objects.count(), 1)

        # Ensure that the message content is correct
        message = Message.objects.first()
        self.assertEqual(message.content, 'Hello, World!')

        # Ensure that the response contains the message
        self.assertContains(response, 'Hello, World!')
