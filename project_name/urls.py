""" {{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

# For handler500
from django.views.defaults import page_not_found, server_error
from django.template import Context, loader
from django.http import HttpResponseServerError


# For your own urls
urlpatterns = [
	
]

# admin page
urlpatterns += [
	url(r'^admin/', admin.site.urls),
]

# configures the debug toolbar
if settings.DEBUG:
	import debug_toolbar
	urlpatterns += [
		url(r'^__debug__/', include(debug_toolbar.urls)),
	]

# 500 error handler which includes request in the context
def handler500(request):
	t = loader.get_template('500.html')
	return HttpResponseServerError(t.render(Context({'request': request,})))
