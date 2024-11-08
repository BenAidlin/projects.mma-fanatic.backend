from django.urls import path

from .views.schedule_view import ScheduleView

urlpatterns = [
    path('schedule/', ScheduleView.as_view(), name='stream')
]