from django.urls import path
from main.views import (
    create_project,
    delete_project,
    get_projects_json,
    show_experience,
    show_interest,
    show_main,
    show_projects,
    create_experience,
    edit_experience,
    delete_experience,
    get_experience_json,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("projects/add/", create_project, name="create_project"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/edit/", edit_experience, name="edit_experience"), # Gunakan <int:experience_id> jika id berupa integer
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("interest/", show_interest, name="show_interest"),
    path("projects/", show_projects, name="show_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
]