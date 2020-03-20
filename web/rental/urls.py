from django.urls import path
from django.views.generic import RedirectView

from web.users.views import dashboard, logout, login, user_delete

urlpatterns = [

    path('payment/', login, name="rental_payment"),
    path('rental/', dashboard, name="rental_rental"),
    path('inventory/list/', dashboard, name="rental_inventory"),
    path('store/list', user_delete, name="rental_store"),
    path('address/list', logout, name="rental_address"),
    path('city/list', logout, name="rental_city"),
    path('country/list', logout, name="rental_country"),
    path('', RedirectView.as_view(url='login/', permanent=False)),

]
#Payment,Rental,Inventory,Store,Address,City,Country