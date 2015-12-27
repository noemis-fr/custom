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

from datetime import datetime
from openerp.osv import fields
from openerp.osv.orm import Model


class ProcurementOrder(Model):
    _inherit = 'procurement.order'


    def _get_purchase_schedule_date(
            self, cr, uid, procurement, company, context=None):
        return datetime.strptime('2000-01-01', "%Y-%m-%d")


    def _get_purchase_order_date(
            self, cr, uid, procurement, company, schedule_date, context=None):
        return datetime.strptime(
            fields.date.context_today(self, cr, uid, context=context),
            "%Y-%m-%d")
