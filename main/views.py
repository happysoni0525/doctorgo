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
    if city == '전체지역':
        hospital_list = Hospital.objects.values('id','hospital_name')
        print(hospital_list)
        hospital_list_json =  json.dumps(list(hospital_list))
        return HttpResponse(hospital_list_json,content_type="text/json-comment-filtered")

    hospital_list = Hospital.objects.values('id','hospital_name').filter(city=city)
    print(hospital_list)
    hospital_list_json =  json.dumps(list(hospital_list))
    return HttpResponse(hospital_list_json,content_type="text/json-comment-filtered")

def read_subjects_list(request,city,hospital_id):
    #hospital_id가 모든 테이블에서 유일하기 때문에 굳이 filter에 city를 안넣어도 된다.
    subjects_list = Subjects.objects.values('id','subjects_name').filter(hospital_id=hospital_id)
    subjects_list_json = json.dumps(list(subjects_list))
    return HttpResponse(subjects_list_json,content_type="text/json-comment-filtered")
    # subjects_list_json ={
    #     {'id' : 1,
    #     'subject_name': 신경의학과},
    #     {

    #     },
    #     {

    #     }


    # }
    



def about(request,subjects_id):
    print(subjects_id)
    subject=Subjects.objects.filter(id=subjects_id)
    print(subject)
    context={'subject':subject}
    return render(request,'main/about.html',context)


    # return HttpResponse() -> 데이터(json) 만 전달할때,
    # return render() -> 데이터(.json) 랑 화면(.html)을 같이 엮어서 전달
    # return render(subjects_list_json, a.html , )
    # return redirect() -> 화면만 

# def about(request,subjects_id):
#     print(subjects_id)
#     subject=Subjects.objects.filter(id=subjects_id)
#     print(subject)
#     context={'subject':subject}
#     # context={'id':subject['id']}
#     return render(request,'main/about.html',context)


def blog(request):
    context={}
    return render(request,'main/blog.html',context)

# def sign_up(request):
#     context={}
#     return render(request,'main/sign_up.html',context)

# def login(request):
#     context={}
#     return render(request,'main/login.html',context)

def about(request,subjects_id):
    print(subjects_id)
    subject=Subjects.objects.filter(id=subjects_id)
    print(subject)
    context={'subject':subject}
    return render(request,'main/about.html',context)

def listing(request):
    hospitals=Hospital.objects.all
    context={'hospitals' : hospitals }
    return render(request,'main/listing.html',context) 

# http://고사부.com/main/cities/<str:city>/hospitals' (http://127.0.0.1:8000/main/cities/서울/hospitals)
def listing_hospital(request,city):
    print(city)
    hospitals=Hospital.objects.filter(city=city)  #만든변수=DB테이블명.objects.filter(DB칼럼명=def에서정의한변수)
    print(hospitals)
    context={ 'hospitals' :   hospitals  } #{key:value}에서 key값은 아무거나 해줘도 된다. -> 이 key는 html에서 사용한다.
    return render(request,'main/listing_hospital.html',context)

# http://고사부.com/main/cities/all/hospitals  (http://127.0.0.1:8000/main/cities/all/hospitals)
def listing_all(request):
    hospitals=Hospital.objects.all()
    context={'hospitals' : hospitals }
    return render(request,'main/listing_all.html',context)    

def main(request):
    context={}
    return render(request,'main/main.html',context)

def single(request):
    context={}
    return render(request,'main/single.html',context)

def testimonials(request):
    context={}
    return render(request,'main/testimonials.html',context)

def contact(request):
    context={}
    return render(request,'main/contact.html')

def review(request,subjects_id):
    subjects=Subjects.objects.filter(id=subjects_id)
    print(subjects)
    hospital_id=Subjects.objects.values('hospital_id').filter(id=subjects_id)
    print(hospital_id)

    hospital=Hospital.objects.filter(id=13)
    print(hospital)
    context={'subjects': subjects,
            'hospital' : hospital
    }
    print(context)
    return render(request,'main/review.html' ,context)

def add_review(request,subjects_id):
    context={}
    return render(request,'main/review.html')

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
