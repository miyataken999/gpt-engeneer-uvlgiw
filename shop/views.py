from django.shortcuts import render
from .models import Shop

def index(request):
    shops = Shop.objects.filter(
        category__icontains='Fluorescence',
        category__icontains='Carat',
        category__icontains='Color Grade',
        category__icontains='Cutting Style',
        name__icontains='FLUORESCENCE',
        category__icontains='Round Brilliant',
        subcategory__icontains='CUT PROPORTION',
        subcategory__icontains='CUT GRADE',
        subcategory__icontains='POLISH',
        subcategory__icontains='SYMMETRY',
        subcategory__icontains='THIN-MEDIUM',
        subcategory__icontains='MEDIUM WHITISH BLUE'
    ).filter(price__gte=0, price__lte=4.41)
    return render(request, 'shop/index.html', {'shops': shops})