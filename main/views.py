from django.shortcuts import render,redirect
from .models import Hospital
from .models import Subjects
from .models import Review
from django.utils import timezone
from django.http import HttpResponse
import pandas as pd
import math
import os
import datetime


def index(request):
    context={}
    return render(request,'main/index.html',context)

def about(request):
    context={}
    return render(request,'main/about.html',context)

def blog(request):
    context={}
    return render(request,'main/blog.html',context)

def contact(request):
    context={}
    return render(request,'main/contact.html',context)

def listing(request):
    context={}
    return render(request,'main/listing.html',context)

def main(request):
    context={}
    return render(request,'main/main.html',context)

def single(request):
    context={}
    return render(request,'main/single.html',context)

def testimonials(request):
    context={}
    return render(request,'main/testimonials.html',context)

def xlsx(request):
    path=os.path.abspath(os.path.dirname(__file__))+'\\'
    xlsx = pd.read_excel(path+'mockup.xlsx')
    for i in range(len(xlsx)):
        print("xlsx is being read")
        hospital_name = xlsx['요양기관명'][i] 
        city = xlsx['시도명'][i] 
        address = xlsx['주소'][i] 
        callnum = xlsx['전화번호'][i] 
        url = xlsx['병원URL'][i] 
        _date = xlsx['평균 : 개설일자'][i]
        established_on=datetime.datetime.strptime(str(_date),"%Y%m%d").date() 
        employees_cnt = xlsx['합계 : 의사총수'][i] 

        subjects_name = xlsx['진료과목코드명'][i] 
        specialist_cnt = xlsx['합계 : 과목별 전문의수'][i]

        if isinstance(hospital_name,str) == True:
            hospital=Hospital.objects.create(hospital_name=hospital_name,city=city,address =address,callnum=callnum,url= url,established_on=established_on,employees_cnt=employees_cnt)
        Subjects.objects.create(hospital=hospital,subjects_name=subjects_name,specialist_cnt=specialist_cnt)

    print("reading xlsx is done")        
    return HttpResponse("xlsx read done")

# Create your views here.
