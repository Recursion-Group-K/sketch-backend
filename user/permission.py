from rest_framework import permissions

class UserObjPersmission(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    create_methods = ("POST")
    edit_methods = ("PUT", "PATCH")
    delete_method = ("DELETE")

    def has_object_permission(self, request, view, obj):
      isAdmin = request.user.is_staff & request.user.is_superuser
      isTheUser = request.params.id == request.user.id

      # GET True if authorized
      if request.method in permissions.SAFE_METHODS:
        return True

      # POST True if isAdmin
      if isAdmin & request.method in self.create_methods:
        return True

      # PUT, PATCH True if isTheUser
      if isTheUser & request.method in self.edit_methods:
        return True

      # DELETE True if isAdmin or isTheUser
      if isAdmin | isTheUser & request.method in self.delete_method:
        return True

      return False