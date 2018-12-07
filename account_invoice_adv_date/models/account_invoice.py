# -*- coding: utf-8 -*-
# Copyright (C) 2015-Today Noemis (http://www.noemis.fr)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp.osv import fields
from openerp.osv.orm import Model


class account_invoice_line(Model):
    _inherit = 'sale.order'

    _columns = {
        'adv_date' : fields.date('ADV date'),
    }