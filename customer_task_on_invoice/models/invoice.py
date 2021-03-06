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


class Invoice(Model):
    _inherit = 'account.invoice'

    

    _columns = {
        'memo_task_ids': fields.related('partner_id','memo_task_ids', type='one2many', relation='project.task', string='Tasks', readonly=True),
        'task_ids': fields.related('partner_id','memo_task_ids', type='one2many', relation='project.task', string='Tasks', readonly=True),
        'partner_comment': fields.related('partner_id','comment', type='text', string='Memo', readonly=True)
    }

    