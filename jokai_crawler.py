from urllib import request
import re
import os
from bs4 import BeautifulSoup
import unicodedata
import string

root = 'http://www.mek.iif.hu/porta/szint/human/szepirod/magyar/jokai/osszes/html/'

# find novel links
html = request.urlopen(root).read().decode('iso-8859-2')
novel_urls = re.findall('<a href="(.*?)">', html)

url = root + novel_urls[0]

# remove annoying characters
chars = {
    '\x82' : ',',        # High code comma
    '\x84' : ',,',       # High code double comma
    '\x85' : '...',      # Tripple dot
    '\x88' : '^',        # High carat
    '\x91' : '\x27',     # Forward single quote
    '\x92' : '\x27',     # Reverse single quote
    '\x93' : '\x22',     # Forward double quote
    '\x94' : '\x22',     # Reverse double quote
    '\x95' : ' ',
    '\x96' : '-',        # High hyphen
    '\x97' : '--',       # Double hyphen
    '\x99' : ' ',
    '\xa0' : ' ',
    '\xa6' : '|',        # Split vertical bar
    '\xab' : '<<',       # Double less than
    '\xbb' : '>>',       # Double greater than
    '\xbc' : '1/4',      # one quarter
    '\xbd' : '1/2',      # one half
    '\xbe' : '3/4',      # three quarters
    '\xbf' : '\x27',     # c-single quote
    '\xa8' : '',         # modifier - under curve
    '\xb1' : ''          # modifier - under line
}

def replace_chars(match):
    char = match.group(0)
    return chars[char]

def clean_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    # get rid of annoying characters
    return re.sub('(' + '|'.join(chars.keys()) + ')', replace_chars, text)

def get_title(html):
    return re.search(r'<title>Jókai Mór: (.*?)</title>', html).group(1)

# chech whether directory exists
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

def make_filename(title):
    filename = unicodedata.normalize('NFKD', title).encode('ASCII', 'ignore')
    fn = re.sub(r'&#150;', '-', str(filename)[2:-1])
    fn = re.sub('['+string.punctuation+']', '', fn)
    return re.sub(r' ', '_', fn).lower()


def download_jokai_novel(url):
    html = request.urlopen(url).read().decode('iso-8859-2')
    title = get_title(html)
    chapters = re.findall('<a href="(.*?)">', html)
    text = ''
    for link in chapters:
        chap = request.urlopen(url[:-9]+link).read().decode('iso-8859-2')
        text = text + clean_text(chap) + '\n'
    #return text
    filename = 'jokai/' + make_filename(title) + '.txt'
    ensure_dir(filename)
    with open(filename, 'w') as f:
        f.write(text)
    print(filename + ' was added to the Jokai corpus')


# download Jokai novels and save them as txt files

for link in novel_urls:
    url = root + link
    download_jokai_novel(url)