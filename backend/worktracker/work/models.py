from django.db import models

class User(models.Model):
    ROLE_CHOICES = [('admin','admin'), ('member','member')]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    skills = models.JSONField(default=list)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='blocked')

class Dependency(models.Model):
    predecessor = models.ForeignKey(Task, related_name='pre', on_delete=models.CASCADE)
    successor = models.ForeignKey(Task, related_name='suc', on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    threshold = models.IntegerField()

