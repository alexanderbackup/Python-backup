from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from basicauth.decorators.validators import is_logged
from basicauth.forms import Login, RegisterForm

# Create your views here.
@csrf_exempt
def login(request):
    
    if request.method == 'GET':
        _log = Login()
        return render(request, 'login.html', {'login_form': _log})

    if request.method == 'POST':
        _log_post = Login(request.POST)
        if _log_post.is_valid():
            request.session['username'] = _log_post.cleaned_data.get('username')
        return redirect(profile)
    return HttpResponse('Not POST request')

test_login = login


@is_logged
def profile(request):
    if request.method == 'GET':
        email = request.session.get('username', None)
        if email:
            return render(request, 'profile.html', locals())
    return redirect(login)


@is_logged
def logout(request):
    if request.method == 'GET':
        print('test')
        request.session.delete()
    return redirect(login)


def registration(request):
    
    if request.method == 'GET':
        reg_get = RegisterForm()
        return render(request, 'registration.html', {'reg_form': reg_get})

    if request.method == 'POST':
        reg_post = RegisterForm(request.POST)
        if reg_post.is_valid():
            reg_post.save(commit=True)
            request.session['username'] = reg_post.cleaned_data.get('email')
            return redirect(profile)
        return redirect(registration)
    return HttpResponse('Not POST request')






