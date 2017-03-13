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
_logger = logging.getLogger(__name__)

_TASK_STATE = [('none', 'None'),('pending', 'Pending'), ('done', 'Done'), ('cancelled', 'Cancelled')]

class SaleOrderLine(Model):
    _inherit = 'sale.order.line'

    
    def _get_tasks(
            self, cr, uid, ids, fields, args, context=None):
        res = {}
        task_model = self.pool.get("project.task")
        for sol in self.browse(cr, uid, ids, context=context):

            task_ids = task_model.search(cr, uid, [
                        ('sale_line_id', '=', sol.id)
                        ], context=context)
            res[sol.id] = [t.id for t in task_model.browse(cr, uid, task_ids)]
        return res
        
        
    _columns = {        
        'operate_task_ids': fields.function(
            _get_tasks, type='one2many', relation="project.task"
            , string='Listing NSP')
        
    }
SaleOrderLine()

class SaleOrder(Model):
    _inherit = 'sale.order'
    
    
    def _get_tasks(
            self, cr, uid, ids, fields, args, context=None):
        res = {}
        task_model = self.pool.get("project.task")
        for so in self.browse(cr, uid, ids, context=context):
            tasks = []
            for sol in so.order_line:
                task_ids = task_model.search(cr, uid, [
                            ('sale_line_id', '=', sol.id)
                            ], context=context)

                tasks += [t.id for t in task_model.browse(cr, uid, task_ids)]
            res[so.id] = tasks 
        return res
    
    def _get_task_state(self, cr, uid, ids, name, arg, context=None):
        res = {}
        task_model = self.pool.get("project.task")
        
        for so in self.browse(cr, uid, ids, context=context):            
            if len(so.operate_task_ids) == 0:
                state = 'none'
            else:

                if all(t.state in ('cancelled') for t in so.operate_task_ids):
                    state= 'cancelled'
                if all(t.state in ('done', 'cancelled') for t in so.operate_task_ids):
                    state= 'done'
                else:
                    state='pending'
                            
            res[so.id] = state
        return res
    
    
    _columns = {
        'operate_task_ids': fields.function(
            _get_tasks, type='one2many', relation="project.task"
            , string='Listing NSP', readonly=True),
        'task_state' : fields.function(_get_task_state, type='char',  string='Task State Summary')
    }

    
SaleOrder()