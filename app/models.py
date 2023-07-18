from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('LC','Location'),
    ('ZD','Zordiac'),
    ('NS','Native Species'),
    ('FE','Festivals'),
    ('OT','Other'),
)
STATE_CHOICES = (
    ('Aandra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Karnataka','Karnataka'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Kerala','Kerala'),
    ('Gujarat','Gujarat'),
    ('Rajasthan','Rajasthan'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Bihar','Bihar'),
    ('West Bengal','West Bengal'),
    ('Odisha','Odisha'),
    ('Assam','Assam'),
    ('Punjab','Punjab'),
    ('Haryana','Haryana'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Uttarakhand','Uttarakhand'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Tripura','Tripura'),
    ('Meghalaya','Meghalaya'),
    ('Manipur','Manipur'),
    ('Nagaland','Nagaland'),
    ('Goa','Goa'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Mizoram','Mizoram'),
    ('Sikkim','Sikkim'),
    ('Delhi','Delhi'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Puducherry','Puducherry'),
    ('Chandigarh','Chandigarh'),
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
)

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
    ('Out for Delivery','Out for Delivery'),
    ('Return','Return')
)
PLANT_STATUS_CHOICES = (
    ('Planted', 'Planted'),
    ('On The Way', 'On The Way'),
    ('Pending', 'Pending'),
    ('Growing', 'Growing'),
    ('Diseased', 'Diseased'),
    ('Harvested', 'Harvested'), 
) 


ACTIVITIES_CHOICES = (
    ('Watering', 'Watering'),
    ('Pruning', 'Pruning'),
    ('Fertilizing', 'Fertilizing'),
    ('Mulching', 'Mulching'),
    ('Weeding', 'Weeding'),
    ('Pest Control', 'Pest Control'),
)

SOIL_ACTIVITIES_CHOICES = (
    ('Soil Testing', 'Soil Testing'),
    ('Composting', 'Composting'),
    ('Aerating Soil', 'Aerating Soil'),
    ('pH Adjustment', 'pH Adjustment'),  
    ('Soil Moisture Monitoring', 'Soil Moisture Monitoring'),
    ('Soil Drainage Improvement', 'Soil Drainage Improvement'),  
)

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100)  
    def  _str_(self):
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField()
    razorpay_order_id =models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id=models.CharField(max_length=100,blank=True,null=True)   
    paid=models.BooleanField(default=False)
    
class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE, default="")

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    
class Tracking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, default=None)
    status=models.CharField(max_length=50,choices=PLANT_STATUS_CHOICES,default='Pending')
    planted_date=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=100)
    photographic_documentation=models.ImageField(upload_to='product')
    maintenance=models.CharField(max_length=100,choices=ACTIVITIES_CHOICES,default="Pending")
    soil_assessment=models.CharField(max_length=100,choices=SOIL_ACTIVITIES_CHOICES,default="Pending")