from django.db import models
from django import forms


from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, FieldRowPanel
from wagtail.models import Page, Orderable
from datetime import datetime
from wagtail import blocks
from modelcluster.fields import ParentalKey
from .blocks import DescriptionBlock, TaskBlock
from django.shortcuts import render

from wagtail.admin.panels import FieldPanel, InlinePanel, StreamFieldPanel
from django.utils.functional import cached_property
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from django.utils.timezone import now
# Create your models here.


class TaskPage(Page):
    parent_page_types = ['tasks.TaskIndexPage']
    template = 'tasks/task_page.html'

    created_at = models.DateTimeField(default=now, blank=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    complete = models.BooleanField(default=False, blank=True, null=True)
    date = models.DateTimeField(default=now, blank=True, null=True)
    # body = StreamField([
    # ('title', blocks.CharBlock(required=True, form_classname="title")),
    # ('taskblock', TaskBlock()),
    # ('description', DescriptionBlock()),
    # ('complete', blocks.BooleanBlock(required=False)),
    # ('date', blocks.DateTimeBlock(required=True, help_text="chose task deadline")),
    # ], block_counts= {}, max_num=4,
    # use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('complete'),
        FieldPanel('date'),
        FieldPanel('created_at'),   
    ]
    
    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["steps"] = TaskSteps.objects.get().body

        return context
    
    # def save(self, *args, **kwargs):
    #     task_index_page = TaskIndexPage.objects.all()
    #     title = request.POST.get('title', '')
    #     self.get_new_page(task_index_page, title, description, complete, date, created_at)
    #     super().save(*args, **kwargs)


    # def get_new_page(task_index_page, title, description, complete, date, created_at):
        
    #     new_page = TaskPage(
    #                         title = title,
    #                         description = description,
    #                         complete = complete,
    #                         date = date,
    #                         created_at = created_at,
    #                         )

    #     task_index_page.add_child(instance=new_page)
    #     new_page.save_revision().publish()
    #     new_page.save()
    #     return new_page
    
    # new_page = get_new_page(task_index_page, title, description, complete, date, created_at)

class TaskIndexPage(Page):
    subpage_types = ['tasks.TaskPage']
    parent_page_types = ['home.HomePage']
    
    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["tasks"] = TaskPage.objects.live().public()
        return context



class TaskSteps(Page):
    parent_page_types = ['tasks.TaskPage']
    max_count_per_parent = 1
    
    task = models.ForeignKey(
        'tasks.TaskPage',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+')

    step = models.CharField(max_length=50, null=True, blank=True)

    body = StreamField([
        ('step', blocks.CharBlock(required=False))
    ])

    content_panels = Page.content_panels + [
        FieldPanel('task'),
        FieldPanel('body')
    ]

    
    


