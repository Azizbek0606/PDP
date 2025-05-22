from django.urls import path
from main import views

app_name="main"

urlpatterns = [
    path("", views.home, name="home"),
    path("orders/", views.orders, name="orders"),
    path('order/dashboard/', views.orders_dashboard , name="order_dashboard"),
    path("inventory/", views.inventory, name="inventory"),
    path("inventory/products/", views.products, name="products"),
    path("inventory/categories/", views.categories, name="categories"),
    path("inventory/stock-levels/", views.stock_levels, name="stock_levels"),
    path("employees/", views.employees, name="employees"),
    path("reports/", views.reports, name="reports"),
    path("settings/", views.settings, name="settings"),
    path("settings/system/", views.system_settings, name="system_settings"),
    path("settings/user-management/", views.user_management, name="user_management"),
    path("settings/integrations/", views.integrations, name="integrations"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.user_register, name="register")
]
