from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Course(models.Model):
    _name = 'od_openacademy.course'

    name = fields.Char(string='Title', required=True)
    description = fields.Char(string='Description')
    responsible_id = fields.Many2one("res.users", ondelete="set null")
    session_ids = fields.One2many('od_openacademy.session', 'course_id', string="Sessions")
    @api.constrains('name', 'description')
    def _check_name_and_description_different(self):
        for record in self:
            if record.name == record.description:
                raise ValidationError(_("Title and Description must be different."))

    @api.constrains('name')
    def _check_name_unique(self):
        # Check if any other record with the same name exists
        duplicate_records = self.search([('name', '=', self.name)])
        if len(duplicate_records) > 1:
            raise ValidationError(_("Title must be unique."))


class Session(models.Model):
    _name = "od_openacademy.session"
    _description = "Openacademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date(string="Start Date", default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one("res.partner", string="Instructor")
    course_id = fields.Many2one('od_openacademy.course', string='Course', required=True)
    attendee_ids = fields.Many2many('res.partner', 'session_res_partner', 'session_id', 'attendee_id',
                                    string='Attendees')
    taken_seats = fields.Float(string='Taken Seats', compute='_compute_taken_seats')
    active = fields.Boolean(default=True)

    @api.onchange('seats', 'attendee_ids')
    def _onchange_seats_attendees(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Something bad happened",
                    'message': "You can not add a negative value",
                }
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Something bad happened",
                    'message': "You cannot add more attendees than the number of seats",
                }
            }

    @api.depends('attendee_ids', 'seats')
    def _compute_taken_seats(self):
        for session in self:
            if session.seats == 0:
                session.taken_seats = 0
            else:
                session.taken_seats = (len(session.attendee_ids) / session.seats) * 100

    @api.constrains('instructor_id ', 'attendee_ids')
    def check_instructor_as_attendee(self):
        for record in self:
            if record.instructor_id.id in record.attendee_ids.ids:
                raise ValidationError(_("you are not add instructor as attendee!"))

class ResUsers(models.Model):
    _inherit = 'res.users'

    karma = fields.Integer(string='Karma')
