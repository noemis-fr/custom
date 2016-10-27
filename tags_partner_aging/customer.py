# -*- coding: utf-8 -*-

######################################################################
#
#  Note: Program metadata is available in /__init__.py
#
######################################################################

from openerp.osv import fields, osv
import tools

class account_aging_customer(osv.osv):
    _inherit = 'partner.aging.customer'
    

    
    _columns = {
        'category_id': fields.related('partner_id', 'category_id',
                type='many2many', relation='res.partner.category', 
                string=u'Category', readonly=True)
    }
        