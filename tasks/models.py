from django.db import models
from users.models import CustomUser
from projects.models import Project

STATUS_CHOICES = [
    ("todo", "To Do"),
    ("in_progress", "In Progress"),
    ("done", "Done"),
]

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks") #FK1
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="tasks") #FK2
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
