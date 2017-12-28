from django.contrib import admin
from memo.models import Memo

# Register your models here.

class MemoAdmin(admin.ModelAdmin):
    list_display = ('content', 'last_modified')

admin.site.register(Memo, MemoAdmin)