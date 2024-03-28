from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>/", views.HelloWorldDetail.as_view()),
    path("", views.HelloWorldView.as_view()),
]
