"""Shukongdashi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from Shukongdashi.demo import question_zhenduan
from Shukongdashi.demo import question_baocun
from Shukongdashi.demo import question_pa
from Shukongdashi.demo import question_buquan
from Shukongdashi.demo import question_wenda
from . import view
from django.views.generic import TemplateView
from django.urls import path, include


urlpatterns = [
    # url(r'^$', view.test),
    url(r'^qa', question_zhenduan.question_answering),
    url(r'^pa', question_pa.main),
    url(r'^save', question_baocun.question_baocun),
    url(r'^buquan', question_buquan.question_buquan),
    url(r'^wenda', question_wenda.question_wenda),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    path('api/', include('users.urls')),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/add_book/', add_book),
#     path('api/show_books/', show_books),
# ]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('backend.urls')),
#     path(r'', TemplateView.as_view(template_name="index.html")),
# ]

