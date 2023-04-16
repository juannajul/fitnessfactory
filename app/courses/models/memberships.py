"""Courses membership model."""

from django.db import models

# Models
from users.models.users import User

class Membership(models.Model):
    """Courses membership model."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_membership')
    is_membership_active = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='start membership date', blank=True, null=True)
    finish_date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='finish membership date', blank=True, null=True)
    membership_days = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user} {self.is_membership_active}'
    
    class Meta:
        verbose_name_plural = "Memberships"
        ordering = ["start_date"]

