
from django.contrib import admin
from django.urls import path,include
from App_Login import views

from django.conf import settings
from django.contrib.staticfiles.urls import static , staticfiles_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/',include('App_Login.urls')),
    path('',views.Home,name="home"),
    path('product/',include('Organic_Product.urls')),
    path('order/',include('Order.urls')),
    path('waste/',include('waste.urls')),
    path('modern_farming/',include('modern_farming.urls')),
    path('payment/',include('Payment.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
