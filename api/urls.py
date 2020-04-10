from django.urls import path

from . import views


urlpatterns = [
    path('ping/', views.PingView.as_view(), name='ping'),
    path('status/', views.StatusView.as_view(), name='status'),
    path('add/', views.BalanceRefillView.as_view(), name='balance_refill'),
    path('substract/', views.DecreasingBalanceView.as_view(), name='balance_decreasing'),
]
