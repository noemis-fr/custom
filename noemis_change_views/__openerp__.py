# -*- encoding: utf-8 -*-
{
    'name': 'Noemis - Custom Views Changes',
    'version': '1.0',
    'category': 'Custom',
    'description': """
    """,
    'website': 'http://www.noemis.fr',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'sale_margin',
        'sale_order_title',
        'sale_order_dates',
        'e3z_lead_sale_ipbox',
        'web_dashboard_tile',
    ],
    'data': [
        'views/purchase_order_view.xml',
        'views/sale_order_view.xml',
    ],
    'css': [
        'static/src/css/css.css',
    ],
}
