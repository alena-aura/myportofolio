from django.shortcuts import render
from main.models import Experience

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