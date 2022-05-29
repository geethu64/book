from django.urls import path
from owner import views
urlpatterns=[
    path("",views.OwnerHome.as_view(),name="ownerindex"),
    path("books/add",views.AddBook.as_view(),name="addbook"),
    path("books/all", views.AllBooks.as_view(),name="listallbooks"),
    path("books/<int:id>", views.BookDetail.as_view(),name="bookdetail"),
    path("books/change/<int:id>", views.BookUpdate.as_view(),name="editbook"),
    path("books/remove/<int:id>",views.remove_book,name="removebook"),
    path("accounts/signup",views.Registraion.as_view(),name="register"),
    path("accounts/signin",views.SignIN.as_view(),name="signin"),
    path("accounts/signout",views.signout,name="signout")

]