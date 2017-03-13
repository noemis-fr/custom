# -*- encoding: utf-8 -*-
##############################################################################
#
#    Purchase Date to Move Out Date module for Odoo
#    Copyright (C) 2015-Today Noemis (http://www.noemis.fr)
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

from openerp.osv.orm import Model
from openerp.osv import fields

class SaleOrder(Model):
    _inherit = 'sale.order'
      

    def action_wait(self, cr, uid, ids, context=None):
        res = super(SaleOrder, self).action_wait(cr, uid, ids, context=context)
        for o in self.browse(cr, uid, ids):
            if not o.validate_commercial_user:
                self.write(cr, uid, [o.id], {'validate_commercial_user': uid}, context=context)
        return res

    _columns = {
        'validate_commercial_user': fields.many2one('res.users', string='User that validate the SO'),
#        'is_sale_admin': fields.function( _is_admin, type='boolean', string='Sale Admin?')
    }