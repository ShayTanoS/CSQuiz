from django.urls import path
from django.views.generic import TemplateView
from .views import AddPlayerView, QuizView, update_BD, delete_player
urlpatterns = [
    path('update/', TemplateView.as_view(template_name='staff/update_list.html'), name='update_list'),
    path('update/add-player/', AddPlayerView.as_view(), name='add_player'),
    path('update/update-bd/', update_BD, name='update_BD'),
    path('update/delete-player/', delete_player, name='delete_player'),
    path('quiz/', QuizView.as_view(), name='quiz_page'),
]