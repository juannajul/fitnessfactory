"""Courses views."""

# Django rest framework
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Serializers
from courses.serializers.memberships import MembershipModelSerializer, CreateMembershipModelSerializer

# Models 
from courses.models.memberships import Membership

# Permissions
from rest_framework.permissions import IsAuthenticated

# Pagination

class MembershipViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """Courses membership view set"""

    queryset = Membership.objects.all()
    serializer_class = MembershipModelSerializer
    #lookup_field = 'slug'

    def get_serializer_class(self):
        """Return serializer based on actions"""
        if self.action == 'create':
            return CreateMembershipModelSerializer
        return MembershipModelSerializer
    
    def get_permissions(self):
        """Assing permissions based on action."""
        permissions = []
        if self.action == 'create':
            permissions.append(IsAuthenticated)
        return [p() for p in permissions]
    
    # def get_queryset(self):
    #     """Return circle members."""
    #     return Membership.objects.filter(
    #         is_active=True
    #     )
    
    # def get_object(self):
    #     """Return de circle member by using the user username"""
    #     #debugger import pdb; pdb.set_trace()
    #     return get_object_or_404(
    #         Membership,
    #         user__username=self.kwargs['pk'],
    #         circle=self.circle,
    #         is_active=True
    #     )
