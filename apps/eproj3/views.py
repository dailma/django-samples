from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User  #  TODO: and any other models

# rendering functions
def index(request):
	context = {"items": ["Item 1", "Item 2"] }
	return render(request, "eproj3/index.html", context)

def signin(request):
	return render(request, "eproj3/signin.html")

# redirecting functions
def register(request):
	if request.method == "POST":
		result_success, result_obj = User.userManager.create_user()  #  TODO: add arguments
		if not result_success:
			for msg in result_obj:
				messages.add_message(request, messages.ERROR, msg, extra_tags="reg")
			return redirect(reverse("eproj3_signin"))
		pass  #  TODO: stuff like request.session and redirect

def login(request):
	if request.method == "POST":
		result_success, result_obj = User.userManager.login()  #  TODO: add arguments
		if not result_success:
			for msg in result_obj:
				messages.add_message(request, messages.ERROR, msg, extra_tags="log")
			return redirect(reverse("eproj3_signin"))
		pass  #  TODO: stuff like request.session and redirect

def logout(request):
	#  TODO: zap request.session keys
	#  TODO: add success message? (see views.py in journeys_plus)
	return redirect(reverse("eproj3_signin"))