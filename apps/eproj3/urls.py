from django.conf.urls import url

from . import views

urlpatterns = [
	# rendering routes
	url(r'^$',
		views.index, name='eproj3_index'),
	url(r'^signin/?$',
		views.signin, name='eproj3_signin'),
	# redirecting routes
	url(r'^signin/register?$',
		views.register, name='eproj3_register'),
	url(r'^signin/login?$',
		views.login, name='eproj3_login'),
	url(r'^signin/logout?$',
		views.logout, name='eproj3_logout'),
]
