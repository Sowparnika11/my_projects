from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('insert',views.insert,name='insert'),
    path('search',views.search,name='serach'),
    path('find',views.find,name='find'),
    path('update',views.update,name='update'),
    path('change',views.change,name='change'),
    path('delete',views.delete,name='del'),
    path('remove',views.remove,name='remove')

    
]