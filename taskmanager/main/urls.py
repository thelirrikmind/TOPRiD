from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('about', views.about, name='about'),
    path('Video', views.Video, name='Video'),
    path('Photo', views.Photo_views, name='Photo'),
    path('Afisha', views.Afisha_views, name='Afisha'),
    path('buy', views.buy, name='buy'),
    path('Schedule', views.Schedule, name='Schedule'),
    path('Feedback', views.feedback, name='Feedback')

]
