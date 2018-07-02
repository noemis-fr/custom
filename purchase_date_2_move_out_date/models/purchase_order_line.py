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

from datetime import datetime, timedelta

from openerp.osv.orm import Model
from openerp.osv import fields
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrderLine(Model):
    _inherit = 'purchase.order.line'

    _DELIVERY_DELAY_DAYS = 0

    _defaults = {
#        'date_planned': '2000-01-01',
    }

    def write(self, cr, uid, ids, vals, context=None):
        move_obj = self.pool['stock.move']
        res = super(PurchaseOrderLine, self).write(
            cr, uid, ids, vals, context=context) 
        if context is None:
            context = {}
            
        manually_changed = context.get('manually_changed', False)
        _logger.debug("MANUALLY CHANGED ? : %s" % manually_changed)
        if 'date_planned' in vals :
            delivery_date = (
                datetime.strptime(vals['date_planned'], "%Y-%m-%d") +
                timedelta(days=self._DELIVERY_DELAY_DAYS)
                ).strftime('%Y-%m-%d')
            for purchase_order_line in self.browse(
                    cr, uid, ids, context=context):
                
                if purchase_order_line.product_id.produce_delay:
                    delivery_date = (
                        datetime.strptime(vals['date_planned'], "%Y-%m-%d") +
                        timedelta(days=self.product_id.produce_delay)
                        ).strftime('%Y-%m-%d')
                # Get 'in' Moves linked to the current Purchase Order Line
                move_in_ids = move_obj.search(
                    cr, uid,
                    [('purchase_line_id', '=', purchase_order_line.id)],
                    context=context)
                update_vals = {'date_expected': vals['date_planned']}
#                if not manually_changed:
#                    #Prevent initial date to be changed by non human action
#                    update_vals.update({'min_date_asked_for': vals['date_planned']})
                if move_in_ids:
                    # Change Date of the 'In' moves
                    move_obj.write(
                        cr, uid, move_in_ids,
                        update_vals,
                        context=context)

                # Get Sale Orders that have generated this Purchase Order
                # (We use 'origin' field, because user merge a lot of
                # purchase order and order line. So, procurement information
                # could be lost.
                origin = purchase_order_line.order_id.origin
                sale_order_names = origin and origin.split(" ") or []
                for item in sale_order_names:
                    if item and item.startswith('SO'):
                        # Get 'Out' Moves
                        move_out_ids = move_obj.search(
                            cr, uid, [('origin', '=', item)], context=context)
                        for move_out in move_obj.browse(
                                cr, uid, move_out_ids, context=context):
                            if move_out.product_id.id ==\
                                    purchase_order_line.product_id.id and\
                                    move_out.state not in ['done', 'cancel']:
                                update_vals = {'date_expected': delivery_date}
#                                if not manually_changed:
#                                    #Prevent initial date to be changed by non human action
#                                    update_vals.update({'min_date_asked_for': delivery_date})
                                move_obj.write(
                                    cr, uid, [move_out.id],
                                    update_vals,
                                    context=context)
        return res


    def create(self, cr, uid, vals, context=None):
        _logger.debug("CREATE purchase order line %s" % vals)
        if 'date_planned' in vals :
            vals.update({'min_date_asked_for': vals['date_planned']})
        return super(PurchaseOrderLine, self).create(
            cr, uid, vals, context=context)
    
    def _get_initial_date(self, cr, uid, ids, name, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids):
            is_initial_date = line.date_planned == line.min_date_asked_for 
            res[line.id] = is_initial_date
        return res

    def _get_initial_date_text(self, cr, uid, ids, name, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids):
            is_initial_date = line.date_planned == line.min_date_asked_for 
            res[line.id] = "Planned"
            if is_initial_date : 
                res[line.id] = "Theorique"
        _logger.debug("DATE %s" % res)
        return res
            
    _columns = {
        'is_initial_date': fields.function(_get_initial_date, type='boolean', string="Initial Date"),
        'is_initial_date_text': fields.function(_get_initial_date_text, type='char', string="Initial Date",),
        'min_date_asked_for': fields.date('Date of initial demand',),
    }
    
    _defaults = {
        'is_initial_date_text': 'Theorique'
    
    }