from django.urls import path, include
from .views import (ProductListView, CategoryCreateView,
                    ProductListView, ProductCreateView,
                    CategoryDetailView, CategoryListView,product_search )
urlpatterns = [
    path('search/', product_search, name="product_search"),
    path('produts/add/', ProductCreateView.as_view(), name='product_add'),
    path('', ProductListView.as_view(), name='products'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),
    path('categories/<slug:slug>', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    

]
