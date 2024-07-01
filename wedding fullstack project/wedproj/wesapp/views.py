from django.http import JsonResponse
from django.shortcuts import render,redirect
from wesapp.form import CustomUserForm
from wesapp.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    vendors=Traditional.objects.filter(handpicked=1)
    return render(request,"wedding/index.html",{"vendors":vendors})

def fav_view_page(request):
    if request.user.is_authenticated:
        fav= Favourite.objects.filter(user=request.user)
        return render(request,"wedding/fav.html",{"fav":fav})
    else:
        return redirect("/")
  
    
def fav_page(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
       if request.user.is_authenticated:
           data=json.load(request)
           product_id=data['pid']
           #print(request.user.id)
           product_status=Traditional.objects.get(id=product_id)
           if product_status:
               if Favourite.objects.filter(user=request.user,product_id=product_id):
                   return JsonResponse({'status':'Already in favourite'}, status=200)
               else:
                   Favourite.objects.create(user=request.user,product_id=product_id)
                   return JsonResponse({'status':'Added to favourite successfully'}, status=200)
       else:
           return JsonResponse({'status':'Login for adding to favourite'}, status=200)
       
   else:
       return JsonResponse({'status':'Invalid Access'}, status=200)
 
def remove_fav(request,favid):
    favitem=Favourite.objects.get(id=favid)
    favitem.delete()
    return redirect("/fav_view_page")
   
def cart_page(request):
    if request.user.is_authenticated:
        cart= Carts.objects.filter(user=request.user)
        return render(request,"wedding/cart.html",{"cart":cart})
    else:
        return redirect("/")
   
def remove_cart(request,cartid):
    cartitem=Carts.objects.get(id=cartid)
    cartitem.delete()
    return redirect("/cart")

def add_to_cart(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
       if request.user.is_authenticated:
           data=json.load(request)
           product_id=data['pid']
           #print(request.user.id)
           product_status=Traditional.objects.get(id=product_id)
           if product_status:
               if Carts.objects.filter(user=request.user,product_id=product_id):
                   return JsonResponse({'status':'Already in cart'}, status=200)
               else:
                   Carts.objects.create(user=request.user,product_id=product_id)
                   return JsonResponse({'status':'Added to cart successfully'}, status=200)
       else:
           return JsonResponse({'status':'Login for adding to cart'}, status=200)
       
   else:
       return JsonResponse({'status':'Invalid Access'}, status=200)
       
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully!!")
        return redirect("/")
        
def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully!!")
                return redirect("/")
            else:
                messages.error(request,"Invalid Username or  Password")
                return redirect("login")
        return render(request,"wedding/login.html")

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration success you can login now..!! ")
            return redirect('/login')
        
    return render(request,"wedding/register.html",{'form':form})

def vendor(request):
    wedding=Wedding.objects.filter(status=0)
    return render(request,"wedding/vendor.html",{"wedding":wedding})


def vendorview(request,name):
    if(Wedding.objects.filter(name=name,status=0)):
        vendors=Traditional.objects.filter(category__name=name,status=0)
        return render(request,"wedding/vendors/v_index.html",{"vendors":vendors,"wedding_name":name})
    else:
        messages.warning(request,"No Such details found")
        return redirect('vendor')


def vendor_details(request,cname,vname):
    if(Wedding.objects.filter(name=cname,status=0)):
        if(Traditional.objects.filter(name=vname,status=0)):
            products=Traditional.objects.filter(name=vname,status=0).first()
            return render(request,"wedding/vendors/vendor_details.html",{"products":products})
        else:
            messages.warning(request,"No Such details found")
            return redirect('vendor')
    else:
        messages.warning(request,"No Such halls found")
        return redirect('vendor')
   

@login_required(login_url='login') 

def checkout(request):
    rawcart=Carts.objects.filter(user=request.user)
    for item in rawcart:
        if item.product==True:
            Carts.objects.delete(id=item.id)
    cartitems = Carts.objects.filter(user=request.user)
    total_price= 0
    for item in cartitems:
        total_price= total_price + item.product.dis_price
    
    
    
    context={'cartitems':cartitems , 'total_price' : total_price}
    return render(request, "wedding/checkout.html", context)
    

@login_required(login_url='login')
def placeorder(request):
    if request.method == 'POST':
        neworder = Order()
        neworder.user=request.user
        neworder.gname = request.POST.get('gname')
        neworder.bname = request.POST.get('bname')
        neworder.email = request.POST.get('email')
        neworder.occ_date = request.POST.get('occ_date')

        cart = Carts.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.dis_price
        neworder.total_price = cart_total_price
        neworder.save()

        neworderitems = Carts.objects.filter(user=request.user)
        for item in neworderitems:
            OdrderItem.objects.create(
                order = neworder,
                product = item.product,
                price = item.product.dis_price
                
            )
    
        #  To clear user's cart
        Carts.objects.filter(user=request.user).delete()
        
        messages.success(request, "Your order has been confirmed!")
        
        
        
        return redirect('/')  


# client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY,settings.RAZORPAY_API_SECRET_KEY))
# @login_required(login_url='login')
# def proceed_to_pay(request):
#     cart =Carts.objects.filter(user=request.user)
#     total_price = 0
#     for item in cart :
#         total_price = total_price + item.product.dis_price
#     if request.method == "POST":    
#         data={"amount":150000,"currency":"INR", "receipt": "order_recipt_11"}
#         payment = client.order.create(data=data)
#         razorpay_payment_id=payment['id']
#         context={'amount':100,
#              'api_key':settings.RAZORPAY_API_KEY,
#              'order_id':razorpay_payment_id,}
#         return JsonResponse({
#             'total_price' : total_price(request,context)
#         })
   
def myorder(request):
    orders = Order.objects.filter(user=request.user)
    context={"orders":orders}
    return render(request,"wedding/myorder.html",context)

def orderview(request,price):
    order = Order.objects.filter(total_price=price).filter(user=request.user).first()
    orderitem= OdrderItem.objects.filter(order=order)
    context = { 'order':order, 'orderitem':orderitem }
    return render(request, "wedding/orderview.html",context)