from django.shortcuts import render
from django.utils import timezone
from .models import Product
from django.views import generic

class ListView(generic.ListView):
	"""docstring for ListView"""
	template_name = 'stock/templates/stock/product_list.html'
	model = Product
	context_object_name = 'product_list'

def product_list(request):
	product_list = Product.objects.filter(date_add__lte=timezone.now()).order_by('date_add')
	return render(request, 'stock/product_list.html', {'product_list':product_list})