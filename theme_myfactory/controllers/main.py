# -*- coding: utf-8 -*-
from openerp.addons.web import http
from openerp.http import request
from openerp.addons.website.controllers.main import Website

class Website(Website):
    @http.route('/benefits', type='http', auth="public", website=True)
    def page_benefits(self):
        return request.render('theme_myfactory.benefits')

    @http.route('/packages', type='http', auth="public", website=True)
    def page_packages(self):
        return request.render('theme_myfactory.packages')

    @http.route('/features', type='http', auth="public", website=True)
    def page_features(self):
        return request.render('theme_myfactory.features')

