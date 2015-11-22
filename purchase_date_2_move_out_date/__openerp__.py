# -*- encoding: utf-8 -*-
##############################################################################
#
#    Purchase Date to Move Out Date module for Odoo
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
    'name': 'Purchase Date to Move Out Date',
    'version': '1.0',
    'category': 'Sale',
    'description': """
Change purchase Order Line Date impact Customer (out) Moves Date
================================================================

The aim of this module is to deal with floating picking in dates that impact
picking out dates.

* When a purchase order is validated, if the purchaser change dates on purchase
  order line dates, it will changes the date of the associated forcast move in.

Technical Information
---------------------

* This module remove readonly features on purchase order line, when order is
  confirmed. Use this feature with caution.


Copyright
---------
* Noemis (http://www.noemis.fr)

    """,
    'author': 'Sylvain LE GAL',
    'website': 'http://www.noemis.fr',
    'license': 'AGPL-3',
    'depends': [
        'purchase',
        'stock',
        'sale',
    ],
    'data': [
        'views/picking_view.xml',
    ],
}
