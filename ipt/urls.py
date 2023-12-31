"""
URL configuration for ipt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from members.views import index_page
from members import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # memberapp
    path('', views.index_page, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/add/', views.add, name='add_data'),
    path('dashboard/add/addrecord/', views.addrecord, name='addrecord'),
    path('dashboard/delete/<int:id>', views.delete, name='delete'),
    path('dashboard/update/<int:id>', views.update, name='update'),
    path('dashboard/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path("accounts/", include("django.contrib.auth.urls")),
]
