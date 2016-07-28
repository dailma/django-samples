from django.conf.urls import url

from . import views

urlpatterns = [
	# rendering routes
	url(r'^$',
		views.index, name='eproj3_index'),
	url(r'^dashboard/?$',
		views.index, name='eproj3_index'),
	url(r'^main/?$',
		views.signin, name='eproj3_signin'),
	url(r'^wish_items/(?P<id>\d+)$',
		views.showitem, name='eproj3_showitem'),
	url(r'^wish_items/create/?$',
		views.additem, name='eproj3_additem'),
	# redirecting routes
	url(r'^main/register/?$',
		views.register, name='eproj3_register'),
	url(r'^main/login/?$',
		views.login, name='eproj3_login'),
	url(r'^main/logout/?$',
		views.logout, name='eproj3_logout'),
	url(r'^wish_items/link/(?P<id>\d+)$',
		views.linkitem, name='eproj3_linkitem'),
	url(r'^wish_items/unlink/(?P<id>\d+)$',
		views.unlinkitem, name='eproj3_unlinkitem'),
	url(r'^wish_items/make/?$',
		views.createitem, name='eproj3_createitem'),
	url(r'^wish_items/delete/(?P<id>\d+)$',
		views.destroyitem, name='eproj3_destroyitem'),
]
