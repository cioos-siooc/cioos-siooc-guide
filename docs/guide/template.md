# Templates

## 1. Un premier pas vers la structure Darwin Core


<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
    }
    .table-container {
      overflow-x: auto;
      margin-bottom: 40px;    
    }
    table {
      border-collapse: collapse;
      width: max-content;
      min-width: 100%;
    }    
    th, td {
      border: 1px solid #999;
      padding: 6px 10px;
      text-align: center;
      white-space: nowrap;
    }
    thead {
      background-color: #f0f0f0;
    }    
  </style>
</head>
<body>

<h2>Table des événements (event)</h2>
<div class="table-container">
  <table>
    <thead>
      <tr>
        <th>datasetID</th>
        <th>eventID</th>
        <th>station</th>
        <th>eventDate</th>
        <th>countryCode</th>
        <th>locality</th>
        <th>decimalLatitude</th>
        <th>decimalLongitude</th>
        <th>geodeticDatum</th>
        <th>samplingProtocol</th>
        <th>habitat</th>
        <th>eventRemarks</th>
        <th>temperature_degree_C</th>
        <th>vitesse_du_vent_beaufort</th>
        <th>couverture_nuageuse_pourcent</th>
        <th>granulometrie</th>
        <th>precipitations_mm</th>
        <th>measurementRemarks</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>ZIPABC_PLAGE01_2024</td>
        <td>ZIPABC_PLAGE01_2024_ST20</td>
        <td>ST20</td>
        <td>2024-07-10</td>
        <td>CA</td>
        <td>Baie Saint-Nicholas</td>
        <td>49.31574587</td>
        <td>-67.7915172</td>
        <td>WGS84 EPSG:4326</td>
        <td>Bourolle</td>
        <td>marais</td>
        <td>près de la route</td>
        <td>28</td>
        <td>3</td>
        <td>20</td>
        <td>sable</td>
        <td>0</td>
        <td>NA</td>
      </tr>
      <tr>
        <td>ZIPABC_PLAGE01_2024</td>
        <td>ZIPABC_PLAGE01_2024_ST21</td>
        <td>ST21</td>
        <td>2024-07-10</td>
        <td>CA</td>
        <td>Baie Saint-Nicholas</td>
        <td>49.31581678</td>
        <td>-67.7918299</td>
        <td>WGS84 EPSG:4326</td>
        <td>Bourolle</td>
        <td>marais</td>
        <td>NA</td>
        <td>29</td>
        <td>2</td>
        <td>30</td>
        <td>limon</td>
        <td>0</td>
        <td>quelques bourrasques</td>
      </tr>
      <tr>
        <td>ZIPABC_PLAGE01_2024</td>
        <td>ZIPABC_PLAGE01_2024_ST22</td>
        <td>ST22</td>
        <td>2024-07-10</td>
        <td>CA</td>
        <td>Baie Saint-Nicholas</td>
        <td>49.3145898</td>
        <td>-67.7915917</td>
        <td>WGS84 EPSG:4326</td>
        <td>Bourolle</td>
        <td>marais</td>
        <td>NA</td>
        <td>35</td>
        <td>2</td>
        <td>80</td>
        <td>argile</td>
        <td>5</td>
        <td>NA</td>
      </tr>
    </tbody>
  </table>
</div>


<h2>Table des occurrences (occurrence)</h2>
<div class="table-container">
  <table>
    <thead>
      <tr>
        <th>eventID</th>
        <th>occurrenceID</th>
        <th>station</th>
        <th>eventDate</th>
        <th>decimalLatitude</th>
        <th>decimalLongitude</th>
        <th>kingdom</th>
        <th>taxonRank</th>
        <th>vernacularName</th>
        <th>scientificName</th>
        <th>scientificNameID</th>
        <th>organismQuantity</th>
        <th>organismQuantityType</th>
        <th>occurrenceStatus</th>
        <th>basisOfRecord</th>
        <th>occurrenceRemarks</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>ZIPABC_PLAGE01_2024_ST20</td>
        <td>ZIPABC_PLAGE01_2024_ST20_Gmacro</td>
        <td>ST20</td>
        <td>2024-07-10</td>
        <td>49.31574587</td>
        <td>-67.7915172</td>
        <td>Animalia</td>
        <td>species</td>
        <td>Morue du Groenland</td>
        <td>Gadus macrocephalus</td>
        <td>urn:lsid:marinespecies.org:taxname:254538</td>
        <td>2</td>
        <td>nombre d'individus</td>
        <td>present</td>
        <td>LivingSpecimen</td>
        <td>1 individu mort</td>
      </tr>
      <tr>
        <td>ZIPABC_PLAGE01_2024_ST21</td>
        <td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td>
        <td>ST21</td>
        <td>2024-07-10</td>
        <td>49.31581678</td>
        <td>-67.7918299</td>
        <td>Animalia</td>
        <td>species</td>
        <td>Crabe commun</td>
        <td>Cancer irroratus</td>
        <td>urn:lsid:marinespecies.org:taxname:158057</td>
        <td>5</td>
        <td>nombre d'individus</td>
        <td>present</td>
        <td>LivingSpecimen</td>
        <td>NA</td>
      </tr>
      <tr>
        <td>ZIPABC_PLAGE01_2024_ST22</td>
        <td>ZIPABC_PLAGE01_2024_ST22_Crangon</td>
        <td>ST22</td>
        <td>2024-07-10</td>
        <td>49.3145898</td>
        <td>-67.7915917</td>
        <td>Animalia</td>
        <td>genus</td>
        <td>Crangon sp.</td>
        <td>Crangon</td>
        <td>urn:lsid:marinespecies.org:taxname:107007</td>
        <td>1</td>
        <td>nombre d'individus</td>
        <td>present</td>
        <td>LivingSpecimen</td>
        <td>identification incertaine</td>
      </tr>
    </tbody>
  </table>
</div>


<h2>Table mesures sur les occurences (emof_occurence)</h2>
<div class="table-container">
  <table>
    <thead>
      <tr>
        <th>eventID</th>
        <th>occurrenceID</th>
        <th>measurementID</th>
        <th>station</th>
        <th>eventDate</th>
        <th>decimalLatitude</th>
        <th>decimalLongitude</th>
        <th>scientificName</th>
        <th>longueur_cm</th>
        <th>masse_g</th>
        <th>sexe</th>
        <th>age</th>
        <th>measurementRemarks</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>ZIPABC_PLAGE01_2024_ST20</td>
        <td>ZIPABC_PLAGE01_2024_ST20_Gmacro</td>
        <td>ZIPABC_PLAGE01_2024_ST20_Gmacro_01</td>
        <td>ST20</td>
        <td>2024-07-10</td>
        <td>49.31574587</td>
        <td>-67.7915172</td>
        <td>Gadus macrocephalus</td>
        <td>20</td>
        <td>75</td>
        <td>Femelle</td>
        <td>Juvénile</td>
        <td>NA</td>
      </tr>
      <tr>
        <td>ZIPABC_PLAGE01_2024_ST20</td>
        <td>ZIPABC_PLAGE01_2024_ST20_Gmacro</td>
        <td>ZIPABC_PLAGE01_2024_ST20_Gmacro_02</td>
        <td>ST20</td>
        <td>2024-07-10</td>
        <td>49.31574587</td>
        <td>-67.7915172</td>
        <td>Gadus macrocephalus</td>
        <td>19</td>
        <td>182</td>
        <td>Mâle</td>
        <td>Juvénile</td>
        <td>mort</td>
      </tr>
      <tr>
        <td>ZIPABC_PLAGE01_2024_ST21</td>
        <td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td>
        <td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_01</td>
        <td>ST21</td>
        <td>2024-07-10</td>
        <td>49.31581678</td>
        <td>-67.7918299</td>
        <td>Cancer irroratus</td>
        <td>13</td>
        <td>70</td>
        <td>N/D</td>
        <td>N/D</td>
        <td>NA</td>
      </tr>
      <tr>
        <td>ZIPABC_PLAGE01_2024_ST21</td>
        <td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td>
        <td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_02</td>
        <td>ST21</td>
        <td>2024-07-10</td>
        <td>49.31581678</td>
        <td>-67.7918299</td>
        <td>Cancer irroratus</td>
        <td>12</td>
        <td>64</td>
        <td>Mâle</td>
        <td>Adulte</td>
        <td>a perdu une patte</td>
      </tr>
      <tr>
        <td>ZIPABC_PLAGE01_2024_ST21</td>
        <td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td>
        <td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_03</td>
        <td>ST21</td>
        <td>2024-07-10</td>
        <td>49.31581678</td>
        <td>-67.7918299</td>
        <td>Cancer irroratus</td>
        <td>13</td>
        <td>140</td>
        <td>Mâle</td>
        <td>Juvénil</td>
        <td>NA</td>
      </tr>
      <tr>
        <td>ZIPABC_PLAGE01_2024_ST21</td>
        <td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td>
        <td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_04</td>
        <td>ST21</td>
        <td>2024-07-10</td>
        <td>49.31581678</td>
        <td>-67.7918299</td>
        <td>Cancer irroratus</td>
        <td>15</td>
        <td>115</td>
        <td>Femelle</td>
        <td>Adulte</td>
        <td>NA</td>
      </tr>
      <tr>
        <td>ZIPABC_PLAGE01_2024_ST21</td>
        <td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td>
        <td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_05</td>
        <td>ST21</td>
        <td>2024-07-10</td>
        <td>49.31581678</td>
        <td>-67.7918299</td>
        <td>Cancer irroratus</td>
        <td>11</td>
        <td>90</td>
        <td>Femelle</td>
        <td>Adulte</td>
        <td>NA</td>
      </tr>
      <tr>
        <td>ZIPABC_PLAGE01_2024_ST22</td>
        <td>ZIPABC_PLAGE01_2024_ST22_Crangon</td>
        <td>ZIPABC_PLAGE01_2024_ST22_Crangon_01</td>
        <td>ST22</td>
        <td>2024-07-10</td>
        <td>49.3145898</td>
        <td>-67.7915917</td>
        <td>Crangon</td>
        <td>5</td>
        <td>3</td>
        <td>Mâle</td>
        <td>N/D</td>
        <td>NA</td>
      </tr>
    </tbody>
  </table>
</div>

</body>
</html>
