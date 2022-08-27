from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('register/',views.register,name='register'),
    path('companies/',views.company_list,name='companies'),
    path('search/', views.search_view,name='search'),
    path('companies/<slug:industry_type>', views.company_list, name='company_list'),
]
