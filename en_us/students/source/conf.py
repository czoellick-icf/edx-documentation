# -*- coding: utf-8 -*-
import sys, os

sys.path.append('../../../')

from shared.conf import *

html_theme = 'edx_theme'

html_theme_path = ['../../_themes']

html_favicon = '../../_themes/edx_theme/static/css/favicon.ico'

project = u'EdX Learner\'s Guide'

exclude_patterns = ['links.rst', 'reusables/*', 'SFD_mathformatting.rst']

tags.add('Partners')
product = 'Partners'
set_audience(PARTNER, LEARNERS)

def setup(app):
    app.add_config_value('product', '', True)
