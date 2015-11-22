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

from openerp.osv.orm import Model


class PurchaseOrderLine(Model):
    _inherit = 'purchase.order.line'

    def write(self, cr, uid, ids, vals, context=None):
        move_obj = self.pool['stock.move']
        res = super(PurchaseOrderLine, self).write(
            cr, uid, ids, vals, context=context)

        if 'date_planned' in vals:
            for purchase_order_line in self.browse(
                    cr, uid, ids, context=context):
                # Get 'in' Moves linked to the current Purchase Order Line
                move_in_ids = move_obj.search(
                    cr, uid,
                    [('purchase_line_id', '=', purchase_order_line.id)],
                    context=context)
                if move_in_ids:
                    # Change Date of the 'In' moves
                    move_obj.write(
                        cr, uid, move_in_ids,
                        {'date_expected': vals['date_planned']},
                        context=context)

                # Get Sale Orders that have generated this Purchase Order
                # (We use 'origin' field, because user merge a lot of
                # purchase order and order line. So, procurement information
                # could be lost.
                sale_order_names = purchase_order_line.order_id.origin
                for item in sale_order_names.split(" "):
                    if str(item).startswith('SO'):
                        # Get 'Out' Moves
                        move_out_ids = move_obj.search(
                            cr, uid, [('origin', '=', item)], context=context)
                        for move_out in move_obj.browse(
                                cr, uid, move_out_ids, context=context):
                            if move_out.product_id.id ==\
                                    purchase_order_line.product_id.id and\
                                    move_out.state not in ['done', 'cancel']:
                                move_obj.write(
                                    cr, uid, [move_out.id],
                                    {'date_expected': vals['date_planned']},
                                    context=context)
        return res