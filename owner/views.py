from django.shortcuts import render,redirect
from owner import  forms
from owner.models import Books
from django.contrib.auth import authenticate,login,logout
from owner.decoraters import signin_required
from django.views.generic import View,ListView,TemplateView,CreateView,DetailView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.http import HttpResponse
# Create your views here.
# books=[
#     {"id":1,"book_name":"randamoozham","author":"mt","price":450,"copies":50,"image":"	https://images-na.ssl-images-amazon.com/images/I/41fRojGGDUL.jpg"},
#     {"id": 2, "book_name": "halfgf", "author": "chethan", "price": 500, "copies": 45,"image":"https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/bda6cd53570573.5938fd77e82a7.jpg"},
#     {"id": 3, "book_name": "alchmist", "author": "paulo", "price": 550, "copies": 50,"image":"https://images-na.ssl-images-amazon.com/images/I/51NRkX2bPbL.jpg"},
#     {"id": 4, "book_name": "indhuleka", "author": "chandhu", "price": 650, "copies": 20,"image":"https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1413134166l/18042553.jpg"},
#
# # ]
# @signin_required
# def owner_home(request,*args,**kwargs):
#     return render(request,"owner_home.html")
# @method_decorator(signin_required,name="dispatch")
class OwnerHome(TemplateView):
    template_name="owner_home.html"
    # def get(self,request,**kwargs):
    #     return render(request,self.template_name)

# @signin_required
# def add_book(request,*args,**kwargs):
#     form=forms.BookForm()
#     context={"form":form}
#     if request.method=="POST":
#
#         form=forms.BookForm(request.POST,files=request.FILES)
#         if form.is_valid():
#
#             form.save()
#
#           # book=Books(book_name=form.cleaned_data["book_name"],
#           #            author=form.cleaned_data["author"],
#           #            price=form.cleaned_data["price"],
#           #            copies=form.cleaned_data["price"])
#           # book.save()
#             return redirect("listallbooks")
#
#         else:
#             context={"form":form}
#             return render(request,"add_book.html",context)
#
#
#
#
#             # return redirect("listallbooks")
#
#     return render(request, "add_book.html",context)

#
@method_decorator(signin_required,name="dispatch")
class AddBook(CreateView):
    model=Books
    template_name="add_book.html"
    form_class=forms.BookForm
    success_url = reverse_lazy("listallbooks")
    # context={}
    # def get(self,request,*args,**kwargs):
    #     form=self.form_class()
    #     self.context["form"]=form
    #     return render(request,self.template_name,self.context)
    #
    # def post(self,request,*args,**kwargs):
    #     form=self.form_class(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("listallbooks")
    #     else:
    #         self.context["form"]=form
    #         return render(request,self.template_name,self.context)
#
# @signin_required
# def list_books(request,*args,**kwargs):
#     books=Books.objects.all()
#     context={"books":books}
#     return render(request,"book_list.html",context)
@method_decorator(signin_required,name="dispatch")
class AllBooks(ListView):
    model=Books
    template_name="book_list.html"
    context_object_name="books"
    # def get(self,request,*args,**kwargs):
    #     books=self.model.objects.all()
    #     self.context["books"]=books
    #     return render(request,self.template_name,self.context)

# @signin_required
# def book_details(request,*args,**kwargs):
#     id=kwargs["id"]
#     products=Books.objects.get(id=id)
#     context={"book":products}
#     return render(request,"book_detail.html",context)
@method_decorator(signin_required,name="dispatch")
class BookDetail(DetailView):
    model=Books
    template_name="book_detail.html"
    context_object_name = "book"
    pk_url_kwarg = "id"

    # def get(self, request, *args, **kwargs):
    #     id=kwargs["id"]
    #     book=self.model.objects.get(id=id)
    #     self.context["book"]=book
    #     return render(request,self.template_name,self.context)

# @signin_required
# def change_book(request,*args,**kwargs):
#     id = kwargs["id"]
#     item=Books.objects.get(id=id)
#     form=forms.BookForm(instance=item)
#     # context={"form":form}
#     if request.method=="POST":
#         form=forms.BookForm(request.POST,instance=item,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("listallbooks")
#         else:
#             return render(request,"edit_book.html",{"form":form})
#     return render(request,"edit_book.html",{"form":form})
@method_decorator(signin_required,name="dispatch")
class BookUpdate(UpdateView):
    model = Books
    template_name ="edit_book.html"
    # context={}

    form_class=forms.BookForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listallbooks")

    # def get(self,request,*args,**kwargs):
    #     id = kwargs["id"]
    #     book =self.model.objects.get(id=id)
    #     form=self.form_class(instance=book)
    #     self.context["form"]=form
    #     return render(request,self.template_name,self.context)
    #
    # def post(self, request, *args, **kwargs):
    #     id = kwargs["id"]
    #     book = self.model.objects.get(id=id)
    #     form = self.form_class(request.POST,instance=book,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("listallbooks")
    #     else:
    #         self.context["form"]=form
    #         return render(request, self.template_name, self.context)






def remove_book(request,*args,**kwargs):
    id = kwargs["id"]
    book=Books.objects.get(id=id)
    book.delete()
    return redirect("listallbooks")

class Registraion(CreateView):
    model =User
    template_name = "register.html"
    form_class = forms.UseRegistrationform
    success_url = reverse_lazy("signin")

# def user_registeration(request,*args,**kwargs):
#     form=forms.UseRegistrationform()
#     context={"form":form}
#     if request.method=="POST":
#         form=forms.UseRegistrationform(request.POST)
#         if form.is_valid():
#             form.save()
#             print("Account has been created")
#             return render(request,"login.html")
#         else:
#             context = {"form": form}
#             return render(request, "register.html", context)
#
#     return render(request,"register.html",context)
class SignIN(TemplateView):
    template_name = "login.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        form=forms.SigninForm()
        context["form"]=form
        return context
    def post(self,request,*args,**kwargs):
        form = forms.SigninForm(request.POST)
        if form.is_valid():
            u_name = form.cleaned_data["username"]
            pwd = form.cleaned_data["password"]
            user = authenticate(request, username=u_name, password=pwd)
            if user:
                login(request,user)
                if user.is_superuser:
                    return redirect("ownerindex")
                else:
                    return redirect("customerhome")
            else:
                self.context["form"]=form
                return render(request,self.template_name,self.context)



# def signin(request):
#     form=forms.SigninForm()
#     context = {"form": form}
#     if request.method == "POST":
#         form = forms.SigninForm(request.POST)
#         if form.is_valid():
#             u_name=form.cleaned_data["username"]
#             pwd=form.cleaned_data["password"]
#             user=authenticate(request,username=u_name,password=pwd)
#             if user:
#                 login(request,user)
#                 return redirect("ownerindex")
#             else:
#                 return render(request,"login.html",context)
#     return render(request,"login.html",context)
@signin_required
def signout(requset,*args,**kwargs):
    logout(requset)
    return redirect("signin")



