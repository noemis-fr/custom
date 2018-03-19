# -*- coding: utf-8 -*-
##############################################################################

##############################################################################

from openerp.osv import orm, fields
from openerp.tools.translate import _
from openerp.addons.decimal_precision import decimal_precision as dp
from datetime import datetime
from dateutil.relativedelta import relativedelta
import logging

try:
    from unidecode import unidecode
except ImportError:
    unidecode = None

NUMBER_OF_UNUSED_MONTHS_BEFORE_EXPIRY = 36

logger = logging.getLogger(__name__)


class banking_export_natixis(orm.Model):
    '''natixis Direct Debit export'''
    _name = 'banking.export.natixis'
    _description = 'Natixis Direct Debit export'
    _rec_name = 'filename'

    def _generate_filename(self, cr, uid, ids, name, arg, context=None):
        res = {}
        for sepa_file in self.browse(cr, uid, ids, context=context):
            if not sepa_file.payment_order_ids:
                label = 'no payment order'
            else:
                ref = sepa_file.payment_order_ids[0].reference
                if ref:
                    label = unidecode(ref.replace('/', '-'))
                else:
                    label = 'error'
            res[sepa_file.id] = 'natixis_%s.txt' % label
        return res

    _columns = {
        'payment_order_ids': fields.many2many(
            'payment.order',
            'account_payment_order_natixis_rel',
            'banking_export_natixis_id', 'account_order_id',
            'Payment Orders',
            readonly=True),
        'nb_transactions': fields.integer(
            'Number of Transactions', readonly=True),
        'total_amount': fields.float(
            'Total Amount', digits_compute=dp.get_precision('Account'),
            readonly=True),
        'create_date': fields.datetime('Generation Date', readonly=True),
        'file': fields.binary('Natixis File', readonly=True),
        'filename': fields.function(
            _generate_filename, type='char', size=256,
            string='Filename', readonly=True, store=True),
        'state': fields.selection([
            ('draft', 'Draft'),
            ('sent', 'Sent'),
        ], 'State', readonly=True),
    }

    _defaults = {
        'state': 'draft',
    }