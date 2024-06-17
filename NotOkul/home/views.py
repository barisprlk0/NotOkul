from django.shortcuts import render
from school.models import SchoolNote
from .forms import ContactForm
from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['content']
        email_from = settings.EMAIL_HOST_USER
        email = request.user.email
        recipient_list = ['barisparlak16@gmail.com']
        message = message + "\n\n" + email
        send_mail(subject, message, email_from, recipient_list)
        return redirect('home:contact')
    context = {'form': form}
    return render(request, "home/contact.html", context)


def index(request):

    matematik_zaman = 0
    turkce_zaman = 0
    sosyal_zaman = 0
    fizik_zaman = 0
    kimya_zaman = 0
    biyoloji_zaman = 0

    aytmatematik_zaman = 0
    aytfizik_zaman = 0
    aytkimya_zaman = 0
    aytbiyoloji_zaman = 0

    matematik_soru = 0
    turkce_soru = 0
    sosyal_soru = 0
    fizik_soru = 0
    kimya_soru = 0
    biyoloji_soru = 0

    aytmatematik_soru = 0
    aytfizik_soru = 0
    aytkimya_soru = 0
    aytbiyoloji_soru = 0

    username = request.user.username
    posts = SchoolNote.objects.filter(author__username=username)
    for post in posts:
        if post.lesson == "TYT Matematik":
            matematik_zaman += post.time
            matematik_soru += post.question
        if post.lesson == "TYT Türkçe":
            turkce_zaman += post.time
            turkce_soru += post.question
        if post.lesson == "TYT Sosyal Bilimler":
            sosyal_zaman += post.time
            sosyal_soru += post.question
        if post.lesson == "TYT Fizik":
            fizik_zaman += post.time
            fizik_soru += post.question

        if post.lesson == "TYT Kimya":
            kimya_zaman += post.time
            kimya_soru += post.question

        if post.lesson == "TYT Biyoloji":
            biyoloji_zaman += post.time
            biyoloji_soru += post.question

        if post.lesson == "AYT Matematik":
            aytmatematik_zaman += post.time
            aytmatematik_soru += post.question

        if post.lesson == "AYT Fizik":
            aytfizik_zaman += post.time
            aytfizik_soru += post.question

        if post.lesson == "AYT Kimya":
            aytkimya_zaman += post.time
            aytkimya_soru += post.question

        if post.lesson == "AYT Biyoloji":
            aytbiyoloji_zaman += post.time
            aytbiyoloji_soru += post.question

    context = {
        'posts': posts,
        'matematik_zaman': matematik_zaman,
        'turkce_zaman': turkce_zaman,
        'sosyal_zaman': sosyal_zaman,
        'fizik_zaman': fizik_zaman,
        'kimya_zaman': kimya_zaman,
        'biyoloji_zaman': biyoloji_zaman,

        'matematik_soru': matematik_soru,
        'turkce_soru': turkce_soru,
        'sosyal_soru': sosyal_soru,
        'fizik_soru': fizik_soru,
        'kimya_soru': kimya_soru,
        'biyoloji_soru': biyoloji_soru,

        'aytmatematik_zaman': aytmatematik_zaman,
        'aytfizik_zaman': aytfizik_zaman,
        'aytkimya_zaman': aytkimya_zaman,
        'aytbiyoloji_zaman': aytbiyoloji_zaman,

        'aytmatematik_soru': aytmatematik_soru,
        'aytfizik_soru': aytfizik_soru,
        'aytkimya_soru': aytkimya_soru,
        'aytbiyoloji_soru': aytbiyoloji_soru,












    }

    return render(request, 'home/index.html', context)
