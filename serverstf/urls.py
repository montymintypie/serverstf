from django.conf.urls import patterns, include, url
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
	url(r'^admin/', include(admin.site.urls)),
	url(r"", include("browser.urls")),
	url(r"^api/", include("api.urls")),
	url(r"^openid/", include("steam_auth.urls")),
	#url(r"^$", TemplateView.as_view(template_name="home.html")),
	url(r"^$", views.home, name="home"),
	url(r"^settings", views.manage_settings, name="settings"),
	url(r"^faq$", TemplateView.as_view(template_name="faq.html"), name="faq"),
)