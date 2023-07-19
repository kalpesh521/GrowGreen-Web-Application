from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . forms import Loginform ,MyPasswordChangeForm ,MyPasswordResetForm ,MyPasswordSetForm

urlpatterns = [
    path('',views.home),
    path('about/',views.about,name='about'),
    path('contact/',views.contact ,name='contact'),
    path('category/<slug:val>',views.CategoryView.as_view(),name='category'),
    path('category-title/<val>',views.TitleView.as_view(),name='category-title'),
    path('productdetails/<int:id>',views.ProductDetailView.as_view(),name='product-detail'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('updateaddress/<int:pk>',views.UpdateAddress.as_view(),name='updateaddress'),

    # Cart
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('showcart/',views.show_cart,name='showcart'),
    path('checkout/',views.checkout.as_view(),name='checkout'),
    path('paymentdone/',views.payment_done,name='paymentdone'),
    path('orders/',views.orders,name='orders'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.removecart),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('pluswishlist/',views.plus_wishlist),
    path('minuswishlist/',views.minus_wishlist),
    path('track/',views.TrackView.as_view(),name='track'),
    
    
    
    # Authentication
    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),
    
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=Loginform),name='login'),
    
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/passwordreset.html',form_class=MyPasswordResetForm),name='password_reset'),
    
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm ,success_url='/passwordchangedone'),name='passwordchange'),
    
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/passwordresetdone.html'),name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/passwordresetconfirm.html',form_class=MyPasswordSetForm),name='password_reset_confirm'),
    
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/passwordresetcomplete.html'),name='password_reset_complete'),
    
    path('search/',views.search,name='search')
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



admin.site.site_header = "GrowGreen Admin"
admin.site.site_title = "GrowGreen Admin Portal"
admin.site.index_title = "Welcome to GrowGreen Portal"

