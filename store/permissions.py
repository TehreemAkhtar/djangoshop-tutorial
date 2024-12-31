from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS, DjangoModelPermissions


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return IsAdminUser().has_permission(request, view)


class FullDjangoModelPermissions(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']


class ViewCustomerHistory(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('store.view_history')