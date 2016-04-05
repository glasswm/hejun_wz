from django.conf.urls import patterns, include, url
from django.contrib import admin
from hejun_wz import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hejun_wz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^infor/', include('infor.urls', namespace='infor')),
)



if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))