# -*- coding: utf-8 -*-
# Copyright (C) Copyright (C) 2015-Today Noemis (http://www.noemis.fr)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.osv.orm import Model
from openerp.osv import fields

from openerp.addons import decimal_precision as dp


class StockPicking(Model):
    _inherit = 'stock.picking'

    def _get_purchase_amount_total_vat_excl(
            self, cr, uid, ids, fields, args, context=None):
        res = {x: 0 for x in ids}
        for picking in self.browse(cr, uid, ids, context=context):
            for move in picking.move_lines:
                res[picking.id] += move.purchase_amount_total_vat_excl
        return res

    def _get_purchase_amount_from_move(self, cr, uid, ids, context=None):
        res = set()
        for move in self.browse(cr, uid, ids, context=context):
            res.add(move.picking_id.id)
        return list(res)

    _columns = {
        'purchase_amount_total_vat_excl':  fields.function(
            _get_purchase_amount_total_vat_excl, type='float',
            digits_compute=dp.get_precision('Account'), store={
                'stock.picking': (lambda self, cr, uid, ids, context: ids, [
                    'move_lines', 'state'], 10),
                'stock.move': (_get_purchase_amount_from_move, [
                    'purchase_amount_total_vat_excl',
                    'unit_purchase_price_vat_excl',
                    'product_qty', 'product_id'], 20),
            },
            string='Purchase Subtotal VAT Excl'),
    }


class StockPickingIn(Model):
    _inherit = 'stock.picking.in'

    # Due to this bug https://bugs.launchpad.net/openobject-addons/+bug/1169998
    # you need do declare new fields in both picking models
    def __init__(self, pool, cr):
        super(StockPickingIn, self).__init__(pool, cr)
        for field in ['purchase_amount_total_vat_excl']:
            self._columns[field] = \
                self.pool['stock.picking']._columns[field]
