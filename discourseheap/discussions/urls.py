from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),

    path('event/<int:pk>', views.event, name="event"),
    path('post-event/<int:event_pk>', views.post_view, name="post_view"),
    path('get-event-posts/<int:pk>', views.get_event_posts, name="get_event_posts"),

    path('discussion/<int:pk>', views.discussion, name="discussion"),
]