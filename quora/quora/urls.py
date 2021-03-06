"""quora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', anasayfa),
    url(r'^new-account/$', sign),    
    url(r'^login/$', giris),
    url(r'^logout/$', cikis),
    url(r'^newquestion/$', yeni_soru),
    url(r'^question/(?P<number>[-\w]+)/$', soru_sayfasi),
    url(r'^profil/(?P<user>[-\w]+)/$', profil),  
    url(r'^search/$', search, name="search"),          
    url(r'^qud/(?P<updown>[-\w]+)/(?P<number>[-\w]+)/$', question_up),
    url(r'^aud/(?P<updown>[-\w]+)/(?P<number>[-\w]+)/$', answer_up),
    url(r'^newanswer/(?P<number>[-\w]+)/(?P<sub>[-\w]+)/$', reply),
    
]
