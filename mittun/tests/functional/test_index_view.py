# -*- coding: utf-8 -*-

from datetime import date

from django.test import TestCase
from django.test.client import RequestFactory

from events.views import EventsListView
from events.models import Event


class EventsIndexViewTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('index')
        self.event = Event.objects.create(
            name= 'Dojo',
            description= 'Dojo',
            date= date.today(),
            location= 'location',
            address= 'address'
        )

    def tearDown(self):
        self.event.delete()

    def test_should_get_the_index_and_get_a_200_status_code(self):
        response = EventsListView.as_view()(self.request)
        self.assertEqual(response.status_code, 200)

    def test_index_view_should_use_index_template(self):
        response = EventsListView.as_view()(self.request)
        self.assertTrue('index.html' in response.template_name)

    def test_index_must_be_called_event_in_context(self):
        response = EventsListView.as_view()(self.request)
        self.assertTrue('event' in response.context_data)