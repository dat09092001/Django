"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from django.contrib.auth import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name='home'),
    path("sinhvien/<int:sinhvien_id>/",views.viewsv,name="viewsv"),
    path("delete/<int:id>",views.deletesv,name="delete"),
    path("addsv/",views.addsinhvien,name="addsv"),
    path("dangki/",views.dangki,name="dangki"),
    path("login/",views.login1,name="login"),
    path("logout",views.logout1,name="logout"),
    path("edit/<int:sinhvien_id>/",views.editsv,name="editsv"),
    path("danhmuc/<int:pk>/",views.product,name="danhmuc")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
