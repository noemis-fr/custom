# -*- encoding: utf-8 -*-
##############################################################################
#
#    Sale Order Title module for Odoo
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
    'name': 'Customer Task On invoice',
    'version': '1.0',
    'category': 'Sale',
    'description': """
Use the task fields on partner to display additionnal info on invoices
======================================



Copyright
---------
* Noemis (http://www.noemis.fr)

    """,
    'author': 'Florent THOMAS',
    'website': 'http://www.noemis.fr',
    'license': 'AGPL-3',
    'depends': [
        'sale','stock', 'project'
    ],
    'data': [
        'views/invoice.xml',
        'views/picking.xml',
        'views/partner.xml',
    ],
    'demo': [
    ],
}
