# -*- encoding: utf-8 -*-
##############################################################################
#
#    Stored Stock Quantity module for Odoo
#    Copyright (C) 2015-Today Noemis (http://www.noemis.fr)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Stored Stock Quantity',
    'version': '1.0',
    'category': 'Stock',
    'description': """
Compute and store in Database Stock value
=========================================

* Adds 2 new fields on 'product.product' models 'stored_qty_available' and
  'stored_virtual_available'.
  That two fields are based on non stored according fields.

* Allows to reorder product by qty in a tree view.

* Adds two filters, quantity > 0 and quantity <= 0

Copyright
---------
* Noemis (http://www.noemis.fr)

    """,
    'author': 'Sylvain LE GAL',
    'website': 'http://www.noemis.fr',
    'license': 'AGPL-3',
    'depends': [
        'product','stock', 'e3z_lead_sale_ipbox'
    ],
    'data': [
        'views/view_product_product.xml',
        'views/action.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/res_groups.yml',
    ],
}
