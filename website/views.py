from django.shortcuts import render
from django.http import HttpResponse
from .models import ProjectModel
from django.template import loader


def index(request):
    latest_projects_list = ProjectModel.objects.order_by('-start_date')[:10]
    context = {'latest_projects_list': latest_projects_list}
    template = loader.get_template('templates/projects.html')
    return HttpResponse(template.render(context, request))

def logo(request):
    return render(request, 'templates/logo.html')

def projects(request):
    return HttpResponse(render(ProjectModel,'templates/projects.html'))
