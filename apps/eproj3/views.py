from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User, Wish

# rendering functions
def index(request):
	if not "user_id" in request.session:
		return redirect(reverse("eproj3_signin"))
	context = { "products": Wish.wishManager.get_all() }
	return render(request, "eproj3/index.html", context)

def signin(request):
	if "user_id" in request.session:
		return redirect(reverse("eproj3_index"))
	return render(request, "eproj3/signin.html")

def showitem(request, id):
	context = { "product": Wish.wishManager.get_one(id), "users": ["Dail", "Tim"] }
	return render(request, "eproj3/showitem.html", context)

def additem(request):
	return render(request, "eproj3/additem.html")

# redirecting functions
def register(request):
	if request.method == "POST":
		result_success, result_obj = User.userManager.create(			request.POST["reg_name"],
			request.POST["reg_username"], 
			request.POST["reg_password"],
			request.POST["reg_password_confirm"] )
		if not result_success:
			for msg in result_obj:
				messages.add_message(request, messages.ERROR, msg, extra_tags="reg")
			return redirect(reverse("eproj3_signin"))
		request.session["user_id"] = result_obj.id
		request.session["name"] = result_obj.name
		return redirect(reverse("eproj3_index"))

def login(request):
	if request.method == "POST":
		result_success, result_obj = User.userManager.login(
			request.POST["log_username"],
			request.POST["log_password"] )
		if not result_success:
			for msg in result_obj:
				messages.add_message(request, messages.ERROR, msg, extra_tags="log")
			return redirect(reverse("eproj3_signin"))
		request.session["user_id"] = result_obj.id
		request.session["name"] = result_obj.name
		return redirect(reverse("eproj3_index"))

def logout(request):
	if "user_id" in request.session:
		del request.session["user_id"]
	if "name" in request.session:
		del request.session["name"]
	messages.add_message(request, messages.SUCCESS,
						 "You've successfully logged out.",
						 extra_tags="log")
	return redirect(reverse("eproj3_signin"))

def linkitem(request, id):
	Wish.wishManager.link(id, request.session["user_id"])
	return redirect(reverse("eproj3_index"))

def unlinkitem(request, id):
	Wish.wishManager.unlink(id, request.session["user_id"])
	return redirect(reverse("eproj3_index"))

def createitem(request):
	if request.method == "POST":
		result_success, result_obj = Wish.wishManager.create( 
			request.POST["inp_product"],
			request.session["user_id"] )
		if not result_success:
			for msg in result_obj:
				messages.add_message(request, messages.ERROR, msg, extra_tags="item")
			return redirect(reverse("eproj3_additem"))
		return redirect(reverse("eproj3_index"))

def destroyitem(request, id):
	Wish.wishManager.destroy(id)
	return redirect(reverse("eproj3_index"))