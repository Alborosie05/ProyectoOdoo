from odoo import models,fields

class film(models.Model):
    _name = 'modulocinebase.film'
    nameFilm = fields.Char(string="name", required=True, help="Nombre de la pelicula")
    directorids = fields.One2many("modulocinebase.director", "filmid", string="director")
    