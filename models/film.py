from odoo import models,fields, api

class film(models.Model):
    _name = 'cinemateca.film'
    name = fields.Char(string="name", required=True, help="Nombre de la pelicula")
    director_id = fields.Many2one("cinemateca.director", string="director")
    category_id = fields.Many2one("cinemateca.category", string="category")