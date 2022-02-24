from random import randint
from tracemalloc import get_traced_memory
from django.shortcuts import redirect, render
from random import randint
from django.conf import settings
from django.core.mail import send_mail
# from ..reseller import models
# from e_commerce.reseller.models import Resellers
from django.utils.crypto import get_random_string

from reseller.models import Resellers
from .models import Customer

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):

    if request.method=='POST':

        user_type=request.POST['user_type']
        
        if user_type=='customer':
        
            first_name=request.POST['first_name'].lower()
            last_name=request.POST['last_name'].lower()
            gender=request.POST['gender']
            dob=request.POST['dob']
            addr=request.POST['addr']
            country=request.POST['country']
            mobile=request.POST['mobile']
            email=request.POST['email']
            password=request.POST['password']
            
            customer_exist=Customer.objects.filter(email=email).exists()

            if not customer_exist:
                otp = randint(1000, 9999)
                send_mail(
                    'please verify your otp',
                    str(otp),
                    settings.EMAIL_HOST_USER,
                    [email],
                    
                )
                customer_data=Customer(first_name=first_name,last_name=last_name,gender=gender,
                user_type=user_type,email=email,dob=dob,address=addr,country=country,mobile=mobile,passwd=password,status='otpverify', otp=str(otp))


                customer_data.save()

                customer=Customer.objects.get(email=email)

                request.session['cust_id']=customer.id

                return redirect('customer:verify_otp')

        if user_type=='reseller':

            cmp_name=request.POST['cmp_name']
            cmp_reg=request.POST['cmp_reg']
            cmp_addr=request.POST['addr']
            country=request.POST['country']
            mobile=request.POST['mobile']
            email=request.POST['email']
            acc_holder=request.POST['acc_name']
            acc_no=request.POST['acc_no']
            acc_ifsc=request.POST['acc_ifsc']
            password=request.POST['password']
            log_id=randint(1000, 9999)

            reseller_exist=Resellers.objects.filter(email=email).exists()

            if not reseller_exist:
                reseller=Resellers(cmp_name=cmp_name,company_regid=cmp_reg,cmp_addr=cmp_addr,
                country=country,cmp_phno=mobile,acc_no=acc_no,acc_holder=acc_holder,acc_ifsc=acc_ifsc,user_type=user_type,
                email=email,user_id=log_id,passwd=password)

                reseller.save()
                subject='You Login ID is '+str(log_id)
                send_mail(
                    'login credentials',
                    subject,
                    settings.EMAIL_HOST_USER,
                    [email],
                    
                )
                msg='Registration Successfull'
            else:
                msg='Email Exist'   
            return render(request,'signup.html',{'msg':msg,})

    return render(request,'signup.html')

def login(request):

    if request.method=='POST':
        
        user_name=request.POST['user_name']
        passwd=request.POST['passwd']

        if '@' in user_name:
            customer_exist=Customer.objects.filter(email=user_name,passwd=passwd).exists()
            if customer_exist:
                customer=Customer.objects.get(email=user_name,passwd=passwd)
                request.session['cust_id']=customer.id
                if customer.status=='otpverify':
                    otp = randint(1000, 9999)
                    send_mail(
                        'please verify your otp',
                        str(otp),
                        settings.EMAIL_HOST_USER,
                        [customer.email],
                        fail_silently=False,
                    )
                    customer.otp=otp
                    customer.save()
                    return redirect('customer:verify_otp')
                return redirect('customer:cust_home')
            else:
                return render(request, 'login.html', {'error': 'Invalid user details'})
                
        elif user_name.isdigit():

            seller_exist=Resellers.objects.filter(user_id=user_name).exists()
            if seller_exist:
                seller_data=Resellers.objects.get(user_id=user_name,passwd=passwd)
               
                if seller_data.status=='active':
                    request.session['s_id']=seller_data.id
                    return redirect('reseller:reseller_home')
                else:
                     
                    return render(request, 'login.html', {'error': 'Account Not Approved Yet'})
            else:
                    return render(request, 'login.html', {'error': 'UserName Or Password Incorrect'})


    return render(request,'login.html')

def verify_otp(request):
    
    if request.method=='POST':

        otp = request.POST['inp_otp']
        c_id=request.session['cust_id']
        data=Customer.objects.get(id=c_id)
       
        if otp==data.otp:
            Customer.objects.filter(id=c_id).update(status='active')
            return redirect('customer:cust_home')
        else:
            return render(request, "verify_otp.html", {"msg": "Invalid otp"})
    return render(request,'verify_otp.html')

def customer_home(request):
    return render(request,'home.html')

def cust_logout(request):
    if 'cust_id' in request.session:
        del request.session['cust_id']
        request.session.flush()
    return redirect('customer:index')