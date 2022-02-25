from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.test, name="test"),
    path("buyer", views.buyer, name='buyer'),
    path("seller", views.seller, name="seller")
]
