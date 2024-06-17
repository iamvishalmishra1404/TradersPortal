from django.contrib import admin
from .models import Company,Watchlist

# Register your models here.
class Company_model(admin.ModelAdmin):
  #readonly_fields=['slug']                  # so that user cannot change it
    # prepopulated_fields={'slug':['bname']}      #slug field can be autofilled and edited too 
    list_display=['id','company_name','symbol','scripcode']   #columns to be displayed on the admin page
    # list_filter=['author','cost']       #to get the filter option on the screen 
    # list_display_links=['bname']     
class Watchlist_model(admin.ModelAdmin):
    list_display = ['user',"company"]


admin.site.register(Company,Company_model) 
admin.site.register(Watchlist,Watchlist_model)
