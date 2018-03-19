# -*- coding: utf-8 -*-
##############################################################################

#
##############################################################################

from openerp.osv import orm
from mock.mock import right
from openerp.osv import expression


class payment_order_create(orm.TransientModel):
    _inherit = 'payment.order.create'

    def extend_payment_order_domain(
            self, cr, uid, payment_order, domain, context=None):
        super(payment_order_create, self).extend_payment_order_domain(
            cr, uid, payment_order, domain, context=context)
        related_domain=[]
        if payment_order.payment_order_type == 'debit':
            for element in domain:
                if expression.is_leaf(element):
                    left, operator, right = element
                    if left == 'invoice.state' and right == 'debit_denied':
                        operator = '='
                        right = 'open'
                        related_domain.append(element)
                        element = left, operator, right
                        domain.append(element)
                    if left =='amount_to_receive':
                        related_domain.append(element)
            for element in related_domain:
                domain.remove(element)
        return True
