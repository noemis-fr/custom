# -*- coding: utf-8 -*-
##############################################################################
#
#
##############################################################################

from openerp.osv import orm, fields
import logging

logger = logging.getLogger(__name__)


class account_invoice(orm.Model):
    _inherit = 'account.invoice'

    _columns = {
        'payment_type': fields.selection([('CHQ','check'), ('VIR','transfert'),('TRT','effect')],'payment type'),
        'payment_line_ids': fields.one2many('payment.line', 'account_invoice_id', readonly=True, copy=False),
        'historic_invoice': fields.boolean( string ='Old invoice sent to natixis'),
    }
    
    _defaults = {
        'payment_line_ids' : []
        }
    def copy(self, cr, uid, id, default=None, context=None):
        default = default or {}
        default.update({
            'payment_line_ids': []
        })
        
        return super(account_invoice, self).copy(cr, uid, id, default, context)
    
