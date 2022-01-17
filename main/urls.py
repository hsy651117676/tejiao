"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from .views import page_error, page_not_found, permission_denied
from django.contrib import admin
from . import views,main
from django.urls import path,include,re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_view),
    path('pjxt/',include("pjxt.urls")),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('order/', views.order),
    path('index/',views.index_view),
    path('test/',main.usermanage),

    path('main/sysmenuedit/',main.menuedit),
    path('main/sysmenuedit/menulevel',main.menulevel),
    path('main/sysmenuedit/update',main.menuupdate),
    path('main/sysmenuedit/ajax',main.menuajax),
    path('main/usermanage/',main.usermanage),
      ]

handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error
