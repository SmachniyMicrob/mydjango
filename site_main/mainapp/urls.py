from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.products, name='products'),
    path("product/new/", views.new_product, name='new_product'),
    path("product/<int:kp>/edit/", views.edit_product, name='edit_product'),
    path("product/<int:kp>/delete/", views.del_product, name='del_product'),
    path("dishes/", views.dishes, name='dishes'),
    path("dish/<int:dk>", views.dish, name='dish'),
    path("register/", views.register_user, name='register'),
    path("login/", views.login_user, name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("", views.index, name="index"),
    path('aboutme/', views.about_me, name='about_me'),
]
