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
    'name': 'Intermediate Stock Quantity',
    'version': '1.0',
    'category': 'Stock',
    'description': """
Compute intermediate Stock value
=========================================


Copyright
---------
* Noemis (http://www.noemis.fr)

    """,
    'author': 'Floren THOMAS',
    'website': 'http://www.noemis.fr',
    'license': 'AGPL-3',
    'depends': [
        'stock','e3z_lead_sale_ipbox'
    ],
    'data': [
        'views/view_product_product.xml',
    ],
    'demo': [

    ],
}
