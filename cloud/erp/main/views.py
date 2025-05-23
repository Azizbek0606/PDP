from django.shortcuts import render, redirect
from django.db.models import Count, Sum, Avg
from .models import Customer, Supplier, Product, Order, OrderItem, Transaction, Admin, Employee
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import timedelta
import json


def home(request):
    # Umumiy statistika
    total_customers = Customer.objects.count()
    total_suppliers = Supplier.objects.count()
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    total_transactions = (
        Transaction.objects.aggregate(total_amount=Sum("amount"))["total_amount"] or 0
    )

    # Buyurtma statuslari
    order_statuses = Order.objects.values("status").annotate(count=Count("status"))
    status_counts = {status["status"]: status["count"] for status in order_statuses}
    status_data = {
        "labels": ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"],
        "data": [
            status_counts.get("PENDING", 0),
            status_counts.get("PROCESSING", 0),
            status_counts.get("SHIPPED", 0),
            status_counts.get("DELIVERED", 0),
            status_counts.get("CANCELLED", 0),
        ],
    }

    # Mahsulot kategoriyalari
    product_categories = Product.objects.values("category").annotate(
        count=Count("category")
    )
    category_counts = {
        cat["category"]: cat["count"] for cat in product_categories if cat["category"]
    }

    # Kam qolgan mahsulotlar
    low_stock_products = Product.objects.filter(stock_quantity__lt=20)

    # So'nggi buyurtmalar
    recent_orders = Order.objects.select_related("customer").order_by("-order_date")[:5]

    # So'nggi tranzaksiyalar
    recent_transactions = Transaction.objects.select_related(
        "order__customer"
    ).order_by("-transaction_date")[:5]

    # Yil bo'yicha umumiy sotuvlar (oxirgi 5 yil)
    current_year = timezone.now().year
    yearly_sales = (
        Order.objects.filter(order_date__year__gte=current_year - 4)
        .extra(select={"year": "strftime('%%Y', order_date)"})
        .values("year")
        .annotate(total_amount=Sum("total_amount"))
        .order_by("year")
    )
    yearly_sales_data = {
        "labels": [sale["year"] for sale in yearly_sales],
        "data": [float(sale["total_amount"] or 0) for sale in yearly_sales],
    }

    # Oy bo'yicha umumiy sotuvlar (joriy yil)
    monthly_sales = (
        Order.objects.filter(order_date__year=current_year)
        .extra(select={"month": "strftime('%%m', order_date)"})
        .values("month")
        .annotate(total_amount=Sum("total_amount"))
        .order_by("month")
    )
    monthly_sales_data = {
        "labels": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
        "data": [0] * 12,
    }
    for sale in monthly_sales:
        month_idx = int(sale["month"]) - 1
        monthly_sales_data["data"][month_idx] = float(sale["total_amount"] or 0)

    # Kontekst
    context = {
        "total_customers": total_customers,
        "total_suppliers": total_suppliers,
        "total_products": total_products,
        "total_orders": total_orders,
        "total_transactions": total_transactions,
        "status_data": json.dumps(status_data),
        "product_categories": category_counts,
        "low_stock_products": low_stock_products,
        "recent_orders": recent_orders,
        "recent_transactions": recent_transactions,
        "product_categories_json": json.dumps(category_counts),
        "yearly_sales_data": json.dumps(yearly_sales_data),
        "monthly_sales_data": json.dumps(monthly_sales_data),
    }

    return render(request, "index.html", context)


@login_required
def orders(request):
    status_filter = request.GET.get('status', '')
    if status_filter:
        orders_list = Order.objects.filter(status=status_filter).select_related('customer').order_by('-order_date')
    else:
        orders_list = Order.objects.select_related('customer').order_by('-order_date')
    paginator = Paginator(orders_list, 30)
    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)
    status_choices = Order.STATUS_CHOICES

    context = {
        'orders': orders,
        'status_choices': status_choices,
        'current_status': status_filter,
    }
    return render(request, 'orders.html', context)


@login_required
def orders_dashboard(request):
    today = timezone.now().date()
    year_start = today.replace(month=1, day=1)
    monthly_orders = (
        Order.objects.filter(order_date__gte=year_start)
        .extra(select={"month": "strftime('%%m', order_date)"})
        .values("month")
        .annotate(order_count=Count("id"), total_amount=Sum("total_amount"))
        .order_by("month")
    )
    status_distribution = (
        Order.objects.values("status").annotate(count=Count("id")).order_by("-count")
    )
    top_status = (
        status_distribution.first()
        if status_distribution
        else {"status": "N/A", "count": 0}
    )

    top_customers = Customer.objects.annotate(
        order_count=Count("orders"), total_spent=Sum("orders__total_amount")
    ).order_by("-order_count", "-total_spent")[:5]

    top_suppliers = (
        Supplier.objects.annotate(
            total_quantity=Sum("products__orderitem__quantity"),
            total_revenue=Sum("products__orderitem__total_price"),
        )
        .filter(total_quantity__gt=0)
        .order_by("-total_quantity")[:5]
    )

    context = {
        "monthly_orders": monthly_orders,
        "status_distribution": status_distribution,
        "top_status": top_status,
        "top_customers": top_customers,
        "top_suppliers": top_suppliers,
        "current_year": today.year,
    }

    return render(request, "orders_dashboard.html", context)


def inventory(request):
    categories = ["T-Shirts", "Pants", "Jackets", "Shoes", "Accessories"]

    category_counts = Product.objects.filter(
        category__in=categories
    ).values('category').annotate(
        product_count=Count('id')
    ).order_by('-product_count')

    top_categories = category_counts[:5]

    low_stock_products = Product.objects.filter(
        stock_quantity__lte=40
    ).select_related('supplier').order_by('stock_quantity')[:10]

    context = {
        'category_counts': category_counts,
        'top_categories': top_categories,
        'low_stock_products': low_stock_products,
        'categories': categories,
    }

    return render(request, 'inventory.html', context)


@login_required
def products(request):
    category_filter = request.GET.get("category", "")
    categories = ["T-Shirts", "Pants", "Jackets", "Shoes", "Accessories"]

    if category_filter in categories:
        products_list = (
            Product.objects.filter(category=category_filter)
            .select_related("supplier")
            .order_by("name")
        )
    else:
        products_list = Product.objects.select_related("supplier").order_by("name")

    paginator = Paginator(products_list, 30)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    context = {
        "products": products,
        "category_choices": categories,
        "current_category": category_filter,
    }
    return render(request, "products.html", context)


@login_required
def employees(request):
    # Umumiy statistika
    total_employees = Employee.objects.count()
    active_employees = Employee.objects.filter(is_active=True).count()
    average_salary = (
        Employee.objects.aggregate(avg_salary=Avg("salary"))["avg_salary"] or 0
    )

    # Bo'limlar bo'yicha taqsimot
    department_distribution = (
        Employee.objects.values("department")
        .annotate(employee_count=Count("id"))
        .order_by("-employee_count")
    )
    recent_employees = Employee.objects.order_by("-hire_date")[:10]

    top_salary_employees = Employee.objects.order_by("-salary")[:7]

    context = {
        "total_employees": total_employees,
        "active_employees": active_employees,
        "average_salary": round(average_salary, 2),
        "department_distribution": department_distribution,
        "recent_employees": recent_employees,
        "top_salary_employees": top_salary_employees,
        "current_date": timezone.now().date(),
    }

    return render(request, "employee.html", context)


def reports(request):
    pass


def settings(request):
    pass


def system_settings(request):
    pass


def user_management(request):
    pass


def integrations(request):
    pass


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfuly login! ')
            return redirect('/')
        else:
            messages.error(request, 'Wrong Username or password')
    
    return redirect('/')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('/')


def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = 'EMPLOYEE'
        phone = request.POST.get('phone', '')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'This user name already exist')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'This email already exist')
        else:
            # Yangi foydalanuvchi yaratish
            user = User.objects.create_user(username=username, email=email, password=password)

            # Admin modeliga qo‘shish
            Admin.objects.create(user=user, role=role, phone=phone)

            # Avtomatik login
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {user.username}!')
                return redirect('/')

            messages.success(request, 'Register successfuly')
            return redirect('/')

    return redirect('/')
