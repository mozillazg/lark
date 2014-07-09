from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^music/', include('music.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
