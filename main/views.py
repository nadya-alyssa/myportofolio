from django.shortcuts import render

from main.models import Experience, Education


def show_main(request):
    context = {
        "name": "Nadya Alyssa Azzahra",
        "npm": "2506599270",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Creative and ambitious second-year Information Systems student at Universitas Indonesia with strong experience in event coordination and creative design. Skilled at managing projects, collaborating with teams, and delivering impactful results. Passionate about combining technology, creativity, and social impact. Highly adaptable, eager to learn, and committed to continuous growth."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Nadya Alyssa Azzahra",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Nadya Alyssa Azzahra",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)