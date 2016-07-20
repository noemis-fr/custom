# -*- encoding: utf-8 -*-
##############################################################################
#
#    Sale Order Duration module for Odoo
#    Copyright (C) 2016-Today Noemis (http://www.noemis.fr)
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
    'name': 'Sale Order Duration',
    'version': '1.0',
    'category': 'Sale',
    'description': """
Compute duration for Sale orders
================================

The module extends sale functionnalities, adding two new dates fields on
sale order:

* begin Date, when the order is validated
* End Date, when the order is shipped

An extra computed duration field is available, that is the difference
between the two dates.

Copyright
---------
* Noemis (http://www.noemis.fr)

    """,
    'author': 'Sylvain LE GAL',
    'website': 'http://www.noemis.fr',
    'license': 'AGPL-3',
    'depends': [
        'sale',
    ],
    'data': [
        'views/view_sale_order.xml',
    ],
}
