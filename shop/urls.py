from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.index,name='home'),
    path('signin/',views.signin,name='signin'),
    path('contact/',views.contact,name='contact'),
    path('about_us/',views.aboutus,name='about_us'),
    path('products/<int:id>',views.products,name='products'),
    path('tracker/',views.tracker,name='tracker'),
    path('checkout/',views.checkout,name='checkout')

]