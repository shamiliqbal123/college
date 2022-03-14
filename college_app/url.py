from college_app import views
from django.urls import path, include


urlpatterns = [
    path("loginview", views.login_view, name="loginview"),
    path("home", views.home, name="home"),
    path("viewstudent", views.viewstudent, name="viewstudent"),

    path("collegeregister", views.college_register, name="collegeregister"),
    path("addstudent", views.addstudent, name="addstudent"),
    path("admin_home", views.admin_home, name="admin_home"),
    path("logout", views.logout_view, name="logout"),
    path("", views.main, name="main"),
]