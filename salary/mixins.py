from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin

from account.models import CustomUser

class RecruiterPermissionMixin(AccessMixin):
    """ Verify if the current user is a recruiter. """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            if not request.user.is_recruiter:
                return redirect('salary:job_board_page')
        return super().dispatch(request, *args, **kwargs)