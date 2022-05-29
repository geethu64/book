from django.shortcuts import render,redirect
from django.views.generic import View
from owner.models import Books
from django.views.generic import View,TemplateView,ListView,CreateView
from owner.models import Books,Cart,Orders
from owner.forms import UseRegistrationform
from customer.forms import UserProfileForm,OrderForm


class Index(TemplateView):
    template_name = "cbase.html"
class CustomerHome(ListView):
    model=Books
    template_name="cust_home.html"
    context_object_name = "books"




class CustomerRegistration(TemplateView):
    template_name = "cust_reg.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        user_form=UseRegistrationform()
        profile_form=UserProfileForm()
        context["user_form"]=user_form
        context["profile_form"]=profile_form
        return context
    def post(self,request,*args,**kwargs):
        u_form=UseRegistrationform(request.POST)
        p_form=UserProfileForm(request.POST)
        if u_form.is_valid() & p_form.is_valid():
            user=u_form.save()
            profile=p_form.save(commit=False)
            profile.user=user
            profile.save()
            return redirect("signin")
        else:
            u_form = UseRegistrationform(request.POST)
            p_form = UserProfileForm(request.POST)
            context={}
            context["user_form"]=u_form
            context["profile_form"]=p_form
            return render(request,"cust_reg.html",context)

class AddtoCart(View):
    model=Cart

    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        book=Books.objects.get(id=id)
        user=request.user
        cart=self.model(book=book,user=user)
        cart.save()
        print("added to cart")
        return redirect("customerhome")

class ViewMyCart(ListView):
    model = Cart
    template_name="list_cart.html"
    context_object_name ="carts "
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).exclude(status="orderplaced")
def get_object(model,id):
    return model.objects.get(id=id)
class OrderCreate(CreateView):
    model =Orders
    form_class = OrderForm
    template_name = "order_place.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)

        id=self.kwargs["p_id"]
        book=get_object(Books,id)
        context["book"]=book
        return context
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.user=request.user
            id = self.kwargs["p_id"]
            book = get_object(Books, id)
            order.book=book
            order.save()
            cart=get_object(Cart,self.kwargs["c_id"])
            cart.status="orderplaced"
            cart.save()
            print("order has been placed")
            return redirect("customerhome")


class MyOrders(ListView):
    model =Orders








