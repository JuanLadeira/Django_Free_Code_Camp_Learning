from django.shortcuts import render
from .models import Product


# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #    'title': obj.title,
    #    'description': obj.description,
    #    'price': obj.price,
    #    'summary': obj.summary,
    #    'featured': obj.featured,
    #}
    context = {'object': obj}
    return render(request, 'detail.html', context)
