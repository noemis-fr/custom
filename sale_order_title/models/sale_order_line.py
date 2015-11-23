# -*- encoding: utf-8 -*-
##############################################################################
#
#    No Sale Warning module for Odoo
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
from openerp.tools.translate import _


class sale_order_line(Model):
    _inherit = 'sale.order.line'

    _LAYOUT_TYPE_SELECTION = [
        ('article', 'Product'),
        ('title', 'Title'),
        ('text', 'Note'),
        ('subtotal', 'Sub Total'),
        ('break', 'Page Break'),
    ]

    _columns = {
        'layout_type': fields.selection(
            _LAYOUT_TYPE_SELECTION, 'Layout Type', required=True),
    }

    _defaults = {
        'layout_type': 'article',
    }

    def layout_type_2_vals(self, layout_type):
        vals = {}
        if layout_type and layout_type != 'article':
            vals = {
                'product_id': False,
                'price_unit': 0,
                'product_uom_qty': 0,
            }
            if layout_type == 'subtotal':
                vals['name'] = _('SUB TOTAL')
            elif layout_type == 'break':
                vals['name'] = _('PAGE BREAK')
        return vals

    def create(self, cr, uid, vals, context=None):
        vals.update(self.layout_type_2_vals(vals.get('layout_type', False)))
        return super(sale_order_line, self).create(
            cr, uid, vals, context=context)

    def write(self, cr, uid, ids, vals, context=None):
        vals.update(self.layout_type_2_vals(vals.get('layout_type', False)))
        return super(sale_order_line, self).write(
            cr, uid, ids, vals, context=context)

    def onchange_layout_type(self, cr, uid, ids, layout_type, context=None):
        return {'value': self.layout_type_2_vals(layout_type)}
