from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from wagtail.models import Page
from .forms import TaskCreateForm, CustomTaskUpdateForm, StepsForm
from .models import TaskPage, TaskSteps, TaskIndexPage
from django.conf import settings
from django.shortcuts import render, redirect
from django.utils.timezone import now
from datetime import datetime
class TaskCreate(LoginRequiredMixin, CreateView):
    model = TaskPage
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = 'tasks/task_create.html'
    form_class = TaskCreateForm
    
    # def get_context_data(self, *args, **kwargs):
    #     context = super(TaskCreate, self).get_context_data(**kwargs)
    #     context['form'] = TaskCreateForm()
    #     context['user'] =  self.request.user
       
    #     return context
    
    # parent_page = TaskIndexPage.objects.all()[0] # get a suitable parent 

    # page = TaskPage(
    #         title="Sample name",
    #         depth=4,
    #         path="Some random path",
    # )

    # parent_page.add_child(instance=page)

def create_page(request, pk):
    form = TaskCreateForm()
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():

            title = request.POST.get('title', ''),
            description = request.POST.get('description', ''),
            complete = True if request.POST.get('complete', '') == "on" else False,
            date = request.POST.get('date', ''),
            parent_page = TaskIndexPage.objects.all()[0]
            create_page_data(parent_page, title, description, complete, date)
        return redirect(settings.LOGIN_REDIRECT_URL)
    
    context = {'form': form}
    return render(request, 'tasks/task_create.html', context)

def create_page_data(parent_page, title, description, complete, date):
    new_page = TaskPage(
                        title = title[0],
                        description = description[0],
                        complete = complete[0],
                        date = date[0],
                        )
    
    parent_page.add_child(instance=new_page)
    new_page.save_revision().publish()
    new_page.save()
    return new_page


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = TaskPage
    success_url = settings.LOGIN_REDIRECT_URL
    context_object_name = 'task'
    template_name = 'tasks/task_confirm_delete.html'
    

class CustomTaskUpdateView(UpdateView):
    model = TaskPage
    form_class = CustomTaskUpdateForm
    success_url = settings.LOGIN_REDIRECT_URL

    def get_context_data(self, *args, **kwargs):
        context = super(CustomTaskUpdateView, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context['tasks'] = TaskPage.objects.live().public()
        return context

class TaskStepsUpdateView(UpdateView):
    model = TaskSteps
    form_class = StepsForm
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = 'tasks/task_steps.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TaskStepsUpdateView, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context['steps'] = TaskSteps.objects.all()
        return context


