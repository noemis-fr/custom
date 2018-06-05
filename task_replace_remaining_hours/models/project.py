# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-today OpenERP SA (<http://www.openerp.com>)
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

from datetime import datetime, date
from lxml import etree
import time

import logging
from openerp.osv import fields
from openerp.osv.orm import Model
from openerp.addons.base_util_refcodes import name_tools


class ProjectTask(Model):
    _inherit = "project.task"

    # Compute: effective_hours, total_hours, progress
    def _noemis_task_values_get(self, cr, uid, ids, field_names, args, context=None):
        res = {}
#         hours = dict(cr.fetchall())
#         tasks_group=self.browse(cr, uid, ids, context=context)
#         for task in tasks_group:
#             res[task]['remain_hours']=(task.planned_hours or 0.0)-(res[task]['effective_hours'] or 0.0)
#             res[task].update({'remain_hours':-3.0})
        for task in self.browse(cr, uid, ids, context=context):
            res[task.id] = {'remain_hours': (task.planned_hours or 0.0)-(task.effective_hours or 0.0)}
            res[task.id]['noemis_task_total']= (task.effective_hours or 0.0) + res[task.id]['remain_hours']
        return res


    _columns = {
        'remain_hours': fields.function(_noemis_task_values_get, string='Remaining Hours',multi='noemis',
                                         help="Total remaining time, can be re-estimated periodically by the assignee of the task."),
        'noemis_task_total': fields.function(_noemis_task_values_get,
                                             multi='noemis', string='Total', help="Computed as: Time Spent + Remaining Time."),
    }
    
    