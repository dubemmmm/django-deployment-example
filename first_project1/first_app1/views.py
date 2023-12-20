from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from first_app1.forms import Userform, Userprofileform
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'first_app1/index.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = Userform(data=request.POST)
        profile_form = Userprofileform(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors)
            print(profile_form.errors)
    else:
        user_form = Userform()
        profile_form = Userprofileform()
    return render(request, 'first_app1/registration.html', {'user_form': user_form, 'profile_form': profile_form,'registered': registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app1:index'))

def homepage(request):
    return render(request, 'first_app1/homepage.html')


def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('first_app1:homepage'))
            else:
                return HttpResponse('Your account is inactive. Please contact admin.')
        else:
            return HttpResponse('Invalid username or password.')
    else:
        return render(request, 'first_app1/login.html',{})
    
          
    
