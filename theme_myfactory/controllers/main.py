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
    def page_contact(self, **kwargs):
        #return super(contactus, self).contact(**kwargs)
        return request.render('theme_myfactory.contact_us')

    @http.route('/contact-us/thank-you', type='http', auth="public", website=True)
    def page_thank_you(self, **kwargs):
        # return super(contactus, self).contact(**kwargs)
        return request.render('theme_myfactory.contact_us_thank_you')

    @http.route()
    def contact(self, **kwargs):
        return request.redirect('/contact-us')

    @http.route(['/crm/contactus'], type='http', auth="public", website=True)
    def contactus(self, **kwargs):
        def dict_to_str(title, dictvar):
            ret = "\n\n%s" % title
            for field in dictvar:
                ret += "\n%s" % field
            return ret

        _TECHNICAL = ['show_info', 'view_from', 'view_callback']  # Only use for behavior, don't stock it
        _BLACKLIST = ['id', 'create_uid', 'create_date', 'write_uid', 'write_date', 'user_id',
                      'active']  # Allow in description
        _REQUIRED = ['name', 'contact_name', 'email_from',
                     'description']  # Could be improved including required from model

        post_file = []  # List of file to add to ir_attachment once we have the ID
        post_description = []  # Info to add after the message
        values = {}

        values['medium_id'] = request.registry['ir.model.data'].xmlid_to_res_id(request.cr, SUPERUSER_ID,
                                                                                'crm.crm_medium_website')
        values['section_id'] = request.registry['ir.model.data'].xmlid_to_res_id(request.cr, SUPERUSER_ID,
                                                                                 'website.salesteam_website_sales')
        for field_name, field_value in kwargs.items():
            if hasattr(field_value, 'filename'):
                post_file.append(field_value)
            elif field_name in request.registry['crm.lead']._fields and field_name not in _BLACKLIST:
                values[field_name] = field_value
            elif field_name not in _TECHNICAL:  # allow to add some free fields or blacklisted field like ID
                post_description.append("%s: %s" % (field_name, field_value))

        # If name (subject) is not defined, use contact_name as name
        if "name" not in kwargs and values.get("contact_name"):
            values["name"] = values.get("contact_name")

        # description is required, so it is always already initialized
        if post_description:
            values['description'] += dict_to_str(_("Custom Fields: "), post_description)

        # Show technical info on description
        if kwargs.get("show_info"):
            post_description = []
            environ = request.httprequest.headers.environ
            post_description.append("%s: %s" % ("IP", environ.get("REMOTE_ADDR")))
            post_description.append("%s: %s" % ("USER_AGENT", environ.get("HTTP_USER_AGENT")))
            post_description.append("%s: %s" % ("ACCEPT_LANGUAGE", environ.get("HTTP_ACCEPT_LANGUAGE")))
            post_description.append("%s: %s" % ("REFERER", environ.get("HTTP_REFERER")))
            values['description'] += dict_to_str(_("Environ Fields: "), post_description)

        # Create lead
        lead_id = self.create_lead(request, dict(values, user_id=False), kwargs)
        values.update(lead_id=lead_id)

        # Create attachment if any
        if lead_id:
            for field_value in post_file:
                attachment_value = {
                    'name': field_value.filename,
                    'res_name': field_value.filename,
                    'res_model': 'crm.lead',
                    'res_id': lead_id,
                    'datas': base64.encodestring(field_value.read()),
                    'datas_fname': field_value.filename,
                }
                request.registry['ir.attachment'].create(request.cr, SUPERUSER_ID, attachment_value,
                                                         context=request.context)

        return request.redirect('/contact-us/thank-you')