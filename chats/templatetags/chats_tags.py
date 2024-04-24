from django import template
from chats.models import *
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

@register.filter
def get_last_msg(pk):
    thread = PrivateThread.objects.get(id=pk)
    try:
        latest_message = PrivateMessage.objects.filter(thread=thread).latest('timestamp')
    except ObjectDoesNotExist:
        latest_message = None
    return latest_message

@register.filter
def get_unread_msgs(pk):
    thread = PrivateThread.objects.get(id=pk)
    try:
        unread_msgs = PrivateMessage.objects.filter(thread=thread, is_read=False).count()
    except ObjectDoesNotExist:
        unread_msgs = 0
    return unread_msgs

