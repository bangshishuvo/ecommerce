from django.contrib import admin


# Register your models here.
from loansystem.models import LoanCart


class LoanCartAdmin(admin.ModelAdmin):
	list_display=['product','user','quantity','price','amount']
	list_filter=['user']








admin.site.register(LoanCart,LoanCartAdmin)
