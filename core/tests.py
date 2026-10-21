from django.test import TestCase
from django.urls import reverse
from .models import Task


class TaskTests(TestCase):
    def test_task_str(self):
        task = Task.objects.create(title="Buy milk")
        self.assertEqual(str(task), "Buy milk")

    def test_list_page_loads(self):
        response = self.client.get(reverse("task_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Task Manager")

    def test_add_task(self):
        self.client.post(reverse("task_list"), {"title": "Write report"})
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, "Write report")

    def test_empty_title_is_not_added(self):
        self.client.post(reverse("task_list"), {"title": "   "})
        self.assertEqual(Task.objects.count(), 0)

    def test_toggle_task(self):
        task = Task.objects.create(title="Test")
        self.client.post(reverse("toggle_task", args=[task.pk]))
        task.refresh_from_db()
        self.assertTrue(task.completed)

    def test_delete_task(self):
        task = Task.objects.create(title="Test")
        self.client.post(reverse("delete_task", args=[task.pk]))
        self.assertEqual(Task.objects.count(), 0)