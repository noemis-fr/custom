# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-Today OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from openerp import tools
from openerp.osv import osv, fields



class mail_compose_message(osv.TransientModel):
    _inherit = 'mail.compose.message'


    def send_mail(self, cr, uid, ids, context=None):
        """ Override of send_mail to duplicate attachments linked to the email.template.
            Indeed, basic mail.compose.message wizard duplicates attachments in mass
            mailing mode. But in 'single post' mode, attachments of an email template
            also have to be duplicated to avoid changing their ownership. """
        email_context = dict(context or {})
        template = False
        email_template = self.pool.get('email.template')
        wizards = self.browse(cr, uid, ids, context=context)
        for wizard in wizards:
            post_values = {
                    'body': wizard.body or '',
                }
            context
            if wizard.composition_mode == 'mass_mail' or not wizard.template_id:
                continue
            template = self.pool.get('email.template').browse(cr, uid, wizard.template_id, context=context)
            # TODO v8, remove me
            # template specific outgoing mail server and email from is lost in super send_mail
            # store them in the context to avoid falling back to default values
            if template.mail_server_id:
                email_context['mail_server_id'] = template.mail_server_id.id
            if template.email_from:
                email_context['email_from'] = template.email_from
            if template.reply_to:
                email_context['reply_to'] = template.reply_to
            if wizard.body:
                email_context['body_html'] = wizard.body
            new_attachment_ids = []
            for attachment in wizard.attachment_ids:
                if attachment in template.attachment_ids:
                    new_attachment_ids.append(self.pool.get('ir.attachment').copy(cr, uid, attachment.id, {'res_model': 'mail.compose.message', 'res_id': wizard.id}, context=context))
                else:
                    new_attachment_ids.append(attachment.id)
                self.write(cr, uid, wizard.id, {'attachment_ids': [(6, 0, new_attachment_ids)]}, context=context)

        if not template:
            return super(mail_compose_message, self).send_mail(cr, uid, ids, context=email_context)

        return email_template.send_mail(cr, uid, template.id, email_context.get('default_res_id', None) , force_send=False, context=email_context)

    
