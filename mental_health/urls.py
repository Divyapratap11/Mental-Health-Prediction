
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home),
    path("test/",views.testpage),
    path('predict/',views.result,name="res"),
    path("",include(('user.urls','user'),"user")),
    path('contact/',views.contact),


]
