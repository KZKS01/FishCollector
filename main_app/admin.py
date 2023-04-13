from django.contrib import admin
from .models import Fish, Tank

# Register your models here.
admin.site.register([Fish, Tank])