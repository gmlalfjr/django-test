from django.urls import path
from . import views
urlpatterns = [
    path('', views.article),
    path('list', views.list_product),
    path('create', views.add_rating),

]