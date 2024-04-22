from django.urls import path
from . import views

app_name = 'atm_management'

urlpatterns = [
    path('upload/', views.upload_excel, name='upload'),
    path('sites/', views.atm_site_list, name='atm_site_list'),
    path('sites/<str:site_id>/', views.atm_site_detail, name='atm_site_detail'),
]
