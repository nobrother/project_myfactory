# -*- coding: utf-8 -*-

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp


def _get_uom_id(self):
    cr, uid = self.env.cr, self.env.uid
    try:
        proxy = self.pool.get('ir.model.data')
        result = proxy.get_object_reference(cr, uid, 'product', 'product_uom_unit')
        return result[1]
    except Exception, ex:
        return False

class crm_lead_line(models.Model):

    """ Type of leads """

    _name = 'crm.lead.line'

    lead_id = fields.Many2one('crm.lead', 'Lead')
    product_id = fields.Many2one('product.product', 'Product')
    description = fields.Text('Description')
    product_uom_qty = fields.Float('Quantity', digits_compute=dp.get_precision('Product UoS'), default=1)
    product_uom = fields.Many2one('product.uom', 'Unit of Measure', compute='product_id_change', default=_get_uom_id)

    @api.one
    @api.depends('product_id')
    def product_id_change(self):
        if self.product_id:
            self.product_uom = self.product_id.uom_id.id

class crm_lead(models.Model):

    _inherit = 'crm.lead'

    line_ids = fields.One2many('crm.lead.line', 'lead_id', string='Preferred products')

