"""Memberships models."""
from django.db import models
from users.models.users import User


class Membership(models.Model):
    """User model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_membership')
    is_membership_active = models.BooleanField(default=False)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    membreship_days = models.IntegerField(default=0)

    def __str__(self):
        return self.is_membership_active
    
    class Meta:
        verbose_name_plural = "Memberships"
        ordering = ["-start_date"]
      
