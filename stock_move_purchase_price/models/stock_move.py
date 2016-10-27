# -*- coding: utf-8 -*-
# Copyright (C) Copyright (C) 2015-Today Noemis (http://www.noemis.fr)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.osv.orm import Model
from openerp.osv import fields

from openerp.addons import decimal_precision as dp


class stock_move(Model):
    _inherit = 'stock.move'

    def _get_purchase_unit_price_vat_excl(
            self, cr, uid, ids, fields, args, context=None):
        res = {x: 0 for x in ids}
        for move in self.browse(cr, uid, ids, context=context):
                res[move.id] = (move.purchase_line_id\
                    and move.purchase_line_id.price_unit ) or \
                    (not move.purchase_line_id\
                    and move.product_id.purchase_price ) \
                    or 0
        return res

    def _get_purchase_amount_total_vat_excl(
            self, cr, uid, ids, fields, args, context=None):
        res = {}
        for move in self.browse(cr, uid, ids, context=context):
            res[move.id] =\
                move.purchase_unit_price_vat_excl * move.product_qty or 0
        return res

    _columns = {
        'purchase_unit_price_vat_excl': fields.function(
            _get_purchase_unit_price_vat_excl, type='float',
            digits_compute=dp.get_precision('Product Price'), 
#            store=False
            store={
                'stock.move': (lambda self, cr, uid, ids, context: ids, [
                    'purchase_line_id', 'product_id'], 5),
            }
            , string='Unit Purchase Price VAT Excl'),
        'purchase_amount_total_vat_excl':  fields.function(
            _get_purchase_amount_total_vat_excl, type='float',
            digits_compute=dp.get_precision('Account'), 
#            store=False,
            store={
                'stock.move': (lambda self, cr, uid, ids, context: ids, [
                    'unit_purchase_price_vat_excl', 'product_qty',
                    'product_id'], 10),
            },
            string='Purchase Subtotal VAT Excl'),
    }
