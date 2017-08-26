# -*- coding: utf-8 -*-
import re

from django import forms


class DtpMixin(object):
    def __init__(self, attrs=None, dtp_attrs=None):
        # Immediate finalization, return the structure
        if dtp_attrs is None:
            dtp_attrs = {}
        if attrs is None:
            attrs = {}
        for k, v in dtp_attrs.items():
            # We set properties as underscore string
            underscore = re.sub('([A-Z]+)', r'-\1', k).lower()
            # we convert value to string (mainly for boolean values)
            attrs["dtp-%s" % underscore] = str(v)

        attrs['data-dtp'] = "dtp"
        super(DtpMixin, self).__init__(attrs)

    def _get_media(self):
        """
        Construct Media as a dynamic property.
        .. Note:: For more information visit
            https://docs.djangoproject.com/en/1.8/topics/forms/media/#media-as-a-dynamic-property
        """
        return forms.Media(
            js=('dtp_widget/js/dtp_init.js',),
        )

    media = property(_get_media)


class DtpWidget(DtpMixin, forms.DateTimeInput):
    pass
