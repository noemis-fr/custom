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
    def _compute_stored_qty(
            self, cr, uid, ids, field_names=None, arg=False, context=None):
        res = {}
        for product in self.browse(cr, uid, ids, context=context):
            res[product.id] = {
                'stored_qty_available': product.qty_available,
                'stored_virtual_available': product.virtual_available,
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
        'stored_qty_available': fields.function(
            _compute_stored_qty, string='Quantity On Hand (Stored Field)',
            type='float', multi='compute_stored_qty', store={
                'stock.move': (_recompute_product_from_stock_move_change, [
                    'product_id', 'product_qty', 'type', 'state'], 10),
            }),
        'stored_virtual_available': fields.function(
            _compute_stored_qty, string='Forecasted Quantity (Stored Field)',
            type='float', multi='compute_stored_qty', store={
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
