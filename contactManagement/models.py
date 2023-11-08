from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Name must be unique
    email = models.EmailField(unique=True)  # Email must be unique and a valid email address
    created_time = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name  # This is optional, it's just for a human-readable representation in the admin interface

    class Meta:
        ordering = ['name']