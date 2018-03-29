# -*- coding: utf-8 -*-
##############################################################################

##############################################################################

import logging
import time

from openerp.osv import fields, osv, orm
from openerp import netsvc
from openerp.tools.translate import _


_logger = logging.getLogger(__name__)

class payment_order_create(orm.TransientModel):
    _inherit = 'payment.order.create'

    def search_entries(self, cr, uid, ids, context=None):
        """
        This method taken from account_payment module.
        We adapt the domain based on the payment_order_type
        """
        
        payment = self.pool.get('payment.order').browse(
            cr, uid, context['active_id'], context=context)
         
        if not (payment.mode.type.ir_model_id.model=='banking.export.natixis.wizard') :
            return super(payment_order_create, self).search_entries(cr, uid, ids, context)
        
        line_obj = self.pool.get('account.move.line')
        mod_obj = self.pool.get('ir.model.data')
        if context is None:
            context = {}

        # start account_banking_payment
#         payment = self.pool.get('payment.order').browse(
#             cr, uid, context['active_id'], context=context)
        # Search for move line to pay:
        domain = [
            ('move_id.state', '=', 'posted'),
            ('reconcile_id', '=', False),
            ('company_id', '=', payment.mode.company_id.id),
            ('invoice.payment_mode_id','=',payment.mode.id)
        ]
        self.extend_payment_order_domain(
            cr, uid, payment, domain, context=context)
        # end account_direct_debit
        line_ids = line_obj.search(cr, uid, domain, context=context)
        context.update({'line_ids': line_ids})
        model_data_ids = mod_obj.search(
            cr, uid, [
                ('model', '=', 'ir.ui.view'),
                ('name', '=', 'view_create_payment_order_lines')],
            context=context)
        resource_id = mod_obj.read(
            cr, uid, model_data_ids, fields=['res_id'],
            context=context)[0]['res_id']
        return {
            'name': _('Entry Lines'),
            'context': context,
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'payment.order.create',
            'views': [(resource_id, 'form')],
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
