from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Books(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=120)
    copies=models.PositiveIntegerField(default=5)
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.book_name

#fetching all objects
#books=Books.objects.all
#fetching a specific object
#book=Books.objects.get(id=1)
#filter query
#books=Books.objects.filter(price>400)
class Cart(models.Model):
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("incart","incart"),
        ("orderplaced","orderplaced"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=120,choices=options,default="incart")
class Orders(models.Model):
    delivery_address=models.CharField(max_length=120)
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options = (
        ("orderplaced", "orderplaced"),
        ("cancelled", "cancelled"),
        ("dispatched", "dispatched"),
        ("intransmit","intransmit"),
        ("delivered","delivered")

    )
    status=models.CharField(max_length=120,choices=options,default="orderplaced")
    created_date=models.DateField(auto_now_add=True)
    expected_date=models.DateField(auto_now_add=True,null=True)

