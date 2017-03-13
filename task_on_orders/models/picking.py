# -*- encoding: utf-8 -*-
##############################################################################
#
#    No Sale Warning module for Odoo
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

from openerp.osv import fields
from openerp.osv.orm import Model
from openerp.tools.translate import _
import logging

_TASK_STATE = [('none', 'None'),('pending', 'Pending'), ('done', 'Done'), ('cancelled', 'Cancelled')]


_logger = logging.getLogger(__name__)


class Picking(Model):
    _inherit = 'stock.picking'
    
    
    _columns = {
    
        'task_state' : fields.related('sale_id', 'task_state', type='char',  relation='sale.order', string='Task State Summary'),
        'operate_task_ids': fields.related('sale_id','operate_task_ids', type='one2many', relation='project.task', string='Listing NSP', readonly=True),
    }

    
Picking()

class PickingOut(Model):
    _inherit = 'stock.picking.out'

    _columns = {               
        'operate_task_ids': fields.related('sale_id','operate_task_ids2', 
                    type='one2many', 
                    relation='project.task', 
                    string='Associated Tasks', readonly=True),
        'task_state' : fields.related('sale_id', 'task_state', type='char',  relation='sale.order', string='Task State Summary'),

    }

PickingOut()