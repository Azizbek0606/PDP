from django.urls import path
from main import views

app_name="main"

urlpatterns = [
    path("", views.home, name="home"),
    path("orders/", views.orders, name="orders"),
    path('order/dashboard/', views.orders_dashboard , name="order_dashboard"),
    path("inventory/", views.inventory, name="inventory"),
    path("inventory/products/", views.products, name="products"),
    path("employees/", views.employees, name="employee"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.user_register, name="register")
]
