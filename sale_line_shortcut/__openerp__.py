# -*- encoding: utf-8 -*-
##############################################################################
#
#    Sale - Custom Behaviour on Line Changes module for Odoo
#    Copyright (C) 2015-Today Noemis (http://www.noemis.fr)
#    Copyright (C) 2015-Today GRAP (http://www.grap.coop)
#
#    @author: Sylvain LE GAL (https://www.twitter.com/legalsylvain)
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
    'name': 'Sale Order Add button on lines to display next moves',
    'version': '1.0',
    'category': 'Sale',
    'description': """
Customization when Sale Order Lines Change during quotation
===========================================================

Let users customize quotation options:

* Possibility to disable stock warning;

* Possibility to disable data changes (and above all prices), when user change
  quantity;

Note
----

This module is not active by default, and settings must be done by users,
because there are managed by groups.

    """,
    'author': 'Florent THOMAS,Noemis',
    'license': 'AGPL-3',
    'depends': [
        'sale_stock',
    ],
    'data': [
        'views/sale_order_view.xml',
        'views/picking_view.xml',
    ],
}
