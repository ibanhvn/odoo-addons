# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Config(models.Model):
    _name = 'ib.config'
    category = fields.Char(string='Category', required=True)
    name = fields.Char(string='Name', required=True)
    value = fields.Char(string='Value', required=True)
    description = fields.Text(string='Description', required=False)

class CallRecord(models.Model):
    _name = 'ib.callrecord'
    # _inherit = ['mail.thread']
    _order = 'id desc'
    _rec_name = 'partner_id'

    date = fields.Datetime(
        string='Date', track_visibility='onchange', copy=False,
        default=lambda self: fields.Datetime.now(), required=True)
    
    partner_id = fields.Many2one(
        'res.partner', string='Partner', required=True, ondelete='cascade')
    
    user_id = fields.Many2one(
        'res.users', string='Responsible', track_visibility='onchange',
        default=lambda self: self.env.user, required=True)

    time_id = fields.Many2one(
        'ib.config', string='Time', required=True, ondelete='cascade')

    out_going_call_id = fields.Many2one('ib.config', string='Out going call', required=False)

    in_coming_call_id = fields.Many2one('ib.config', string='In coming call', required=False)

    approach_type_id = fields.Many2one('ib.config', string='Approach type', required=False)

    result = fields.Text(string='Result', required=False)
    call_content = fields.Text(string='Call content', required=False)

    issues = fields.Char(string='Issues', required=False)
    resolve_method = fields.Char(string='Resolve method', required=False)

    approach_eval_id = fields.Many2one('ib.config', string='Approach eval.', track_visibility='onchange', required=False)
    customer_eval_id = fields.Many2many('ib.config', 'customer_eval_config_rel', 'callrecord_id', 'config_id', string='Customer Evaluation', track_visibility='onchange', required=False)

    call_eval_id = fields.Many2one('ib.config', string='Call eval.', track_visibility='onchange', required=False)

    description = fields.Text(string='Description', required=False)

    note = fields.Char(string='Note', required=False)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    callrecord_ids = fields.One2many(
        'ib.callrecord', 'partner_id', string='Call record')

    callrecord_count = fields.Integer(
        compute='_count_callrecords', string='# Call records',
        readonly=True)

    @api.multi
    @api.depends('callrecord_ids')
    def _count_callrecords(self):
        callrecord = self.env['ib.callrecord']
        for partner in self:
            try:
                partner.callrecord_count = callrecord.search_count(
                    [('partner_id', 'child_of', partner.id)])
            except:
                partner.callrecord_count = 0