# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Config(models.Model):
    _name = 'ib.config'
    category = fields.Char(string='Category', required=True, translate=True)
    key = fields.Char(string='Key', required=True, translate=True)
    value = fields.Char(string='Value', required=True, translate=True)
    description = fields.Text(string='Description', required=False, translate=True)

# class crm-ccm(models.Model):
#     _name = 'crm-ccm.crm-ccm'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
