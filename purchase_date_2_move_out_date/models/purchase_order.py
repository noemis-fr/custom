# -*- encoding: utf-8 -*-
##############################################################################
#
#    Purchase Date to Move Out Date module for Odoo
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


class PurchaseOrder(Model):
    _inherit = 'purchase.order'

    # Remove readonly depending of state.
    # TODO V8. refactor with new API
    _columns = {
        'order_line': fields.one2many(
            'purchase.order.line', 'order_id', 'Order Lines'),
    }

    _defaults = {
#        'minimum_planned_date': '2000-01-01',
    }

    def write(self, cr, uid, ids, vals, context=None):
        line_obj = self.pool['purchase.order.line']
        res = super(PurchaseOrder, self).write(
            cr, uid, ids, vals, context=context)
        if vals.get('minimum_planned_date', False):
            for order in self.browse(cr, uid, ids, context=context):
                # We force to rewrite date_planned on each line to change date
                # on stock moves
                line_ids = [x.id for x in order.order_line]
                line_obj.write(cr, uid, line_ids, {
                    'date_planned': vals['minimum_planned_date']},
                    context=context)
        return res
