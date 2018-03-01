from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # if the URL pattern match /admin/ then open up admin panel

    url(r'', include('shortenersite.urls', namespace='shortenersite')),
    # if anything rather then /admin/ then it will look for shortenersite/urls
)