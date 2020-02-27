from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact
from .models import Auth_user

# Register your models here.



class ContactForm(admin.ModelAdmin):
    list_display = ('fname','email','subject','message','Written')
    list_filter = ['Written']
    

admin.site.register(Auth_user)
admin.site.register(Contact, ContactForm)
admin.site.unregister(Group)