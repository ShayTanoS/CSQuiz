from django.urls import path
from django.views.generic import TemplateView
urlpatterns = [
    path('update/', TemplateView.as_view(template_name='update_list.html'), name='update_list'),
]