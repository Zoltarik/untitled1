from django.shortcuts import render, redirect
from cart.models import tblBook, tblCart, tblCategory, tblPublesher
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    categ = tblCategory.objects.all()
    publesh =tblPublesher.objects.all()
    books = tblBook.objects.all()
    return render(request, 'catalog.html', {'books':books, 'categ':categ, 'publesh':publesh})

def basket(request):
    if request.user.is_authenticated:
        tovari = tblCart.objects.filter(cartUser=request.user)
        return render(request, 'basket.html', {'tovar': tovari})
    else:
        return render(request, 'notAutem.html', {})


def basket_add(request, id_book):
    if request.user.is_authenticated:
        key_book = tblBook.objects.get(id=id_book)
        r = tblCart.objects.create(book=key_book, cartUser=request.user, countBook=1, send=False, close=False)
        r.save
        return redirect('home')
    else:
        return render(request, 'notAutem.html', {})

def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})
    return render(request, 'signup.html', {'form':form})

def namecategory(request, name):
    categ = tblCategory.objects.all()
    publesh = tblPublesher.objects.all()
    books = tblBook.objects.filter(category_id=name)
    return render(request, 'catalog.html', {'books': books, 'categ': categ, 'publesh': publesh})

def namepublisher(request, name):
    categ = tblCategory.objects.all()
    publesh = tblPublesher.objects.all()
    books = tblBook.objects.filter(publesher_id=name)
    return render(request, 'catalog.html', {'books': books, 'categ': categ, 'publesh': publesh})


def deleteCartItem(request, id_cart):
    delRow = tblCart.objects.get(id=id_cart)
    delRow.delete()
    return redirect('basket')

def changeCountAdd(request, id_cart):
    changeCount = tblCart.objects.get(id=id_cart)
    changeCount.countBook += 1
    changeCount.save()
    return redirect('basket')

def changeCountRet(request, id_cart):
    changeCount = tblCart.objects.get(id=id_cart)
    if changeCount.countBook > 1:
        changeCount.countBook -= 1
        changeCount.save()
    return redirect('basket')

def deleteRowsCart(request):
    changeCount = tblCart.objects.filter(cartUser=request.user)
    changeCount.delete()
    return redirect('basket')