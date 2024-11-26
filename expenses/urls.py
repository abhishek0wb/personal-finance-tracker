from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('add/', views.add_expense, name='add_expense'),
    # path('report/', views.view_report, name='view_report'),
    path('add_budget/', views.add_budget, name='add_budget'),
    path('view_budget/', views.view_budget, name='view_budget'),
]
