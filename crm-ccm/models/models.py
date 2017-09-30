# -*- coding: utf-8 -*-

from openerp import models, fields, api

class CallType(models.Model):
    _name = 'ib.calltype'
    name = fields.Char()
    description = fields.Text()

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
