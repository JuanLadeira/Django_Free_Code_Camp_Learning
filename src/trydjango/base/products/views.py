from django.shortcuts import render
from .models import Product
from .forms import Productform

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

def product_create_view(request):
    form = Productform(request.Post or None)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'create.html', context)