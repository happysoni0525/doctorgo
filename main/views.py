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
# from django.core import serializers
# from .serializers import HospitalSerializer
import json


def index(request):
    context={}
    # print(request.GET)
    # print(request.GET['area'])
    return render(request,'main/index.html',context)

def read_city_list(request):
    city_list = Hospital.objects.values('city').distinct()
    # print(hospitals)
    # 걍 장고 시리얼라이저 사용
    # hospitals_json = serializers.serialize('json',hospitals)
    # print(hospitals_json)

    #장고 rest Framework에서 시리얼라이저 재정의해서 사용
    # hospitals_json = HospitalSerializer(hospitals,many=True)
    # print(hospitals_json)

    #걍 장고 json.dumps
    city_list_json = json.dumps(list(city_list))
    # print(hospitals_json)
    return HttpResponse(city_list_json,content_type="text/json-comment-filtered")

def read_hospital_list(request,city):
    hospital_list = Hospital.objects.values('id','hospital_name').filter(city=city)
    print(hospital_list)
    hospital_list_json =  json.dumps(list(hospital_list))
    return HttpResponse(hospital_list_json,content_type="text/json-comment-filtered")

def read_subjects_list(request,hospital_id):
    subjects_list = Subjects.objects.values('id','subjects_name').filter(hospital_id=hospital_id)
    subjects_list_json = json.dumps(list(subjects_list))
    return HttpResponse(subjects_list_json,content_type="text/json-comment-filtered")

def about(request,subjects_id):
    print(subjects_id)
    subject=Subjects.objects.filter(id=subjects_id)
    print(subject)
    context={'subject':subject}
    # context={'id':subject['id']}
    return render(request,'main/about.html',context)

def blog(request):
    context={}
    return render(request,'main/blog.html',context)

def sign_up(request):
    context={}
    return render(request,'main/sign_up.html',context)

def login(request):
    context={}
    return render(request,'main/login.html',context)

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
