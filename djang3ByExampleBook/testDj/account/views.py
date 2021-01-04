from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # authenticate() checks user credentials and returns a User object if they are correct;
            user = authenticate(req,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    # login() sets the user in the current session.
                    login(req, user)
                    return HttpResponse('Authenticated successfully.')
                else:
                    return HttpResponse('Account disabled.')

        else:
            return HttpResponse('Invalid login.')

    else:
        form = LoginForm()

    return render(req, 'account/login.html', {'form': form})
