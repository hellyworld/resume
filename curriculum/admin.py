from django.contrib import admin
from curriculum.models import Experience, Education


class ExperienceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Experience._meta.get_fields()]
    change_form_template = 'curriculum/admin/change_form.html'

    class Meta:
        model = Experience


class EducationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Education._meta.get_fields()]
    change_form_template = 'curriculum/admin/change_form.html'

    class Meta:
        model = Education


admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
