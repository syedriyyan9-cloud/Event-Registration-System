from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def registration(request):
    '''registers the user'''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login()
            return redirect('users:login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html',{'form':form})

@login_required
def profile(request):
    '''load user profile'''
    return render(request, 'users/profile.html', {'user':request.user})