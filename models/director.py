from odoo import models,fields

class director(models.Model):
    _inherit = 'base.entidad'
    _name = 'modulocinebase.director'
    nameDirector = fields.Char(string="name", required=True, help="Nombre del director")
    filmid = fields.Many2one("modulocinebase.film", ondelete="set null", string="film", required=True, index=True)
    