from django.urls import path
from Organic_Product import views


app_name = "Organic_Product"

urlpatterns = [
    path('',views.Products.as_view(),name='products'),
    path('product/<pk>',views.ProductDetail.as_view(),name='product_detail'),
    path('sell_product/',views.SellProduct.as_view(),name='sell_product'),
    path('comment/<pk>',views.comment,name='comment')
]
