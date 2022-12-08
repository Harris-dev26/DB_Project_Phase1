from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

def login_user(request):
    
    if request.method == "POST":

        searched = request.POST['searched']
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            
            if searched == "Local" or searched == "local":
                return redirect('home_local')

            if searched == "Tourist" or searched == "tourist":
                return redirect('home_tourist')

            if searched == "Hotel" or searched == "hotel":
                return redirect('home_hotel')
            

        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))	
            return redirect('login')	


    else:
	        return render(request, 'authentication/login.html', {})


def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('home')


def register_user(request):
    if request.method == "POST":
        searched = request.POST['searched']
        form = RegisterUserForm(request.POST)

        if form.is_valid():

            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))

            if searched == "Local" or searched == "local":
                return redirect('home_local')

            if searched == "Tourist" or searched == "tourist":
                return redirect('home_tourist')

            if searched == "Hotel" or searched == "hotel":
                return redirect('home_hotel')
            
    
    else:
        
        form = RegisterUserForm()

    return render(request, 'authentication/register_user.html', {
        'form':form,
    })