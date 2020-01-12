from django import template

register = template.Library()
@register.filter
def in_stage(matches, stage):
    return matches.filter(stage=stage)