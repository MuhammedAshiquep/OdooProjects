from dataclasses import field

from  odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Master'

    name = fields.Char(string='Name', required=True, tracking=True )
    age = fields.Integer(string='age', tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender")

    @api.onchange('age')
    def _onchange_age(self):
        if self.age <=10:
            self.is_child =True
        else:
            self.is_child=False