from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^ListView$', views.ListView.as_view(), name='product_list'),
]
