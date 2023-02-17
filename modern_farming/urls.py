from django.urls import path
from modern_farming import views


app_name = "modern_farming"

urlpatterns = [
    path('',views.FarmingTech.as_view(),name='farm_tech_list'),
    path('tech_detail/<pk>',views.FarmingTechDetail.as_view(),name='tech_detail'),
]
