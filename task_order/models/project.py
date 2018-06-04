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

    _columns = {
        'sale_order_id': fields.related(
            'sale_line_id', 'order_id', type='many2one',relation='sale.order', string='order',
            readonly=True,store=True),
    }
    
    