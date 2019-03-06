from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Share_thought.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('thought.urls')),
    url(r'^account/',include('registration.backends.default.urls')),
    url(r'', include('social_django.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
]
