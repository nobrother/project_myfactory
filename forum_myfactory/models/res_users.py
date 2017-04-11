# -*- coding: utf-8 -*-

from openerp import SUPERUSER_ID, models, fields, api

class ResUsers(models.Model):

    _inherit = 'res.users'

    def process_forum_validation_token(self, cr, uid, token, user_id, email, forum_id=None, context=None):
        validation_token = self.pool['res.users']._generate_forum_token(cr, uid, user_id, email)
        user = self.pool['res.users'].browse(cr, SUPERUSER_ID, user_id, context=context)
        if token == validation_token:
            if not forum_id:
                forum_ids = self.pool['forum.forum'].search(cr, uid, [], limit=1, context=context)
                if forum_ids:
                    forum_id = forum_ids[0]
            if forum_id:
                forum = self.pool['forum.forum'].browse(cr, uid, forum_id, context=context)

                if user.karma == 0:
                    # karma gained: karma to ask a question and have 2 downvotes
                    karma = forum.karma_ask + (-2 * forum.karma_gen_question_downvote)
                    user.write({'karma': karma})
            return True
        return False
