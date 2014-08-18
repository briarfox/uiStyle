uiStyle
=======

Style pythonista ui.View from one .pyui template.

###To use: 
    *create a ui view and add the controls that you would like styled.
    *Each control needs a unique name such as lbl1 - a style of label, lbl2 - another style of label.
    *To access any of your styles in a projects ui.View controlls, just set the name of the style to the front of the control name.

Example: Style ui.View has a lbl1. Your main view could have a lbl1name. the lbl1 is removed when the view is styled.
    
To style a view call uiStyle.style([path|ui.View],view_to_style)
