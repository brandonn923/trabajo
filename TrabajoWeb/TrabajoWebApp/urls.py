from django import urls
from django.urls import conf, path
from django.views.generic.base import TemplateView
from TrabajoWebApp import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.index, name="index"),
    path('registar/',views.registar, name="registar"),
    path('login/', LoginView.as_view(template_name='TrabajoWebApp/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='TrabajoWebApp/logout.html'),name='logout'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)