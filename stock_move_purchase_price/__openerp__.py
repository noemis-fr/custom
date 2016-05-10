# -*- coding: utf-8 -*-
# Copyright (C) Copyright (C) 2015-Today Noemis (http://www.noemis.fr)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Stock Move - Purchase Price',
    'version': '1.0',
    'category': 'Purchase',
    'description': """
Add Purchase price on stock Moves
=================================

Copyright
---------
* Noemis (http://www.noemis.fr)

    """,
    'author': 'Sylvain LE GAL',
    'website': 'http://www.noemis.fr',
    'license': 'AGPL-3',
    'depends': [
        'stock',
        'purchase',
    ],
    'data': [
        'views/view_stock_move.xml',
        'views/view_stock_picking.xml',
    ],
}
