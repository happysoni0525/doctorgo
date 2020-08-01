from django.urls import path
from . import views

app_name='main'
urlpatterns = [
    path('',views.index, name="index"),
    # path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('listing/',views.listing,name='listing'),
    path('main/',views.main,name='main'),
    path('single/',views.single,name='single'),
    path('testimonials/',views.testimonials,name='testimonials'),
    path('xlsx/',views.xlsx, name='xlsx'),

    path('city_list/',views.read_city_list,name='city_list'),
    path('<str:city>/hospital_list',views.read_hospital_list,name='hospital_list'),
    path('<int:hospital_id>/subjects_list',views.read_subjects_list,name='read_subjects_list'),
    path('about/<int:subjects_id>',views.about,name='about'),
]
