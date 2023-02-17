from django.urls import path
from waste import views

app_name = 'waste'

urlpatterns = [
    path('post_waste/',views.WastePost.as_view(),name='post_waste'),
    path('',views.WasteList.as_view(),name = 'wastage'),
    path('my_waste/',views.MyWaste.as_view(),name='my_waste'),
    path('delete_waste/<pk>',views.WasteDelete.as_view(),name='delete_waste'),
    path('detail_waste/<pk>',views.WasteDetail.as_view(),name='detail_waste'),
]
