'''
Style pythonista ui.View from one .pyui template.

To use: 
    *create a ui view and add the controls that you would like styled.
    *Each control needs a unique name such as lbl1 - a style of label, lbl2 - another style of label.
    *To access any of your styles in a projects ui.View controlls, just set the name of the style to the front of the control name.
    Example: Style ui.View has a lbl1. Your main view could have a lbl1name. the lbl1 is removed when the view is styled.
    
    To style a view call uiStyle.style([path|ui.View],view_to_style)
    
'''
import ui


#attributes to style. 
#These attributes will be used to style the passed ui.view
attr_list = ['background_color',
             'tint_color',
             'border_width',
             'border_color',
             'corner_radius',
             'font',
             'alpha',
             'alignment',
             'line_break_mode',
             'text_color',
             'bar_tint_color',
             'title_color',
             'indicator_style',
             'bordered',
             ]

style_list = {}


def style(style,view):
    '''
    Used to set the style of a ui.View. 
    style(style,view)
    @param (string|ui.View) style - ui.View or String path of the ui.View
    @param (ui.View) view - view to style
    '''
    if type(style) == str:
        try:
            style = ui.load_view(style)
        except Exception, e:
            print e
    style_list = _generate_styles(style)
    view.background_color = style.background_color
    for v in view.subviews:
        passed_type = str(type(v).__name__)

        if passed_type in style_list:
            for key in style_list[passed_type]:

                if v.name:
                    if key in v.name:
                        for attr in attr_list:
                            try:
                                style_attr = getattr(style[key],str(attr))
                                setattr(view[v.name],attr,style_attr)
                            except:
                                pass #attribue does not exist for controll
                        v.name = v.name.replace(key,'')
                        break



def _generate_styles(view):
    style_list = {}
    for v in view.subviews:
        try:
            style_list[str(type(v).__name__)].append(v.name)
        except :
            style_list[str(type(v).__name__)] = []
            style_list[str(type(v).__name__)].append(v.name)
    return style_list


