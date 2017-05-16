# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-today OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

import base64
import logging
import re
from email.utils import formataddr
from urllib import urlencode
from urlparse import urljoin

import psycopg2

from openerp import tools
from openerp import SUPERUSER_ID
from openerp.osv import fields, osv
from openerp.osv.orm import except_orm
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)


class mail_mail(osv.Model):
    """ Model holding RFC2822 email messages to send. This model also provides
        facilities to queue and send new email messages.  """
    _inherit = 'mail.mail'
    
   
    def create(self, cr, uid, values, context=None):
        if 'email_template' in context:
            template = self.pool.get('email.template').browse(cr, uid, context['email_template'], context=context)
            if template.reply_to:
                values.update({'reply_to' : template.reply_to})
        return super(mail_mail, self).create(cr, uid, values, context=context)
    