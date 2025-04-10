# Dictionnaire

## Pourquoi un dictionnaire ?

Afin de faciliter la réutilisation et l'interopérabilité des données, il est important d'utiliser un vocabulaire commun pour désigner les différentes variables. Certains standards ont été conçus à cet effet tels que le vocabulaire de la [Convention CF](https://cfconventions.org/) pour les données océanographiques de physico-chimie, ou encore le vocabulaire issu du [Darwin Core](https://dwc.tdwg.org/list/) pour les données de biologie et de biodiversité. Ces vocabulaires contrôlés assignent à des termes uniques une variable précise. Ainsi par exemple, en dehors de tout standard, une simple variable _profondeur_ pourrait être interprétée de très nombreuses manières (figure ci-dessous). Dans la convention CF par contre, _depth_ sera spécifiquement défini par la "distance verticale sous la surface" et d'autres variables telles que *sea_floor_depth* désignera précisément la profondeur du fond marin depuis la surface de l'eau. 

![Exemple de profondeur](../assets/images/profondeur_standard.png)

Bien que l'utilisation dès le départ d'un vocabulaire contrôlé soit fortement recommandée, dans certains cas les termes associés aux différentes variables peuvent ne pas sembler intuitifs et ne sont pas forcément pratiques à utiliser sur le terrain ou au moment des analyses. Il est donc important de toujours construire et associer un dictionnaire de variables aux bases de données en elles-mêmes. Ce dictionnaire contiendra le plus de métadonnées possible associées à chaque variable de manière à maximiser les chances que les données soient interprétées correctement. Par exemple, pour des variables de *profondeurs* les informations du dictionnaire pourraient être :  
**profondeur_r**  
    - unité : *mètres*  
    - description : *profondeur depuis le fond marin de l'extrémité maximale à laquelle s'enfonce les racines des végétaux benthiques*  
    - méthode : *observation visuelle*  
**profondeur_b**  
    - unité : *mètres*  
    - description : *profondeur du fond marin depuis la surface de la *mer*  
    - méthode : *sonde de pression au niveau du fond marin dont les mesures sont converties en distance*  

> 💡 **Pas de panique :**  Les standards et les vocabulaires contrôlés évoluent au fur et à mesure que la recherche avance et que l'effort de diffusion des données s'intensifie. Ce domaine constitue en soi une discipline scientifique à part entière. Les scientifiques de données sont là pour effectuer et/ou raffiner le processus de standardisation de vos données. L'important est que toute l'information soit disponible pour comprendre ce que représente la donnée.  


## liste des variables et descriptions

## epsg (système de coordonnées de référence)

## instruments de récolte de données

## définition de la méthode