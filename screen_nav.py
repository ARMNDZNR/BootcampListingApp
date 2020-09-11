toolbar_helper = """
ScreenManager:
    ListScreen:
    PlusScreen:

<ListScreen>:
    name: 'Lists'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar: 
            title: 'Bootcamp'
            elevation: 7
            MDFloatingActionButton:
                icon: 'plus'
                theme_text_color: 'Custom'
                elevation: 0
                pos_hint: {'center_y':0.5}
                md_bg_color: app.theme_cls.primary_color
                on_release: root.manager.current = 'Plus'
        MDLabel:
            text: ''
            halign: 'center'

<PlusScreen>:
    name: 'Plus'
    BoxLayout:
        orientation: 'vertical'
        MDTextField:
            hint_text: "Enter list title"
            size_hint_x: None
            width: 300 
        MDTextField:
            hint_text: "Enter list description"
            size_hint_x: None
            width: 300
        MDTextField:
            hint_text: "Deadline"
            size_hint_x: None
            width: 300
        MDLabel:
            text: ''
            halign: 'center'
"""
