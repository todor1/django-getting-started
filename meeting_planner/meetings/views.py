from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Meeting, Room


def detail(request, id):
    # meeting = Meeting.objects.get(pk=id) ### throws an error if id not available
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

# add a new webpage showing list of all room objects (just text, no links)
# 3 things needed: a view function, a template and a url mapping

# def room_detail(request, id):
#     '''my try, not working - saved for reference only'''
#     room = get_object_or_404(Room, pk=id)
#     return render(request, "meetings/rooms.html", {'room': room})

# def test_rooms_list(request):
#     ctx = {"rooms": Room.objects.all(),
#            "meetings": Meeting.objects.all(),
#            "test_key": Room.objects.all(),
#            }
#     return render(request, "meetings/rooms_list.html", context=ctx)


def rooms_list(request):
    return render(request, "meetings/rooms_list.html",
                  {"rooms": Room.objects.all()})