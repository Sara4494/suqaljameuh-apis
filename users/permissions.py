from rest_framework import permissions


class IsUserProfile (permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class UserActive(permissions.BasePermission):
    """
    This permission ensures that the user isn't suspended and his account is verified, this is must be set
    to some views that are only executable for only sort of users (such as subscribing in a membership or chatting)
    """

    def has_permission(self, request, view):
        user = request.user
        if user.is_superuser == True and user.verified == True:
            return True

        if user.is_suspended == False and user.verified == True:
            return True

        return False


class UserOwnerOnly(permissions.BasePermission):
    """
    This permission ensures that the user isn't suspended and his account is verified, this is must be set
    to some views that are only executable for only sort of users (such as subscribing in a membership or chatting)
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
