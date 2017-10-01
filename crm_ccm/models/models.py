# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Config(models.Model):
    _name = 'ib.config'
    category = fields.Char(string='Category', required=True, translate=True)
    name = fields.Char(string='Key', required=True, translate=True)
    value = fields.Char(string='Value', required=True, translate=True)
    description = fields.Text(string='Description', required=False, translate=True)

class CallRecord(models.Model):
    _name = 'ib.callrecord'
    _order = "id desc"

    date = fields.Datetime(
        string='Date', track_visibility='onchange', copy=False,
        default=lambda self: fields.Datetime.now(), required=True, translate=True)
    partner_id = fields.Many2one(
        'res.partner', string='Customer Name', required=True, translate=True)
    
    user_id = fields.Many2one(
        'res.users', string='Responsible', track_visibility='onchange',
        default=lambda self: self.env.user, required=True, translate=True)

    time_id = fields.Many2one(
        'ib.config', string='Call Time', track_visibility='onchange', required=True, translate=True)

    out_going_call_id = fields.Many2one('ib.config', string='Out going Call', track_visibility='onchange', required=False, translate=True)
    in_coming_call_id = fields.Many2one('ib.config', string='In coming Call', track_visibility='onchange', required=False, translate=True)

    approach_type_id = fields.Many2one('ib.config', string='Approach Type', track_visibility='onchange', required=False, translate=True)

    result = fields.Text(string='Result', required=False, translate=True)
    call_content = fields.Text(string='Call Content', required=True, translate=True)

    issues = fields.Char(string='Issues', required=False, translate=True)
    resolve_method = fields.Char(string='Resolve Method', required=False, translate=True)

    approach_eval_id = fields.Many2one('ib.config', string='Approach Evaluation', track_visibility='onchange', required=False, translate=True)
    customer_eval_id = fields.Many2many('ib.config', 'customer_eval_config_rel', 'callrecord_id', 'config_id', string='Customer Evaluation', track_visibility='onchange', required=False, translate=True)

    call_eval_id = fields.Many2one('ib.config', string='Call Evaluation', track_visibility='onchange', required=False, translate=True)

    description = fields.Text(string='Description', required=False, translate=True)

    note = fields.Char(string='Note', required=False, translate=True)
