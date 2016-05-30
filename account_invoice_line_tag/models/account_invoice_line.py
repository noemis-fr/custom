# -*- coding: utf-8 -*-
# Copyright (C) 2015-Today Noemis (http://www.noemis.fr)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp.osv import fields
from openerp.osv.orm import Model


class account_invoice_line(Model):
    _inherit = 'account.invoice.line'

    _columns = {
        'tag_ids': fields.many2many(
            'product.tag', 'account_invoice_line_product_tag_rel',
            'invoice_line_id', 'tag_id', 'Tags'),
    }

    def create(self, cr, uid, vals, context=None):
        product_obj = self.pool['product.product']
        if vals.get('product_id', False):
            product = product_obj.browse(
                cr, uid, vals['product_id'], context=context)
            vals.update({
                'tag_ids': [(6, False, [x.id for x in product.tag_ids])]})
        return super(account_invoice_line, self).create(
            cr, uid, vals, context=context)

    def write(self, cr, uid, ids, vals, context=None):
        product_obj = self.pool['product.product']
        if vals.get('product_id', False):
            product = product_obj.browse(
                cr, uid, vals['product_id'], context=context)
            vals.update({
                'tag_ids': [(6, False, [x.id for x in product.tag_ids])]})
        return super(account_invoice_line, self).write(
            cr, uid, ids, vals, context=context)
