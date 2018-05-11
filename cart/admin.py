from django.contrib import admin
from cart.models import tblBook, tblCategory, tblPublesher, tblCart
# Register your models here.
admin.site.register(tblBook)
admin.site.register(tblCategory)
admin.site.register(tblPublesher)
admin.site.register(tblCart)