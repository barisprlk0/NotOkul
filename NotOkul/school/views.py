from django.shortcuts import render , redirect , get_object_or_404
from .models import SchoolNote
from .forms import SchoolNoteForm , TestSihirbaziForm
# Create your views here.

def create(request):
    form = SchoolNoteForm(request.POST or None , request.FILES or None)
    if form.is_valid() :
        post = form.save(commit=False)

        post.author_id = request.user.id
        post.save()
        return redirect("account:profile")

    context = {
    'form' : form
    }
    return render(request,'school/form.html', context)

def update(request,id):
    post = get_object_or_404(SchoolNote , id=id)
    form = SchoolNoteForm(request.POST or None , instance=post)
    if request.user == post.author:
        if form.is_valid():
            post.save()
            return redirect('account:profile')
    else:
        return redirect('home:home')
    context = {'form':form}
    return render(request,'school/form.html', context)

def delete(request,id):
    post = get_object_or_404(SchoolNote , id=id)
    if request.user == post.author:
        post.delete()
        return redirect('account:profile')
    else:
        return redirect('home:home')

def sihirbaz(request):

    #yayınlar

    #TYT Türkçe
    tytturkce_level1 = "Çap Yayınları"
    tytturkce_level2 = "345 Yayınları"
    tytturkce_level3 = "Palme Yayınları"
    tytturkce_level4 = "Limit Yayınları"
    tytturkce_level5 = "Fen Bilimleri Yıldız Serisi"

    #TYT Matematik
    tytmat_level1 = "Antremanlarla Matematik"
    tytmat_level2 = "Eis Yayınları"
    tytmat_level3 = "345 Yayınları"
    tytmat_level4 = "Paraf yayınları"
    tytmat_level5 = "Karekök Yayınları"


    #AYT Matematik
    aytmat_level1 = "Sonuç Yayınları"
    aytmat_level2 = "3D Yayınları"
    aytmat_level3 = "345 Yayınları"
    aytmat_level4 = "Acil Yayınları"
    aytmat_level5 = "Apotemi Yayınları"

    #AYT Fizik
    aytfizik_level1 = "Okyanus Yayınları 40 Seans"
    aytfizik_level2 = "Palme Yayınları"
    aytfizik_level3 = "Bilgi Sarmal Yayınları"
    aytfizik_level4 = "Çap Yayınları"
    aytfizik_level5 = "3D Yayınları"

    #AYT Kimya
    aytkimya_level1 = "kimya level 1"
    aytkimya_level2 = "kimya level 2"
    aytkimya_level3 = "kimya level 3"
    aytkimya_level4 = "kimya level 4"
    aytkimya_level5 = "kimya level 5"

    #AYT Biyoloji
    aytbiyoloji_level1 = ""
    aytbiyoloji_level2 = "Palme Yayınları"
    aytbiyoloji_level3 = "Biyotik Yayınları"
    aytbiyoloji_level4 = "Paraf Yayınları"
    aytbiyoloji_level5 = "Apotemi Yayınları"





    top_point = 0
    form = TestSihirbaziForm(request.POST or None )
    context = {
    'form' : form
    }
    if form.is_valid():
        #net aralığı
        lesson = form.cleaned_data.get('lesson')
        net = form.cleaned_data.get('net_araligi')
        if net == "0-10":
            top_point += 1
        elif net == "10-20":
            top_point += 5
        elif net == "20-25":
            top_point += 10
        elif net == "25-30":
            top_point += 15
        elif net == "30-40":
            top_point += 25




        if lesson == "TYT Türkçe":
            if top_point == 1:
                context = {'form':form,'tytturkce_level1': tytturkce_level1}
            elif top_point == 5:
                context = {'form':form , 'tytturkce_level2' : tytmat_level2}
            elif top_point == 10:
                context = {'form':form , 'tytturkce_level3' : tytmat_level3}
            elif top_point == 15:
                context = {'form':form , 'tytturkce_level4':tytturkce_level4}
            elif top_point == 25:
                context = {'form' : form , 'tytturkce_level5' : tytturkce_level5}

        elif lesson == "TYT Matematik":
            if top_point == 1:
                context = {'form':form,'tytmat_level1': tytmat_level1}
            elif top_point == 5:
                context = {'form': form , 'tytmat_level2' : tytmat_level2}
            elif top_point == 10:
                context = {'form':form , 'tytmat_level3' : tytmat_level3}
            elif top_point == 15:
                context = {'form':form , 'tytmat_level4':tytmat_level4}
            elif top_point == 25:
                context = {'form' : form , 'tytmat_level5' : tytmat_level5}

        elif lesson == "AYT Matematik":
            if top_point == 1:
                context = {'form':form,'aytmat_level1': aytmat_level1}
            elif top_point == 5:
                context = {'form': form , 'aytmat_level2' : aytmat_level2}
            elif top_point == 10:
                context = {'form':form , 'aytmat_level3' : aytmat_level3}
            elif top_point == 15:
                context = {'form':form , 'aytmat_level4':aytmat_level4}
            elif top_point == 25:
                context = {'form' : form , 'aytmat_level5' : aytmat_level5}

        elif lesson == "AYT Fizik":
            if top_point == 1:
                context = {'form':form,'aytfizik_level1': aytfizik_level1}
            elif top_point == 5:
                context = {'form': form , 'aytfizik_level2' : aytfizik_level2}
            elif top_point == 10:
                context = {'form':form , 'aytfizik_level3' : aytfizik_level3}
            elif top_point == 15:
                context = {'form':form , 'aytfizik_level4':aytfizik_level4}
            elif top_point == 25:
                context = {'form' : form , 'aytfizik_level5' : aytfizik_level5}

        elif lesson == "AYT Kimya":
            if top_point == 1:
                context = {'form':form,'aytkimya_level1': aytkimya_level1}
            elif top_point == 5:
                context = {'form': form , 'aytkimya_level2' : aytkimya_level2}
            elif top_point == 10:
                context = {'form':form , 'aytkimya_level3' : aytkimya_level3}
            elif top_point == 15:
                context = {'form':form , 'aytkimya_level4':aytkimya_level4}
            elif top_point == 25:
                context = {'form' : form , 'aytkimya_level5' : aytkimya_level5}

        elif lesson == "AYT Biyoloji":
            if top_point == 1:
                context = {'form':form,'aytbiyoloji_level1': aytbiyoloji_level1}
            elif top_point == 5:
                context = {'form': form , 'aytbiyoloji_level2' : aytbiyoloji_level2}
            elif top_point == 10:
                context = {'form':form , 'aytbiyoloji_level3' : aytbiyoloji_level3}
            elif top_point == 15:
                context = {'form':form , 'aytbiyoloji_level4':aytbiyoloji_level4}
            elif top_point == 25:
                context = {'form' : form , 'aytbiyoloji_level5' : aytbiyoloji_level5}

    return render(request, "school/sihirbaz.html" , context)
