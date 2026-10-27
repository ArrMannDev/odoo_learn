{
    "name": "Shop Management",
    "version": "19.0.1.0.0",
    "category": "Sales",
    "summary": "Simple Shop Course Example for Junior Odoo Developers",
    "depends":["product"],
    "data":[
        'security/ir.model.access.csv',
        'views/shop_item_views.xml',
        'views/shop_menu_view.xml',    
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}