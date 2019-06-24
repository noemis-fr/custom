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

from openerp.osv import fields, osv
from openerp.osv.orm import Model
from openerp.tools.translate import _


class sale_order_line(Model):
    _inherit = 'sale.order.line'

    _LAYOUT_TYPE_SELECTION = [
        ('article', 'P'),
        ('title', 'T'),
        ('text', 'R'),
        ('subtotal', 'ST'),
        ('break', 'PB'),
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
                'product_uom_qty': 0,
                'tax_id': False,
                'price_unit': 0,
                'discount': 0,
            }
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
        res = {'value': self.layout_type_2_vals(layout_type)}
        if layout_type == 'subtotal':
            res['value']['name'] = _('SUB TOTAL')
        elif layout_type == 'text':
            res['value']['name'] = _('REMARK')
        elif layout_type == 'title':
            res['value']['name'] = _('TITLE')
        elif layout_type == 'break':
            res['value']['name'] = _('PAGE BREAK')
        return res
    
class sale_order(Model):
    _inherit = 'sale.order'
    
    def action_button_confirm(self, cr, uid, ids, context=None):
        # fetch the partner's id and subscribe the partner to the sale order
        assert len(ids) == 1
        order = self.browse(cr, uid, ids[0], context=context)
        
        for line in order.order_line:
            if not line.product_id and line.layout_type=="article" :
                raise osv.except_osv(_('Error'), _('You can not have one product and type different of "P" on the same line.'))
        return super(sale_order, self).action_button_confirm(cr, uid, ids, context=context)
