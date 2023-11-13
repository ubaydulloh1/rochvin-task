from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'users'
urlpatterns = [
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    path("statistics/employee/<int:pk>/", views.EmployeeStatisticsView.as_view(), name="employee-statistics"),
    path("employee/statistics/", views.EmployeeStatisticsListView.as_view(), name="employee-statistics-list"),
    path("statistics/client/<int:pk>/", views.ClientStatisticsView.as_view(), name="client-statistics"),
]
