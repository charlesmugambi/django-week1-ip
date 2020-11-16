from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('',views.index,name = 'index'),
    url('about/', views.about, name='about'),
    url('search/', views.search_results, name='search_results'),
    url('image/<int:image_id>', views.view_image,name='view_image'),
    url('category/<int:id>', views.category,name='category')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

