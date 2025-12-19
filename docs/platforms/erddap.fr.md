# Serveur de données ERDDAP&trade;

ERDDAP est un serveur de données qui simplifie la recherche, le téléchargement et le sous-ensemble de jeux de données scientifiques via une API REST cohérente, conviviale pour les humains et les machines. Il prend en charge deux principaux types de jeux de données :

- **tabledap** : Données tabulaires (p. ex., séries temporelles, profils, trajectoires).
- **griddap** : Données grilles (p. ex., grilles régulières lat/lon/temps).

Avec ERDDAP, vous construisez une URL qui spécifie le jeu de données, les variables à retourner et les contraintes (fenêtres temporelles, boîtes spatiales, indicateurs de qualité, etc.). La même URL fonctionne dans un navigateur et dans des scripts.

## Anatomie de l’URL (tabledap)

Modèle général :

```
https://VOTRE-ERDDAP/erddap/tabledap/ID_JEU_DE_DONNEES.FORMAT?var1,var2&contrainte1&contrainte2
```

**Décomposition :**

- `https://VOTRE-ERDDAP/erddap/tabledap/` : L’URL de base pour les requêtes tabledap.
- `ID_JEU_DE_DONNEES` : L’identifiant unique du jeu de données à interroger (p. ex., `osd-1234`, `ctd_abc`).
- `FORMAT` : Le format de sortie souhaité (p. ex., `csv`, `json`, `nc`, `tsv`).
- `?var1,var2` : Liste de variables séparées par des virgules à récupérer (p. ex., `time,latitude,longitude,temperature`). Si aucune n’est fournie, ERDDAP peut retourner toutes les variables.
- `&contrainte1&contrainte2` : Contraintes optionnelles pour filtrer les données (p. ex., plage temporelle, limites spatiales, profondeur).

**Exemple :**

```
https://erddap.cioos.ca/erddap/tabledap/amundsen12713.csv?time,latitude,longitude,TEMP&time>=2023-01-01T00:00:00Z&time<=2023-01-31T23:59:59Z&latitude>=45&latitude<=50&longitude>=-130&longitude<=-120
```

**Contraintes courantes :**

- **Fenêtre temporelle :**
    - `time>=YYYY-MM-DDTHH:MM:SSZ`
    - `time<=YYYY-MM-DDTHH:MM:SSZ`
- **Boîte spatiale :**
    - `latitude>=latMin&latitude<=latMax`
    - `longitude>=lonMin&longitude<=lonMax`
- **Profondeur :**
    - `depth>=profondeurMin&depth<=profondeurMax`
- **Indicateurs de qualité ou autres variables :**
    - `qc_flag=1` (données valides)

**Conseils :**

- Les noms de variables et de contraintes sont sensibles aux majuscules et minuscules et doivent correspondre aux noms listés sur la page d’info du jeu de données.
- Vous pouvez demander autant ou aussi peu de variables que nécessaire, séparées par des virgules.
- Les contraintes sont reliées par `&` et peuvent être combinées.
- L’ordre des variables dans l’URL détermine l’ordre des colonnes dans le fichier de sortie.
- Si vous omettez les contraintes, vous pouvez récupérer le jeu de données entier (souvent très volumineux).
- Utilisez la page « Form » du jeu de données dans ERDDAP pour construire et tester les URL de manière interactive avant de les utiliser dans du code.

Pour plus de détails, consultez la [documentation tabledap d’ERDDAP](https://erddap.cioos.ca/erddap/tabledap/documentation.html).

## Exemples

ERDDAP permet d’accéder programmatique­ment à un jeu de données.

=== "Python"

    Utilise une URL directe (sans paquet supplémentaire) et retourne un `pandas` DataFrame.

    ```python
    import pandas as pd

    base = "https://VOTRE-ERDDAP/erddap"
    dataset_id = "ID_JEU_DE_DONNEES"  # p. ex., station, trajectoire, ou jeu CTD
    variables = ["time", "latitude", "longitude", "VARIABLE_NAME"]

    query = (
            f"{base}/tabledap/{dataset_id}.csv?" + ",".join(variables) +
            "&time>=2023-01-01T00:00:00Z"
            "&time<=2023-01-31T23:59:59Z"
            "&latitude>=45&latitude<=50"
            "&longitude>=-130&longitude<=-120"
    )

    # DataFrame avec votre sous-ensemble, ignorer la ligne des unités
    df = pd.read_csv(query, parse_dates=["time"], skiprows=[2])
    print(df.head())
    ```

=== "R rerddap"
    Utilisez `rerddap` (rOpenSci) pour construire des requêtes.

    ```r
    # install.packages("rerddap")
    library(rerddap)

    base <- "https://VOTRE-ERDDAP/erddap"
    dataset_id <- "ID_JEU_DE_DONNEES"

    res <- tabledap(
        datasetx = dataset_id,
        fields   = c("time", "latitude", "longitude", "VARIABLE_NAME"),
        url      = base,
        time >= "2023-01-01T00:00:00Z",
        time <= "2023-01-31T23:59:59Z",
        latitude >= 45, latitude <= 50,
        longitude >= -130, longitude <= -120
    )

    df <- as.data.frame(res)
    head(df)
    ```
=== "R base"
    Lire directement une URL CSV (sans paquet supplémentaire) :

    ```r
    library(readr)

    base <- "https://VOTRE-ERDDAP/erddap"
    dataset_id <- "ID_JEU_DE_DONNEES"
    vars <- c("time", "latitude", "longitude", "VARIABLE_NAME")
    url <- paste0(
        base, "/tabledap/", dataset_id, ".csv?", paste(vars, collapse = ","),
        "&time>=2023-01-01T00:00:00Z",
        "&time<=2023-01-31T23:59:59Z",
        "&latitude>=45&latitude<=50",
        "&longitude>=-130&longitude<=-120"
    )

    df <- read_csv(url, show_col_types = FALSE)
    head(df)
    ```

=== "Matlab"
    Utilisez `readtable` (R2019a+) ou `webread` pour ingérer du CSV.

    ```matlab
    base = "https://VOTRE-ERDDAP/erddap";
    dataset_id = "ID_JEU_DE_DONNEES"; % p. ex., jeu de séries temporelles avec lat/lon/temps
    vars = strjoin({"time","latitude","longitude","VARIABLE_NAME"}, ",");

    url = strcat(base, "/tabledap/", dataset_id, ".csv?", vars, ...
            "&time>=2023-01-01T00:00:00Z", ...
            "&time<=2023-01-31T23:59:59Z", ...
            "&latitude>=45&latitude<=50", ...
            "&longitude>=-130&longitude<=-120");

    opts = detectImportOptions(url, 'NumHeaderLines', 0);
    opts = setvaropts(opts, 'time', 'Type', 'datetime', 'InputFormat', 'yyyy-MM-dd''T''HH:mm:ssXXX');
    T = readtable(url, opts);
    head(T)
    ```


## Notes sur griddap (Données grilles)

Pour les jeux de données grilles, utilisez `griddap` et spécifiez un format (souvent NetCDF) :

https://VOTRE-ERDDAP/erddap/griddap/ID_JEU_DE_DONNEES.nc?VARIABLE_NAME[(time_start):(time_end)][(lat_min):(lat_max)][(lon_min):(lon_max)]

Beaucoup d’utilisateurs préfèrent NetCDF pour les réponses grilles, puis chargent le fichier avec des outils dédiés (p. ex., xarray en Python, ncdf4 en R, ou `ncread` de MATLAB).

## Conseils de dépannage

- Commencez petit : demandez un seul instant et un seul point pour vérifier les noms de variables.
- Utilisez la page « Form » du jeu de données pour prototyper les requêtes, puis copiez l’URL générée dans votre code.
- Consultez la page `info` du jeu de données pour les noms de variables, unités et plages valides.
- En cas d’erreurs HTTP 400/500, simplifiez les contraintes et vérifiez que le jeu de données contient bien la période/la zone demandée.
