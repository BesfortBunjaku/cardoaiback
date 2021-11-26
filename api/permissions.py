from rest_framework import permissions


class InvestorAndAnalystPermissions(permissions.BasePermission):

    def is_investor(self, request):
        if request.user.groups.filter(name='Investor').exists() and request.user.is_authenticated:
            return True
        return False
    
    def is_analyst(self, request):
        if request.user.groups.filter(name='Analyst').exists() and request.user.is_authenticated:
            return True
        return False

    def has_permission(self, request, view):
        if self.is_investor(request=request):
            return True

        if self.is_analyst(request=request) and request.method in ['GET']:
            return True


    