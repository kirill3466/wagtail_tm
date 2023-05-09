from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page, Orderable
from datetime import datetime
from wagtail import blocks
from modelcluster.fields import ParentalKey

from django.utils.timezone import now

class HomePage(Page):
    max_count = 1