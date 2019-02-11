from odoo import models,fields

class film(models.Model):
    _name = 'cine.film'
    nameFilm = fields.Char(string="name", required=True, help="Nombre de la pelicula")
    director_ids = fields.One2many("cine.director", "film_id", string="director")
    