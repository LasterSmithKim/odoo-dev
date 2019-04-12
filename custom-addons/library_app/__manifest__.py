{
    'name': 'Library Management',
    'description': 'Manage library book catalogue and lending.',
    'author': 'Alan Hou',
    'depends': ['base'],
    'application': True,
    'data': [
        'views/library_menu.xml',
        'security/ir.model.access.csv',
        'security/library_security.xml',
        'views/book_view.xml',
        'views/book_list_template.xml',
    ],
}
