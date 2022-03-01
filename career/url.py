from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings # new
from django.conf.urls.static import static # new
from .views import *

urlpatterns = [
    # path('Bus',views.Bus,name="Bus"),
    #path('excel/',ExportImportExcel.as_view()),
    #path('career_first',views.front,name='blog_details'),
    path('career_second',views.info,name='blog_form'),
    path('your_apply',views.apply,name='apply_form'),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)