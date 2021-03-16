from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),

    path('my-discussions', views.my_discussions, name="my_discussions"),
    path('accept-common-ground/<int:message_pk>', views.accept_common_ground, name="accept_common_ground"),

    path('event/<int:pk>', views.event, name="event"),
    path('post-view/<int:event_pk>', views.post_view, name="post_view"),
    path('get-event-posts/<int:pk>', views.get_event_posts, name="get_event_posts"),

    path('join-discussion/<int:message_pk>', views.join_discussion, name="join_discussion"),
    path('discussion/<int:pk>', views.discussion, name="discussion"),

    path('post-message/<int:discussion_pk>', views.post_message, name="post_message"),
    path('get-discussion-messages/<int:pk>', views.get_discussion_messages, name="get_discussion_messages"),
]