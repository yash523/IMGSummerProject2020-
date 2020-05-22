from django.contrib import admin
from .models import App, Bug, Comment, Reply

# Register your models here.
admin.site.register(App)
admin.site.register(Bug)
admin.site.register(Comment)
admin.site.register(Reply)