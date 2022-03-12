from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Volunteer)
admin.site.register(News)
admin.site.register(Team)
admin.site.register(Member)

admin.site.register(Alumni)
