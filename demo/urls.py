from django.conf.urls import include, url
from django.contrib import admin
from django.views import generic
from material.frontend import urls as frontend_urls


urlpatterns = [
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', generic.RedirectView.as_view(url='/workflow/', permanent=False)),
    url(r'', include(frontend_urls)),
]
