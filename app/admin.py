from django.contrib import admin
from . models import Product,Customer ,Cart ,Payment ,OrderPlaced ,Wishlist,Tracking
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.auth.models import Group
 
# Register your models here.
@admin.register(Product) #decorator to register the model
class ProductModel(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','category','description','image']

@admin.register(Customer) #decorator to register the model
class ProductModel(admin.ModelAdmin):
    list_display = ['name','locality','city','mobile','zipcode','state']
     
@admin.register(Cart) #decorator to register the model
class CartModel(admin.ModelAdmin):
    list_display = ['id','user','products','quantity']
    def products(self,obj):
        link=reverse("admin:app_product_change",args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link,obj.product.title)
    
@admin.register(Payment) #decorator to register the model
class PaymentModel(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_id','razorpay_payment_status','paid']
     
@admin.register(OrderPlaced) #decorator to register the model
class OrderPlacedModel(admin.ModelAdmin):
    list_display = ['id','user','customers','products','quantity','ordered_date','status','payments']
    def customers(self,obj):
            link=reverse("admin:app_customer_change",args=[obj.customer.pk])
            return format_html('<a href="{}">{}</a>',link,obj.customer.name)
        
    def products(self,obj):
            link=reverse("admin:app_product_change",args=[obj.product.pk])
            return format_html('<a href="{}">{}</a>',link,obj.product.title)
        
    def payments(self,obj):
            link=reverse("admin:app_payment_change",args=[obj.payment.pk])
            return format_html('<a href="{}">{}</a>',link,obj.payment.razorpay_payment_id)
    
@admin.register(Wishlist)
class WishlistModel(admin.ModelAdmin):
    list_display = ['id','user','product']
    
    
@admin.register(Tracking)
class trackModel(admin.ModelAdmin):
    list_display=['id','user','products','status','planted_date','location','photographic_documentation','maintenance','soil_assessment']
    
    def products(self,obj):
            link=reverse("admin:app_product_change",args=[obj.product.pk])
            return format_html('<a href="{}">{}</a>',link,obj.product.title)
admin.site.unregister(Group)