from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# User profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(blank=True)

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
    start_date = models.DateTimeField('date created')
    end_date = models.DateTimeField('date created')

    def __str__(self):
        return self.title

# Discussion
class Discussion(models.Model):
    ONGOING = 0
    COMMON_GROUND_ACHIEVED = 1
    NO_CONCLUSION = 2

    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    creation_date = models.DateTimeField('date created')
    conclusion = models.IntegerField(default=0)

    def __str__(self):
        return self.title

# Message
class Message(models.Model):
    INITIAL = 0
    RESPONSE = 1
    COMMON_GROUND_PROPOSAL = 2

    message_type = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, null=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    text = models.TextField(null=False)
    date = models.DateTimeField('date')