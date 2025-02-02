from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import logout

User = settings.AUTH_USER_MODEL

# Create your views here.
def register_views(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        print("User registred successfully")
        if form.is_valid() :
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, Your account was created successfully.")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect("store:index")
    else:
        form = UserRegisterForm()
    
    context = {
        'form' : form
    }
    
    return render(request,"userauths/sign-up.html", context)


def login_views(request):
    if request.user.is_authenticated:
        messages.warning(request, "Hey you are already Logged In.")
        return redirect("store:index")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
        except :
            messages.warning(request, f"User with email {email} doesn't exist")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in.")
            return redirect("store:index")
        else:
            messages.warning(request, "Invalid credentials. Please try again.")
            
    context = {
       
    }       
    return render(request,"userauths/sign-in.html", context)

def logout_views(request):
    logout(request)
    messages.success(request, "You logged out.")
    return redirect("userauths:sign-in")
