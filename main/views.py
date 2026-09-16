from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Education
from main.forms import ExperienceForm


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
    json_response = get_experience_json(request)

    experience = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experience = [exp.object for exp in experience]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Nadya Alyssa Azzahra",
        "experience_list": experience,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Nadya Alyssa Azzahra",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Alyssa",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")