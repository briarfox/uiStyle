# coding: utf-8

import ui
from uiStyle import style

view = ui.load_view('test_uiStyle')
style('example_style',view)
view.present('sheet')

