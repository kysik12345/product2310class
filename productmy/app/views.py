from django.shortcuts import render
from django.views.generic import (ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView)
from .models import Product, Category
from django.urls import reverse_lazy
from .forms import CategoryCreateForm, ProductCreateForm
from django.core.paginator import Paginator
from django.db.models import Q

class AdminTemplateView(TemplateView):
    template_name='app/admin/html'

class ProductCreateView(CreateView):
        model = Product
        exclude = ['slug', 'create', 'update']
        template_name = 'app/app.html'
        context_object_name = 'products'

class CategoryCreateView(CreateView):
     model = Product
     template_name = 'app/products.html'
     context_object_name = 'products'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['total'] = 5
    #     return context

class ProductListView(ListView):
    model = Product
    template_name = 'app/app.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    form = CategoryCreateForm
    template_name = 'app/product_add.html'
    success_url = reverse_lazy('categories')

class CategoryListView(ListView):
    model = Category
    template_name = 'app/categories.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'app/category_detail.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    form = CategoryCreateForm
    template_name = 'app/category_add.html'
    success_url = reverse_lazy('categories')

def index(request):
    ads = Category.objects.all().order_by('-created_at')
    paginator= Paginator(ads, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'app/app.html', context)

def product_search(request):
     query = request.GET.get('query')
     query_text = Q(name__icontains = query)

     results = Product.objects.filter(query_text)
     categories = Category.objects.all()
     
     context = {'categories':categories, 'products': results}

     return render (request,template_name="app/app.html", context=context)
