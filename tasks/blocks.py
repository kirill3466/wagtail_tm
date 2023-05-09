from wagtail.core.blocks import StructBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks

class DescriptionBlock(blocks.RichTextBlock):
    
        template = 'blocks/description.html'

class TaskBlock(StructBlock):
    title = blocks.CharBlock(required=True, form_classname="title")
    description = blocks.RichTextBlock(required=True)
    complete = blocks.BooleanBlock(required=False)
    date = blocks.DateTimeBlock(required=True, help_text="chose task deadline")

    class Meta:
        template = 'blocks/taskblock.html'