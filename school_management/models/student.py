from odoo import fields,models

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student Description'

    student_name = fields.Char(string='Student Name')
    student_id = fields.Char(string='Student ID')
    gender = fields.Selection(selection=[('M','Male'),('F','Female')])
    date_of_birth = fields.Date(string='Date of Birth')
    phone_no = fields.Char(string='Phone Number')
    email = fields.Char(string='Email Address')
    address = fields.Text(string='Address')
    active=fields.Boolean()

