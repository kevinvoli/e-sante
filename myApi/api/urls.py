from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from api.views import UserDetailViews,UserListViews, PharmacieDetailViews,PharmacieList, HospitalListViews,HospitalDetailViews,MedicamentListviews,MedicamentDetailviews,OrdonnanceListViews,OrdonnanceDetailViews
from rest_framework import renderers

# User_list = UserViews.as_view({
#     'get': 'list'
# })

# User_datail= UserViews.as_view({
#     'get':'retrieve',
#     'put':'update',
#     'delete':'destroy',
# })

router= DefaultRouter(trailing_slash=False)
urlpatterns = [
   
    path('phamacie/', PharmacieList.as_view(),name="phamacies"),
    path("phamacie/<int:pk>",PharmacieDetailViews.as_view(),name="phamacies-detail"),
    path('users/', UserListViews.as_view(),name="users"),
    path('users/<int:pk>', UserDetailViews.as_view(),name="users-dedail"),
    path('hospitol/', HospitalListViews.as_view(),name="users"),
    path('hospitol/<int:pk>', HospitalDetailViews.as_view(),name="users-dedail"),
    path('medicament/', MedicamentListviews.as_view(),name="users"),
    path('medicament/<int:pk>', MedicamentDetailviews.as_view(),name="users-dedail"),
    path('ordonnence/', OrdonnanceListViews.as_view(),name="users"),
    path('ordonnence/<int:pk>', OrdonnanceDetailViews.as_view(),name="users-dedail"),
]
