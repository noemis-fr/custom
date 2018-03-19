# -*- coding: utf-8 -*-
##############################################################################
#
#
##############################################################################

from openerp.osv import orm, fields
import logging

logger = logging.getLogger(__name__)


class account_invoice(orm.Model):
    _inherit = 'account.invoice'

    _columns = {
        'payment_type': fields.selection([('CHQ','check'), ('VIR','transfert'),('TRT','effect')],'payment type')
    }
