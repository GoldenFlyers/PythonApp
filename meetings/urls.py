from django.urls import path
from .views import meeting_list, details, room_list, add_meeting

urlpatterns = [
    path('<int:id>', details, name="detail"),
    path('', meeting_list, name="meeting_list"),
    path('rooms', room_list, name="rooms"),
    path('add_meeting', add_meeting, name="add_meeting"),

]
