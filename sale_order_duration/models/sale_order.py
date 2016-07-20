# -*- encoding: utf-8 -*-
##############################################################################
#
#    Sale Order Duration module for Odoo
#    Copyright (C) 2016-Today Noemis (http://www.noemis.fr)
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

from datetime import datetime
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT
from openerp.osv import fields
from openerp.osv.orm import Model


class SaleOrder(Model):
    _inherit = 'sale.order'

    # Compute section
    def _compute_duration(
            self, cr, uid, ids, field_names=None, arg=False, context=None):
        res = {}
        current_date = fields.date.context_today(
            self, cr, uid, context=context)
        for order in self.browse(cr, uid, ids, context=context):
            if order.shipped == True and not order.date_end:
                date_begin = datetime.strptime(
                    order.date_begin, DEFAULT_SERVER_DATE_FORMAT)
                date_end = datetime.strptime(
                    current_date, DEFAULT_SERVER_DATE_FORMAT)
                if order.date_begin:
                    res[order.id] = {
                        'date_end': current_date,
                        'duration': (date_end - date_begin).days,
                    }
            if order.state == 'progress' and not order.date_begin:
                    res[order.id] = {
                        'date_begin': current_date,
                        'date_end': False,
                        'duration': 0,
                    }
        return res

    # Column Section
    _columns = {
        'date_begin': fields.function(
            _compute_duration, string='Begin Date', type='date',
            multi='duration', store={
                'sale.order': (lambda self, cr, uid, ids, context: ids, [
                    'state'], 5)},
            help="Date when the Sale Order is validated."),
        'date_end': fields.function(
            _compute_duration, string='End Date', type='date',
            multi='duration', store={
                'sale.order': (lambda self, cr, uid, ids, context: ids, [
                    'shipped'], 5)},
            help="Date when the Sale Order is shipped."),
        'duration': fields.function(
            _compute_duration, string='Duration', type='integer',
            multi='duration', store={
                'sale.order': (lambda self, cr, uid, ids, context: ids, [
                    'state'], 5)},
            help="Duration between the begin and the end dates. (in Days)"),
    }
