# -*- coding: utf-8 -*-
from openerp import SUPERUSER_ID
from openerp.addons.web import http
from openerp.http import request
from openerp.addons.website.controllers.main import Website
from openerp.addons.website_crm.controllers.main import contactus

class Website(Website):

    @http.route()
    def index(self, **kw):
        try:
            return request.render('theme_myfactory.home')
        except Exception:
            return super(Website, self).index(**kw)

    @http.route('/benefits', type='http', auth="public", website=True)
    def page_benefits(self):
        return request.render('theme_myfactory.benefits')

    @http.route('/packages', type='http', auth="public", website=True)
    def page_packages(self):
        return request.render('theme_myfactory.packages')

    @http.route('/features', type='http', auth="public", website=True)
    def page_features(self):
        return request.render('theme_myfactory.features')

    @http.route('/about-us', type='http', auth="public", website=True)
    def page_about_us(self):
        return request.render('theme_myfactory.about_us')

    @http.route('/demo', type='http', auth="public", website=True)
    def page_demo(self):
        return request.render('theme_myfactory.demo')



    @http.route('/ask-for-trial', type='http', auth="public", website=True)
    def page_ask_for_trial(self, **kwargs):

        values = {}

        products = request.registry['product.product'].search_read(request.cr, SUPERUSER_ID,[],['name'])

        values.update(products=products)

        for field in ['description', 'partner_name', 'phone', 'contact_name', 'email_from', 'name']:
            if kwargs.get(field):
                values[field] = kwargs.pop(field)
        values.update(kwargs=kwargs.items())

        return request.render('theme_myfactory.ask_for_trial', values)



class contactus(contactus):

    @http.route('/contact-us', type='http', auth="public", website=True)
    def contact(self, **kwargs):
        return super(contactus, self).contact(**kwargs)