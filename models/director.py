from odoo import models,fields

class director(models.Model):
    _name = 'cine.director'
    nameDirector = fields.Char(string="name", required=True, help="Nombre del director")
    film_id = fields.Many2one("cine.film", ondelete="cascade", string="Film", required=True)
    