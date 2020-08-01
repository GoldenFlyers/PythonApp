from django.urls import path
from .views import meeting_list, details, room_list

urlpatterns = [
    path('<int:id>', details, name="detail"),
    path('', meeting_list),
    path('rooms', room_list, name="rooms"),

]
