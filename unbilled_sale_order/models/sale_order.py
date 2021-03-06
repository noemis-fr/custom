# -*- encoding: utf-8 -*-
##############################################################################
#
#    Unbilled Sale Order module for Odoo
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
from openerp.osv import fields

import openerp.addons.decimal_precision as dp


class sale_order(Model):
    _inherit = 'sale.order'

    # Compute Section
    def _compute_amount_untaxed_unbilled(
            self, cr, uid, ids, field_names=None, arg=False, context=None):
        res = {}
        for order in self.browse(cr, uid, ids, context=context):
            res[order.id] = 0
            for line in order.order_line:
                res[order.id] += line.amount_untaxed_unbilled
        return res

    # Recompute Section
    def _get_order_from_order_line(
            self, cr, uid, ids, context=None):
        order_ids = [x.order_id.id for x in self.browse(
            cr, uid, ids, context=context)]
        return list(set(order_ids))

    _columns = {
        'amount_untaxed_unbilled': fields.function(
            _compute_amount_untaxed_unbilled,
            string='Untaxed and Unbilled Amount',
            digits_compute=dp.get_precision('Account')),
    }
