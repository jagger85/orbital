def get_icon(icon_class, paths):
    return SVG_TEMPLATE.format(icon_class=icon_class, paths=paths)


SVG_TEMPLATE = """
<svg xmlns="http://www.w3.org/2000/svg" width="{{width}}" height="{{height}}" viewBox="0 0 24 24" fill="none" stroke="{{color}}" stroke-width="{{stroke_width}}" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-{icon_class}">
{paths}
</svg>
"""

ICONS = {

    "house": get_icon("house", """
        <path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/>
        <path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
    """),
    "user": get_icon("user", """
        <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/>
        <circle cx="12" cy="7" r="4"/>
    """),
    "close": get_icon("square-x", """
    <path d="M18 6 6 18"/><path d="m6 6 12 12"/>
    """),
    "plus": get_icon("plus", """
        <path d="M5 12h14"/>
        <path d="M12 5v14"/>
    """),
    "settings": get_icon("settings", """
        <path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/>
        <circle cx="12" cy="12" r="3"/>
    """),
    "info": get_icon("info", """"
        <circle cx="12" cy="12" r="10"/>
        <path d="M12 16v-4"/>
        <path d="M12 8h.01"/>
    """),
    "error": get_icon("error", """"
        <circle cx="12" cy="12" r="10"/>
        <path d="m15 9-6 6"/>
        <path d="m9 9 6 6"/>
    """),
    "warning": get_icon("warning", """"
        <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/>
        <path d="M12 9v4"/>
        <path d="M12 17h.01"/>
                       """),
    "success": get_icon("success", """"
        <circle cx="12" cy="12" r="10"/>
        <path d="m9 12 2 2 4-4"/>
    """),
    "download": get_icon("download", """"
        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
        <polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/>
    """),
    "trash": get_icon("trash", """"
        <path d="M3 6h18"/><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/>
        <path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/><line x1="10" x2="10" y1="11" y2="17"/>
        <line x1="14" x2="14" y1="11" y2="17"/>              
    """),
     "file": get_icon("file", """"
        <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/>
        <path d="M14 2v4a2 2 0 0 0 2 2h4"/>
        <path d="M10 9H8"/>
        <path d="M16 13H8"/>
        <path d="M16 17H8"/>              
    """),
}