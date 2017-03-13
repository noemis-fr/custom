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


class Picking(Model):
    _inherit = 'stock.picking'
    
    
    def action_confirm(self, cr, uid, ids, context=None):
        res = super(Picking, self).action_confirm(cr, uid, ids, context=context)
        _logger.debug("CONFIRM SALE ORDER %s" % ids)
        for pick_id in self.browse(cr, uid, ids):
            self.write(cr, uid, pick_id.id, 
                            {'min_date_asked_for' : pick_id.min_date})
            
            
        return res
        
    def _get_initial_date(self, cr, uid, ids, name, arg, context=None):
        res = {}
        for pick in self.browse(cr, uid, ids):
            is_initial_date = all(line.date_expected == pick.min_date_asked_for for line in pick.move_lines)
            res[pick.id] = is_initial_date
        return res
    
    _columns = {
        'is_initial_date': fields.function(_get_initial_date, type='boolean', string="Initial Date"),
        'min_date_asked_for': fields.datetime('Date of initial demand',),
    }

    
Picking()

class PickingOut(Model):
    _inherit = 'stock.picking.out'

    def _get_initial_date(self, cr, uid, ids, name, arg, context=None):
        res = {}
        for pick in self.browse(cr, uid, ids):
            is_initial_date = all(line.date_expected == pick.min_date_asked_for for line in pick.move_lines)
            res[pick.id] = is_initial_date
        return res
            
    _columns = {
        'is_initial_date': fields.function(_get_initial_date, type='boolean', string="Initial Date"),
        'min_date_asked_for': fields.datetime('Date of initial demand',),
    }


PickingOut()

class StockMove(Model):
    _inherit = 'stock.move'

    def _get_initial_date(self, cr, uid, ids, name, arg, context=None):
        res = {}
        for mv in self.browse(cr, uid, ids):
            is_initial_date = mv.date_expected == mv.picking_id.min_date_asked_for 
            res[mv.id] = is_initial_date
        return res

    def _get_initial_date_text(self, cr, uid, ids, name, arg, context=None):
        res = {}
        for mv in self.browse(cr, uid, ids):
            is_initial_date = mv.date_expected == mv.picking_id.min_date_asked_for 
            res[mv.id] = "Planned"
            if is_initial_date : 
                res[mv.id] = "Theorique"
            
        return res
            
    _columns = {
        'is_initial_date': fields.function(_get_initial_date, type='boolean', string="Initial Date"),
        'is_initial_date_text': fields.function(_get_initial_date_text, type='Char', string="Initial Date")
    }


StockMove()