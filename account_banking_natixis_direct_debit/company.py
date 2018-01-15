# -*- coding: utf-8 -*-
##############################################################################
#
#    SEPA Direct Debit module for OpenERP
#    Copyright (C) 2013 Akretion (http://www.akretion.com)
#    @author: Alexis de Lattre <alexis.delattre@akretion.com>
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
import logging

logger = logging.getLogger(__name__)


class res_company(orm.Model):
    _inherit = 'res.company'

    _columns = {
        'natixis_customer_number': fields.char(
            'natixis customer number', size=6,
            help="Enter the natixis customer number that has been attributed "),
    }

    def _check_natixis_creditor_identifier(self, cr, uid, ids):
        for company in self.browse(cr, uid, ids):
            if company.natixis_customer_number and len(company.natixis_customer_number)!=6:
                    return False
        return True

    _constraints = [
        (_check_natixis_creditor_identifier,
            "Invalid Natixis Creditor Identifier.",
            ['natixis_customer_number']),
    ]
