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


class Partner(Model):
    _inherit = 'res.partner'

    

    _columns = {
#        'memo_task_ids': fields.related('partner_id','task_ids', type='one2many', relation='project.task', string='Tasks', readonly=True,
#                                    
#                                    )
        'memo_task_ids': fields.one2many('project.task', 'partner_id', 'Tasks', domain=[('sale_line_id', '=', False)]),
        'operate_task_ids': fields.one2many('project.task', 'partner_id', 'Tasks', domain=[('sale_line_id', '!=', False)]),
    }

    

    