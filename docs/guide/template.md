# Templates

## 1. Données structurées selon le standard Darwin Core


**Fichier des événements (event)** 

<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <style>
    table {
      white-space: nowrap;
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid black;
      padding: 4px 8px;
    }
  </style>
</head>
<body>
  <div style="overflow-x: auto;">
    <table>
      <thead>
        <tr>
          <th>datasetID</th>
          <th>datasetName</th>
          <th>ownerInstitutionCode</th>
          <th>basisOfRecord</th>
          <th>samplingProtocol</th>
          <th>samplingEffort</th>
          <th>datasetContact</th>
          <th>datasetContactEmail</th>
          <th>bibliographicCitation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>ZIPABC2024</td>
          <td>Suivi de la biodiversité dans le cadre du programme ZIP ABC</td>
          <td>Organisme de bassin versant ABC</td>
          <td>LivingSpecimen</td>
          <td>Échantillonnage à l’épuisette + tri sur le terrain</td>
          <td>3 stations sur une plage sableuse (1 jour)</td>
          <td>Jean Dupont</td>
          <td>jean.dupont@obvabc.org</td>
          <td>OBV ABC (2024). Suivi de la biodiversité sur la plage ABC. Données brutes de terrain - été 2024. https://www.obvabc.org/zipabc2024</td>
        </tr>
      </tbody>
    </table>
  </div>
</body>
</html>


**Fichier des occurences (occurence)**

<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <style>
    table {
      white-space: nowrap;
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid black;
      padding: 4px 8px;
    }
  </style>
</head>
<body>
  <div style="overflow-x: auto;">
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
</body>
</html>


**Fichier des mesures sur les occurences (emof_occurence)**

<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <style>
    table {
      white-space: nowrap;
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid black;
      padding: 4px 8px;
    }
  </style>
</head>
<body>
  <div style="overflow-x: auto;">
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
          <th>âge</th>
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
          <td>F</td>
          <td>J</td>
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
          <td>M</td>
          <td>J</td>
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
          <td>M</td>
          <td>A</td>
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
          <td>M</td>
          <td>J</td>
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
          <td>F</td>
          <td>A</td>
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
          <td>F</td>
          <td>A</td>
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
          <td>M</td>
          <td>N/D</td>
          <td>NA</td>
        </tr>
      </tbody>
    </table>
  </div>
</body>
</html>
