from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from recipe.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RecipeListView.as_view(), name='recipe-list'),
    url(r'^create/$', RecipeCreateView.as_view(), name='recipe-create'),
    url(r'^(?P<slug>[\w-]+)/$', RecipeDetailView.as_view(), name='recipe-detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', RecipeUpdateView.as_view(), name='recipe-update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', RecipeDeleteView.as_view(), name='recipe-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
