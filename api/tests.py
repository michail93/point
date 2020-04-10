import json
import uuid

from django.test import TestCase
from django.urls import reverse

from .models import Abonent


class PingViewTestCase(TestCase):
    def test_ping(self):
        url = reverse('api:ping')

        response = self.client.get(url)

        assert response.status_code == 200


class BaseTestCase(TestCase):
    def setUp(self):
        uid = uuid.UUID('867f0924-a917-4711-939b-90b179a96392')

        self.abonent = Abonent.objects.create(ab_uuid=uid, full_name="Bob Smith", balance=123.46, hold=20.394,
                                              status=True)

        self.request_data = {'uuid': str(self.abonent.ab_uuid)}


class StatusViewTestCase(BaseTestCase):
    def test_status_view(self):
        url = reverse('api:status')

        response = self.client.post(url, data=json.dumps(self.request_data), content_type="application/json")

        assert response.status_code == 200


class BalanceRefillViewTestCase(BaseTestCase):
    def test_balance_refill(self):
        url = reverse('api:balance_refill')

        self.request_data.update({'amount': '10.53'})

        response = self.client.post(url, data=json.dumps(self.request_data), content_type="application/json")

        assert response.status_code == 200


class DecreasingBalanceViewTestCase(BaseTestCase):
    def test_decrease_balance(self):
        url = reverse('api:balance_decreasing')

        self.request_data.update({'amount': '7'})

        response = self.client.post(url, data=json.dumps(self.request_data), content_type="application/json")

        assert response.status_code == 200
