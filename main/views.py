from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProjectForm
from main.models import Experience, Interest, Project


def show_main(request):
    context = {
        "name": "Alena Aura Deviyana",
        "npm": "2506656394",
        "study_program": "S1 Sistem Informasi",
        "bio": "A university student and UI/UX designer, I am committed to developing functional and aesthetically pleasing digital solutions. Beyond my academic responsibilities, I actively pursue interests in global cuisine, fine art appreciation, and reading, which continually inspire my creative process",
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Alena Aura Deviyana",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_interest(request):
    interests = Interest.objects.all()
    context = {
        'name': 'Alena Aura Deviyana',
        'interests': interests
    }
    return render(request, 'interest.html', context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "project_form.html", context)

def show_projects(request):
    json_response = get_projects_json(request)
    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Alena",
        "surname": "Alena",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")
    return redirect("main:show_projects")