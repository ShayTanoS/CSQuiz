from django.urls import path
from django.views.generic import TemplateView
from .views import AddPlayerView, QuizView
urlpatterns = [
    path('update/', TemplateView.as_view(template_name='staff/update_list.html'), name='update_list'),
    path('update/add_player/', AddPlayerView.as_view(), name='add_player'),
    path('quiz/', QuizView.as_view(), name='quiz_page')
]