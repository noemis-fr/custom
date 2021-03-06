# -*- encoding: utf-8 -*-
##############################################################################
#
#    Stored Stock Quantity module for Odoo
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

from openerp.osv import fields
from openerp.osv.orm import Model


class product_product(Model):
    _inherit = 'product.product'

    # Compute Section
    def _compute_last_date(
            self, cr, uid, ids, field_names=None, arg=False, context=None):
        res = {
            id: {'last_incoming_date': False, 'last_outgoing_date': False}
            for id in ids}
        move_obj = self.pool['stock.move']
        for id in ids:
            in_move_id = move_obj.search(cr, uid, [
                ('product_id', '=', id),
                ('type', '=', 'in'),
                ('state', '=', 'done')], order='date desc', limit=1,
                context=context)
            out_move_id = move_obj.search(cr, uid, [
                ('product_id', '=', id),
                ('type', '=', 'out'),
                ('state', '=', 'done')], order='date desc', limit=1,
                context=context)
            if in_move_id:
                res[id]['last_incoming_date'] = move_obj.browse(
                    cr, uid, in_move_id[0], context=context).date
            if out_move_id:
                res[id]['last_outgoing_date'] = move_obj.browse(
                    cr, uid, out_move_id[0], context=context).date

        return res

    def _compute_stored_qty(
            self, cr, uid, ids, field_names=None, arg=False, context=None):
        res = {}
        for product in self.browse(cr, uid, ids, context=context):
            qt = float(product.qty_available) + float(product.outgoing_qty)
            print("QT %s" % qt)
            res[product.id] = {
                'stored_qty_available': product.qty_available,
                'stored_virtual_available': product.virtual_available,
                'stored_intermediate_stock':  qt if qt > 0.0 else 0.0
            }
        return res

    def _compute_total_standard_price(
            self, cr, uid, ids, field_names=None, arg=False, context=None):
        res = {}
        for product in self.browse(cr, uid, ids, context=context):
            res[product.id] = {
                'total_standard_price':
                product.standard_price * product.stored_qty_available,
                'total_standard_price_virtual':
                product.standard_price * product.stored_virtual_available,
            }
        return res

    # Recompute Section
    def _recompute_product_from_stock_move_change(
            self, cr, uid, ids, context=None):
        """stock Move context"""
        res = [x['product_id'][0] for x in self.read(
            cr, uid, ids, ['product_id'], context=context)]
        return res

    # Column Section
    _columns = {
        'last_incoming_date': fields.function(
            _compute_last_date, string='Last Global Incoming Date',
            type='datetime', multi='compute_last_date', store={
                'stock.move': (_recompute_product_from_stock_move_change, [
                    'product_id', 'type', 'state', 'date'], 10),
            }),
        'last_outgoing_date': fields.function(
            _compute_last_date, string='Last Global Outgoing Date',
            type='datetime', multi='compute_last_date', store={
                'stock.move': (_recompute_product_from_stock_move_change, [
                    'product_id', 'type', 'state', 'date'], 10),
            }),
        'stored_qty_available': fields.function(
            _compute_stored_qty, type='float',
            string='Total Quantity On Hand (Stored Field)',
            multi='compute_stored_qty', store={
                'stock.move': (_recompute_product_from_stock_move_change, [
                    'product_id', 'product_qty', 'type', 'state'], 10),
            }),
        'stored_virtual_available': fields.function(
            _compute_stored_qty, type='float',
            string='Total Forecasted Quantity (Stored Field)',
            multi='compute_stored_qty', store={
                'stock.move': (_recompute_product_from_stock_move_change, [
                    'product_id', 'product_qty', 'type', 'state'], 10),
            }),
        'stored_intermediate_stock': fields.function(_compute_stored_qty, 
            type='float', string='Intermediate Quantity',
            multi='compute_stored_qty', store={
                'stock.move': (_recompute_product_from_stock_move_change, [
                    'product_id', 'product_qty', 'type', 'state'], 10),
            }),
        'total_standard_price': fields.function(
            _compute_total_standard_price, type='float',
            multi='total_standard_price',
            string='Total Value'),
        'total_standard_price_virtual': fields.function(
            _compute_total_standard_price, type='float',
            multi='total_standard_price',
            string='Total Forcasted Value'),
    }
