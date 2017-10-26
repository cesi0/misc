#!/usr/bin/python

from documentcloud import DocumentCloud
client = DocumentCloud()

doc_list = client.documents.search('group:the-intercept')

for i in doc_list:
	print i.pdf_url
