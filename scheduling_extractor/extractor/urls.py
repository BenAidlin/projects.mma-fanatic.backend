from django.urls import path

from .views.extractor_view import ExtractorView

urlpatterns = [
    path('stream/', ExtractorView.as_view(), name='stream')
]