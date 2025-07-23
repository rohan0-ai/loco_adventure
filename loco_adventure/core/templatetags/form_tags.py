from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """
    Adds a CSS class to a form field widget.
    Usage: {{ form.field|add_class:"class-name" }}
    """
    # Check if field has 'field' attribute (BoundField)
    if hasattr(field, 'field'):
        existing_classes = field.field.widget.attrs.get('class', '')
        if existing_classes:
            css_class = existing_classes + ' ' + css_class
        field.field.widget.attrs['class'] = css_class
        return mark_safe(str(field))
    else:
        # If not a BoundField, return as is
        return field
