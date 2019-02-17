"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from hjres.views import hello
from hjres.views import detail
from hjres.views import create
from hjres.views import templatetest

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
urlpatterns = [
    path('hello/', hello),  # 이 줄도 추가합니다.
    path('admin/', admin.site.urls),
    path('photos/upload/',create,name='create'),
    path('photos/<pk>/', detail, name='detail'),
    path('templatetest/',templatetest,name='templatetest'),
]

urlpatterns += static('upload_files', document_root=settings.MEDIA_ROOT)