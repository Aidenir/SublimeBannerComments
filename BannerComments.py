import sublime, sublime_plugin
import urllib.request
from html.parser import HTMLParser

comment = ""

class Makebanner(sublime_plugin.TextCommand):
	def run(self,edit):
		global comment
		comment = ""
		view = self.view
		sel = view.sel()
		selection = view.substr(sel[0])

		url = 'http://www.network-science.de/ascii/ascii.php?TEXT=' + selection + '&x=24&y=9&FONT=banner3&RICH=no&FORM=left&STRE=no&WIDT=80'
		response = urllib.request.urlopen(url)
		data = response.read()      # a `bytes` object
		text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
		parser = MyHTMLParser(strict=False)
		parser.feed(text)

		view.replace(edit,sel[0],comment)


class MyHTMLParser(HTMLParser): 
	def handle_data(self, data):
		if data[0] == '#':
			global comment
			comment = data
			print(data)