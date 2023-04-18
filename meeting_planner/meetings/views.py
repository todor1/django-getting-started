from django.shortcuts import render, get_object_or_404, redirect

from .models import Meeting, Room
# from django.forms import modelform_factory
### using custom class instead of modelform_factory
from .forms import MeetingForm 

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
    
# Create a new form based on our Meeting class (imported from models)
# exclude=[]-> see all the fields from my meeting model in the html form
# after the function call below the result is a newly generated ModelForm class
# MeetingForm is a Class, not a regular object
# MeetingForm = modelform_factory(Meeting, exclude=[]) ### MeetingForm from custom class used instead

def new(request):
    if request.method == "POST":
        # form hase been submitted, process data
        form = MeetingForm(request.POST)
        # check if all necessary fields are filled in 
        # and whether they contain proper data types 
        # use the check always before saving data to the database, both for security and consistency reasons
        if form.is_valid():
            form.save()                        
            return redirect("welcome")
    else:
        form = MeetingForm() # instance of the MeetingForm class
    # form below will be displayed in 2 cases:
    # either the request method was not POST and we created and empty meeting 
    # or the user has not filled it properly (is_valid=false, not passing the validity check), 
    # the inaccurate data will be shown again, and the is_valid method will have added errors to the invalid fields
    return render(request, "meetings/new.html", {'form': form})