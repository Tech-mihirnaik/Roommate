# from datetime import datetime
# from email.mime import application
# from urllib import response
from django.shortcuts import render
# import xlwt
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
import os

from main import settings
# from rest_framework.views import APIView
# from rest_framework.views import Response
# from rest_framework.authtoken.models import Token
# from rest_framework import serializers

from django.http import HttpResponse
from career.models import Apply
from django.core.mail import send_mail 
# Create your views here.
# def front(request):
#     if request.session['x']:
#         if request.method=='POST':
#            Comment=request.POST['comment']
#            name=request.POST['Author']
#            email=request.POST['email']
#            website=request.POST['url']
#
#            detail=Careerdetails(Comment=Comment,name=name,email=email,website=website)
#
#            detail.save()
#            return render(request,'career/blog-details.html')
#     return render(request,'career/blog-details.html')

def info(request): 
    return render(request,'career/blog-standard.html')

def apply(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        collage_name=request.POST['collage_name']
        course=request.POST['course']
        applied_for=request.POST['applied_for']

        # send_mail(
        #     name,
        #     name+" is applying for "+ os.linesep +applied_for+os.linesep+" studying in "+collage_name,
        #     email,
        #     ['aishwarya.yadav.techmihirnaik@gmail.com'],
        #     fail_silently=False
        # )

        # #str="rahulkumar.techmihirnaik@gmail.com"
        # str = "aishwarya.yadav.techmihirnaik@gmail.com"
        # send_mail(
        #     name,
        #     "your application is submitted",
        #     str,
        #     [email],
        #     fail_silently=False
        # )




        appl=Apply(name=name,email=email,collage_name=collage_name,course=course,applied_for=applied_for)
        appl.save()
        sendmail_candidate(request,email)
        sendmail_roommate(request)
        return render(request,'career/blog-standard.html')


def sendmail_candidate(request,email):
    email_subject = 'APPLICATION SUBMITTED'
    html_message = render_to_string('career/response.html')
    email_body = strip_tags(html_message)
    msg = EmailMultiAlternatives(email_subject, email_body, settings.EMAIL_FROM_USER, [email])
    msg.attach_alternative(html_message, "text/html")
    msg.send()

def sendmail_roommate(request):
    email_subject = 'NEW APPLICATION'
    html_message = render_to_string('career/response_roommate.html')
    email_body = strip_tags(html_message)
    msg = EmailMultiAlternatives(email_subject, email_body, settings.EMAIL_FROM_USER, ['aishwarya.yadav.techmihirnaik@gmail.com'])
    msg.attach_alternative(html_message, "text/html")
    msg.send()


# import pandas as pd
# class ExportImportExcel(APIView):
#
#     def get(self,request):
#         apply_obj=Apply.objects.all()
#         serializer=serializers(apply_obj,many=True)
#         df=pd.DataFrame(serializer.data)
#         print(df)
#
#         return Response({'status':200})




