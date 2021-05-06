# open a link in browser using python
import webbrowser
url = 'https://pythonexamples.org'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open(url)

#google search using python
#pip install google
try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

# to search
query = "images for scenery"

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
	print(j)
