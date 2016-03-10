# -*- encoding: utf-8 -*-
from openerp.osv import fields
from openerp.osv.orm import Model


class account_invoice(Model):
    _inherit = 'account.invoice'

    _columns = {
        'partner_ref': fields.related(
            'partner_id', 'ref', type='char', string='Customer Ref.'),
    }
