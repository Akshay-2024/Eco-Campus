from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'pnr', 'department', 'semester')
    search_fields = ('user__username', 'user__email', 'pnr', 'department')
    list_filter = ('department', 'semester')
