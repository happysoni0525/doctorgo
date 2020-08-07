from django.urls import path
from . import views

app_name='main'
urlpatterns = [
    path('',views.index, name="index"),
    # path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('listing/',views.listing,name='listing'), #나중에 없앨것
    path('main/',views.main,name='main'),
    path('single/',views.single,name='single'),
    path('testimonials/',views.testimonials,name='testimonials'),
    path('contact/',views.contact,name='contact'),
    path('xlsx/',views.xlsx, name='xlsx'),

    path('cities',views.read_city_list,name='read_city_list'),
    path('cities/<str:city>/hospitals',views.read_hospital_list,name='read_hospital_list'),
    path('cities/<str:city>/hospitals/<int:hospital_id>/subjects',views.read_subjects_list,name='read_subjects_list'),
    path('about/<int:subjects_id>',views.about,name='about'),
    path('review/<int:subjects_id>',views.review,name='review'),
    
    path('city_list/',views.read_city_list,name='city_list'),  #index.html
    path('<str:city>/hospital_list',views.read_hospital_list,name='hospital_list'),
    path('<int:hospital_id>/subjects_list',views.read_subjects_list,name='read_subjects_list'),
    path('about/<int:subjects_id>',views.about, name='about'),
    path('cities/<str:city>/hospitals', views.listing_hospital, name='listing_hospital'),
    path('cities/all/hospitals', views.listing_all, name='listing_all'),


]
# http://127.0.0.1:8000/main/country/
# http://127.0.0.1:8000/main/all/
# http://127.0.0.1:8000/main/seoul/
# http://127.0.0.1:8000/main/about/70
