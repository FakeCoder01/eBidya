from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('subscriptions', views.subscriptions, name='subscriptions'),
    path('update/<str:update_key>', views.updateAccount, name='update'),
    path('valid', views.valid_account_logged_in, name='valid_account_logged_in'),
]