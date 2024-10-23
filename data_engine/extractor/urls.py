from django.urls import path

from .views.ExtractorView import ExtractorView

urlpatterns = [
    path('stream/', ExtractorView.as_view(), name='stream')
]