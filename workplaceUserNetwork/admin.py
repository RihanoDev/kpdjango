from django.contrib import admin
from .models import User, Department, Division, Interaction, WorkplaceUserNetwork

admin.site.register(User)
admin.site.register(Department)
admin.site.register(Division)
admin.site.register(Interaction)
admin.site.register(WorkplaceUserNetwork)
