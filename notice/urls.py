
from django.urls import path
from .import views

urlpatterns = [
    path('',views.notices,name='notices'),
    path('notices/<int:notices_id>/',views.ndetail,name='ndetail'),
    #path('',views.timetable,name='timetable'),
    #path('<int:timetable_id>/',views.timetabledetail,name='timetabledetail'),

] 