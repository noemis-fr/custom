# -*- coding: utf-8 -*-
##############################################################################
#
#    Mandate module for openERP
#    Copyright (C) 2014 Compassion CH (http://www.compassion.ch)
#    @author: Cyril Sester <csester@compassion.ch>,
#             Alexis de Lattre <alexis.delattre@akretion.com>
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

from openerp.osv import orm, fields
from openerp.tools.translate import _


class payment_line(orm.Model):
    _inherit = 'payment.line'

    _columns = {
        'account_invoice_id': fields.many2one(
            'account.invoice',
            copy=False),
        'invoice_amount': fields.related(
            'move_line_id', 'amount_residual', type='float', string='Total Amount',
            readonly=True,
            copy=False),
        'partner_ref': fields.related(
            'partner_id', 'ref', type='string', string='partner ref',
            readonly=True),
        
    }

    