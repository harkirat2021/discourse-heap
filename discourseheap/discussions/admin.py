from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Discussion)
admin.site.register(Message)