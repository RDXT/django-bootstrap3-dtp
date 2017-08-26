# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import get_language

from dtp_widget.conf import settings

register = template.Library()

supported_locales = [
    'ar', 'az', 'bg', 'bn', 'ca', 'cs', 'da', 'de', 'ee', 'el', 'es', 'fi', 'fr', 'he', 'hr', 'hu', 'hy', 'id', 'is',
    'it', 'ja', 'ka', 'ko', 'lt', 'lv', 'ms', 'nb', 'nl', 'no', 'pl', 'pt-BR', 'pt', 'ro', 'rs-latin', 'rs', 'ru',
    'sk', 'sl', 'sv', 'sw', 'th', 'tr', 'ua', 'uk', 'zh-CN', 'zh-TW'
]


def get_supported_language(language_country_code):
    if not language_country_code:
        return 'en'

    if language_country_code in supported_locales:
        return language_country_code

    language = language_country_code.split('-')[0]
    if language in supported_locales:
        return language

    return 'en'


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
