from django.db import models
from projects.models import Project
from users.models import CustomUser

class Report(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="reports")
    generated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="reports")
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    report_file = models.FileField(upload_to="reports/", blank=True, null=True)

    def __str__(self):
        return self.title
