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
from openerp.osv.orm import Model
from base_util_refcodes import name_tools

_logger = logging.getLogger(__name__)
   
class ResPartner(Model):
    _inherit = 'res.partner'
    

    def name_get(self, cr, uid, ids, context=None):

        return name_tools.extended_name_get(self, cr, uid, ids,'[#%(id)s] %(name)s', ['id', 'name'], context=context)

        # ^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^ # template mask field list
    def name_search(self, cr, user, name='', args=None, operator='ilike', context=None, limit=100):
        
        return name_tools.extended_name_search(self, cr, user, name, args,operator, context=context, limit=limit, keys=['name','id'])

        # ^^^^^^^^^^^^^^^^^^^^ # field list to search


    
    