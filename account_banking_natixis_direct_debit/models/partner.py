# -*- coding: utf-8 -*-
##############################################################################
#
#
##############################################################################

from openerp.osv import orm, fields
import logging

logger = logging.getLogger(__name__)


class res_partner(orm.Model):
    _inherit = 'res.partner'

    _columns = {
        'fiscal_country_id': fields.many2one('res.country', 'Fiscal Country', help="If the fiscal country is different to the address country."),
    }
