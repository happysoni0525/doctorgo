from django.urls import path
from . import views

app_name='main'
urlpatterns = [
    path('',views.index, name="index"),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('listing/',views.listing,name='listing'),
    path('main/',views.main,name='main'),
    path('single/',views.single,name='single'),
    path('testimonials/',views.testimonials,name='testimonials'),
    path('xlsx/',views.xlsx, name='xlsx'),
]
