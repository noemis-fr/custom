# -*- coding: utf-8 -*-
##############################################################################
#
#    SEPA Direct Debit module for OpenERP
#    Copyright (C) 2013 Akretion (http://www.akretion.com)
#    @author: Alexis de Lattre <alexis.delattre@akretion.com>
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


from openerp.osv import orm, fields
from openerp.tools.translate import _
from openerp import netsvc
from datetime import datetime, timedelta
from lxml import etree
from dateutil import parser
import base64

class banking_export_natixis_wizard(orm.TransientModel):
    _name = 'banking.export.natixis.wizard'
    _inherit = ['banking.export.pain']
    _description = 'Export Natixis Direct Debit File'
    _columns = {
        'state': fields.selection([
            ('create', 'Create'),
            ('finish', 'Finish'),
        ], 'State', readonly=True),
        'nb_transactions': fields.related(
            'file_id', 'nb_transactions', type='integer',
            string='Number of Transactions', readonly=True),
        'total_amount': fields.related(
            'file_id', 'total_amount', type='float', string='Total Amount',
            readonly=True),
        'file_id': fields.many2one(
            'banking.export.natixis', 'natixis File', readonly=True),
        'file': fields.related(
            'file_id', 'file', string="File", type='binary', readonly=True),
        'filename': fields.related(
            'file_id', 'filename', string="Filename", type='char', size=256,
            readonly=True),
        'payment_order_ids': fields.many2many(
            'payment.order', 'wiz_natixis_payorders_rel', 'wizard_id',
            'payment_order_id', 'Payment Orders', readonly=True),
    }

    _defaults = {
        'state': 'create',
    }

    def create(self, cr, uid, vals, context=None):
        payment_order_ids = context.get('active_ids', [])
        vals.update({
            'payment_order_ids': [[6, 0, payment_order_ids]],
        })
        return super(banking_export_natixis_wizard, self).create(
            cr, uid, vals, context=context)
    
    
    def create_header(self, cr, uid, vals, context=None):
        
        
        header=self.company_registration_code( cr, uid, context=None)
        
        val = self.company_sequential_code( cr, uid, vals, context=None)
        header = header + val
        
        val = self.factor_code( cr, uid, vals, context=None)
        header = header + val
    
        val = self.company_customer_code( cr, uid, vals, context=None)
        header = header + val
    
        val = self.contract_currency( cr, uid, vals, context=None)
        header = header + val
        
        val = self.company_name( cr, uid, vals, context=None)
        header = header + val
        
        val = self.bankruptcy_date( cr, uid, vals, context=None)
        header = header + val
        
        val = self.production_date( cr, uid, vals, context=None)
        header = header + val
    
        val = self.reference( cr, uid, vals, context=None)
        header = header + val
    
        val = self.version( cr, uid, vals, context=None)
        header = header + val

        header=header.ljust(275,' ')
        
        return header

    
    def company_registration_code(self, cr, uid, context=None):   
        return "01"
            
        
    def company_sequential_code(self, cr, uid, vals, context=None):
        return "000001"
        
    def factor_code(self, cr, uid, vals, context=None):
        return "138"
    
    def company_customer_code(self, cr, uid, vals, context=None):
        return vals.company_id.natixis_customer_number
    
    def contract_currency(self, cr, uid, vals, context=None):
        return vals.company_id.currency_id.name
        
    def company_name(self, cr, uid, vals, context=None):
        name=vals.company_id.name.upper()
#         _logger len 
        name=name.ljust(25,' ')
        return name
        
    def bankruptcy_date(self, cr, uid, vals, context=None):
        date=parser.parse(vals.date_created)
        date = date- timedelta(days=1)
        strdate = date.strftime('%d%m%Y')
        return strdate
        
    def production_date(self, cr, uid, vals, context=None):
        date=parser.parse(vals.date_created).strftime('%d%m%Y')
        return date
    
    def reference(self, cr, uid, vals, context=None):
        return "123"
    
    def version(self, cr, uid, vals, context=None):
        return "7.0"
    
    
    
    def customer_registration_code(self, cr, uid, vals, context=None):
        return "02"
        
    def customer_sequential_code(self, cr, uid, vals, context=None):
        lines_count=str(vals[0])
        lines_count=lines_count.rjust(6,'0')
        return lines_count
        
    def customer_siret(self, cr, uid, vals, context=None):
        siret = ""
        if vals.partner_id.commercial_partner_id.siret:
            siret=vals.partner_id.commercial_partner_id.siret
            siret=siret.rjust(14,'0')
        siret=siret.ljust(14,' ')
        return siret
    
    
    def customer_name(self, cr, uid, vals, context=None):
        name=vals.partner_id.commercial_partner_id.name
        name=name.ljust(15,' ')
        return name
    
    def customer_account_number(self, cr, uid, vals, context=None):
        account=""
        if vals.partner_id.commercial_partner_id.id:
            account = str(vals.partner_id.commercial_partner_id.id)
        account=account.rjust(10,'0')
        return account
        
        
    def activity(self, cr, uid, vals, context=None):
        if vals.partner_id.commercial_partner_id.country_id.code =="FR":
            return"D"
        return "E"
        
    def comment(self, cr, uid, vals, context=None):
        comment = " "
        comment = comment.ljust(20,' ')
        return comment
        
    def move_id(self, cr, uid, vals, context=None):
        move_id = vals.move_id.name
        move_id=move_id.ljust(30,' ')
        return move_id
        
    def natixis_move_id(self, cr, uid, vals, context=None):
        natixis_move_id = vals.move_id.name+parser.parse(vals.date_maturity).strftime('%d%m%Y')
        natixis_move_id=natixis_move_id.ljust(30,' ')
        return natixis_move_id
        
    def move_type(self, cr, uid, vals, context=None):
        type=""
        if vals.invoice.type=="out_invoice":
            type ="FAC"
        elif vals.invoice.type=="out_refund":
            type ="AVO"
        else:
            type="   "
        
        return type
        
    def payment_method(self, cr, uid, vals, context=None):
        type=""
        if vals.invoice.payment_type:
            type =vals.invoice.payment_type
        else:
            type="   "
            
        return type
    
    def move_date(self, cr, uid, vals, context=None):
        
        date=parser.parse(vals.date_created).strftime('%d%m%Y')
        return date
    
    def maturity_date(self, cr, uid, vals, context=None):
        
        date=parser.parse(vals.date_maturity).strftime('%d%m%Y')
        return date
        
    def line_total_amount(self, cr, uid, vals,total_amount, context=None):
        total=""
        if vals.invoice.residual:
            total_amount[0] +=vals.invoice.residual
            total ="%.2f" % vals.invoice.residual
        total=total.replace(',','')
        total=total.replace('.','')
        total=total.rjust(13,'0')
        
        return total
        
    def move_currency(self, cr, uid, vals, context=None):
        return vals.invoice.currency_id.name
        
    def indicator(self, cr, uid, vals, context=None):
        return " "
        
    def effect_number(self, cr, uid, vals, context=None):
        value =""
        value=value.ljust(7,' ')
        return value
        
    def effect_total_amount(self, cr, uid, vals, context=None):
        value =""
        value=value.ljust(13,' ')
        return value
        
    def effect_amount(self, cr, uid, vals, context=None):
        value =""
        value=value.ljust(13,' ')
        return value
        
    def rib(self, cr, uid, vals, context=None):
        value =""
        value=value.ljust(23,' ')
        return value
        
    def effect_maturity_date(self, cr, uid, vals, context=None):
        value =""
        value=value.ljust(8,' ')
        return value
        
    def ref_drawn(self, cr, uid, vals, context=None):
        value =""
        value=value.ljust(10,' ')
        return value
        
    def effect_type(self, cr, uid, vals, context=None):
        return " "




    def footer_registration_code(self, cr, uid, context=None):   
        return "09"
    
    def total_amount(self, cr, uid, total_amount, context=None):
        
        total ="%.2f" % total_amount[0]
        total=total.replace(',','')
        total=total.replace('.','')
        total=total.rjust(13,'0')
        
        return total
    

    def create_body(self, cr, uid, vals,nb_lines,amount, context=None):
        
        bodyfinal=""
        
        for line in vals.line_ids:
            nb_lines[0] +=1
            body=""
            
            val=self.customer_registration_code( cr, uid, vals, context=None)
            body = body + val
            
            val = self.customer_sequential_code( cr, uid, nb_lines, context=None)
            body = body + val
            
            val = self.customer_siret( cr, uid, line, context=None)
            body = body + val
        
            val = self.customer_name( cr, uid, line, context=None)
            body = body + val
        
            val = self.customer_account_number( cr, uid, line, context=None)
            body = body + val
            
            body=body.ljust(52,' ')
        
            val = self.activity( cr, uid, line.move_line_id, context=None)
            body = body + val
            
            body=body.ljust(62,' ')
            
            val = self.comment( cr, uid, vals, context=None)
            body = body + val
            
            val = self.move_id( cr, uid, line.move_line_id, context=None)
            body = body + val
            
            val = self.natixis_move_id( cr, uid, line.move_line_id, context=None)
            body = body + val
            
            val = self.move_type( cr, uid, line.move_line_id, context=None)
            body = body + val
            
            val = self.payment_method( cr, uid, line.move_line_id, context=None)
            body = body + val
        
            val = self.move_date( cr, uid, line.move_line_id, context=None)
            body = body + val
        
            val = self.maturity_date( cr, uid, line.move_line_id, context=None)
            body = body + val
            
            val = self.line_total_amount( cr, uid, line.move_line_id,amount, context=None)
            body = body + val
            
            val = self.move_currency( cr, uid, line.move_line_id, context=None)
            body = body + val
            
            body=body.ljust(182,' ')
            
            
            
            val = self.indicator( cr, uid, vals, context=None)
            body = body + val
            
            val = self.effect_number( cr, uid, vals, context=None)
            body = body + val
            
            val = self.effect_total_amount( cr, uid, vals, context=None)
            body = body + val
            
            val = self.effect_amount( cr, uid, vals, context=None)
            body = body + val
            
            val = self.rib( cr, uid, vals, context=None)
            body = body + val
            
            val = self.effect_maturity_date( cr, uid, vals, context=None)
            body = body + val
            
            val = self.ref_drawn( cr, uid, vals, context=None)
            body = body + val
            
            val = self.effect_type( cr, uid, vals, context=None)
            body = body + val
            
            body=body.ljust(275,' ')
            
            bodyfinal += body + "\r\n"
        
        
        return bodyfinal
    
    def create_footer(self, cr, uid, vals,nb_lines,total_amount, context=None):
        
        nb_lines[0]+=1
        
        footer=self.footer_registration_code( cr, uid, context=None)
        
        val = self.customer_sequential_code( cr, uid, nb_lines, context=None)
        footer = footer + val
        
        val = self.factor_code( cr, uid, vals, context=None)
        footer = footer + val
    
        val = self.company_customer_code( cr, uid, vals, context=None)
        footer = footer + val
        
        val = self.company_name( cr, uid, vals, context=None)
        footer = footer + val
        
        val = self.total_amount( cr, uid, total_amount, context=None)
        footer = footer + val

        footer=footer.ljust(275,' ')
        
        footer+="\r\n"
        
        return footer
    
    
    
    

    def create_natixis(self, cr, uid, ids, context=None):
        '''
        Creates the Natixis Direct Debit file. That's the important code !
        '''
        gen_args = {'test':"test",
                    'file_obj': self.pool['banking.export.natixis']}

        pain_ns = {
            'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        }
        
        nb_lines = [1]
        total_amount = [0.00]
        
        payment_order = self.pool['payment.order'].browse(cr, uid, context['active_id'], context=context)
        
        xml_root = self.create_header(cr, uid, payment_order, context)
        
        value= self.create_body(cr, uid, payment_order,nb_lines,total_amount, context)
        xml_root=xml_root+"\r\n"+value
        
        value = self.create_footer(cr, uid, payment_order,nb_lines,total_amount, context)
        xml_root+=value

        transactions_count_1_6 = 0

        return self.finalize_natixis_file_creation(
            cr, uid, ids, xml_root, total_amount[0], transactions_count_1_6,
            gen_args, context=context)
        

    def finalize_natixis_file_creation(
            self, cr, uid, ids, xml_root, total_amount, transactions_count,
            gen_args, context=None):
        
        file_id = gen_args['file_obj'].create(
            cr, uid, self._prepare_export_natixis(
                cr, uid, total_amount, transactions_count,
                xml_root, gen_args, context=context),
            context=context)

        self.write(
            cr, uid, ids, {
                'file_id': file_id,
                'state': 'finish',
            }, context=context)

        action = {
            'name': 'natixis File',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form,tree',
            'res_model': self._name,
            'res_id': ids[0],
            'target': 'new',
        }
        return action
    
    def _prepare_export_natixis(
            self, cr, uid, total_amount, transactions_count, xml_string,
            gen_args, context=None):
        "quasi bon pour natixis, il faut juste vérifier des données et supprimer certaines variables"
        return {
#             'batch_booking': gen_args['sepa_export'].batch_booking, 
#             'charge_bearer': gen_args['sepa_export'].charge_bearer,
            'total_amount': total_amount,
            'nb_transactions': transactions_count,
            'file': base64.encodestring(xml_string),
#             'payment_order_ids': [(
#                 6, 0, [x.id for x in gen_args['sepa_export'].payment_order_ids]
#             )],
        }
    
    

    def cancel_natixis(self, cr, uid, ids, context=None):
        '''
        Cancel the Natixis file: just drop the file
        '''
        sepa_export = self.browse(cr, uid, ids[0], context=context)
        self.pool.get('banking.export.natixis').unlink(
            cr, uid, sepa_export.file_id.id, context=context)
        return {'type': 'ir.actions.act_window_close'}

    def save_natixis(self, cr, uid, ids, context=None):

        sepa_export = self.browse(cr, uid, ids[0], context=context)
        self.pool.get('banking.export.natixis').write(
            cr, uid, sepa_export.file_id.id, {'state': 'sent'},
            context=context)
        wf_service = netsvc.LocalService('workflow')
        return {'type': 'ir.actions.act_window_close'}
