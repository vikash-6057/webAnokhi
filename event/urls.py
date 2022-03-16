
from django.urls import path
from .import views

app_name='event'

urlpatterns = [
    path('upcoming/',views.upcoming,name='upcoming'),
    path('program/',views.program, name='program'),
    path('past/',views.past,name='past'),

    path('detail/<int:past_id>/',views.detail,name='detail'),
    #path('',views.timetable,name='timetable'),
    #path('<int:timetable_id>/',views.timetabledetail,name='timetabledetail'),
    path('addevent/', views.addevent, name='addevent'),
    path('deleteevent/<int:ev_id>/', views.deleteevent, name='deleteevent'),
    path('addimage/', views.addimage, name='addimage'),
    path('deleteimage/<int:ev_id>/', views.deleteimage, name='deleteimage'),
    path('addpro/', views.addpro, name='addpro'),
    path('deletepro/<int:ev_id>/', views.deletepro, name='deletepro'),


    #class based urls for admin
    path('al/', views.EventList.as_view(), name='event_list'),
    path('view/<int:pk>', views.EventView.as_view(), name='event_view'),
    path('new', views.EventCreate.as_view(), name='event_new'),
    path('edit/<int:pk>', views.EventUpdate.as_view(), name='event_edit'),
    path('delete/<int:pk>', views.EventDelete.as_view(), name='event_delete'),

    #

] 