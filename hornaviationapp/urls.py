from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name='index'),
    path('About', v.About, name='About'),
    path('Services', v.Services, name='Services'),
    path('Blog', v.Blog, name='Blog'),
    path('Contactus', v.Contactus, name='Contactus'),
    path('contact_info', v.contact_info, name='contact_info'),
]