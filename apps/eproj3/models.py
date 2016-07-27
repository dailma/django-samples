from __future__ import unicode_literals
from django.db import models
import datetime
import bcrypt

class UserManager(models.Manager):
	def create_user(self):  # TODO: add params
		error_msgs = []
		# TODO: validations
		error_msgs.append("Placeholder error message")
		if error_msgs:
			return (False, error_msgs)
		# TODO: call User.objects.create() and
		# return (True, user_obj)
		pass  # TODO: remove

	def login(self):  # TODO: add params
		error_msgs = []
		# TODO: validations
		error_msgs.append("Placeholder error message")
		if error_msgs:
			return (False, error_msgs)
		# TODO: call User.objects.login() and
		# return (True, user_obj)
		pass  # TODO: remove
# end UserManager

class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=100)
	pw_hash = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userManager = UserManager()
	objects = models.Manager()