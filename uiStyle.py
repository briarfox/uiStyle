'''
Style pythonista ui.View from one .pyui template.

To use: 
    *create a ui view and add the controls that you would like styled.
    *Each control needs a unique name such as lbl1 - a style of label, lbl2 - another style of label.
    *To access any of your styles in a projects ui.View controlls, just set the name of the style to the front of the
        control name.
    Example: Style ui.View has a lbl1. Your main view could have a lbl1name. the lbl1 is removed when the view is
        styled.
    
    To style a view call uiStyle.style([path|ui.View],view_to_style)
    
'''
import ui

#attributes to style. 
#These attributes will be used to style the passed ui.view
attr_list = '''alignment alpha background_color bar_tint_color border_color border_width bordered 
    corner_radius font indicator_style line_break_mode text_color tint_color title_color'''.split()

#style_list = {}  # do we need this global?

def object_type_as_str(obj):
    return str(type(obj).__name__)

def style(style_view, view):  # function and parameter have same name... Eeekk.
    '''
    Used to set the style of a ui.View. 
    style(style,view)
    @param (string|ui.View) style - ui.View or String path of the ui.View
    @param (ui.View) view - view to style
    '''
    if type(style_view) == str:
        try:
            style_view = ui.load_view(style_view)
        except Exception, e:
            print e
    style_list = _generate_styles(style_view)
    view.background_color = style_view.background_color
    for v in view.subviews:
        passed_type = object_type_as_str(v)
        if v.name and passed_type in style_list:
            for key in style_list[passed_type]:
                if key in v.name:
                    for attr in attr_list:
                        try:
                            style_attr = getattr(style_view[key], str(attr))
                            setattr(view[v.name], attr, style_attr)
                        except:
                            pass #attribue does not exist for this control
                    v.name = v.name.lstrip(key)
                    break

def _generate_styles(style_view):
    style_list = {}
    for v in style_view.subviews:
        view_type_str = object_type_as_str(v)
        try:
            style_list[view_type_str].append(v.name)
        except KeyError:
            style_list[view_type_str] = [ v.name ]
    return style_list

if __name__ == '__main__':
    import test_uiStyle
