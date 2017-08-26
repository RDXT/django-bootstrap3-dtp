# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import get_language

from .conf import settings
from .widgets import get_supported_language

register = template.Library()


@register.simple_tag
def dtp_widget_css():
    css_template = u'<link rel="stylesheet" href="{}" type="text/css" charset="utf-8">'
    css = css_template.format(settings.B3DATETIMEPICKER_CSS)
    return mark_safe(css)


@register.simple_tag()
def dtp_widget_js():
    lang = get_language()
    language = get_supported_language(lang)
    js_template = u'<script src="{}" type="text/javascript" charset="utf-8"></script>'
    js = js_template.format(settings.B3DATETIMEPICKER_JS)
    if language != 'en':
        lang_template = \
            u"//cdnjs.cloudflare.com/ajax/libs/smalot-bootstrap-datetimepicker/{}/js/locales/bootstrap-datetimepicker.{}.js".format(
                settings.BOOTSTRAP_DATETIMEPICKER_VERSION,
                language
            )
        js += js_template.format(lang_template)
    return mark_safe(js)
