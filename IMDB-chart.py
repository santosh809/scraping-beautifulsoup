from bs4 import BeautifulSoup
import requests, openpyxl
# at i ma creating the excel sheel to load the data which has been scraped
excel = openpyxl.Workbook()
#print(excel.sheetnames)
sheet = excel.active
sheet.title = "Movies to watch"
#print(excel.sheetnames)
sheet.append(['Rank','Movie Name','Release Date','IMDB Ratig'])

try:
    source = requests.get("https://www.imdb.com/chart/top/")
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser') # we cam use xml parse as well
    #print(soup)
    movies = soup.find('tbody',class_= "lister-list").find_all('tr')
    #print(movies)
    #movies = soup.find_all('tr') #find_all is to find the all related tag in the particular web
    #print(len(movies)) # len is to know the perfect counting of the given data 
    for film in movies:
        name = film.find('td',class_="titleColumn").a.text
        #print(name) #it will print all the text content present inside the a tag 
        rank = film.find('td',class_="titleColumn").get_text(strip = True).split('.')[0] #split will split the given datafrom pointed point like . , etc return value n list
        #print(rank)
        relesedate = film.find('td',class_="titleColumn").span.text.strip('()')
        #print(relesedate)
        rating = film.find('td',class_="ratingColumn imdbRating").strong.text
        print(name)
        #print(rating)
        #print(rank,name,relesedate,rating)
        sheet.append([rank,name,relesedate,rating])
except Exception as e:
    print(e)

excel.save('top rated movies to watch.xlsx')