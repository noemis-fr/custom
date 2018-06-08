# -*- coding: utf-8 -*-
# Copyright (C) 2015-Today Noemis (http://www.noemis.fr)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp.osv import fields
from openerp.osv.orm import Model


class account_invoice_line(Model):
    _inherit = 'account.invoice.line'

    _columns = {
               'invoice_state': fields.related(
            'invoice_id', 'state', type='selection', string='order status',
            readonly=True),
            }
