from django import forms
from django.forms import ModelForm
from owner.models import Books
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(ModelForm):
    class Meta:
        model=Books
        fields="__all__"
        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "copies":forms.NumberInput(attrs={"class":"form-control"})
        }
# class BookForm(forms.Form):
#     book_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     author=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     copies=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#
#     def clean(self):
#         cleaned_data=super().clean()
#         price=cleaned_data["price"]
#         copies=cleaned_data["copies"]
#         if price<0:
#             msg="invalid price"
#             self.add_error("price",msg)
#         if copies<0:
#             msg="invalid copies"
#             self.add_error("copies",msg)
# class BookChangeForm(forms.Form):
#     book_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     author = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     price = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     copies = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#
#     def clean(self):
#         cleaned_data = super().clean()
#         price = cleaned_data["price"]
#         copies = cleaned_data["copies"]
#         if price < 0:
#             msg = "invalid price"
#             self.add_error("price", msg)
#         if copies < 0:
#             msg = "invalid copies"
#             self.add_error("copies", msg)
class UseRegistrationform(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"})
        }
class SigninForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

