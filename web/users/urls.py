
from django.urls import path
from django.views.generic import RedirectView

from web.users.views import dashboard, logout, login, user_delete

urlpatterns = [

    path('login/', login, name="admin_login"),
    path('dashboard/', dashboard, name="dashboard"),
    path('user/list/', dashboard, name="user_list"),
    path('user/delete/<int:id>/', user_delete, name="user_delete"),
    path('logout/', logout, name="logout"),
    path('', RedirectView.as_view(url='login/', permanent=False)),

]
