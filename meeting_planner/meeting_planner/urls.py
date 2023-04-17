"""meeting_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from website.views import welcome, date, about
# from meetings.views import detail, rooms_list  ## commented out after adding the local meetings/urls file
### from meetings.views import test_rooms_list ## used for test only

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'), ### index page url may be denoted with an empty string
    path('welcome.html', welcome), ### optional, just for the first example (no real html file configured for this)
    path('date', date),
    path('about', about),
    # path('meetings/<int:id>', detail, name='detail'),
    # path('rooms', rooms_list, name='rooms')
    # # path('rooms', test_rooms_list, name='rooms'), ### my test for context used in templates
    ### paths above replaced with local urls.py file in the meetings app, 
    ### the include function adds the app-local urlpatterns to the project-wide url patterns list with the prefix meetings
    path('meetings/', include('meetings.urls'))
]
