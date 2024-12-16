from allmovies import readhhtml,gethtml

count = 2
for i in range(297):
    url = "https://letterboxd.com/annwilson50/list/all-movies/page/"+str(count)+"/"
    count += 1
    html = gethtml(url)
    data = readhhtml(html)
    print(count)
