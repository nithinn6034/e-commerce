
from django.urls import path

from ecommerce_app import views

urlpatterns = [

    path('',views.display,name='display'),
    path('loginload',views.loginload,name='loginload'),
    path('signupload',views.signupload,name='signupload'),
    path('signup',views.signup,name='signup'),
    path('admin_load',views.admin_load,name='admin_load'),
    path('user_load',views.user_load,name='user_load'),
    path('log_in',views.log_in,name='log_in'),
    path('add_cat',views.add_cat,name='add_cat'),
    path('store_category',views.store_category,name='store_category'),
    path('cat_list_load',views.cat_list_load,name='cat_list_load'),
    path('list_cat',views.list_cat,name='list_cat'),
    path('add_product',views.add_product,name='add_product'),
    path('product_add',views.product_add,name='product_add'),
    path('pro_list_load',views.pro_list_load,name='pro_list_load'),
    path('edit_load/<int:pk>',views.edit_load,name='edit_load'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('pro_list',views.pro_list,name='pro_list'),
    path('buy_now',views.buy_now,name='buy_now')

]
