from django.urls import path
from main.views import (
    create_experience,
    create_project,
    create_experience_ajax, # Diimpor untuk endpoint AJAX
    delete_experience,
    delete_project,
    edit_experience,
    get_experience_json,
    get_projects_json,
    login_user,
    logout_user,
    register,
    show_experience,
    show_interest,
    show_main,
    show_projects,
    toggle_star,
    toggle_star_experience,
    create_project_ajax
)

app_name = "main"

urlpatterns = [
    # Main & Experience
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"), # Rute baru AJAX
    path("experience/<uuid:experience_id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("experience/<uuid:experience_id>/star/", toggle_star_experience, name="toggle_star_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    
    # Projects
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/<int:project_id>/delete/", delete_project, name="delete_project"),
    path("projects/<int:project_id>/star/", toggle_star, name="toggle_star"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    
    # Auth & Interest
    path("interest/", show_interest, name="show_interest"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]