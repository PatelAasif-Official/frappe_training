# Copyright (c) 2021, Aasif Patel and contributors
# For license information, please see license.txt

# import frappe
from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class DataTypeThree(WebsiteGenerator):
	def before_save(self):

		self.readonlytype = "It's Come From The Module"
