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
Pour le SIOOC, les schémas les plus pertinents sont la [norme ISO-19115](https://www.iso.org/standard/53798.html) (métadonnées), les [Conventions sur le Climat et les Prévisions](https://cfconventions.org/) (CF) (pour les données océanographiques physiques ou biogéochimiques) et le standard [Darwin Core](https://dwc.tdwg.org/) (pour les données sur les occurrences biologiques marines). La documentation et les données fournie dans l'un de ces formats standard, lisibles par machine et librement accessibles, permet un échange efficace d'informations entre les utilisateurs et les systèmes.

La documentation peut également inclure un vocabulaire contrôlé, qui est une liste normalisée de terminologie pour décrire l'information. Des exemples de vocabulaires contrôlés incluent les [vocabulaires du NERC](https://www.bodc.ac.uk/resources/products/web_services/vocab/) ou les mots-clés du [Global Change Master Directory](https://www.earthdata.nasa.gov/earth-observation-data/find-data/idn/gcmd-keywords) (GCMD) de la NASA.  

**Q3.** Quelles sont les processus qui seront mis en place pour améliorer continuellement la qualité des données (révision, indicateurs de qualité, tests, vérifications, etc.) pendant et après la phase active du projet ? Qui a la responsabilité exécutive de la qualité des données ?  

**Q3. Directives** 
Parmi les erreurs les plus courantes, on trouve par exemple les doublons, les valeurs manquantes, les valeurs aberrantes dans les données, et le format incorrect (caractère, numérique). Veuillez décrire les processus, mécanismes de rétroaction, outils ou logiciels en place pour identifier ces problèmes et améliorer continuellement la qualité des données pendant et après la phase active de votre projet (par exemple, QARTOD, etc.). Le cas échéant, veuillez fournir des liens vers les scripts utilisés pour nettoyer les données.  

## III. Stockage et sauvegarde  

**Q1.** Quels sont les besoins de stockage prévus tout au long de la phase active du projet, en terme d’espaces de stockage (en mégaoctets, téraoctets, etc.) et en terme de durée?

**Q1. Directives**  
Les estimations de stockage doivent prendre en compte les exigences de gestion des versions de fichiers, de sauvegarde et croissance au fil du temps. Si vous collectez des données sur une longue période (par exemple, plusieurs mois ou années), votre stratégie de stockage et de sauvegarde des données doit pouvoir s’adapter à l’augmentation du volume de données tout au long du projet actif.  

**Q2.** Comment et où vos données de recherche seront stockés et sauvegardés pendant la phase active du projet?

**Q2. Directives**  
Le risque de perte de données due à une erreur humaine, des catastrophes naturelles ou d'autres incidents doit être pris en compte. Une option pour atténuer ce risque peut inclure, mais ne se limite pas à, la règle de sauvegarde 3-2-1 :   
- Avoir au moins trois copies de vos données.   
- Stocker les copies sur deux supports différents.   
- Garder une copie de sauvegarde hors site.  

Des informations supplémentaires sur les bonnes pratiques de stockage et de sauvegarde sont disponibles auprès de [l'Alliance de recherche numérique du Canada](https://docs.alliancecan.ca/wiki/Storage_and_file_management/fr).  

**Q3.** De quelle manière l’équipe de recherche et les autres collaborateurs vont-ils accéder aux données, les modifier et y contribuer tout au long du projet? Comment organiserez-vous le nommage et les différentes versions des fichiers dans les dossiers (partagés)?  

**Q3. Directives**  
Un environnement de collaboration idéal facilite la coopération et assure la sécurité des données, tout en étant adoptable par les participants au projet avec une formation minimale. Il est important de suivre les différentes copies ou versions des fichiers, les fichiers détenus dans différents formats ou emplacements, et les informations croisées entre les fichiers. Pour faciliter le suivi des versions de fichiers, il est fortement recommandé de convenir d'un environnement de collaboration (par exemple, Google Drive, GitHub, Sharepoint, etc.) à utiliser tout au long de la phase active du projet, et de décrire les hiérarchies et les conventions de nommage utilisées lors de l'organisation et du partage des fichiers de données. Des structures de fichiers logiques, des conventions de nommage des fichiers, des indications claires des versions des fichiers, etc., contribuent toutes à une meilleure utilisation de vos données pendant et après votre projet de recherche. Ces pratiques aideront à garantir que vous et votre équipe de recherche utilisez la version appropriée de vos données et minimisent la confusion concernant les copies sur différents ordinateurs et/ou sur différents supports. Pour les résultats de recherche en cours, veuillez décrire comment les nouvelles données sont ajoutées (par exemple, pour minimiser les doublons, réconcilier les données différées et en temps réel). Pour des exemples et en savoir plus sur le nommage des fichiers et le contrôle des versions : [UBC Library](https://researchdata.library.ubc.ca/plan/organize-your-data/).  

Veuillez contacter info@cioos.ca pour déterminer la meilleure solution pour votre projet de recherche.  

## IV. Préservation  

**Q1.** Où et pendant combien de temps allez-vous déposer ou archiver vos données et matériels supplémentaires (c'est-à-dire les protocoles) pour leur préservation à long terme et leur accès à la fin de votre projet de recherche ?   

**Q1. Directives**  
L'archivage ou la préservation des données est différent du stockage des données. L'archivage consiste à déplacer les données vers un système de stockage de données à long terme (c'est-à-dire un dépôt) où elles peuvent être localisées et récupérées au besoin. Cette décision peut être motivée par des politiques externes (par exemple, agences de financement, éditeurs de revues, etc.). Les dépôts recommandés pour le SIOOC sont le Système d'Information sur la Biodiversité des Océans (OBIS) pour les données biologiques, et ERDDAP pour les données océanographiques physiques et géochimiques. Alternativement, les données peuvent être archivées dans des dépôts publics tels que le [Dépôt fédéré de données de recherche](https://www.frdr-dfdr.ca/repo/?locale=fr) (DFDR), [DRYAD Digital Repository](https://datadryad.org/), [Zenodo](https://zenodo.org/) et [Open Science Framework](https://osf.io/). Un aperçu des dépôts de données de recherche peut être trouvé sur le [Registry of research Data Repositories](https://www.re3data.org/)(re3data).  

Pour les protocoles, ceux-ci peuvent être archivés dans des dépôts généralistes ou des dépôts plus spécifiques tels que [protocols.io](https://www.protocols.io/), le  [Ocean Best Practice system](https://www.oceanbestpractices.org/) ou [Aquadocs](https://aquadocs.org/home?tl.page=1). Certaines associations régionales du SIOOC peuvent également fournir des espaces de stockage.  

Si vous avez besoin d'aide pour trouver un dépôt ou une archive de données approprié(e), veuillez contacter info@cioos.ca.   


## V. Partage et réutilisation  

**Q1.** Quelles données de recherche seront partagées et sous quelle forme? (ex: brut, traité, analysé, modèlisé)  

**Q1. Directives** 
Les données brutes sont les données obtenues directement de l'instrument, de la simulation ou de l’échantillonnage. Les données traitées résultent de certaines manipulations des données brutes pour éliminer les erreurs ou les valeurs aberrantes, préparer les données pour l'analyse, dériver de nouvelles variables ou désidentifier les participants humains. Les données analysées sont les résultats d'analyses qualitatives, statistiques ou mathématiques des données traitées. Elles peuvent être présentées sous forme de graphiques ou de tableaux statistiques. Les données de modèle sont des produits de données utilisés pour simuler des conditions réelles afin de prédire une instance future.   

Réfléchissez aux données ou autres résultats de recherche qui peuvent nécessiter d'être partagés pour répondre aux exigences institutionnelles ou de financement, et ceux qui peuvent être restreints en raison de considérations de confidentialité, de protection de la vie privée ou de propriété intellectuelle.  

**Q2.** Vos données et résultats de recherche peuvent-ils être partagés avec une licence ouverte ?   

**Q2. Directives**  
Pour le partage de données dans le SIOOC, il est recommandé d’appliquer une licence ouverte tel que la [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), licence ouverte du gouvernement (ex. [Open Government Licence - Canada](https://open.canada.ca/en/open-government-licence-canada)) ou une licence du domaine publique (ex: [CC0](https://creativecommons.org/public-domain/cc0/)). 
Les licences déterminent les utilisations qui peuvent être faites de vos données. Les agences de financement et/ou les dépôts de données peuvent avoir des exigences de licence pour les utilisateurs finaux ; sinon, ils peuvent toujours vous guider sur la licence à attribuer. Notez que seuls les détenteurs des droits de propriété intellectuelle peuvent émettre une licence, il est donc crucial de clarifier qui détient ces droits (voir Section VII).

**Q3.** Quelles mesures seront prises pour aider la communauté de recherche à savoir que vos résultats de recherche existent ?

**Q3. Directives** 
Décrivez comment le SIOOC aide à répondre aux exigences des financeurs en matière de données ouvertement accessibles, et comment il constitue une ressource communautaire. Les possibilités incluent : registres de données, catalogues de métadonnées, dépôts, index, bouche-à-oreille, publications, médias sociaux. Le SIOOC recommande à chaque enregistrement de données d'avoir un identifiant pérenne unique (DOI).  
Les associations régionales du SIOOC peuvent émettre de nouveaux DOIs ou faire la liaison avec des DOIs existants. Il est recommandé que les collaborateurs et les organisations affiliées disposent également d'identifiants persistants (par exemple, ORCID et ROR).  

**_Exemple de réponse pour les agences de financement :_**
Le SIOOC utilise des identifiants pérennes (PIDs) tels que les DOIs, les identifiants ORCID (Open Researcher and Contributor ID) et les identifiants ROR (Research Organization Registry) pour permettre des liaisons faciles entre les résultats de recherche. Le SIOOC crée des citations de données recommandées pour chaque enregistrement de données conformément aux normes/pratiques recommandées ISO 19115 et DataCite, assurant ainsi la conformité aux principes FAIR. Le schéma de métadonnées utilisé dans le SIOOC facilite la lisibilité par machine et permet le moissonnage des métadonnées par d'autres catalogues de données/métadonnées et points d'accès aux données, tels que DFDR et Google Dataset Search. Enfin, le SIOOC apporte une valeur ajoutée grâce à l'utilisation de vocabulaires contrôlés et à une couverture médiatique et sur les réseaux sociaux.

## VI. Responsabilité et ressources  

**Q1.** Qui sera responsable de la gestion des résultats de recherche de ce projet pendant et après celui-ci ? Veuillez énumérer les tâches spécifiques de gestion des données dont les contributeurs du projet seront responsables.  

**Q1. Directives**   
Votre plan de gestion des données et des résultats de recherche a identifié les activités importantes liées aux données dans votre projet. Identifiez les personnes responsables (individuelles ou organisations) de leur réalisation. Cela pourrait également inclure le calendrier associé à ces responsabilités et toute formation nécessaire pour préparer le personnel à ces tâches.  

**Q2.** Comment les responsabilités en matière de gestion des activités de données seront-elles gérées si des changements substantiels surviennent au sein du personnel supervisant les données du projet, y compris un changement de chercheur principal ? 

**Q2. Directives** 
Indiquez une stratégie de rechange, ou un plan d’urgence, pour ces résultats de recherche au cas où une ou plusieurs personnes responsables de la gestion des résultats partiraient (par exemple, un étudiant diplômé quittant après l’obtention de son diplôme ou un chercheur principal quittant le projet). 

**Q3.** De quelles ressources aurez-vous besoin pour mettre en œuvre la gestion de vos résultats de recherche ? Quel sera, selon vous, le coût global ?  

**Q3. Directives** 
Cette estimation doit intégrer les coûts de gestion des résultats de recherche engagés pendant le projet, ainsi que ceux nécessaires au soutien à long terme des données après la fin du projet. Parmi les éléments à prendre en compte dans cette dernière catégorie de dépenses figurent les coûts de documentation, de conservation et d'accès à long terme aux données. Certains organismes de financement précisent explicitement le soutien qu'ils fourniront pour couvrir les coûts de préparation des données en vue de leur dépôt. Cela peut inclure les aspects techniques de la gestion des données, les besoins en formation, le stockage et la sauvegarde des fichiers, ainsi que la contribution du personnel extérieur au projet.  

## VII. Éthique et conformité juridique

_Remarque : Ce modèle de plan de gestion des données et des résultats de recherche se concentre sur les données en libre accès destinées à la découverte et à l'accessibilité publique via le SIOOC. Par conséquent, il pourrait ne pas s'appliquer à toutes les données océanographiques, telles que les données sensibles ou à accès restreint. Afin de faciliter la découverte de données via le SIOOC pour ces résultats de recherche, les fournisseurs de données peuvent souhaiter masquer les données (par généralisation, anonymisation, omission ou dépersonnalisation), imposer un embargo sur les données sensibles ou envisager de créer un enregistrement de métadonnées uniquement pour permettre la découverte._

_Si vous avez besoin d'aide pour déterminer si vos données (ou une partie) sont sensibles et nécessitent un accès restreint, ou pour créer un enregistrement de métadonnées uniquement, veuillez contacter info@cioos.ca._

**Q1.** À qui appartient la propriété intellectuelle des résultats de la recherche et comment cette personne ou cette institution gérera-t-elle les questions juridiques, éthiques et de propriété intellectuelle ?  

**Q1. Directives**
Veuillez inclure ici une description des droits de propriété, de licence et de propriété intellectuelle des résultats de la recherche. Les conditions de réutilisation doivent être clairement énoncées, conformément aux exigences légales et éthiques applicables (par exemple, consentement du sujet, autorisations, restrictions, etc.).

Le respect de la législation sur la protection de la vie privée et des lois susceptibles d'imposer des restrictions de contenu des données doit être discuté avec le responsable de la protection de la vie privée ou le bureau des services de recherche de votre établissement. Les comités d'éthique de la recherche sont au cœur du processus de recherche.  

**Q2.** Votre projet inclut-il la participation de partenaires autochtones et, si oui, respecte-t-il les principes CARE et PCAP ?  

**Q2. Directives**  
Réfléchissez à l'impact ou aux avantages que votre recherche pourrait apporter aux communautés locales de la région concernée. Toute recherche impliquant des partenaires autochtones nécessite une sensibilisation à la souveraineté des données autochtones, conformément aux principes [CARE](https://www.gida-global.org/care) et [PCAP](https://fnigc.ca/fr/les-principes-de-pcap-des-premieres-nations/). Ces ressources aideront les chercheurs non autochtones à comprendre les exigences inhérentes à la collecte de données en collaboration avec des partenaires autochtones, leur permettant ainsi de procéder de manière appropriée avant, pendant et après la fin du projet. Outre ces ressources, les communautés autochtones devraient être sensibilisées à la manière de soutenir efficacement leur souveraineté des données et les principes CARE.  

**Q3.** Si votre projet de recherche comprend des données sensibles ou restreintes, comment garantirez-vous que les droits de propriété intellectuelle sont protégés et que les données sensibles ou restreintes sont gérées de manière sécurisée et accessibles uniquement aux membres approuvés du projet, pendant la phase active de la recherche ?  

**Q3. Directives** 
Déterminez où, comment et à qui les données sensibles ayant une valeur reconnue à long terme devraient être mises à disposition, ainsi que leur durée d'archivage. Les cas peuvent inclure, sans s'y limiter, les aires marines protégées (AMP), les données des communautés autochtones, les espèces menacées, etc. Les considérations relatives aux données sensibles et restreintes doivent être discutées avec les parties concernées (partenaires des communautés autochtones) et les gestionnaires de données, et être conformes aux exigences de financement.

Décrivez les problèmes anticipés liés au partage des données et les mesures envisageables pour les atténuer. Ces problèmes peuvent concerner, entre autres, la confidentialité, l'absence d'accords de consentement ou des préoccupations relatives aux droits de propriété intellectuelle. Dans certains cas, une période d'embargo peut être justifiée ; ces cas peuvent être définis par la politique de l'organisme de financement relative aux données de recherche.

Des restrictions peuvent être imposées en limitant l'accès physique aux périphériques de stockage, en stockant les données sur des ordinateurs sans accès réseau externe (c'est-à-dire à Internet), en les protégeant par mot de passe et en chiffrant les fichiers. Les données sensibles ne doivent jamais être partagées par e-mail ou via des services de stockage cloud comme Dropbox.  

**Q3.**  Le cas échéant, quelles stratégies mettrez-vous en œuvre pour faire face aux utilisations secondaires des données sensibles ?  

**Q3. Directives**  
L'obtention du consentement approprié des participants à la recherche est une étape importante pour garantir que les données puissent être partagées avec des chercheurs extérieurs à votre projet. La déclaration de consentement (par exemple, un protocole d'accord ou un accord de recherche) peut préciser certaines conditions clarifiant l'utilisation des données (au-delà et tout au long de la phase active du projet) par d'autres chercheurs, ou si les données ne sont accessibles que sur demande, et qui en fournira l'accès.





