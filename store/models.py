from django.db import models

# Create your models here.
class Order(models.Model):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, related_name="+")

class Order_Item(models.Model):
    item = models.CharField(max_length=255)

class Collection(models.Model):
    title = models.CharField(max_length=255)

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="-")
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)


class Order(models.Model):
    CONFIRM_CHOICE = "C"
    FAILED_CHOICE = "F"
    PENDING_CHOICE = "P"
    STATUS_CHOICES = [
        (PENDING_CHOICE,'Pending'),
        (CONFIRM_CHOICE, 'Complete'),
        (FAILED_CHOICE, 'Failed' )
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING_CHOICE)
    order_item = models.ForeignKey(Order_Item, on_delete=models.CASCADE)

class Customer(models.Model):
    MEMEBER_GOLD = 'G'
    MEMBER_CHOICES = [
        (MEMEBER_GOLD, 'GOLD'),
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('P', 'Platinum')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.SmallIntegerField()
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBER_CHOICES, default=MEMEBER_GOLD)
    customer_order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    zip = models.SmallIntegerField(null=True)

class Cart(models.Model):
    order_item = models.ForeignKey(Order_Item, on_delete=models.CASCADE)
