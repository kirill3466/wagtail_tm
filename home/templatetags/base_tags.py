from wagtail.core.models import Site

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    # This returns a core.Page. The main menu needs to have the site.root_page
    # defined else will return an object attribute error ('str' object has no
    # attribute 'get_children')
    return Site.find_for_request(context["request"]).root_page

@register.inclusion_tag("tags/top_menu.html", takes_context=True)
def top_menu(context, parent):
    menuitems = parent.get_children().live().in_menu()
    
    return {
        "menuitems": menuitems,
        # required by the pageurl tag that we want to use within this template
        "request": context["request"],
    }

@register.inclusion_tag("tags/left_menu.html", takes_context=True)
def left_menu(context, parent):
    menuitems = parent.get_children().live().in_menu()
    
    return {
        "menuitems": menuitems,
        # required by the pageurl tag that we want to use within this template
        "request": context["request"],
    }