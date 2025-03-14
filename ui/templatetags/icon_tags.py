from django import template
from .icons import ICONS
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def render_icon(name, width=24, height=24, color="currentColor", stroke_width=2):
    """
    Renders an SVG icon with customizable attributes.

    Django's template engine escapes HTML by default for security reasons. 
    This means that when returning an SVG string from a custom template tag
    gets treated as plain text instead of being rendered as HTML

    To fix this, it has to be marked as safe 
    so that Django knows it should be rendered as HTML.
    Django's mark_safe function from the django.utils.safestring
    will mark the string as safe and will properly render as an html tag

    Usage:
        {% load icon_tags %}
        {% render_icon 'house' width=32 height=32 color='#FF5733' stroke_width=1.5 %}
    """
    if name not in ICONS:
        raise ValueError(f"Icon '{name}' not found.")

    icon_template = ICONS[name]
    icon_template = icon_template.format(
        width=width,
        height=height,
        color=color,
        stroke_width=stroke_width
    )
    
    return mark_safe(icon_template)
