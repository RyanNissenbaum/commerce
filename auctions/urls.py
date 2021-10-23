from django.urls import path

from . import views

app_name = "auctions"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("add", views.add, name="add" ),
    path("<int:listing_id>", views.listing, name="listing"),
    path("<str:category>", views.by_category, name="by_category")
]
