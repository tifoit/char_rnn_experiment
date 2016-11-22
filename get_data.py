from bs4 import *
import urllib2

def page_parser(url):
    print "downloading %s now" % url
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page)
    paragraphs = soup.find_all('p')
    text = [p.getText() for p in paragraphs]
    return " ".join(text)


url_list = ["https://cran.r-project.org/doc/manuals/R-intro.html",
            "https://cran.r-project.org/doc/manuals/R-exts.html",
            "https://cran.r-project.org/doc/manuals/R-data.html",
            "https://cran.r-project.org/doc/manuals/R-lang.html",
            "https://cran.r-project.org/doc/manuals/R-admin.html",
            "http://adv-r.had.co.nz/Introduction.html",
            "http://adv-r.had.co.nz/Environments.html",
            "http://adv-r.had.co.nz/Functionals.html",
            "http://adv-r.had.co.nz/Performance.html",
            "http://adv-r.had.co.nz/memory.html",
            "http://adv-r.had.co.nz/Rcpp.html",
            "http://r-pkgs.had.co.nz/r.html"]
            
text = [page_parser(url) for url in url_list]
text = " ".join(text).encode('utf-8')

with open("input.txt", "w") as file:
file.write(text)
