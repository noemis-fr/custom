# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Add task list on orders",
    "summary": "Add task on orders and deliveries",
    "version": "7.0.1.0.0",
    "category": "Uncategorized",
    "website": "https://odoo-community.org/",
    "author": "<AUTHOR(S)>, Florent THOMAS",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "sale", "project_mrp", "stock"
    ],
    "data": [
        
        "views/sale_order_view.xml",
        "views/picking.xml",
    
    ],
    'css': ['static/src/css/noemis.css',
     
	], 
    "demo": [
        
    ],
    
}
