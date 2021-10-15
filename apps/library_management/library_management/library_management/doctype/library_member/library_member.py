# Copyright (c) 2021, Asif Patel and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LibraryMember(Document):
	
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'
