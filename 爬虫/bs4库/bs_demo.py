from bs4 import BeautifulSoup
html = '''
<!-- This is the example.html example file. -->
<html><head><title>The Website Title</title></head>
<body>
<p>Download my <strong>Python</strong> book from <a href="http://
inventwithpython.com">my website</a>.</p>
<p class="slogan">Learn Python the easy way!</p>
<p>By <span id="author">Al Sweigart</span></p>
</body>
</html>
'''
soup = BeautifulSoup(html, 'lxml')
element = soup.select('#author')
print(element[0].getText())
