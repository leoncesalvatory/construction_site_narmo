from django import template

register = template.Library()

@register.filter
def filter_category(queryset, category):
    return queryset.filter(category=category)