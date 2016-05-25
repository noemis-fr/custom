# -*- coding: utf-8 -*-
# Copyright (C) 2016-Today Noemis (http://www.noemis.fr)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.osv.orm import Model
from openerp.osv import fields


class stock_location(Model):
    _inherit = 'stock.location'
    _columns = {
        'name': fields.char(
            'Location Name', size=64, required=True, translate=False),
    }
