from django.contrib import admin
from curriculum.models import Experience, Education, Skill, Category


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


class SkillAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Skill._meta.get_fields()]

    class Meta:
        model = Skill


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']


admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Category, CategoryAdmin)
