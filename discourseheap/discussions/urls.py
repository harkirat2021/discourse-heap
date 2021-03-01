from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),

    path('event/<int:pk>', views.event, name="event"),
    path('discussion/<int:pk>', views.discussion, name="discussion"),
]