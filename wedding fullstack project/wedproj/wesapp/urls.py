from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('register/',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('cart',views.cart_page,name="cart"),
    path('remove_cart/<str:cartid>',views.remove_cart,name="remove_cart"),
    path('fav',views.fav_page,name="fav"),
    path('fav_view_page',views.fav_view_page,name="fav_view_page"),
    path('remove_fav/<str:favid>',views.remove_fav,name="remove_fav"),
    path('vendor',views.vendor,name="vendor"),
    path('vendor/<str:name>',views.vendorview,name="vendor"),
    path('vendor/<str:cname>/<str:vname>',views.vendor_details,name="vendor_details"),
    path('checkout',views.checkout,name="checkout"),
    path('placeorder',views.placeorder,name="placeorder"),
    # path('proceed_to_pay',views.proceed_to_pay,name="proceed_to_pay"),
    path('placeorder',views.placeorder,name="placeorder"),
    path('myorder',views.myorder,name="myorder"),
    path('orderview/<str:price>',views.orderview,name="orderview"),
    

    

]
