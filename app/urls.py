from django.urls import path

from app import views

urlpatterns = [
    path('', views.ExcelPageView.as_view(), name='home'),
    path('export/excel', views.export_users_xls, name='export_excel'),

]
