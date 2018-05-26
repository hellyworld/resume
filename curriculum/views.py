from django.shortcuts import render
from curriculum.models import Experience, Education, Skill, Category


def home(request):
    all_experiences = Experience.objects.order_by("-id")
    all_educations = Education.objects.order_by("-id")
    all_categories = Category.objects.all()
    all_skills = Skill.objects.all()
    context = {
        'all_experiences': all_experiences,
        'all_educations': all_educations,
        'all_categories': all_categories,
        'all_skills': all_skills,
    }

    return render(request, 'base.html', context)
