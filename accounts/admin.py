from django.contrib import admin
from django.contrib.auth.models import User

# Optionally customize the admin display
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

admin.site.unregister(User)  # Unregister the default
admin.site.register(User, UserAdmin)
