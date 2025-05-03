from django.contrib import admin
from .models import Message, Thread
# Register your models here.
class ThreadAdmin(admin.ModelAdmin):
    readonly_fields = ("updated",)
admin.site.register(Message)
admin.site.register(Thread, ThreadAdmin)