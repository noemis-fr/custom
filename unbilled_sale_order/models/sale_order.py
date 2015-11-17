# -*- encoding: utf-8 -*-
##############################################################################
#
#    Unbilled Sale Order module for Odoo
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

from openerp.osv.orm import Model
from openerp.osv import fields

import openerp.addons.decimal_precision as dp


class sale_order(Model):
    _inherit = 'sale.order'

    # Compute Section
    def _compute_amount_untaxed_unbilled(
            self, cr, uid, ids, field_names=None, arg=False, context=None):
        sol_obj = self.pool['sale.order.line']
        res = {}
        for order in self.browse(cr, uid, ids, context=context):
            res[order.id] = 0
            for line in order.order_line:
                if not line.invoiced:
                    res[order.id] += line.price_subtotal
        return res

    # Recompute Section
    def _get_order_from_order_line(
            self, cr, uid, ids, context=None):
        print "_get_order_from_order_line"
        order_ids = [x.order_id.id for x in self.browse(
            cr, uid, ids, context=context)]
        return list(set(order_ids))

    _columns = {
        'amount_untaxed_unbilled': fields.function(
            _compute_amount_untaxed_unbilled,
            string='Untaxed and Unbilled Amount',
            digits_compute=dp.get_precision('Account'),
#            store={
#                'sale.order': (
#                    lambda self, cr, uid, ids, c={}: ids, ['order_line'], 10),
#                'sale.order.line': (_get_order_from_order_line, [
#                    'price_unit', 'tax_id', 'discount', 'invoiced',
#                    'product_uom_qty', 'invoice_lines'], 10),
#            }
            ),
    }

class sale_order_line(Model):
    _inherit = 'sale.order.line'

    # Compute Section
    def _compute_amount_untaxed_unbilled(
            self, cr, uid, ids, field_names=None, arg=False, context=None):
        sol_obj = self.pool['sale.order.line']
        res = {}
        for order_line in self.browse(cr, uid, ids, context=context):
            res[order_line.id] = order_line.price_subtotal
            for invoice_line in order_line.invoice_lines:
                if invoice_line.invoice_id.state not in ['draft', 'cancel']:
                    res[order_line.id] -= invoice_line.price_subtotal
        return res

    _columns = {
        'amount_untaxed_unbilled': fields.function(
            _compute_amount_untaxed_unbilled,
            string='Untaxed and Unbilled Amount',
            digits_compute=dp.get_precision('Account'),
##            store={
##                'sale.order.line': (
##                    lambda self, cr, uid, ids, c={}: ids, ['invoiced', 'invoice_lines'], 10),
###                'sale.order.line': (_get_order_from_order_line, [
###                    'price_unit', 'tax_id', 'discount', 'invoiced',
###                    'product_uom_qty', 'invoice_lines'], 10),
##            }
            
            ),
    }
