import json
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import Task


class TaskTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        user_class = get_user_model()
        cls.user = user_class.objects.create(username="john", email="foo@bar.com")
        cls.token = Token.objects.create(user=cls.user)
        cls.task = Task.objects.create(
            title="My Task", description="My task description", status= "DELAYED", deadline="2025-08-12",priority="2", user=cls.user
        )

    @classmethod
    def tearDownClass(cls):
        cls.task.delete()
        cls.token.delete()
        cls.user.delete()

    def setUp(self):
        self.client.force_authenticate(user=self.user, token=self.token)

    def test_get_task_list(self):
        url = reverse("task-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 1)

    def test_get_task_detail(self):
        url = reverse("task-detail", kwargs={"pk": self.task.id})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("title"), self.task.title)
        
    def test_patch_task(self):
        data = {"status": "En progreso"}
        url = reverse("task-detail", kwargs={"pk": self.task.id})
        response = self.client.patch(url, data=json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_task = Task.objects.get(pk=self.task.id)
        self.assertEqual(updated_task.status, "Terminado")

    def test_delete_task(self):
        url = reverse("task-detail", kwargs={"pk":self.task.id})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
