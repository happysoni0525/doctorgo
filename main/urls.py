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
    path('contact/',views.contact,name='contact'),
    path('xlsx/',views.xlsx, name='xlsx'),

    path('cities',views.read_city_list,name='read_city_list'),
    path('cities/<str:city>/hospitals',views.read_hospital_list,name='read_hospital_list'),
    path('cities/<str:city>/hospitals/<int:hospital_id>/subjects',views.read_subjects_list,name='read_subjects_list'),
    path('about/<int:subjects_id>',views.about,name='about'),
    
]
