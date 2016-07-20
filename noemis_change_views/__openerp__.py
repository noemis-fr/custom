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
        'purchase',
        'sale',
        'sale_margin',
        'sale_order_title',
        'sale_order_dates',
        'e3z_lead_sale_ipbox',
        'web_dashboard_tile',
    ],
    'data': [
        'views/view_stock_picking.xml',
        'views/view_purchase_order.xml',
        'views/view_sale_order.xml',
        'views/view_account_invoice.xml',
    ],
    'css': [
        'static/src/css/css.css',
    ],
}
