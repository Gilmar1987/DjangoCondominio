from django.contrib import admin

# Register your models here.
# proprietarios/admin.py
from django.contrib import admin
from .models import Morador

@admin.register(Morador)
class MoradorAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'telefone')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('is_staff', 'is_active')
