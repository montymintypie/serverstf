from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from serverstf import views

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'serverstf.views.home', name='home'),
	# url(r'^serverstf/', include('serverstf.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r"^admin/", include(admin.site.urls)),
	url(r"", include("browser.urls")),
	url(r"^lobby/", include("lobby.urls")),
	url(r"^$", RedirectView.as_view(url="/~")),
	url(r"^openid/", include("steam_auth.urls")),
	url(r"^home$", views.home, name="home"),
	url(r"^faq$", TemplateView.as_view(template_name="faq.html"), name="faq"),
)


## REST urls
from rest_framework import routers
import browser.views
import lobby.views
import steam_auth.views

router = routers.SimpleRouter()
router.register("servers", browser.views.ServerViewSet, "servers")
router.register("parties", lobby.views.PartyViewSet, "parties")
router.register("users", steam_auth.views.UserViewSet, "users")

urlpatterns += (url(r"^rest/", include(router.urls)),)
