from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('contact.urls')),
    url(r'^plugins/postmark/', include('contact.plugins.postmark')),
    url(r'^plugins/sendgrid/', include('contact.plugins.sendgrid')),
)
