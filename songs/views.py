from django.shortcuts import render
from .models import song
from artists.models import artist


def index(request):
	content={'songs':song.objects,'artists':artist.objects}
	return render(request,'songs/allsongs.html',content)

def add(request):
	return render(request,'songs/add.html')