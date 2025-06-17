# PGD du SIOOC

Ce modèle est destiné aux chercheur.es universitaires et gouvernementaux, aux organisations de recherche, aux institutions, aux ONG et aux agences au sein du Canada qui souhaitent rendre les données océaniques plus découvrables et accessibles. Les questions fournies ci-dessous sont destinées à aider les fournisseurs de données à évaluer leurs pratiques de gestion des données de recherche, documenter les résultats de recherche attendus, identifier les lacunes et évaluer si le dépôt et l'accès aux données via les AR du SIOOC peuvent bénéficier à la découverte et à l'intégration de leurs données à un niveau mondial. 
Ce PGD (« Plan de Gestion des Données et des Résultats de Recherche ») est adopté du [Modèle Standard de l’Assistant Portage](https://dmp-pgd.ca/), et modifié pour répondre aux exigences de découverte et d'intégration des données mises en avant par le SIOOC. Bien que les données soient considérées comme un résultat de recherche, ces termes seront utilisés de manière interchangeable tout au long du modèle. Si l'intention est de rendre vos données découvrables via le SIOOC, il est fortement recommandé de remplir ce Plan de Gestion des Données et des Résultats de Recherche avant de commencer votre projet de recherche ou de publier vos données.

Contactez info@cioos.ca pour en savoir plus sur le SIOOC, obtenir de l'aide pour compléter ce modèle et rendre vos données découvrables via le SIOOC.

## I. Résultats du projet  

**Q1.** Quels types de données allez-vous collecter, et quels résultats de recherche sera créés, dérivés, acquis et/ou enregistrés?   

**Q1. Directives**   
Selon la définition de DataCite, les résultats de projet de recherche couvre un large éventail de ressources produites tout au long du projet. Cela inclut par exemple: ensembles de données, logiciels, code, rapport, images, vidéos, graphiques, modèles, publication, etc.  

**Q2.** Est-ce que vos résultats de recherche inclus des variables essentielles océaniques (EOVs) ou des variables essentielles climatiques (ECVs) ?   
Oui/Non, si oui précisez

**Q2. Directives**   
Pour une intégration des données dans le SIOOC, il est préférable que les données contiennent au moins une EOV. Une liste des EOVs supportée par le SIOOC est disponible [ici](https://cioos.ca/fr/variables-oceaniques-essentielles/). Les groupes d’experts du GOOS (Global Ocean Observing System) ont définis et identifiés des EOVs basés sur leur impact et de leur faisabilité, la liste complète est disponible [ici](https://goosocean.org/what-we-do/framework/essential-ocean-variables/). Une liste des variables essentielles climatiques peut-être retrouvée [ici](https://gcos.wmo.int/site/global-climate-observing-system-gcos/essential-climate-variables).  
Veuillez noter qu'il existe un chevauchement entre les EOVs et les ECVs, et les deux contiennent également des sous-variables et des produits dérivés dans leurs fiches de spécifications.  

**Q3.** Quels formats de fichiers vos résultats de recherche auront-ils? Ces formats permettront-ils la réutilisation des données, le partage et l'accès à long terme aux données?  

**Q3. Directives**   
Les formats de fichiers recommandés pour le SIOOC sont des formats non propriétaires (format de fichiers ouverts), par exemple: .csv, .netCDF, GeoTiff, .kmz, etc. Des informations supplémentaires sur les formats de fichiers propriétaires par rapport aux formats de fichiers ouverts peuvent être trouvées sur la [bibliothèque de l’UBC](https://ubc-library-rc.github.io/rdm/content/02_file_formats.html). 
Les formats de fichiers propriétaires nécessitant des logiciels ou matériels spécialisés pour être utilisés ne sont pas recommandés, mais peuvent être nécessaires pour certaines méthodes de collecte ou d'analyse de données.


## II. Documentation et métadonnées  

**Q1.** Quelles documentations et métadonnées seront nécessaires pour que les résultats de la recherche puissent être lus et interprétés correctement à l'avenir ? Décrivez comment la documentation est saisie ou mise à jour de manière cohérente tout au long de la phase active du projet.  

**Q1. Directives**  
Une bonne documentation comprend du matériel supplémentaire référencé et des informations sur l'étude ainsi que d'autres informations contextuelles nécessaires pour rendre les résultats de recherche (ré)utilisables par d'autres. Le développement d'un fichier README/Codebook tout au long du cycle de vie du projet peut inclure des éléments tels que : description des méthodes de capture et de collecte des données (par exemple, procédures de laboratoire, instruments), étapes de traitement, description de la granularité des données (par exemple, les taxons ont été identifiés au rang taxonomique le plus bas possible, résolution spatiale), définitions des variables (par exemple, via un dictionnaire de données), unités de mesure, hypothèses et limitations de l'étude, et types d'analyses effectuées (pour chaque type d'échantillon).  
Pour la documentation des données de modèle, veuillez fournir une description du modèle prévu et (références à) des sources de données d'entrée prévues. Si applicable et disponible, envisagez de fournir le code, les outils et/ou des liens vers des publications existantes décrivant le modèle prévu.  

**Q2.** Si vous utilisez des normes pour la standardisation des données ou des métadonnées et/ou des outils pour documenter et décrire vos données, veuillez les énumérer ici.  

**Q2. Directives**  
Pour le SIOOC, les schémas les plus pertinents sont la [norme ISO-19115](https://www.iso.org/standard/53798.html) (métadonnées), les [Conventions sur le Climat et les Prévisions](https://cfconventions.org/) (CF) (pour les données océanographiques physiques ou biogéochimiques) et la [norme Darwin Core](https://dwc.tdwg.org/) (pour les données sur les occurrences biologiques marines). La documentation et les données fournie dans l'un de ces formats standard, lisibles par machine et librement accessibles, permet un échange efficace d'informations entre les utilisateurs et les systèmes.

La documentation peut également inclure un vocabulaire contrôlé, qui est une liste normalisée de terminologie pour décrire l'information. Des exemples de vocabulaires contrôlés incluent les [vocabulaires du NERC](https://www.bodc.ac.uk/resources/products/web_services/vocab/) ou les mots-clés du [Global Change Master Directory](https://www.earthdata.nasa.gov/earth-observation-data/find-data/idn/gcmd-keywords) (GCMD) de la NASA.  

**Q3.** Quelles sont les processus qui seront mis en place pour améliorer continuellement la qualité des données (révision, indicateurs de qualité, tests, vérifications, etc.) pendant et après la phase active du projet ? Qui a la responsabilité exécutive de la qualité des données ?  

**Q3. Directives** 
Parmi les erreurs les plus courantes, on trouve par exemple les doublons, les valeurs manquantes, les valeurs aberrantes dans les données, et le format incorrect (caractère, numérique). Veuillez décrire les processus, mécanismes de rétroaction, outils ou logiciels en place pour identifier ces problèmes et améliorer continuellement la qualité des données pendant et après la phase active de votre projet (par exemple, QARTOD, etc.). Le cas échéant, veuillez fournir des liens vers les scripts utilisés pour nettoyer les données.  

## III. Stockage et sauvegarde  





