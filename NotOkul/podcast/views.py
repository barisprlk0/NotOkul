from django.shortcuts import render , redirect
from .forms import PodcastForm
from .models import Podcast
# Create your views here.



def create(request):
    form = PodcastForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('podcast:tytturkce')
    context = {
    'form': form,
    }
    return render(request,"podcast/form.html", context)
