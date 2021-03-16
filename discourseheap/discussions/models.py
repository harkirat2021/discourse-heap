from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# User profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    common_ground_points = models.IntegerField(default=0)

    #TODO figure out why it says => NameError: name 'receiver' is not defined
    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            instance.profile.save()

# Event
class Event(models.Model):
    title = models.CharField(max_length=400, null=False)
    description = models.TextField(null=False)
    img_src = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField('date start')
    end_date = models.DateTimeField('date end')

    def __str__(self):
        return self.title

# Discussion
class Discussion(models.Model):
    NOT_STARTED = 0
    ONGOING = 1
    COMMON_GROUND_ACHIEVED = 2
    NO_CONCLUSION = 3

    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    creation_date = models.DateTimeField('date created')
    state = models.IntegerField(default=0)

# Message
class Message(models.Model):
    INITIAL_VIEW = 0
    DISCUSSION = 1
    COMMON_GROUND_PROPOSAL = 2

    message_type = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    text = models.TextField(null=False)
    date = models.DateTimeField('date')

    def __str__(self):
        return self.text