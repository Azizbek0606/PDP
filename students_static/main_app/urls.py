from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *

app_name='main_app'

urlpatterns = [
    path('' , homePageView , name='home'),
    path("del/std/<int:std_id>", del_std , name='del_std'),
    path('std/<pk>', full_std_about , name='full_std_about'),
    path("std/com/<pk>" , add_new_coment , name='add_new_coment'),
    path('cards/' , cards , name='card'),
    path('com/del/<pk>' , del_com , name='del_com'),
    path('filter/payment/true/' , filter_payment_true , name='filter_payment_true'),
    path('filter/payment/false/' , filter_payment_false , name='filter_payment_false'),
    path('filter/age15/' , filter_age15 , name='filter_age15'),
    path('filter/age18/' , filter_age15 , name='filter_age18'),
    path('filter/age20/' , filter_age20 , name='filter_age20'),
    path('filter/lvl/green/' , filter_lvl_green , name='filter_lvl_green'),
    path('filter/lvl/yellow/' , filter_lvl_yellow , name='filter_lvl_yellow'),
    path('filter/lvl/red/' , filter_lvl_red , name='filter_lvl_red'),
    path('filter/lvl/green/' , filter_lvl_green , name='filter_lvl_green'),
    path('search/method/' , search_method , name='search_method'),
    path("update/students/<pk>", Update_student_profile.as_view(), name='update'),
    path("add/students", add_new_student, name='create'),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'), name='logout'),    
]
