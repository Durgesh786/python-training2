from django.urls import path
from django.views.generic import RedirectView

from web.users.views import dashboard, logout, login, user_delete
from web.film.views import language, add_language, edit_language, language_delete, check_language, actor, add_actor, \
    actor_delete, edit_actor

urlpatterns = [

    path('language/list', language, name="language_list"),
    path('add/language', add_language, name="add_language_list"),
    path('language/edit/<int:id>/',edit_language , name="edit_language"),
    # path('add/language/again',demo_language,name="again_edit"),
    path('language/delete/<int:id>/',language_delete, name="language_delete"),
    path('check/language/',check_language, name="check_language"),


    path('actor/list',actor, name="actor_list"),
    path('add/actor',add_actor, name="add_actor_list"),
    path('actor/delete/<int:id>/',actor_delete, name="actor_delete"),
    path('actor/edit/<int:id>/',edit_actor , name="edit_actor"),

    path('category/list', category, name="category_list"),
    path('add/category', add_category, name="add_category_list"),
    path('category/edit/<int:id>/', edit_category, name="edit_category"),
    # path('add/category/again',demo_category,name="again_edit"),
    path('category/delete/<int:id>/', category_delete, name="category_delete"),
    path('check/category/', check_category, name="check_category"),
    
    
    
    path('film/list/', dashboard, name="film_list"),
    path('filmcategory/list', user_delete, name="film_filmcategory"),

    path('filmactor/list', logout, name="film_filmactor"),
    path('', RedirectView.as_view(url='login/', permanent=False)),

]
#Language,Category,Films,FilmCategory,Actor,FilmActor