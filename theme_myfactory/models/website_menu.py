# -*- coding: utf-8 -*-
from openerp import models, fields


class website_menu(models.Model):
    _name = "website.menu"
    _inherit = "website.menu"

    active = fields.Boolean("Active", default=True)