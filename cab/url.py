from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings # new
from django.conf.urls.static import static # new

urlpatterns = [
    path('cabhome',views.Cab,name='cab_home'),
    path('ride',views.ride,name='booking_ride'),
    path('CabDash',views.Dashboard,name='Cab_kyc'),
    path('CabVerification',views.verify,name='verifydriver'),
    path('profile',views.Cabprofile,name='Cabprofile'),
    path('editprofile',views.Cabeditprofile,name='Cabeditprofile'),
    # path('cablisting', views.cablisting, name='cablisting'),
    path('allbookings', views.allcab, name='allcab'),
    path('addcab', views.addcab1, name='addcab'),
    path('addedcab', views.addedcab, name='addedcab'),
    path('pendingcab.html', views.pendingcab, name='pendingcab'),
    path('completedride.html', views.completedride, name='completedride'),
    path('rejectedride', views.rejectedride, name='rejectedride'),
    path('cabneworder', views.cabneworder, name='cabneworder'),
    path('driver_details', views.driver_details, name='driver_details'),

    path('advpay_confirm', views.advpay_confirm, name='advpay_confirm'),

    # path('cabvendorlisting/<name>', views.cabvendorlisting, name='cabvendorlisting'),
    # path('cabvendorlisting', views.cabdetail, name=''),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)