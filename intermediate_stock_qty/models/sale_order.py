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


import logging
_logger = logging.getLogger(__name__)



class sale_order_line(Model):
    _inherit = 'sale.order.line'
    
    def _get_qty_display(self, cr, uid, ids, field_name, arg, context):
        _logger.debug("_get_qty_display ")
        line_obj = self.pool.get('sale.order.line')
        res = {}
        for line in line_obj.browse(cr, uid, ids):
            if line.product_id:
                # res[line.id] = str(line.product_id.qty_available) + ' / ' + str(line.product_id.qty_available + line.product_id.outgoing_qty)
                context.update({ 'states': ('confirmed','waiting','assigned','done'), 'what': ('in', 'out') })
                context.update({'shop': line.order_id.shop_id.id})
                stock_virtual = self.pool.get('product.product').get_product_available(cr, uid, [line.product_id.id], context=context)
                context.update({ 'states': ('done',), 'what': ('in', 'out') })
                stock_available = self.pool.get('product.product').get_product_available(cr, uid, [line.product_id.id], context=context)
                res[line.id] = str(stock_available[line.product_id.id]) + ' / ' + str(stock_virtual[line.product_id.id]) +  ' / ' + str(line.product_id.intermediate_stock)
            else:
                res[line.id] = ''
        return res
    
   
    _columns = {
        'qty_display': fields.function(_get_qty_display, type='char', string='Qty/Available', context="{'shop_id': order_id.shop_id}"),
    }
