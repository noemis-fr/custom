# -*- coding: utf-8 -*-
# Copyright (C) 2015-Today Noemis (http://www.noemis.fr)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account - Tag on Account Invoice line',
    'version': '1.0',
    'category': 'Accounting',
    'description': """
Products tags on account invoice line and tags on invoice line search criterias
===============================================================================

    """,
    'author': 'Sylvain LE GAL',
    'website': 'http://www.noemis.fr',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'product_tags',
        'e3z_account_invoice_line',
    ],
    'data': [
        'views/view_account_invoice_line.xml',
    ],
}
