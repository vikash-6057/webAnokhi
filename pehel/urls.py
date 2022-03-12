"""pehel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import home.views
import donate.views
from django.conf import settings
from django.conf.urls.static import static
from notice import views
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name = 'home'),

    path('donate', donate.views.donate, name = 'donate'),
    path('add_list', home.views.add_list, name = 'add_list'),
    path('del_list/<int:pk>/', home.views.del_list, name = 'del_list'),
    path('amount', donate.views.amount, name = 'amount'),
    path('payment/<int:don_id>/', donate.views.payment, name = 'payment'),
    path('viewdon', donate.views.viewdon, name = 'viewdon'),
    path('verify/<int:don_id>/', donate.views.verify, name = 'verify'),
    path('deletedon/<int:don_id>/', donate.views.deletedon, name = 'deletedon'),

    path('contact/', home.views.contact, name = 'contact'),
    path('achieve/', home.views.achieve, name = 'achieve'),
    path('connect/', home.views.connect, name = 'connect'),
    path('allconnect/', home.views.allconnect, name = 'allconnect'),
    path('allmember/', home.views.allmember, name = 'allmember'),
    path('deletecon/<int:con_id>/', home.views.deletecon, name = 'deletecon'),
    path('delmem/<int:mem_id>/', home.views.delmem, name = 'delmem'),
    path('addmember/', home.views.addmember, name='addmember'),


    path('addteam/', home.views.add_team, name = 'add_team'),
    path('delteam/<int:team_id>/', home.views.del_team, name='del_team'),


    path('addnews/', home.views.add_news, name = 'add_news'),
    path('delnews/<int:news_id>/', home.views.del_news, name='del_news'),

    path('evening/',home.views.evening, name = 'evening'),
    path('team/',home.views.team, name = 'team'),
    path('antyodaya/',home.views.antyodaya, name = 'antyodaya'),
    path('notice/', include('notice.urls')),
    path('event/', include('event.urls', namespace='event')),
    path('users/', include('users.urls', namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
