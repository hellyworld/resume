from django.contrib import admin
from .models import Experience


class ExperienceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Experience._meta.get_fields()]

    class Meta:
        model = Experience


admin.site.register(Experience, ExperienceAdmin)

