from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user_login(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
			if user is not None:
				login(request, user)
				messages.success(request, 'you logged in successfully', 'success')
				return redirect('shop:home')
			else:
				messages.error(request, 'username or password is wrong', 'danger')
	else:
		form = UserLoginForm()
	return render(request, 'accounts/login.html', {'form':form})


def user_logout(request):
	logout(request)
	messages.success(request, 'you logged out successfully', 'success')
	return redirect('shop:home')

@csrf_exempt
def user_register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.save()
			login(request, user)
			messages.success(request, 'you registered successfully', 'success')
			return redirect('shop:home')
	else:
		form = UserRegistrationForm()
	return render(request, 'accounts/register.html', {'form':form})