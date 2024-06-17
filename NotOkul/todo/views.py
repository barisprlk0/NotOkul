from django.shortcuts import render , redirect , get_object_or_404
from .models import TodoModel
from .forms import TodoForm

# Create your views here.



def index(request):
    posts = TodoModel.objects.filter(user__username=request.user.username)
    
    form = TodoForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit= False)
        post.user = request.user
        post.save()
        return redirect('todo:index')
    context = {'posts': posts , 'form': form}
    return render(request , 'todo/index.html', context)

def delete(request,id):
    post = get_object_or_404(TodoModel , id=id)
    if post.user == request.user or request.user.is_superuser:
        post.delete()
        return redirect('todo:index')
    else:
        return redirect('home:home')

def complete(request,id):
    post = get_object_or_404(TodoModel, id=id)
    if post.user == request.user and post.status == False:
        post.status = True
        post.save()
        return redirect('todo:index')
    elif post.user == request.user and post.status == True :
        post.status = False
        post.save()
        return redirect('todo:index')

    else:
        return redirect('home:home')

def update(request,id):
    post = get_object_or_404(TodoModel, id=id)
    form = TodoForm(request.POST or None , instance=post)
    if form.is_valid():
        form.save()
        return redirect('todo:index')

    context = {'form':form}
    return render(request , 'todo/form.html',context)
