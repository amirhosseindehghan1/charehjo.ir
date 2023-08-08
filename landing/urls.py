from django.urls import path
from .views import discovery, market, develop_and_launch, problem_solving, register, grade_sheet, roadmap


urlpatterns = [
    path('', discovery),
    path('market/', market),
    path('develop-and-launch/', develop_and_launch),
    path('problem-solving/', problem_solving),
    path('register/', register),
    path('grade-sheet/', grade_sheet),
    path('roadmap/', roadmap, name='roadmap'),
    ]