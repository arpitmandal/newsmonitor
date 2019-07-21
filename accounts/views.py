from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm, LogInForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.template import loader

def user_new(request):
    p= SignUpForm(request.POST or None)
    if p.is_valid():
        p.save()
        messages.success(request,'Registration Successfull')
        return HttpResponseRedirect('http://localhost:8000')
    context= {'form':p}
    return render(request, 'accounts/signup.html', context)

def login(request):
    form = LogInForm(request.POST or None)
    if form.is_valid():
       username = form.username
       password=str(form.cleaned_data['password'])
       user = authenticate(username=username, password=password)
       user.backend='django.contrib.auth.backends.ModelBackend'
       if user is not None:
           login(request, user)
           return HttpResponseRedirect('http://localhost:8000/source')
    return render(request, 'accounts/login.html', {'form': form})

def homepage(request):
    #template = loader.get_template('home.html')
    return render(request, 'accounts/home.html')


'''def login(self,request):
    form = LogInForm(request.POST or None)
    if form.is_valid():
        #text=form.cleaned_data['post']
        username = form.cleaned_data.get("Username")
        password = form.cleaned_data.get("Password")

        user = authenticate(username=username, password=password)
        if not user:
            raise form.ValidationError("This user does not exist")
            return render(request,self.signin.html)
        else:
            return render(request,self.signin.html)
    else:
        return render(request, 'accounts/login.html')'''