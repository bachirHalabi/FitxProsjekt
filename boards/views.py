from django.shortcuts import render, get_object_or_404
from .models import Board
# Create your views here.

def boards(request):
    boards = Board.objects.all()
    return render(request,'boards.html',{'boards':boards})


def board_topics(request, boards_id):
    board= get_object_or_404(Board, pk=boards_id)
    return render(request,'topics.html',{'board':board})

def new_topics(request, boards_id):
    board = get_object_or_404(Board, pk=boards_id)
    return render(request, 'new_topic.html',{'board':board})