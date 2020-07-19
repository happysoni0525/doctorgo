from django.db import models
from django.contrib.auth.models import User

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    callnum = models.CharField(max_length=20)
    url = models.CharField(max_length=50)
    established_on= models.DateField()
    employees_cnt= models.IntegerField()
    def __str__(self):
        return f'병원명 : {self.hospital_name} / 위치 : {self.city} / 설립일 : {self.established_on}'

class Subjects(models.Model):
    hospital = models.ForeignKey(Hospital , on_delete=models.CASCADE)
    subjects_name = models.CharField(max_length=20)
    specialist_cnt = models.IntegerField()
    def __str__(self):
        return f'병원명 : {self.hospital.hospital_name} / 진료과목 : {self.subjects_name} / 전문의 수 : {self.specialist_cnt}'
    

class Review(models.Model):
    subjects = models.ForeignKey(Subjects , on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=10)
    contents = models.TextField()
    speed = models.IntegerField()
    kindness = models.IntegerField()
    responsibility = models.IntegerField()
    professionality = models.IntegerField()
    liked_users = models.ManyToManyField(User, related_name='liked_reviews')
    disliked_users = models.ManyToManyField(User, related_name='disliked_reviews')
    def __str__(self):
        return f'병원명 : {self.subjects.hospital.hospital_name} / 진료과목 : {self.subjects.subjects_name} / 내용 : {self.contents}'

# Create your models here.
