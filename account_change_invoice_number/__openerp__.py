# -*- encoding: utf-8 -*-
##############################################################################
#
#    Account - Change Invoice Number module for Odoo
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
    'name': 'Account - Change Invoice Number',
    'version': '1.0',
    'category': 'Accounting',
    'description': """
Possibility to change the number of an invoice
==============================================

In certains cases, it is interesting to change the number of the supplier
or customer invoices generated by default.
A typical case is when accounting year is set on 2 years, and so accounting
sequences can not be correctly.

Important
---------

Use this module with caution.


Copyright
---------

* Noemis (http://www.noemis.fr)

    """,
    'author': 'Sylvain LE GAL',
    'website': 'http://www.noemis.fr',
    'license': 'AGPL-3',
    'depends': [
        'account',
    ],
}
