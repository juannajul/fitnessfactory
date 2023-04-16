"""Courses serializers. """

# Django restframework
from rest_framework import serializers

# Utilities
from datetime import timedelta
from django.utils import timezone
import datetime
import pytz

# Django

# Models
from courses.models.memberships import Membership

# Serializers
from users.serializers.users import UserModelSerializer

class MembershipModelSerializer(serializers.ModelSerializer):
    """Membership model serializer."""
    user = UserModelSerializer(read_only=True)
    class Meta:
        model = Membership
        fields = '__all__'
        

class CreateMembershipModelSerializer(serializers.ModelSerializer):
    """Membershu\ip create model serializer."""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    membership_days = serializers.IntegerField()
    class Meta:
        model = Membership
        fields = ('membership_days', 'user')
  
    # def validate(self, data):
    #     """Validate if de slug already exists. If exists modificate."""
    
    def create(self, data):
        """Create membership."""
        start_date = timezone.now()
        finish_date = start_date + timedelta(days=data['membership_days'])
        print(f'start_day: {start_date}')
        print(f'finish_day: {finish_date}')
        now = timezone.now()
        print(now)
        print(now > finish_date)
        print(datetime.datetime.now())
        print(timezone.activate(pytz.timezone('America/Caracas')))
        membership = Membership.objects.create(
            **data, 
            start_date=start_date,
            finish_date=finish_date
            )
        membership.save()

        return membership