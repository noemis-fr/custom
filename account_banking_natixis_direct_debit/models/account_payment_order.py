# -*- coding: utf-8 -*-
##############################################################################

##############################################################################

import logging
import time

from openerp.osv import fields, osv
from openerp import netsvc

_logger = logging.getLogger(__name__)

class payment_order(osv.osv):
    _inherit = 'payment.order'

    def search_entries_invoice(self, cr, uid, ids, context=None):
        
        context.update({'active_id' : ids[0]})
        wizard = self.pool.get('payment.order.create').create(cr, uid, {}, context=context)
        wizard_id = self.pool.get('payment.order.create').browse(cr,uid,wizard)
        return wizard_id.search_entries(context)
    
    def _total(self, cursor, user, ids, name, args, context=None):
        res = {}
        for order in self.browse(cursor, user, ids, context=context):
            if order.line_ids:
                res[order.id] = reduce(lambda x, y: x + y.invoice_amount, order.line_ids, 0.0)
            else:
                res[order.id] = 0.0
        return res
    
    _columns = {
        'total_residual': fields.function(_total, string="Total", type='float'),
    }