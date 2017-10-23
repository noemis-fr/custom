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

_logger = logging.getLogger(__name__)
   
class ResPartner(Model):
    _inherit = 'res.partner'
    

    _columns={
        'commercial_parent_id': fields.related('commercial_partner_id', 'id', string='id of society', type='integer', store=True)
    }

    def name_get(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        if isinstance(ids, (int, long)):
            ids = [ids]
        res = []
        for record in self.browse(cr, uid, ids, context=context):
            name = record.name
            if record.parent_id and not record.is_company:
                name = "%s, %s" % (record.parent_name, name)
            if context.get('show_address'):
                name = name + "\n" + self._display_address(cr, uid, record, without_company=True, context=context)
                name = name.replace('\n\n','\n')
                name = name.replace('\n\n','\n')
            if context.get('show_email') and record.email:
                name = "%s <%s>" % (name, record.email)
            name = "[%s] %s" % (record.commercial_parent_id, name)
            res.append((record.id, name))
        return res


        # ^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^ # template mask field list
    def name_search(self, cr, user, name='', args=None, operator='ilike', context=None, limit=100):
        
        return name_tools.extended_name_search(self, cr, user, name, args,operator, context=context, limit=limit, keys=['name','commercial_parent_id'])

        # ^^^^^^^^^^^^^^^^^^^^ # field list to search


    
    