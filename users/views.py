from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
	# this function shows the registration page to the users
	if request.method != 'POST':
		# check the type
		form = UserCreationForm()
	else:
		# process the data
		form = UserCreationForm(data=request.POST)
		# check for validation and responding
		if form.is_valid():
			new_user = form.save()
			login(request, new_user)
			return redirect('learning_logs:index')	
	context = {'form': form}
	return render(request, 'registration/register.html', context)		
