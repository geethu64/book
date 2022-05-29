from django.urls import path
from customer import views
from django.views.generic import TemplateView
urlpatterns=[
   # path("",TemplateView.as_view(template_name="cbase.html"),name="cindex"),
   path("home",views.CustomerHome.as_view(),name="customerhome"),
   path("accounts/customer/signin",views.CustomerRegistration.as_view(),name="custreg"),
   path("carts/add/<int:id>",views.AddtoCart.as_view(),name="addtocart"),
   path("carts/all",views.ViewMyCart.as_view(),name="viewmycart"),
   path("orders/add/<int:c_id>/<int:p_id>",views.OrderCreate.as_view(),name="ordercreate")
]