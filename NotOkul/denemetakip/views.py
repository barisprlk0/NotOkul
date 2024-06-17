from django.shortcuts import render, redirect, get_object_or_404
from .models import DenemeTakip, DenemeTakipAYT
from .forms import DenemeTakipForm, DenemeTakipAYTForm
# Create your views here.


def create(request):
    form = DenemeTakipForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        form.save()
        return redirect('denemetakip:index')

    context = {'form': form}
    return render(request, 'denemetakip/form.html', context)


def index(request):
    set = DenemeTakip.objects.filter(
        user__username=request.user.username)
    setAYT = DenemeTakipAYT.objects.filter(
        user__username=request.user.username)
    context = {'set': set, 'setAYT': setAYT}

    return render(request, 'denemetakip/index.html', context)


def delete(request, id):
    post = get_object_or_404(DenemeTakip, id=id)
    if request.user == post.user or request.user.is_superuser:
        post.delete()
        return redirect('denemetakip:index')
    else:
        return redirect('home:home')


def update(request, id):
    post = get_object_or_404(DenemeTakip, id=id)
    form = DenemeTakipForm(request.POST or None, instance=post)
    if form.is_valid():
        if request.user == post.user or request.user.is_superuser:
            form.save()
            return redirect('denemetakip:index')
        else:
            return redirect('home:home')
    context = {'form': form}
    return render(request, 'denemetakip/form.html', context)


"""

AYT

"""


def createAYT(request):
    form = DenemeTakipAYTForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.netSayisi = post.matNet + post.fizikNet + post.biyoNet + post.kimyaNet
        form.save()
        return redirect('denemetakip:index')

    context = {'form': form}
    return render(request, 'denemetakip/form.html', context)


def deleteAYT(request, id):
    post = get_object_or_404(DenemeTakipAYT, id=id)
    if request.user == post.user or request.user.is_superuser:
        post.delete()
        return redirect('denemetakip:index')
    else:
        return redirect('home:home')


def updateAYT(request, id):
    post = get_object_or_404(DenemeTakipAYT, id=id)
    form = DenemeTakipAYTForm(request.POST or None, instance=post)
    if form.is_valid():
        if request.user == post.user or request.user.is_superuser:
            form.save()
            return redirect('denemetakip:index')
        else:
            return redirect('home:home')
    context = {'form': form}
    return render(request, 'denemetakip/form.html', context)
