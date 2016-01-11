from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from recipe.views import RecipeListView, RecipeDetailView, RecipeCreateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RecipeListView.as_view(), name='recipe-list'),
    url(r'^add/$', RecipeCreateView.as_view(), name='recipe-add'),
    url(r'^(?P<slug>[\w-]+)/$', RecipeDetailView.as_view(), name='recipe-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
