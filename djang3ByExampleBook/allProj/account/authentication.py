from django.contrib.auth.models import User

class EmailAuthBackend(object):
    """Authenticate user using email address"""

    # An authentication backend is a class that provides the following two methods:
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if  user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try :
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None