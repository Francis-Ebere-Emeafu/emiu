from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy


from project.models import Project
from project.forms import ProjectForm
from location.models import *


def new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            lga_id = request.POST.get('lga')
            lga = LGA.objects.get(id=lga_id)
            print("***********")
            print(lga.name)
            print("***********")
            print(project)
            project.lga = lga
            project.save()
            messages.info(request, 'New Project Save Successfully')
            return redirect('new_project')
    else:
        form = ProjectForm()
    return render(request, 'project/new_project2.html', {'form':form})


def load_lgas(request):
    state_id = request.GET.get('state')
    print('-----')
    print(state_id)
    lgas = LGA.objects.filter(state_id=state_id).order_by('name')
    for lga in lgas:
        print(lga)
    return render(request, 'project/lga_dropdown_list.html', {'lgas': lgas})



class ProjectListView(ListView):
    model = Project
    context_object_name = 'project'


class ProjectCreateView(CreateView):
    model = Project
    fields = ('title', 'award_date', 'proposed_completion_date', 'contract_sum_ngn', 'contract_sum_usd', 
        'state', 'lga', 'contractor', 'consultant', 'department', 'description')
        
    # fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('project_test_list')


class ProjectUpdateView(UpdateView):
    model = Project
    fields = ('title', 'award_date', 'proposed_completion_date', 'contract_sum_ngn', 'contract_sum_usd', 
        'state', 'lga', 'contractor', 'consultant', 'department', 'description')
        
    # fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('project_test_list')