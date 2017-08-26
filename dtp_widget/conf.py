# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.conf import settings as base_settings


class DtpWidgetConfig(AppConfig):
    name = 'dtp_widget'


class Settings(object):
    BOOTSTRAP_DATETIMEPICKER_VERSION = '2.4.4'
    B3DATETIMEPICKER_JS = '//cdnjs.cloudflare.com/ajax/libs/smalot-bootstrap-datetimepicker/{}/js/bootstrap-datetimepicker.min.js'.format(
        BOOTSTRAP_DATETIMEPICKER_VERSION)
    B3DATETIMEPICKER_CSS = '//cdnjs.cloudflare.com/ajax/libs/smalot-bootstrap-datetimepicker/{}/css/bootstrap-datetimepicker.min.css'.format(
        BOOTSTRAP_DATETIMEPICKER_VERSION)

    def __getattribute__(self, name):
        if hasattr(base_settings, name):
            return getattr(base_settings, name)
        return object.__getattribute__(self, name)


settings = Settings()
