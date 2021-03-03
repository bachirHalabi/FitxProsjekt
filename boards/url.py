from django.urls import path
from . import views


urlpatterns = [
    path('boards', views.boards, name = 'boards'),
    path('boards/<int:boards_id>/', views.board_topics, name='board_topics'),
    path('boards/<int:boards_id>/new/', views.new_topics, name='new_topics')

]