from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from csvapp.views import ProfileImageIndexView

from django.contrib import admin
admin.autodiscover()

from csvapp.views import ProfileImageView, ProfileDetailView

urlpatterns = patterns('',
    url(r'^$', ProfileImageIndexView.as_view(), name='home'),

    url(r'^upload/', ProfileImageView.as_view(), name='profile_image_upload'),
    url(
        r'^uploaded/(?P<pk>\d+)/$', ProfileDetailView.as_view(),
        name='profile_image'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
