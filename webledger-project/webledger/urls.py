"""webledger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ledger import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #ledger
    path('', views.home, name = 'home'),
    path('dealerform/', views.dealerform, name = 'dealerform'),
    path('ledger/<int:pk>/', views.ledger, name = 'ledger'),
    path('dealer/<int:pk>/', views.dealer, name = 'dealer'),
    path('user/', views.userpage, name = 'userpage'),
    path('expense/', views.roadexpense, name = 'roadexpense'),

    #AUTH
    path('login/', views.loginuser, name = 'loginuser'),
    path('logout/', views.logoutuser, name = 'logoutuser'),
]
