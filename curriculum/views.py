from django.shortcuts import render
from curriculum.models import Experience, Education


def home(request):
    all_experiences = Experience.objects.order_by("id").reverse()  # order_by_-id
    all_educations = Education.objects.order_by("id").reverse()
    context = {
        'all_experiences': all_experiences,
        'all_educations': all_educations,
    }
    return render(request, 'base.html', context)
