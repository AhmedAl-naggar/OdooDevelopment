# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Client(models.Model):
    _name = 'alnaggarnet.client'
    _description = "Al-naggar Net Client"

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone Number", required=True)
    date_of_birth = fields.Char(string="Date Of Birth")
    address = fields.Char(string="Address")
    notes = fields.Text()

    package_price = fields.Integer(string="Package Price", required=True)
    max_speed = fields.Integer(string="Max Speed", required=True)
    mac_address = fields.Char(string="Mac Address", required=True)
    wifi_name = fields.Char(string="Wifi Name")
    wifi_password = fields.Char(string="Wifi Password")
    router_password = fields.Char(string="Router Password")
    start_date = fields.Char(string="Start Date")

    color = fields.Integer()
#
# class Partner(models.Model):
#     _inherit = 'res.partner'
#
#     # Add a new column to the res.partner model, by default partners are not
#     # instructors
#     instructor = fields.Boolean("Instructor", default=False)
#
