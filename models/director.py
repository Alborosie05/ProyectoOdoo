from odoo import models,fields, api

class director(models.Model):
    _name = 'cinemateca.director'
    name = fields.Char(string="nombre de Director", required=True, help="Nombre del director")
    film_ids = fields.One2many("cinemateca.film", "director_id", string="Peliculas")