from . import views
from django.urls import path,include

urlpatterns = [

    path('dresses',views.DressCreateList.as_view(), name="dresses"),
    path('dress/<int:pk>',views.DressReadUpdate.as_view(), name="dress"),
    path('users', views.UserCreateList.as_view(), name="users"),
    path('user/<int:pk>',views.UserReadUpdate.as_view(), name="user"),
    path('cupboards', views.CupboardCreateList.as_view(), name="cupboards"),
    path('cupboard/<int:pk>', views.CupboardReadUpdate.as_view(), name="cupboard"),
    path('tops',views.ListTops.as_view(),name="tops"),
    path('bottoms',views.ListBottoms.as_view(),name="bottoms")

]

