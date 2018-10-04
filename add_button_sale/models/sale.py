# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015-Today Mind And Go (<https://mind-and-go.com>)
#    Copyright (C) 2004 OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################
import logging
from openerp.osv import fields
from openerp.osv.orm import Model
from openerp.addons.base_util_refcodes import name_tools
from datetime import datetime

_logger = logging.getLogger(__name__)
   
class ResPartner(Model):
    _inherit = 'sale.order'


    _columns = {
            'validation_request_date' : fields.date('validation Request Date'),
            'validation_request_date_box' : fields.boolean('validation Request Date box'),
            'express' :fields.boolean('Express'),
            'account_box':fields.boolean('blocked in account'),
            }

    
    def validate_validation_request_date(self, cr, uid, ids, context=None):
        today = datetime.today()
        return self.write(cr, uid, ids, {'validation_request_date_box': True,
                                         'validation_request_date':today})
        
    def validate_express(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'express': True})
        
    def validate_blocked_in_account(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'account_box': True})
    