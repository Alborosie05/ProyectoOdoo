from odoo import models,fields, api

class category(models.Model):
    _name = 'cinemateca.category'
    name = fields.Char(string="Nombre de la categoria", required=True, help="Nombre de la categoria")
    film_ids = fields.One2many("cinemateca.film", "category_id", string="film")