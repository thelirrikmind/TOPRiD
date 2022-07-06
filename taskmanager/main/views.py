from django.shortcuts import render

from .forms import ImageForm, AfishaForm, PhotoForm
from .models import Task, Image, Afisha,  Album


def main(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/main.html', {'title': "Главная страница сайта", 'tasks': tasks})


def about(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'main/main.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'main/about.html', {'form': form,
                                               'image': True,
                                               'images': Image.objects.all()})


def feedback(request):
    return render(request, 'main/feedback.html', {'title': "Обратная связь"})


def Afisha_views(request):
    if request.method == 'POST':
        form = AfishaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            afh_obj = form.instance
            return render(request, 'main/main.html', {'form': form, 'afh_obj': afh_obj})
    else:
        form = AfishaForm()
    return render(request, 'main/Afisha.html', {'form': form,
                                                'afisha': True,
                                                'afishi': Afisha.objects.all()})


def Photo_views(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            Ph_obj = form.instance
            return render(request, 'main/main.html', {'form': form, 'Phg_obj': Ph_obj})
    else:
        form = PhotoForm()
    return render(request, 'main/Photo.html', {'form': form,
                                               'photo': True,
                                               'albums': Album.objects.all()})


def buy(request):
    return render(request, 'main/buy.html', {'title': "Купить билет"})


def Video(request):
    return render(request, 'main/Video.html', {'title': "Видеоархив"})


def Schedule(request):
    return render(request, 'main/Schedule.html', {'title': "Расписание представлений"})
