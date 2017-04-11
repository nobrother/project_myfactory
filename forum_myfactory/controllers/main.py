# -*- coding: utf-8 -*

from openerp import SUPERUSER_ID
from openerp.addons.web import http
from openerp.http import request
from openerp.addons.website_forum.controllers.main import WebsiteForum

class WebsiteForum(WebsiteForum):

    @http.route()
    def validate_email(self, token, id, email, forum_id=None, **kwargs):
        if forum_id:
            try:
                forum_id = int(forum_id)
            except ValueError:
                forum_id = None

        user_obj = request.registry['res.users']
        done = user_obj.process_forum_validation_token(request.cr, request.uid, token, int(id),
                                                       email, forum_id=forum_id,
                                                       context=request.context)
        # Set this email as validated
        user = user_obj.browse(request.cr, request.uid, int(id))
        if user and done:
            request.registry['res.partner'].set_email_validated(request.cr, request.uid, [user.partner_id])

        if done:
            request.session['validation_email_done'] = True

        if forum_id:
            return request.redirect("/forum/%s" % int(forum_id))
        return request.redirect('/forum')

    @http.route()
    def questions(self, forum, tag=None, page=1, filters='all', sorting='date', search='', **post):
        res = super(WebsiteForum, self).questions(forum, tag, page, filters, sorting, search, **post)

        res.qcontext.update({
            'test': 'apple'
        })

        return res