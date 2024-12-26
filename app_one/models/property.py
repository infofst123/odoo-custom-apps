from odoo import models, fields, api

class Property(models.Model):
    _name = 'property'
    _log_access = False
    name= fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    diff = fields.Float(compute="__compute_diff",sotre=1,readonly=1)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        [
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West'),
        ]
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('pending', 'Pending'),
            ('sold', 'Sold')
        ]
    )

    def action_pending(self):
        for rec in self:
            rec.state = 'pending'
            rec.write({
                'state':'pending'
            })

    def action_sold(self):
        for rec in self:
            rec.state = 'sold'
            rec.write({
                'state':'sold'
            })

    @api.depends('selling_price','expected_price', 'owner_id.phone')
    def __compute_diff(self):
        for rec in self:
            self.diff = self.selling_price - self.expected_price

    @api.onchange('expected_price') # should be a simple field not computed or reference to another class
    def __onchange_expected_price(self):
        for rec in self:
            self.diff = self.selling_price - self.expected_price
        