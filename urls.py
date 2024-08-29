from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name='index'),
    path('appointment', views.appointment, name='appointment'),
    path('details', views.details, name='details'),
    path('save',views.save,name='save'),
    path('delete<int:id>/',views.delete_data,name='delete'),
    path('edit<int:id>/',views.edit_data,name='edit'),
    path('update<int:id>/',views.edit_data,name='edit'),
    path('success',views.success,name='success'),
    path('add',views.add,name='add'),
    path('data',views.data,name='data'),
    
]