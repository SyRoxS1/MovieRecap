Site web hébergé à l'adresse https://movierecap.syroxs.online

Il prend en charge les listes stockées sur IMdB et Letterboxd :

Vous devez l'exporter :

Sur Letterboxd :

Commencez par aller dans les paramètres :

![image](https://github.com/SyRoxS1/MovieRecap/assets/114361806/db5d96a5-033d-4d92-bb04-57c988869aeb)

Ensuite, allez dans l'onglet des données et cliquez sur "Exporter vos données" :

![image](https://github.com/SyRoxS1/MovieRecap/assets/114361806/e5576604-6735-4fe4-9cb4-824b8442d4db)

Cela téléchargera un fichier zip, et celui à téléverser sur le site devrait être diary.csv :

![image](https://github.com/SyRoxS1/MovieRecap/assets/114361806/115ab216-af41-445a-b016-7e750987f759)

Pour IMDB maintenant :

Allez sur la liste où vous avez stocké vos films (mais pas en mode édition), puis faites défiler tout en bas et vous devriez voir le bouton "Exporter cette liste" en bas :

![image](https://github.com/SyRoxS1/MovieRecap/assets/114361806/27539e08-5f85-4ff0-87dc-de3474400d1c)

Cela téléchargera un fichier nommé WATCHLIST.csv que vous pouvez téléverser directement sur le site.

Notez que IMDB est beaucoup plus rapide car il stocke toutes les données des films à l'intérieur du fichier, tandis que pour Letterboxd, je dois récupérer les données via l'API que j'ai créée pour ce projet.

La majeure partie de la partie "intéressante" se trouve dans WebSiteClient.py, qui est la partie principale du programme. J'ai l'intention d'ajouter plus de statistiques et d'améliorer le design, mais j'ai déjà passé tellement de temps sur cela et je veux passer à autre chose.