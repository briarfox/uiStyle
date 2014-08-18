uiStyle
=======

Style pythonista ui.View from one .pyui template.

###To use: 
* Create a ui.View file and add controls that you would like to have all other views styled after.
* Each control needs a unique name such as lbl1 - a style of label, lbl2 - another style of label.
* To use a controls style, just set the name of the style to the front of the control name.
    * Example: Style ui.View has a lbl1. Your main view could have a lbl1name. the lbl1 is removed when the view is styled.
    
To style a view call uiStyle.style(path_or_view_object, view_to_style)
