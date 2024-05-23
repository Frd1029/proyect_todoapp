from django.db import models
from django.contrib.auth.models import User

STATUS_OPTIONS = {
    "COMPLETED": "COMPLETED",
    "PENDING": "PENDING",
    "DELAYED": "DELAYED",
}

# Create your models here.
class Task(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_OPTIONS, default="PENDING")
    deadline = models.DateField()
    priority = models.PositiveSmallIntegerField(default=0);
    user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        limit_choices_to={"is_superuser": False},
        related_name="tasks",
        null=True,
    )
    
    def __str__(self):
        return self.title
