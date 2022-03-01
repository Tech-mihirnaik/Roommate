# from distutils.command.upload import upload
# from email.policy import default
# from xml.etree.ElementTree import Comment
from django.db import models
# from django.forms import CharField, FileField

# Create your models here.
# class Careerdetails(models.Model):
#     Comment=models.CharField(max_length=100,default="none")
#     name=models.CharField(max_length=50,default="")
#     email=models.EmailField(max_length=254,default="")
#     website=models.CharField(max_length=300)
#     def __str__(self):
#         return self.name

class Apply(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    collage_name=models.CharField(max_length=100)
    course=models.CharField(max_length=50)
    applied_for=models.CharField(max_length=50,default="backend")
    def __str__(self):
        return self.name

# class ExcelFileUpload(models.Model):
#     excel_file_upload=models.FileField(upload_to="excel")
#
