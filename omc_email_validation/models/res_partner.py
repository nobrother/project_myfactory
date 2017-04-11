# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ResPartner(models.Model):

    _name = 'res.partner'
    _inherit = 'res.partner'

    email_validated = fields.Char('Email validated', compute='check_email_change', store=True)

    @api.one
    @api.depends('email')
    def check_email_change(self):
        if self.email != self.email_validated:
            self.email_validated = ''

    def set_email_validated(self, cr, uid, partners):
        for partner in partners:
            partner.write({
                'email_validated': partner.email
            })