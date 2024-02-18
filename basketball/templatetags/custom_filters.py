from django import template

register = template.Library()


@register.filter(name="get_attribute")
def get_attribute(attributes, attribute):
    return attributes.get(attribute, None)
