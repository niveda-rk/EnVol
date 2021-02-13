import webbrowser
import os
#open an HTML file on my own (Windows) computer
url = 'file://' + os.path.realpath('index.html')
webbrowser.open(url,new=2)
