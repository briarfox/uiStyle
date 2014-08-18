# coding: utf-8

import ui, uiStyle ; reload(uiStyle)

view = ui.load_view('test_uiStyle')
uiStyle.style('example_style',view)
view.present('sheet')
