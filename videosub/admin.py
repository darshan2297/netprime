from django.contrib import admin

# Register your models here.
from videosub.models import subscription,member_record,membership

admin.site.register(membership)
admin.site.register(member_record)
admin.site.register(subscription)
