from __future__ import unicode_literals
from django.db import models
import datetime
import bcrypt

class UserManager(models.Manager):
	def get_user(self, username):
		try:
			user_obj = User.objects.get(username=username)
			return (True, user_obj)
		except:
			return (False, "Username not found")

	def create(self, name, username, password, pw_conf):
		error_msgs = []
		if len(name) < 3:
			error_msgs.append("Name must contain at least 3 characters")
		if len(username) < 3:
			error_msgs.append("Username must contain at least 3 characters")
		else:
			result_success, result_obj = self.get_user(username)
			if result_success:
				error_msgs.append("Username already registered")
		if len(password) < 8:
			error_msgs.append("Password must contain at least 8 characters")
		elif password != pw_conf:
			error_msgs.append("Passwords do not match. Try again")
		if error_msgs:
			return (False, error_msgs)
		else:
			pw_hash = bcrypt.hashpw( password.encode(), bcrypt.gensalt() )
			user_obj = User.objects.create(
				name=name,
				username=username,
				pw_hash=pw_hash )
			return (True, user_obj)

	def login(self, username, password):
		error_msgs = []
		result_success, result_obj = self.get_user(username)
		if not result_success:
			error_msgs.append(result_obj)
		elif not bcrypt.hashpw( password.encode(),
			result_obj.pw_hash.encode() ) == result_obj.pw_hash:
			error_msgs.append("Incorrect password")
		if error_msgs:
			return (False, error_msgs)
		else:
			return (True, result_obj)
# end UserManager

class WishManager(models.Manager):
	def get_all(self):
		wish_obj = Wish.objects.all()
		return wish_obj

	def get_one(self, id):
		wish_obj = Wish.objects.get(id=id)
		return wish_obj

	def create(self, product, user_id):
		error_msgs = []
		if len(product) < 3:
			error_msgs.append("Name must contain at least 3 characters")
		if error_msgs:
			return (False, error_msgs)
		user_obj = User.objects.get(id=user_id)
		wish_obj = Wish.objects.create(product=product, creator=user_obj)
		return (True, wish_obj)

	def destroy(self, id):
		Wish.objects.get(id=id).delete()
		return True

	def link(self, wish_id, user_id):
		user_obj = User.objects.get(id=user_id)
		return True

	def unlink(self, wish_id, user_id):
		user_obj = User.objects.get(id=user_id)
		return True
# end WishManager

class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=100)
	pw_hash = models.CharField(max_length=255)
	# date_hired = models.DateTimeField(auto_now_add = True)  # on wireframe but never used
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userManager = UserManager()
	objects = models.Manager()

class Wish(models.Model):
	product = models.CharField(max_length=255)
	creator = models.ForeignKey(User, related_name="creator")
	metoo = models.ManyToManyField(User, related_name="metoo")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	wishManager = WishManager()
	objects = models.Manager()
