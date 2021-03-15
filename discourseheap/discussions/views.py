from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import datetime

# Utils...
def get_messages_dict(messages):
    messages_dict = [model_to_dict(m) for m in messages]
    for i, m in enumerate(messages):
        messages_dict[i]['pk'] = m.pk
        messages_dict[i]['user'] = m.user.username
    return messages_dict

# Views...
def home(request):
    latest_event = Event.objects.order_by('start_date').last()
    return render(request, 'home.html', context={"event":latest_event})

def about(request):
    return render(request, 'about.html', context={})

def event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event.html', context={"event":event})

def get_event_posts(request, pk):
    event = get_object_or_404(Event, pk=pk)
    messages = Message.objects.filter(event=event, message_type=Message.INITIAL_VIEW).order_by("-date")

    # Convert each message and its user to a dict
    messages_dict = get_messages_dict(messages)

    data = {
        "messages": messages_dict
    }
    return JsonResponse(data)

def post_view(request, event_pk):
    if request.POST and request.user.is_authenticated:
        # Safety check for empty text
        if request.POST['text'] == "" or request.POST['text'] == " ":
            return JsonResponse({"wasPosted": False})

        event = get_object_or_404(Event, pk=event_pk)
        discussion = Discussion(event=event, creation_date=datetime.datetime.now())
        discussion.save()
        message = Message(user=request.user, message_type=Message.INITIAL_VIEW, event=event, discussion=discussion, text=request.POST['text'], date=datetime.datetime.now())
        message.save()

        return JsonResponse({"wasPosted": True})
    return JsonResponse({"wasPosted": False})

def join_discussion(request, message_pk):
    message = get_object_or_404(Message, pk=message_pk)

    # Create new discussion and copy message to it
    discussion = Discussion(event=message.event, creation_date=datetime.datetime.now())
    discussion.save()

    message = Message(message_type=Message.DISCUSSION, user=message.user, event=message.event, discussion=discussion, text=message.text, date=message.date)
    message.save()

    return redirect('/discussions/discussion/' + str(discussion.pk))

def discussion(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)
    messages = Message.objects.filter(discussion=discussion)

    return render(request, 'discussion.html', context={'discussion':discussion, 'messages':messages})

def get_discussion_messages(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)
    messages = Message.objects.filter(discussion=discussion).order_by("date")

    # Convert each message and its user to a dict
    messages_dict = get_messages_dict(messages)

    data = {
        "messages": messages_dict
    }
    return JsonResponse(data)

def post_message(request, discussion_pk):
    if request.POST and request.user.is_authenticated:
        # Safety check for empty text
        if request.POST['text'] == "" or request.POST['text'] == " ":
            return JsonResponse({"wasPosted": False})
        discussion = get_object_or_404(Discussion, pk=discussion_pk)
        message = Message(message_type=(Message.COMMON_GROUND_PROPOSAL if request.POST['isCommonGroundProposal']=='true' else Message.DISCUSSION), user=request.user, event=discussion.event, discussion=discussion, text=request.POST['text'], date=datetime.datetime.now())
        message.save()

        return JsonResponse({"wasPosted": True})
    return JsonResponse({"wasPosted": False})