"""User serializers."""
# Django
from django.contrib.auth import authenticate

# Django rest framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Models
from users.models.users import User

class UserModelSerializer(serializers.ModelSerializer): 
    """User model serializer."""

    class Meta:
        """Meta class."""
        #definir atributos del serializer
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )


class UserSignUpModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Passwords must match.')
        if len(data['password']) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long.')
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        user = User.objects.create_user(**validated_data) 
        return user

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password', 'password_confirmation',
            'first_name', 'last_name',
        )


class UserUpdatePasswordModelSerializer(serializers.ModelSerializer):
    email  = serializers.CharField()
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Passwords must match.')
        if len(data['password']) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long.')
        return data

    def update(self, instance, validated_data):
        validated_data.pop('password_confirmation')
        password = validated_data['password']
        email = validated_data['email']
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = (
             'email', 'password', 'password_confirmation'
        )

class UserLoginSerializer(serializers.Serializer):
    """
    User login serializer.
    Handle the login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    # validar
    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials.')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
