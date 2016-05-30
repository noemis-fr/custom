# -*- coding: utf-8 -*-
# Copyright (C) 2015-Today Noemis (http://www.noemis.fr)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp.osv.orm import Model


class product_product(Model):
    _inherit = 'product.product'

    def write(self, cr, uid, ids, vals, context=None):
        line_obj = self.pool['account.invoice.line']
        if 'tag_ids' in vals:
            line_ids = line_obj.search(
                cr, uid, [('product_id', 'in', ids)], context=context)
            line_obj.write(
                cr, uid, line_ids, {'tag_ids': vals['tag_ids']},
                context=context)
        return super(product_product, self).write(
            cr, uid, ids, vals, context=context)
