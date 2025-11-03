from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path("",views.index, name = 'home'),
    path("home",views.index, name = 'home'),
    path("about",views.about,name = 'about'),
    path("vehicles", views.vehicles, name= "vehicles"),
    path("register", views.register, name="register"),
    path("signin", views.signin, name="signin"),
    path("signout",views.signout,name = "signout"),
    path("bill",views.bill,name = "bill"),
    path("order",views.order,name = "order"),
    path("contact",views.contact,name = 'contact'),
    path("manage_cars", views.manage_cars, name="manage_cars"),
    path("report_issue/<int:order_id>", views.report_issue, name="report_issue"),
    path("manage_orders", views.manage_orders, name="manage_orders"),
    path("update_order_status/<int:order_id>/<str:status>", views.update_order_status, name="update_order_status"),
    ]