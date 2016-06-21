import mechanize # Importing external modules
import lxml.html

class Imdb_Crawler(object) : #classes

     def __init__(self) : # Functions
        self.cur_url = "http://www.imdb.com/chart/top?ref_=nv_wl_img_3"
        self.txtfile = "movie.txt"
        print "The program is ready to crawl the data of movies..."

     def find_title(self):
         b = mechanize.Browser()
         fd = b.open(self.cur_url)
         doc = lxml.html.fromstring(fd.read())

         self.Title = doc.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "titleColumn", " " ))]//a/text()') #list
         self.Year = doc.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "secondaryInfo", " " ))]//text()')
         self.IMDbRating = doc.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "ratingColumn imdbRating", " " ))]//strong/text()')
         self.list =[] # data structure list
         for x in  xrange(0, len(self.Title)):
             self.list.append(self.Title[x]) #List comprehension
             self.list.append(self.Year[x].strip("()"))
             self.list.append(self.IMDbRating[x])

     def writefile(self):
         with open(self.txtfile, "w+") as my_file : # File input and output
             my_file.write("Rank - Title - Year - Rating\n")
             for x in xrange(0, len(self.list),3):
                 my_file.write( str((x+1)/3 +1) + " - " + self.list[x].encode('utf8') + " - " + self.list[x+1].encode('utf8') + " -  " + self.list[x+2].encode('utf8') + "\n")


def main() :
     print ""
     my_crawler = Imdb_Crawler()
     my_crawler.find_title()
     my_crawler.writefile()
     print "Done..."

if __name__ == '__main__':
    main()