from django.contrib import admin
from .models import *

admin.site.register(Good)
admin.site.register(Order)


# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "is_superuser", "is_staff", "is_active", "test"]
    fields = ["email"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["name", "updated_at"]
    readonly_fields = ["updated_at"]