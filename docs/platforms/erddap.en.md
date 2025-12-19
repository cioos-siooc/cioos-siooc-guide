# ERDDAP&trade; Server

ERDDAP is a data server that simplifies searching, downloading, and subsetting scientific datasets using a consistent, human- and machine-friendly REST API. It supports two main dataset types:

- **tabledap**: Tabular data (e.g., time-series, profiles, trajectories).
- **griddap**: Gridded data (e.g., regular lat/lon/time grids).

With ERDDAP, you construct a URL that specifies the dataset, variables to return, and constraints (time ranges, bounding boxes, quality flags, etc.). This same URL works in a browser and from scripts.

## URL Anatomy (tabledap)


General pattern:

```
https://YOUR-ERDDAP/erddap/tabledap/DATASET_ID.FORMAT?var1,var2&constraint1&constraint2
```

**Breakdown:**

- `https://YOUR-ERDDAP/erddap/tabledap/`: The base URL for tabledap requests.
- `DATASET_ID`: The unique identifier for the dataset you want to access (e.g., `osd-1234`, `ctd_abc`).
- `FORMAT`: The desired output file format (e.g., `csv`, `json`, `nc`, `tsv`).
- `?var1,var2`: Comma-separated list of variables to retrieve (e.g., `time,latitude,longitude,temperature`). If none is provided, ERDDAP will send all the variables.
- `&constraint1&constraint2`: Optional constraints to filter the data (e.g., time range, spatial bounds, depth).

**Example:**

```
https://erddap.cioos.ca/erddap/tabledap/amundsen12713.csv?time,latitude,longitude,TEMP&time>=2023-01-01T00:00:00Z&time<=2023-01-31T23:59:59Z&latitude>=45&latitude<=50&longitude>=-130&longitude<=-120
```

**Common constraints:**

- **Time window:**
    - `time>=YYYY-MM-DDTHH:MM:SSZ`
    - `time<=YYYY-MM-DDTHH:MM:SSZ`
- **Bounding box:**
    - `latitude>=minLat&latitude<=maxLat`
    - `longitude>=minLon&longitude<=maxLon`
- **Depth:**
    - `depth>=minDepth&depth<=maxDepth`
- **Quality flags or other variables:**
    - `qc_flag=1` (for good data)

**Tips:**

- Variable and constraint names are case-sensitive and must match those listed on the dataset’s info page.
- You can request as many or as few variables as you need, separated by commas.
- Constraints are joined with `&` and can be combined as needed.
- The order of variables in the URL determines their order in the output file.
- If you omit constraints, you may retrieve the entire dataset (which can be very large).
- Use the dataset’s “Form” page in ERDDAP to build and test URLs interactively before using them in code.

For more details, see the [ERDDAP tabledap documentation](https://erddap.cioos.ca/erddap/tabledap/documentation.html).

## Examples

ERDDAP allows the user to access programetically a dataset 

=== "Python"

    Uses a direct URL (no extra packages) and returns a `pandas` DataFrame.

    ```python
    import pandas as pd

    base = "https://YOUR-ERDDAP/erddap"
    dataset_id = "DATASET_ID"  # e.g., a station, trajectory, or CTD dataset
    variables = ["time", "latitude", "longitude", "VARIABLE_NAME"]

    query = (
            f"{base}/tabledap/{dataset_id}.csv?" + ",".join(variables) +
            "&time>=2023-01-01T00:00:00Z"
            "&time<=2023-01-31T23:59:59Z"
            "&latitude>=45&latitude<=50"
            "&longitude>=-130&longitude<=-120"
    )

    # DataFrame with your subset, skip units row
    df = pd.read_csv(query, parse_dates=["time"], skiprows=[2])  
    print(df.head())
    ```

=== "R rerddap"
    Use `rerddap` (rOpenSci) to build requests.

    ```r
    # install.packages("rerddap")
    library(rerddap)

    base <- "https://YOUR-ERDDAP/erddap"
    dataset_id <- "DATASET_ID"

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
    Read a CSV URL directly (no extra packages):

    ```r
    library(readr)

    base <- "https://YOUR-ERDDAP/erddap"
    dataset_id <- "DATASET_ID"
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
    Use `readtable` (R2019a+) or `webread` to ingest CSV.

    ```matlab
    base = "https://YOUR-ERDDAP/erddap";
    dataset_id = "DATASET_ID"; % e.g., a time-series dataset with lat/lon/time
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


## Notes on griddap (Gridded Data)

For gridded datasets, use `griddap` and specify a format (often NetCDF):

https://YOUR-ERDDAP/erddap/griddap/DATASET_ID.nc?VARIABLE_NAME[(time_start):(time_end)][(lat_min):(lat_max)][(lon_min):(lon_max)]

Many users prefer NetCDF for gridded responses and then load the file with domain tools (e.g., xarray in Python, ncdf4 in R, or MATLAB’s `ncread`).

## Troubleshooting Tips

- Start small: request a single time and a single point to verify variable names.
- Use the dataset “Form” page to prototype queries, then copy the generated URL into code.
- Check the dataset’s `info` page for variable names, units, and valid ranges.
- If you get HTTP 400/500 errors, simplify constraints and verify the dataset actually contains your requested time/area.
