from django.contrib import admin
from .models import *


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "first_name", 
        "last_name", 
        "email", 
        "phone",
        "position",
        "department",
        "is_active"
    )
    list_filter = (
        "position", 
        "department",
        "is_active",
        "hire_date",
        "created_at"
    )
    list_editable = (
        "position", 
        "department",
        "is_active"
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "phone"
    )
    list_per_page = 25
    date_hierarchy = "hire_date"
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Employment Details', {
            'fields': ('position', 'department', 'hire_date', 'salary', 'is_active')
        }),
    )


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "phone", "created_at")
    search_fields = ("user__username", "user__email")
    list_filter = ("role", "created_at")
    list_editable = ("role", "phone")


# Inline for OrderItem to show within Order admin
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of empty forms to display
    fields = ("product", "quantity", "unit_price", "total_price")
    readonly_fields = ("total_price",)


# Inline for Transaction to show within Order admin
class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 1
    fields = ("amount", "payment_method", "transaction_date")


# Customer Admin
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "address", "created_at")
    list_filter = ("created_at",)
    search_fields = ("first_name", "last_name", "email", "phone")
    date_hierarchy = "created_at"
    ordering = ("last_name", "first_name")

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    full_name.short_description = "Name"


# Supplier Admin
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "contact_person", "email", "phone", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "contact_person", "email", "phone")
    date_hierarchy = "created_at"
    ordering = ("name",)


# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "stock_quantity",
        "supplier",
        "created_at",
    )
    list_filter = ("category", "supplier", "created_at")
    search_fields = ("name", "description", "category")
    list_editable = ("price", "stock_quantity")
    date_hierarchy = "created_at"
    ordering = ("name",)

    actions = ["restock_products"]

    def restock_products(self, request, queryset):
        for product in queryset:
            product.stock_quantity += 100
            product.save()
        self.message_user(
            request, "Selected products have been restocked with 100 units."
        )

    restock_products.short_description = "Restock selected products (+100 units)"


# Order Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "order_date",
        "status",
        "total_amount",
        "created_at",
    )
    list_filter = ("status", "order_date", "created_at")
    search_fields = ("customer__first_name", "customer__last_name", "customer__email")
    date_hierarchy = "order_date"
    inlines = [OrderItemInline, TransactionInline]
    ordering = ("-order_date",)

    actions = ["mark_as_shipped", "mark_as_delivered"]

    def mark_as_shipped(self, request, queryset):
        queryset.update(status="SHIPPED")
        self.message_user(request, "Selected orders marked as shipped.")

    mark_as_shipped.short_description = "Mark selected orders as Shipped"

    def mark_as_delivered(self, request, queryset):
        queryset.update(status="DELIVERED")
        self.message_user(request, "Selected orders marked as delivered.")

    mark_as_delivered.short_description = "Mark selected orders as Delivered"


# OrderItem Admin
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "unit_price", "total_price")
    list_filter = ("order__status",)
    search_fields = (
        "product__name",
        "order__customer__first_name",
        "order__customer__last_name",
    )
    ordering = ("order",)


# Transaction Admin
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "amount",
        "payment_method",
        "transaction_date",
        "created_at",
    )
    list_filter = ("payment_method", "transaction_date", "created_at")
    search_fields = ("order__customer__first_name", "order__customer__last_name")
    date_hierarchy = "transaction_date"
    ordering = ("-transaction_date",)
