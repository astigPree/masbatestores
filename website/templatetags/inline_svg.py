import os
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def inline_svg(path):
    """
    Usage: {% inline_svg 'assets/arrow.svg' %}
    Will load from: static/assets/arrow.svg
    """
    full_path = os.path.join(settings.BASE_DIR, 'static', path)
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return mark_safe(f.read())
    except FileNotFoundError:
        return f"<!-- SVG not found: {path} -->"
