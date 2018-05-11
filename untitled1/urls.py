"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
import cart.views as views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', include('django.contrib.auth.urls')),
    path('', views.index, name='home'),
    path('basket/', views.basket, name='basket'),
    path('cart/<id_book>', views.basket_add, name='add_cart'),
    path('signup/', views.signup, name='signup'),
    path('category/<name>', views.namecategory, name='namecategory'),
    path('publisher/<name>', views.namecategory, name='namecategory'),
    path('CartDeleteItem/<id_cart>', views.deleteCartItem, name='deleteRow'),
    path('ChangeCountAdd/<id_cart>', views.changeCountAdd, name='changeCountAdd'),
    path('ChangeCountRet/<id_cart>', views.changeCountRet, name='changeCountRet'),
    path('clearCart', views.deleteRowsCart, name='clearCart'),
]

