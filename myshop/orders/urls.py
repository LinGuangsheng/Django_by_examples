# -*- coding:utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cvreate/$',views.order_create,name='order_create'),
]