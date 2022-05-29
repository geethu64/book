from django.forms import ModelForm
from customer.models import UserProfile
from  owner.models import Orders
from django import forms

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=["phone","address"]
class OrderForm(ModelForm):
    class Meta:
        model=Orders
        fields=["delivery_address"]
        widgets={
            "delivery_address":forms.Textarea(attrs={"class":"form-control"})
        }