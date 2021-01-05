from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_actve:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Account disabled')

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


# want to : if the provided email doesn't match a user in db, tell user about it
class PwdResetView(PasswordResetView):
    class ResetForm(PasswordResetForm):
        def save(self, domain_override=None,
                 subject_template_name='registration/password_reset_subject.txt',
                 email_template_name='registration/password_reset_email.html',
                 use_https=False, token_generator=default_token_generator,
                 from_email=None, request=None, html_email_template_name=None,
                 extra_email_context=None):
            email = self.cleaned_data["email"]
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            from django.contrib.auth import get_user_model
            UserModel = get_user_model()
            email_field_name = UserModel.get_email_field_name()
            users = self.get_users(email)

            if len(users) < 1:

                pass

            for user in users:

                user_email = getattr(user, email_field_name)
                context = {
                    'email': user_email,
                    'domain': domain,
                    'site_name': site_name,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': token_generator.make_token(user),
                    'protocol': 'https' if use_https else 'http',
                    **(extra_email_context or {}),
                }
                self.send_mail(
                    subject_template_name, email_template_name, context, from_email,
                    user_email, html_email_template_name=html_email_template_name,
                )

    form_class = ResetForm
