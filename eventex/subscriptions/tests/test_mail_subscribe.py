from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Kennedi Malheiros', cpf='12345678945',
                    email='kennedimalheiros@gmail.com', phone='38-99157-3613')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expext = 'Confirmação de inscrição'

        self.assertEqual(expext, self.email.subject)

    def test_subscription_email_from(self):
        expext = 'appagendamoc@gmail.com'

        self.assertEqual(expext, self.email.from_email)

    def test_subscription_email_to(self):
        expext = ['appagendamoc@gmail.com', 'kennedimalheiros@gmail.com']

        self.assertEqual(expext, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Kennedi Malheiros',
            '12345678945',
            'kennedimalheiros@gmail.com',
            '38-99157-3613',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

