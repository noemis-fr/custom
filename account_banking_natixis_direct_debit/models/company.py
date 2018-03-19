# -*- coding: utf-8 -*-
##############################################################################
#
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
