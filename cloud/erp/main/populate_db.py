import os
import django
from faker import Faker
import random
from datetime import datetime, timedelta
from django.utils import timezone

# Loyiha sozlamalarini o'rnatish
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp.settings")  # Loyiha nomi: erp
django.setup()

# Modellarni to'g'ri import qilish
from main.models import Customer, Supplier, Product, Order, OrderItem, Transaction

# Faker ob'ektini yaratish
fake = Faker()


def populate_db():
    # Ma'lumotlar bazasini tozalash (ixtiyoriy)
    Customer.objects.all().delete()
    Supplier.objects.all().delete()
    Product.objects.all().delete()
    Order.objects.all().delete()
    OrderItem.objects.all().delete()
    Transaction.objects.all().delete()

    # 1. Yetkazib beruvchilarni yaratish
    suppliers = []
    for _ in range(5):
        supplier = Supplier.objects.create(
            name=fake.company(),
            contact_person=fake.name(),
            email=fake.unique.email(),
            phone=fake.phone_number(),
            address=fake.address(),
        )
        suppliers.append(supplier)

    # 2. Mijozlarni yaratish
    customers = []
    for _ in range(20):
        customer = Customer.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.unique.email(),
            phone=fake.phone_number(),
            address=fake.address(),
        )
        customers.append(customer)

    # 3. Mahsulotlarni yaratish
    products = []
    categories = ["T-Shirts", "Pants", "Jackets", "Shoes", "Accessories"]
    for _ in range(50):
        product = Product.objects.create(
            name=fake.word().capitalize()
            + " "
            + random.choice(["T-Shirt", "Pants", "Jacket", "Shoes"]),
            description=fake.text(max_nb_chars=200),
            category=random.choice(categories),
            price=round(random.uniform(10.0, 100.0), 2),
            stock_quantity=random.randint(10, 200),
            supplier=random.choice(suppliers),
        )
        products.append(product)

    # 4. Buyurtmalarni yaratish
    orders = []
    statuses = ["PENDING", "PROCESSING", "SHIPPED", "DELIVERED", "CANCELLED"]
    for _ in range(100):
        order_date = fake.date_time_between(start_date="-30d", end_date="now")
        order = Order.objects.create(
            customer=random.choice(customers),
            order_date=order_date,
            status=random.choice(statuses),
            total_amount=0.0,
        )
        orders.append(order)

        # 5. Buyurtma elementlarini yaratish
        num_items = random.randint(1, 5)
        total_amount = 0.0
        for _ in range(num_items):
            product = random.choice(products)
            quantity = random.randint(1, 10)
            unit_price = product.price
            order_item = OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                unit_price=unit_price,
            )
            total_amount += order_item.total_price

        # Buyurtma umumiy narxini yangilash
        order.total_amount = total_amount
        order.save()

    # 6. Tranzaksiyalarni yaratish
    payment_methods = ["CASH", "CARD", "TRANSFER"]
    for order in orders:
        if order.status in ["SHIPPED", "DELIVERED"]:
            Transaction.objects.create(
                order=order,
                amount=order.total_amount,
                payment_method=random.choice(payment_methods),
                transaction_date=order_date + timedelta(days=random.randint(1, 5)),
            )

    print(f"Ma'lumotlar bazasi muvaffaqiyatli to'ldirildi:")
    print(f"- {Customer.objects.count()} ta mijoz")
    print(f"- {Supplier.objects.count()} ta yetkazib beruvchi")
    print(f"- {Product.objects.count()} ta mahsulot")
    print(f"- {Order.objects.count()} ta buyurtma")
    print(f"- {OrderItem.objects.count()} ta buyurtma elementi")
    print(f"- {Transaction.objects.count()} ta tranzaksiya")


if __name__ == "__main__":
    populate_db()
