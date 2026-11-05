from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path('index', views.index),
    path('niews', views.niews),
    path('product', views.product),
    path("products/", views.products, name="products"),
    path('blog', views.blog),
    path('about', views.about),
    path('form/', views.form, name='form'),
    path('form_model/', views.form_model, name='form_model'),
    path('success/', views.success, name='success'),
    
    path('admin/', admin.site.urls),
]
