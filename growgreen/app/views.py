from django.shortcuts import render ,redirect
from django.views import View
from .forms import CustomerRegistrationForm ,CustomerProfileForm 
from django.contrib import messages
from .models import Product,Customer,Cart ,Payment,OrderPlaced ,Wishlist ,Tracking
from django.http import JsonResponse
from django.db.models import Q
import razorpay
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@login_required
# Create your views here.
def home(request):
    totalitem=0
    wishitem=0

    if request.user.is_authenticated:
        totalitem= len(Cart.objects.filter(user=request.user))
        wishitem=  len(Wishlist.objects.filter(user=request.user))

    return render(request,"app/Home.html",locals())  

# Create your views here.
@login_required
def about(request):
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
        totalitem= len(Cart.objects.filter(user=request.user))
        wishitem=  len(Wishlist.objects.filter(user=request.user))
    return render(request,"app/about.html",locals())

# Create your views here.
@login_required
def contact(request):
    totalitem=0
    wishitem=0
    
    if request.user.is_authenticated:
        totalitem= len(Cart.objects.filter(user=request.user))
        wishitem=  len(Wishlist.objects.filter(user=request.user))

    return render(request,"app/contact.html",locals())

@method_decorator(login_required,name='dispatch')
class CategoryView(View):
    def get(self,request,val):
        totalitem=0
        wishitem=0

        if request.user.is_authenticated:
            totalitem= len(Cart.objects.filter(user=request.user))
            wishitem=  len(Wishlist.objects.filter(user=request.user))

        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())
    
@method_decorator(login_required,name='dispatch')
class TitleView(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        totalitem=0
        wishitem=0

        if request.user.is_authenticated:
          totalitem= len(Cart.objects.filter(user=request.user))
          wishitem=  len(Wishlist.objects.filter(user=request.user))
 
        return render(request,"app/category.html",locals())

@method_decorator(login_required,name='dispatch')
class ProductDetailView(View):  
    def get(self,request,id):
        product= Product.objects.get(id=id)
        wishlist= Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
        totalitem=0
        wishitem=0

        if request.user.is_authenticated:
            totalitem= len(Cart.objects.filter(user=request.user))
            wishitem=  len(Wishlist.objects.filter(user=request.user))
 
        return render(request,"app/productdetail.html",locals())
        
 
class CustomerRegistrationView(View):
    def get(self,request):
        forms = CustomerRegistrationForm()
        return render(request,"app/customerregistration.html",locals())
    def post(self,request):
        forms = CustomerRegistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request,"Congratulations!! Registered Successfully... Sign In Now ..")
        else :
            messages.warning(request,"Invalid Form") 
        return render(request,"app/customerregistration.html",locals())

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    
    def get(self,request):
        forms= CustomerProfileForm()
        totalitem=0
        wishitem=0
        additem=0

        if request.user.is_authenticated:
            totalitem= len(Cart.objects.filter(user=request.user))
            wishitem=  len(Wishlist.objects.filter(user=request.user))
            additem=  len(Customer.objects.filter(user=request.user))

      
        return render(request,"app/profile.html",locals())
    
    
    
    def post(self,request):
        forms= CustomerProfileForm(request.POST)
        additem =0 
        if request.user.is_authenticated:
            additem=  len(Customer.objects.filter(user=request.user))

        if forms.is_valid():
            user= request.user
            name= forms.cleaned_data['name']
            locality= forms.cleaned_data['locality']
            city= forms.cleaned_data['city']
            mobile= forms.cleaned_data['mobile']
            state= forms.cleaned_data['state']
            zipcode= forms.cleaned_data['zipcode']  
            
            reg=Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations!! Profile Updated Successfully")
        else :
            messages.warning(request,"Invalid Input Data")
        return render(request,"app/profile.html",locals())

@login_required
def address(request):
    add=Customer.objects.filter(user=request.user)
    totalitem=0
    wishitem=0
    additem=0

    if request.user.is_authenticated:
        totalitem= len(Cart.objects.filter(user=request.user))
        wishitem=  len(Wishlist.objects.filter(user=request.user))
        additem=  len(Customer.objects.filter(user=request.user))
  
    return render(request,"app/address.html",locals())

@method_decorator(login_required,name='dispatch')
class UpdateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk) # pk is the primary key
        forms= CustomerProfileForm(instance=add) # instance is used to show the data in the form
        totalitem=0
        wishitem=0

        if request.user.is_authenticated:
            totalitem= len(Cart.objects.filter(user=request.user))
            wishitem=  len(Wishlist.objects.filter(user=request.user))
 
        return render(request,"app/updateaddress.html",locals()) 
    def post(self,request,pk):
        forms = CustomerProfileForm(request.POST) 
        if forms.is_valid():
            add = Customer.objects.get(pk=pk) # add is the object of the Customer class and pk is the primary key 
            add.name= forms.cleaned_data['name']
            add.locality= forms.cleaned_data['locality']
            add.city= forms.cleaned_data['city']
            add.mobile= forms.cleaned_data['mobile']
            add.state= forms.cleaned_data['state']
            add.zipcode= forms.cleaned_data['zipcode']  
            add.save()
            messages.success(request,"Congratulations!! Address Updated Successfully")
        else :
            messages.warning(request,"Invalid Input Data")
         
        return  redirect('address')
         
@login_required  
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Cart(user=user,product=product).save() 
    return redirect('/showcart') # explain this line of code 
 
@login_required
def show_cart(request):
    user = request.user
    cart=Cart.objects.filter(user=user)
    amount =0
    totalitem=0
    wishitem=0

    if request.user.is_authenticated:
        totalitem= len(Cart.objects.filter(user=request.user))
        wishitem=  len(Wishlist.objects.filter(user=request.user))
 
    for p in cart:
        amount += p.product.discounted_price * p.quantity
    totalamount=amount+40
    return render(request,"app/addtocart.html",locals())

@login_required
def wishlist(request):
    user = request.user
    totalitem=0
    wishitem=0 

    if request.user.is_authenticated:
        totalitem= len(Cart.objects.filter(user=request.user))
        wishitem=  len(Wishlist.objects.filter(user=request.user))
    product = Wishlist.objects.filter(user=user)
    return render(request,"app/wishlist.html",locals())


@method_decorator(login_required,name='dispatch')
class checkout(View):
    def get(self,request):
        user = request.user
        cart=Cart.objects.filter(user=user)
        add=Customer.objects.filter(user=user)
        amount =0
        totalitem=0
        wishitem=0

        if request.user.is_authenticated:
            totalitem= len(Cart.objects.filter(user=request.user))
            wishitem=  len(Cart.objects.filter(user=request.user))
 
        for p in cart:
            amount += p.product.discounted_price * p.quantity
        totalamount=amount+40
        razoramount=int(totalamount*100)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        data={"amount":razoramount,"currency":"INR","receipt":"order_rcptid_11"}
        payment_response=client.order.create(data=data)
        print(payment_response)
        
        order_id=payment_response['id']
        order_status=payment_response['status']
        if order_status=="created":
            payment= Payment( 
                user=user,
                amount=totalamount,
                razorpay_order_id=order_id,
                razorpay_payment_status=order_status
                )
            payment.save()
        return render(request,"app/checkout.html",locals())

@login_required
def payment_done(request):
    # to get the data from the razorpay
    order_id=request.GET.get('order_id')
    payment_id=request.GET.get('payment_id')
    cust_id=request.GET.get('cust_id')
    # to save the data in the database
    user= request.user
    customer=Customer.objects.get(id=cust_id)
    payment=Payment.objects.get(razorpay_order_id=order_id)
    payment_paid=True
    payment.razorpay_payment_id=payment_id
    payment.save()
    # to move the data from the cart to the orderplaced and filter the data from the cart   
    cart=Cart.objects.filter(user=user)
    # to save the data in the orderplaced and remove the data from the cart
    for c in cart:
     OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity,payment=payment).save()
    c.delete()
    return redirect("orders")

@login_required
def orders(request):
    orderplaced=OrderPlaced.objects.filter(user=request.user)
    totalitem=0
    if request.user.is_authenticated:
        totalitem= len(Cart.objects.filter(user=request.user))
        wishitem=  len(Wishlist.objects.filter(user=request.user))

    return render(request,"app/orders.html",locals()) 
  
  
@login_required  
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user)) # Q is used to use multiple conditions
        c.quantity+=1
        c.save()
        amount =0
        cart=Cart.objects.filter(user=request.user)
        for p in cart:
            amount += p.product.discounted_price * p.quantity
        totalamount=amount+40
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
            }
        return JsonResponse(data) # explain this line of code
    
@login_required  
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user)) # Q is used to use multiple conditions
        c.quantity-=1
        c.save()
        amount =0
        cart=Cart.objects.filter(user=request.user)
        for p in cart:
            amount += p.product.discounted_price * p.quantity
        totalamount=amount+40
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
            }
        return JsonResponse(data) # explain this line of code
    
@login_required     
def removecart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user)) # Q is used to use multiple conditions
        c.delete()
        amount =0
        cart=Cart.objects.filter(user=request.user)
        for p in cart:
            amount += p.product.discounted_price * p.quantity
        totalamount=amount+40
        data = {
            'amount':amount,
            'totalamount':totalamount
            }
        return JsonResponse(data) # explain this line of code
  

@login_required
def plus_wishlist(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        product=Product.objects.get(id=prod_id)
        user=request.user
        Wishlist(user=user,product=product).save()
        data={
            'message':'product added to wishlist Successfully'
        }
        return JsonResponse(data)
        
@login_required
def minus_wishlist(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        product=Product.objects.get(id=prod_id)
        user=request.user
        Wishlist.objects.filter(user=user,product=product).delete()
        data={
            'message':'product removed from  wishlist Successfully'
        }
        return JsonResponse(data)
        
@login_required      
def search(request):
    query=request.GET['search']
    product=Product.objects.filter(title__icontains=query)
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
        totalitem= len(Cart.objects.filter(user=request.user))
        wishitem=  len(Wishlist.objects.filter(user=request.user))
 
    return render(request,"app/search.html",locals())

@method_decorator(login_required,name='dispatch')
class TrackView(View):
    def get(self,request):
        trackdata=Tracking.objects.filter(user=request.user)

        totalitem=0
        wishitem=0

        if request.user.is_authenticated:
            totalitem= len(Cart.objects.filter(user=request.user))
            wishitem=  len(Wishlist.objects.filter(user=request.user))

       
        return render(request,"app/track.html",locals())