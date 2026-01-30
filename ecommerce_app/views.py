from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import login ,logout

from ecommerce_app.models import category_model, product_model

def display (request):
    return render (request, 'home.html')

def loginload (request):
    return render (request, 'login.html')


def signupload (request):
    return render (request, 'signup.html')

def admin_load(request):
    return render (request, 'admin_home.html')

def user_load(request):
    products = product_model.objects.all()
    return render (request, 'user_home.html',{'products':products})


def signup(request):
    if request.method=='POST':
        sname=request.POST.get('fname')
        slname=request.POST.get('lname')
        usname=request.POST.get('username')
        smail=request.POST.get('mail')
        spass=request.POST.get('pass')
        cspass=request.POST.get('conpass')
        if spass==cspass:
            if User.objects.filter(username=usname).exists():
                messages.info(request,'username already exist')
                return redirect ('signupload')
            else:
                user=User.objects.create_user(
                    first_name=sname,
                    last_name=slname,
                    username=usname,
                    email=smail,
                    password=spass

                )
                user.save()
                return redirect ('loginload')
        else:
            messages.info(request,'password not match')
            return redirect ('signupload')


def log_in (request):    
    if request.method=='POST':
        name=request.POST.get('uname')
        upass=request.POST.get('pass')
        user=auth.authenticate(username=name,password=upass)
        if user is not None :
            if user.is_staff:
                 login (request,user)
                 return redirect ('admin_load')
            else:
                 auth.login(request,user)
                 return redirect ('pro_list')



    
def add_cat(request):
    return render (request,'category.html')
   

def store_category(request):
    if request.method=='POST':
        cname=request.POST.get('name')
        cstore=request.POST.get('store')
        category=category_model(
            cat_name=cname,
            cat_store=cstore
            )
        category.save()
        return redirect ('admin_load')



def cat_list_load(request):
    li=category_model.objects.all()
    return render (request, 'cat_list.html', {'a':li} )

def list_cat(request):
    li=category_model.objects.all()
    return render (request,'cat_list.html',{'a':li})


def add_product(request):
    i=category_model.objects.all()
    return render (request , 'product_add.html',{'a':i})



def product_add(request):
    if request.method=='POST':
        pname=request.POST.get('name')
        pquantity=request.POST.get('quantity')
        pprice=request.POST.get('price')
        pimage=request.FILES.get('image')
        pcat=request.POST.get('product_cat')
        productcategory=category_model.objects.get(id=pcat)
        products=product_model(
            product_name=pname,
            product_quantity=pquantity,
            product_price=pprice,
            product_image=pimage,
            cat_table=productcategory
            )
        products.save()
        return redirect ('admin_load')
    


def pro_list_load(request):
    pro=product_model.objects.all()
    return render (request, 'product_list.html',{'i':pro})

# def pro_list(request):
#     pro=product_model.objects.all()
#     return render (request , 'product_list.html',{'i':pro})



def edit_load(request,pk):
    edit=product_model.objects.get(id=pk)
    category=category_model.objects.all()
    return render (request,'edit.html',{'prod':edit,'a':category}) 

def edit(request,pk):
    if request.method=='POST':
        prod=product_model.objects.get(id=pk)
        prod.product_name=request.POST.get('name')
        prod.product_quantity=request.POST.get('quantity')
        prod.product_image=request.FILES.get('image')
        prod.product_price=request.POST.get('price')
        prod_cat_table=request.POST.get('product_cat')
        cat_obj=category_model.objects.get(id=prod_cat_table)
        prod.cat_name=cat_obj
        prod.save()
        return redirect ('pro_list_load')
        

def pro_list(request):
    pro=product_model.objects.all()
    return render (request, 'user_home.html',{'i':pro})

# def user_pro(request):
#     produ=product_model.objects.all()
#     return render (request,'user_home_html',{'i':produ})
    

def pro_list(request):
    products = product_model.objects.all()
    return render(request, 'user_home.html', {'products': products})

# <input type="file"   name="image"  value="{{infor.stimage}}">
#            {% if infor.stimage %}

#         <img src="{{infor.stimage.url}}" alt="">
#           {% else %}
#         <p>No image uploaded</p>
#     {% endif %}
# Create your views here.AC

def buy_now(request):
    return render (request,'buy_now.html')