from os import name
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render,HttpResponse
from cab.models import *
import random

from dashboard.models import *
#from main.settings import GOOGLE_RECAPTCHA_SECRET_KEY, Paytm_IndustryType, Paytm_MID, Paytm_MKey, Paytm_Website, TestPaytm
#from payment import Checksum
from roomate.views import register
from django.core.paginator import Paginator
import datetime
# MERCHANT_KEY = '&AM6&aammTGly&9N'
#MERCHANT_KEY = 'RIzZj7u_HfAKscS8'

global log


def Cab(request):
    # print(x)
    global log
    log=False
    try:
        log=request.session['x']
        return render(request, 'cab/home.html',context={'x':log})

    except:
        return redirect(register)
        #return render(request, 'cab/home.html',context={'x':log})
        #return render(request, 'roommate/index.html')



def ride(request):
    try:
        if request.session['x']:
            print(request.session['x'])

            if request.method == 'POST':
                name = request.POST['PassName']
                PhoneNo = request.POST['PassPhone']
                Pickup = request.POST['PassPickup']
                Drop = request.POST['PassDrop']
                car = request.POST['car']
                Date = request.POST['PassDate']

                Time = request.POST['PassTime']
                print('1')
                while True:
                    booking_id= "#"+str(random.randint(1000000,9000000))  
                    try:
                        bookedCab.objects.get(booking_id=booking_id)
                        continue
                    except:
                        break
                email=request.session['email']
                
                Pass = bookedCab(email=email,booking_id=booking_id,PassName=name, PassPhone=PhoneNo, PassPickup=Pickup,
                                PassDrop=Drop, Car=car, PassDate=Date, PassTime=Time)
                Pass.save()
                # print('done')
                # print(booking_id)
                cb = bookedCab.objects.get(booking_id=booking_id)
                # print(cb)
                send_mailstud(request, email)
                # print('mail sent')
                send_mailcab(request, booking_id)
                # print('mail sent')
                return redirect(Cab)
            #   id_new=Pass.booking_id[1:]
            #     current_site = get_current_site(request)
            #     param_dict = {
            #         # 'MID': 'vuNavq92153022692603',
            #         'MID': 'Techmi14398819344230',
            #         'ORDER_ID': str(id_new),
            #         'TXN_AMOUNT': "1.00",
            #         'CUST_ID': Pass.email,
            #         # 'INDUSTRY_TYPE_ID': 'Retail',
            #         'INDUSTRY_TYPE_ID': 'ECommerce',
            #         # 'WEBSITE': 'WEBSTAGING',
            #         'WEBSITE': 'DEFAULT',
            #         'CHANNEL_ID': 'WEB',
            #         'CALLBACK_URL':'http://'+str(current_site)+'/handlerequest2/',
            #         }
            #
            #     generated=Checksum.generate_checksum(param_dict, MERCHANT_KEY)
            #
            #     param_dict['CHECKSUMHASH'] = generated
            #
            #
            # return render(request, 'Website/newPaytm.html', {'param_dict': param_dict})
            # return render(request, 'Website/paytm.html', {'param_dict': param_dict})#donot remove comment
    

        else:
            return redirect(register)
    except:
        return redirect(register)

def send_mailstud(request,mail):
    email_subject = 'CAB BOOKING IN PROCESS'
    html_message = render_to_string('cab/Cab_booked_Student.html')
    email_body = strip_tags(html_message)
    msg = EmailMultiAlternatives(email_subject, email_body, settings.EMAIL_FROM_USER, [mail])
    msg.attach_alternative(html_message, "text/html")
    msg.send()


def send_mailcab(request,id):
    email_subject = 'CAB BOOKED'
    br=bookedCab.objects.filter(booking_id=id)
    # print(id)
    # print(br)
    #html_message = render_to_string('cab/Cab_booked.html')
    html_message = render_to_string('cab/Cab_booked.html',
                                    {
                                        'br': br
                                    }
                                    )
    email_body = strip_tags(html_message)
    #msg = EmailMultiAlternatives(email_subject, email_body, settings.EMAIL_FROM_USER, ['noreply.tmnroommate@gmail.com','tmnroommate@gmail.com'])
    msg = EmailMultiAlternatives(email_subject, email_body, settings.EMAIL_FROM_USER, ['aishwarya0215yadav@gmail.com'])
    msg.attach_alternative(html_message, "text/html")
    msg.send()



############# paytm new code start ##############


'''



import json

# import checksum generation utility
from . import PaytmChecksum as PaytmChecksum
import requests
def ride(request):
    # try:
    if request.session['x']: 
        print('karthik')
        if request.method == 'POST':
            name = request.POST['PassName']
            PhoneNo = request.POST['PassPhone']
            Pickup = request.POST['PassPickup']
            Drop = request.POST['PassDrop']
            car = request.POST['car']
            Date = request.POST['PassDate']
            Time = request.POST['PassTime']
            print('1')
            while True:
                booking_id= "#"+str(random.randint(1000000,9000000))  
                try:
                    bookedCab.objects.get(booking_id=booking_id)
                    continue
                except:
                    break
            email=request.session['email']
            
            Pass = bookedCab(email=email,booking_id=booking_id,PassName=name, PassPhone=PhoneNo, PassPickup=Pickup,
                            PassDrop=Drop, Car=car, PassDate=Date, PassTime=Time)
            Pass.save()
            print('2')
            id_new=Pass.booking_id[1:]
            current_site = get_current_site(request)
            paytmParams = dict()
            
            
            mid = "Techmi14398819344230"
            mkey = MERCHANT_KEY
            order_id=str(id_new)
            paytmParams["body"] = {
                "requestType"   : "Payment",
                "mid"           : mid,
                "websiteName"   : "WEBSTAGING",
                "orderId"       : order_id,
                "callbackUrl"   : 'http://'+str(current_site)+'/handlerequest2/',
                "txnAmount"     : {
                    "value"     : "1.00",
                    "currency"  : "INR",
                },
                "userInfo"      : {
                    "custId"    : Pass.email,
                },
            }
            # Generate checksum by parameters we have in body
            # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
            checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), mkey)

            paytmParams["head"] = {
                "signature"	: checksum
            }

            post_data = json.dumps(paytmParams)
            print(post_data)

            # for Staging
            # url =  "https://securegw-stage.paytm.in/theia/api/v1/initiateTransaction?mid={mid}&orderId={order_id}".format(mid=mid, order_id=order_id)

            # for Production
            url = "https://securegw.paytm.in/theia/api/v1/initiateTransaction?mid={mid}&orderId={order_id}".format(mid=mid, order_id=order_id)
            response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"})
            resp = response.json()
            print(resp)
            payment_page={
                'mid':mid,
                'txnToken':resp['body']['txnToken'],
                'orderId':paytmParams['body']['orderId'],
            }

        return render(request, 'Website/paytm.html', {'data': payment_page})
    else:
        return redirect(register)
    # except:
    #     return redirect(register)



'''

def Dashboard(request):
    email = request.session['email']
    a = cabowner.objects.filter(Email=email).exists()
    try:
        verified = cabowner.objects.get(Email=email).isverified
    except:
        verified = False
    return render(request, 'cab/dashboardCab.html', context={'a': a, 'v': verified})


def verify(request):
    email = request.session['email']
    if request.method == 'POST':
        Name = request.POST['COname']
        Contact = request.POST['COcontact']
        COPhoto = request.FILES.get('COphoto')
        COadhar = request.FILES.get('COadhar')
        COpan = request.FILES.get('COpan')
        VechileDrop = request.POST['VechileDrop']
        Cabname = request.POST['Cabname']
        contact = request.POST['CabContact']
        CabNumber = request.POST['CabNo']
        CabPhoto = request.FILES.get('CabPhoto')
        plate = request.FILES.get('NumberPlate')
        Paper1 = request.FILES.get('Paper1')
        All = request.FILES.get('alldata')
        CAB = cabowner(Email=email, CabOwnerName=Name, CabOwnerContact=Contact, CabOwnerPhoto=COPhoto, CabOwnerAdhar=COadhar, CabOwnerPan=COpan, vechileType=VechileDrop,
                       CabName=Cabname, CabContactNo=contact, CabNumberPlate=CabNumber, CabPhoto=CabPhoto, CabNumberPhoto=plate, Cabregistration=Paper1, CabAllData=All)
        CAB.save()
        return redirect(Dashboard)
    return render(request, 'cab/Verify.html', context={'user': email})


def Cabprofile(request):
    email = request.session['email']
    user = cabowner.objects.get(Email=email)
    return render(request, 'cab/Cabprofile.html', context={'user': user})


def Cabeditprofile(request):
    email = request.session['email']
    if request.method == 'POST':
        update = cabowner.objects.get(Email=email)
        update.CabOwnerName = request.POST.get('coname')
        update.Email = request.POST.get('coemail')
        update.CabOwnerContact = request.POST['cophone']
        update.CabName = request.POST.get('cname')
        update.CabNumberPlate = request.POST.get('cnplate')
        p = request.FILES.get('cophoto')
        if p != None:
            print(1)
            update.CabOwnerPhoto = p
        update.save()
        return redirect(Cabprofile)
    user = cabowner.objects.get(Email=email)
    return render(request, 'cab/Cabedit-details.html', context={'user': user})


def allcab(request):
    services = bookedCab.objects.all()
    email = request.session['email']
    user = cabowner.objects.get(Email=email)
    return render(request, 'cab/Caball.html', context={'services': services, 'user': user})


def completedride(request):
    email = request.session['email']
    user = cabowner.objects.get(Email=email)
    services = bookedCab.objects.filter(completed=True)
    return render(request, 'cab/completedride.html', context={'user': user,'services':services})


def rejectedride(request):
    email = request.session['email']
    user = cabowner.objects.get(Email=email)

    services = bookedCab.objects.filter(rejected=True)
    return render(request, 'cab/rejectedride.html', context={'user': user,'services':services})


# def cabneworder(request):
#     global mail22
#     email = request.session['email']
#     user = cabowner.objects.get(Email=email)
#     services = bookedCab.objects.filter(pending=False, completed=False, rejected=False, confirmation=False)
#     if request.method=='POST':
#         confirm = request.POST.get('confirm')
#         reject = request.POST.get('reject')
#         booking_id = request.POST.get('booking_id')
#         advpay_link = request.POST.get('advpay_link')
#
#         print(booking_id)
#         print(confirm)
#         print(reject)
#         print(advpay_link)
#         #updatestatus = book_service.objects.update_or_create(completed=completed)
#         updatestatus=bookedCab.objects.filter(booking_id=booking_id)
#         print(updatestatus)
#         # for x in updatestatus:
#         #     mail22 = x.email
#         # if confirmation =='Confirm':
#         #     updatestatus.update(confirmation=True,pending=True,advpay_link=advpay_link)
#         #     # updatestatus.update(pending=True)
#         #     # send_mailconfirm(request,mail22)
#         #     print('confirm done')
#         if reject =='Reject':
#             updatestatus.update(rejected=True)
#             # send_mailreject(request,mail22)
#             print('reject done')
#     return render(request, 'cab/cab_new.html',context={'user': user,'services': services})

def cabneworder(request):
    global mail22
    email = request.session['email']
    user = cabowner.objects.get(Email=email)
    services = bookedCab.objects.filter(pending=False, completed=False, rejected=False, confirmation=False)
    if request.method == 'POST':
        confirmed = request.POST.get('confirm')
        rejected = request.POST.get('rejected')
        booking_id = request.POST.get('booking_id')
        total = request.POST.get('total')
        advpay_link = request.POST.get('advpay_link')
        advpay_price = request.POST.get('advpay_price')
        duepay_price = request.POST.get('duepay_price')

        # print(booking_id)
        # print(confirmed)
        # print(rejected)
        # print(advpay_link)
        updatestatus = bookedCab.objects.filter(booking_id=booking_id)
        for x in updatestatus:
            mail22 = x.email
        # print(updatestatus)
        if rejected == 'Reject':
            rejected = True
            confirmed = False
            updatestatus.update(rejected=rejected, confirmation=confirmed)
            send_mailreject(request, mail22)
            # send_mailreject(request, email)
            # print('reject done')

        elif confirmed == 'Confirm':
            confirmed = True
            rejected = False
            updatestatus.update(rejected=rejected, confirmation=confirmed, pending=True, advpay_link=advpay_link,
                                advpay_price=advpay_price, total=total,duepay_price=duepay_price)
            send_mailconfirm(request, mail22,booking_id)
            # send_mailconfirm(request, email,booking_id)
            # print('confirm done')


    return render(request, 'cab/cab_new.html', context={'user': user, 'services': services})



def send_mailconfirm(request,mail22,id):
    email_subject = 'CAB BOOKING CONFIRMED'
    br = bookedCab.objects.filter(booking_id=id)
    # print(id)
    # print(br)
    html_message = render_to_string('cab/Cab_confirmation.html',
                                    {
                                        'br': br
                                    }
                                    )
    # print(mail22)
    email_body = strip_tags(html_message)
    msg = EmailMultiAlternatives(email_subject, email_body, settings.EMAIL_FROM_USER, [mail22])
    # msg = EmailMultiAlternatives(email_subject, email_body, settings.EMAIL_FROM_USER, ['yadavaishwarya42@gmail.com'])
    msg.attach_alternative(html_message, "text/html")
    msg.send()



def send_mailreject(request,mail22):
    email_subject = 'CAB BOOKING REJECTED'
    html_message = render_to_string('cab/Cab_rejection.html')
    email_body = strip_tags(html_message)
    # print(mail22)
    msg = EmailMultiAlternatives(email_subject, email_body, settings.EMAIL_FROM_USER, [mail22])
    # msg = EmailMultiAlternatives(email_subject, email_body, settings.EMAIL_FROM_USER, ['yadavaishwarya42@gmail.com'])
    msg.attach_alternative(html_message, "text/html")
    msg.send()

def driver_details(request):
    global mail33
    email = request.session['email']
    user = cabowner.objects.get(Email=email)
    if request.method=='POST':
        driver_name = request.POST.get('driver_name')
        cab_registration_no = request.POST.get('cab_registration_no')
        price = request.POST.get('price')
        car_type = request.POST.get('car_type')
        booking_id = request.POST.get('booking_id')
        contact_no = request.POST.get('contact_no')
        drive=driver(driver_name=driver_name,cab_registration_no=cab_registration_no,price=price,
                     car_type=car_type,booking_id=booking_id,contact_no=contact_no)
        drive.save()
        dr = bookedCab.objects.filter(booking_id=booking_id)
        # print(dr)
        for x in dr:
            mail33 = x.email
        send_maildetails(request,booking_id,mail33)
        return redirect(pendingcab)
    return redirect(cabneworder)


def send_maildetails(request,id,mail33):
    email_subject = 'CAB RIDE DETAILS'
    br=driver.objects.filter(booking_id=id)
    # print(br)
    # print(mail33)
    html_message = render_to_string('cab/Cab_driverdetails.html',
                                    {
                                        'br': br
                                    }
                                    )
    email_body = strip_tags(html_message)
    #msg = EmailMultiAlternatives(email_subject, email_body, settings.EMAIL_FROM_USER, ['noreply.tmnroommate@gmail.com','tmnroommate@gmail.com'])
    # msg = EmailMultiAlternatives(email_subject, email_body, settings.EMAIL_FROM_USER, ['yadavaishwarya42@gmail.com'])
    msg = EmailMultiAlternatives(email_subject, email_body, settings.EMAIL_FROM_USER, [mail33])
    msg.attach_alternative(html_message, "text/html")
    msg.send()


def pendingcab(request):
    global mail55
    email = request.session['email']
    user = cabowner.objects.get(Email=email)
    services = bookedCab.objects.filter(pending=True)
    if request.method == 'POST':
        completed = request.POST.get('complete')
        booking_id = request.POST.get('booking_id')
        # print(completed)
        # print(booking_id)
        updatestatus = bookedCab.objects.filter(booking_id=booking_id)
        # print(updatestatus)
        for x in updatestatus:
            mail55 = x.email
        if completed == 'True':
            completed = True
            send_mailcompleted(request,mail55)
        else:
            completed = False

        # updatestatus = book_service.objects.update_or_create(completed=completed)
        updatestatus.update(completed=completed, pending=False, payment=True)
        # print('record updated')

    return render(request, 'cab/pendingcab.html', context={'user': user,'services': services})

def send_mailcompleted(request,mail55):
    email_subject = 'CAB RIDE COMPLETED'
    html_message = render_to_string('cab/Cab_completion.html')
    email_body = strip_tags(html_message)
    # print(mail44)
    msg = EmailMultiAlternatives(email_subject, email_body, settings.EMAIL_FROM_USER, [mail55])
    # msg = EmailMultiAlternatives(email_subject, email_body, settings.EMAIL_FROM_USER, ['yadavaishwarya42@gmail.com'])
    msg.attach_alternative(html_message, "text/html")
    msg.send()


def advpay_confirm(request):
    global mail44
    email = request.session['email']
    user = cabowner.objects.get(Email=email)
    services = bookedCab.objects.filter(pending=True)
    if request.method == 'POST':
        advpay_confirm = request.POST.get('advpay_confirm')
        booking_id = request.POST.get('booking_id')
        # print(advpay_confirm)
        # print(booking_id)
        pay = bookedCab.objects.filter(booking_id=booking_id)
        # print(pay)
        for x in pay:
            mail44 = x.email
        if advpay_confirm == 'True':
            send_mailadvpayconfirm(request,mail44)

    return render(request, 'cab/pendingcab.html', context={'user': user,'services': services})


def send_mailadvpayconfirm(request,mail44):
    email_subject = 'ADVANCE PAYMENT CONFIRMATION'
    html_message = render_to_string('cab/Cab_advpayconfirm.html')
    email_body = strip_tags(html_message)
    # print(mail44)
    msg = EmailMultiAlternatives(email_subject, email_body, settings.EMAIL_FROM_USER, [mail44])
    # msg = EmailMultiAlternatives(email_subject, email_body, settings.EMAIL_FROM_USER, ['yadavaishwarya42@gmail.com'])
    msg.attach_alternative(html_message, "text/html")
    msg.send()





# completed
def addcab1(request):
    email = request.session['email']
    user = cabowner.objects.get(Email=email)
    if request.method == "POST":
        cab_name = user.CabName
        discount = request.POST['discount']
        category = request.POST['sharing']
        price = request.POST['price']
        des = request.POST['more']
        pick = request.POST['pick']
        drop = request.POST['drop']
        img1 = request.FILES.get('pic1')
        date = datetime.date.today()
        price = int(price) - (int(price) * int(discount) // 100)
        print(request.POST)
        print(request.FILES)

        while True:
            cab_id = "#" + str(random.randint(1000000, 9000000))
            try:
                addcab.objects.get(cab_id=cab_id)
                continue
            except:
                break
        addcab(date=date, PassPickup=pick, PassDrop=drop, cab_id=cab_id, cab_name=cab_name, category=category,
               discount=discount, description=des, email=request.session['email'], price=price, image1=img1,
               verified=False).save()
        return redirect(addedcab)

    return render(request, 'cab/add_cab.html', context={'user': user})


# completed
def addedcab(request):
    email = request.session['email']
    user = cabowner.objects.get(Email=email)
    cabs = addcab.objects.filter(email=email)
    print(cabs)

    P = Paginator(cabs, 10)
    page = request.GET.get('page')
    pagi_rooms = P.get_page(page)

    return render(request, 'cab/addedcab.html', context={'user': user, 'pagi_rooms': pagi_rooms})


# completed
# def cabvendorlisting(request, name):
#     name = name.replace("%20", " ")
#     request.session['cab_name'] = name
#     return redirect(cabdetail)
#

# completed
def cabdetail(request):
    try:
        cabs = addcab.objects.filter(cab_name=request.session['cab_name'], verified=True)
        print(cabs)
        email = request.session['email']
        newcabs = []
        for i in cabs:
            previous = int(100 / (100 - int(i.discount)) * int(i.price))
            newcabs.append((i, previous))
        print("\n\n")
        return render(request, 'cab/cab-form.html', context={'cab_name': request.session['cab_name'], 'cabs': newcabs})
    except:
        return redirect(Cabprofile)


# completed
# def cablisting(request):
#     email = request.session['email']
#     cab = cabowner.objects.filter(isverified=True)
#
#     P = Paginator(cab, 10)
#     page = request.GET.get('page')
#     pagi_rooms = P.get_page(page)
#
#     return render(request, 'cab/cab-cars.html', context={'pagi_rooms': pagi_rooms})
# def allcab(request):
#     rides=bookedCab.objects.all()
#     return render(request,'cab/Caball.html',context={'rides':rides})
#
#
#
# def pendingcab(request):
#     return render(request,'cab/pendingcab.html')
#
# def completedride(request):
#     return render(request,'cab/completedride.html')