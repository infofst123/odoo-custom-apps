{
    'name':"First App",
    'author':"Kais Louati",
    'category': '',
    'version' :'1.0.0',
    'depends': ['base',		
    
    ],
    'data':[
        'views/base_menu.xml',
        'views/property_view.xml',
        'security/ir.model.access.csv',
           ],
    'assets':{
        'web.assets_backend':['app_one/static/assets/css/properties.css']
    },
    'application': True
}