[![en](https://img.shields.io/badge/lang-en-green.svg)](https://github.com/SyRoxS1/MovieRecap/blob/master/README.md)
[![fr](https://img.shields.io/badge/lang-fr-red.svg)](https://github.com/SyRoxS1/MovieRecap/blob/master/README.fr.md)

Website hosted at https://movierecap.syroxs.online

It supports list stored on IMdB and Letterboxd :

You need to export it :


On letterboxd :

First go to settings :

![image](https://github.com/SyRoxS1/MovieRecap/assets/114361806/db5d96a5-033d-4d92-bb04-57c988869aeb)



Then on the data tab and click export your data :

![image](https://github.com/SyRoxS1/MovieRecap/assets/114361806/e5576604-6735-4fe4-9cb4-824b8442d4db)

It will download a zip files and the one to upload to the site should be diary.csv :

![image](https://github.com/SyRoxS1/MovieRecap/assets/114361806/115ab216-af41-445a-b016-7e750987f759)



For IMdb now:

Go to the list you stored your movies (but not on editor mode) on then scroll all the way down and you should see the buttun export this list at the bottom :

![image](https://github.com/SyRoxS1/MovieRecap/assets/114361806/27539e08-5f85-4ff0-87dc-de3474400d1c)

It will download a file named WATCHLIST.csv wich you can directly upload to the site


Note that IMDB are much faster because they store all the movies data inside the file and for the letterboxd i have to retrive the data for my api I created for this project.


Most of the "interesting" part is in WebSiteClient.py wich is the main part of the program, I plan on adding more stats and improve the design but I've spent so much time on this and want to go do something else
