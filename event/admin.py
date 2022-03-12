from django.contrib import admin

# hey si have to show up something on admin page
#if you dont want superuser to mess with database dont add

from .models import Events
admin.site.register(Events)


from .models import Gallery
admin.site.register(Gallery)


from .models import Program
admin.site.register(Program)