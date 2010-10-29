# -*- coding: utf-8 -*-
"""
    pidsim_models.base
    ~~~~~~~~~~~~~~~~~~

    Base reference model.

    :copyright: 2010 by Rafael Goncalves Martins
    :license: GPL-2, see LICENSE for more details.
"""

__all__ = ['ReferenceModel', 'I18nStr']

import inspect

class ReferenceModel(object):
    
    name = None
    description = None
    latex = None
    
    def __init__(self, locale):
        self._locale = locale
        self._parse_callback_parameters()
    
    def callback(self):
        raise NotImplementedError('You should overwrite this method.')

    def _parse_callback_parameters(self):
        argspec = inspect.getargspec(self.callback)
        self.args = argspec.args[1:]


class I18nStr(list):
    
    def __call__(self, locale):
        for my_locale, string in self:
            if my_locale == locale:
                return string
        return self[0][1]
