# -*- coding: utf-8 -*-
##############################################################################

##############################################################################
{
    'name': 'Account Banking Netixis Direct Debit',
    'summary': 'Create Natixis files for Direct Debit',
    'version': '7.0.0.2.0',
    'license': 'AGPL-3',
    'author': "Mind And Go",
    'website': "http://www.mind-and-go.com",
    'category': 'Banking addons',
    'depends': [
        'account_direct_debit',
        'account_banking_pain_base',
        'account_payment_partner',
        'account'
    ],
    'external_dependencies': {
        'python': ['unidecode', 'lxml'],
    },
    'data': [
        'views/account_banking_natixis_view.xml',
        'views/company_view.xml',
        'wizard/export_natixis_view.xml',
        'security/ir.model.access.csv',
        'views/invoice.xml',
        'data/payment_type_natixis.xml',
        'views/account_payment_view.xml',
    ],
    'demo': ['sepa_direct_debit_demo.xml'],
    'description': '''
Module to export direct debit payment orders in Natixis TXT file format.

    ''',
    'active': False,
    'installable': True,
}
