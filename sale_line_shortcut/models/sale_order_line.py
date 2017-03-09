# -*- encoding: utf-8 -*-
##############################################################################
#    See __openerp__.py file for copyright and licences
##############################################################################

from openerp.osv.orm import Model
import logging

_logger = logging.getLogger(__name__)

class sale_order_line(Model):
    _inherit = 'sale.order.line'

    def get_moves_from_line(self, cr, uid, ids, context=None):
        
        line = self.browse(cr, uid, ids)[0]
        
        _logger.debug("LINE %s" % line)
        
        res = self.pool.get('ir.actions.act_window').for_xml_id(cr, uid, 'stock', 'act_product_stock_move_futur_open', context)
        res['context'] = {
            'active_id': line.product_id.id,
            'search_default_product_id': [line.product_id.id], 
            'default_product_id': line.product_id.id, 
            'search_default_future': 1
            
        }
        return res
