# Modèles de fichiers

## Standard Darwin Core

Le Darwin Core est le standard le plus utilisé pour la gestion et le partage des données de biodiversité. Il permet d'intégrer des observations d'espèces provenant de sources diverses, afin de les rendre découvrables et facilement accessibles. Sa structure repose sur une table principale des événements (event core), à laquelle peuvent s’ajouter des tables d’occurrences et de mesures. 

**Table des événements** *(event core)* : Contient les informations contextuelles liées à la collecte ou l’observation d'espèces : date, lieu de l'échantillonnage, position géographique, protocole utilisé, etc.

**Table des occurrences** *(occurrences core)* : Décrit les spécimens observés lors des événements : nom scientifique, nombre d’individus, la présence ou l'absence d'un taxon et toute autre remarque pertinente relative à l’observation.

**Table de mesures sur les occurrences** *(emof)* : Permet d’associer des mesures précises aux occurrences ou aux événements : longueur, poids, sexe, température, vitesse du vent, etc.

Ces définitions visent à vous familiariser avec le format Darwin Core. Pour plus de détails, veuillez consulter la section Annexes. L’application du format Darwin Core n’est pas obligatoire pour le partage de données avec l’OGSL.

> ⚠️ **À noter :** L’utilisation de ce standard n’est pas requise pour le partage de données avec nous. La structuration selon ce format est prise en charge par notre équipe. Les exemples visent simplement à illustrer les options possibles si vous souhaitez nous transmettre vos données déjà partiellement ou entièrement structurées en Darwin Core.

Des exemples de modèles, partiellement et entièrement conformes à cette structure, sont proposés à titre d’exemples. La section 1.1 présente une première approche du format, tandis que la section 1.2 montre un exemple complet.


### 1. Un premier pas vers la structure Darwin Core


<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <style>
    body {
      margin: 0;
      padding: 0;
    }
    .table-container {
      margin-bottom: 40px;    
    }
    table {
      border-collapse: collapse;
      width: max-content;
    }    
    th, td {
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

<h4>Table des événements (event)</h4>
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


<h4>Table des occurrences (occurrence)</h4>
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


<h4>Table mesures sur les occurrences (emof occurrence)</h4>
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


### 2. Structure Darwin Core


<h4>Table des événements (event)</h4>
<div class="table-container">
  <table>
    <thead>
      <tr>
        <th>datasetID</th>
        <th>eventID</th>
        <th>eventDate</th>
        <th>countryCode</th>
        <th>locality</th>
        <th>decimalLatitude</th>
        <th>decimalLongitude</th>
        <th>geodeticDatum</th>
        <th>samplingProtocol</th>
        <th>habitat</th>
        <th>eventRemarks</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>ZIPABC_PLAGE01_2024</td>
        <td>ZIPABC_PLAGE01_2024_ST20</td>
        <td>2024-07-10</td>
        <td>CA</td>
        <td>Baie Saint-Nicholas</td>
        <td>49.315746</td>
        <td>-67.791517</td>
        <td>WGS84 EPSG:4326</td>
        <td>Bourolle</td>
        <td>marais</td>
        <td>près de la route</td>
      </tr>
      <tr>
        <td>ZIPABC_PLAGE01_2024</td>
        <td>ZIPABC_PLAGE01_2024_ST21</td>
        <td>2024-07-10</td>
        <td>CA</td>
        <td>Baie Saint-Nicholas</td>
        <td>49.315817</td>
        <td>-67.791830</td>
        <td>WGS84 EPSG:4326</td>
        <td>Bourolle</td>
        <td>marais</td>
        <td>NA</td>
      </tr>
      <tr>
        <td>ZIPABC_PLAGE01_2024</td>
        <td>ZIPABC_PLAGE01_2024_ST22</td>
        <td>2024-07-10</td>
        <td>CA</td>
        <td>Baie Saint-Nicholas</td>
        <td>49.314590</td>
        <td>-67.791592</td>
        <td>WGS84 EPSG:4326</td>
        <td>Bourolle</td>
        <td>marais</td>
        <td>NA</td>
      </tr>
    </tbody>
  </table>
</div>

<h4>Table des occurrences (occurrence)</h4>
<div class="table-container">
  <table>
    <thead>
      <tr>
        <th>eventID</th>
        <th>occurrenceID</th>
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

<h4>Table de mesures sur les occurrences (emof occurrence)</h4>
<div class="table-container">
  <table>
    <thead>
      <tr>
        <th>eventID</th>
        <th>occurrenceID</th>
        <th>measurementID</th>
        <th>measurementType</th>
        <th>measurementValue</th>
        <th>measurementUnit</th>
        <th>measurementRemarks</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>ZIPABC_PLAGE01_2024_ST20</td><td>ZIPABC_PLAGE01_2024_ST20_Gmacro</td><td>ZIPABC_PLAGE01_2024_ST20_Gmacro_01_longueur</td><td>longueur_cm</td><td>20</td><td>cm</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST20</td><td>ZIPABC_PLAGE01_2024_ST20_Gmacro</td><td>ZIPABC_PLAGE01_2024_ST20_Gmacro_02_longueur</td><td>longueur_cm</td><td>19</td><td>cm</td><td>mort</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_01_longueur</td><td>longueur_cm</td><td>13</td><td>cm</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_02_longueur</td><td>longueur_cm</td><td>12</td><td>cm</td><td>a perdu une patte</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_03_longueur</td><td>longueur_cm</td><td>13</td><td>cm</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_04_longueur</td><td>longueur_cm</td><td>15</td><td>cm</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_05_longueur</td><td>longueur_cm</td><td>11</td><td>cm</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST22</td><td>ZIPABC_PLAGE01_2024_ST22_Crangon</td><td>ZIPABC_PLAGE01_2024_ST22_Crangon_01_longueur</td><td>longueur_cm</td><td>5</td><td>cm</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST20</td><td>ZIPABC_PLAGE01_2024_ST20_Gmacro</td><td>ZIPABC_PLAGE01_2024_ST20_Gmacro_01_masse</td><td>masse_g</td><td>75</td><td>g</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST20</td><td>ZIPABC_PLAGE01_2024_ST20_Gmacro</td><td>ZIPABC_PLAGE01_2024_ST20_Gmacro_02_masse</td><td>masse_g</td><td>182</td><td>g</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_01_masse</td><td>masse_g</td><td>70</td><td>g</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_02_masse</td><td>masse_g</td><td>64</td><td>g</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_03_masse</td><td>masse_g</td><td>140</td><td>g</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_04_masse</td><td>masse_g</td><td>115</td><td>g</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_05_masse</td><td>masse_g</td><td>90</td><td>g</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST22</td><td>ZIPABC_PLAGE01_2024_ST22_Crangon</td><td>ZIPABC_PLAGE01_2024_ST22_Crangon_01_masse</td><td>masse_g</td><td>3</td><td>g</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST20</td><td>ZIPABC_PLAGE01_2024_ST20_Gmacro</td><td>ZIPABC_PLAGE01_2024_ST20_Gmacro_01_sexe</td><td>sex</td><td>Femelle</td><td>NA</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST20</td><td>ZIPABC_PLAGE01_2024_ST20_Gmacro</td><td>ZIPABC_PLAGE01_2024_ST20_Gmacro_02_sexe</td><td>sex</td><td>Male</td><td>NA</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_01_sexe</td><td>sex</td><td>N/D</td><td>NA</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_02_sexe</td><td>sex</td><td>Male</td><td>NA</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_03_sexe</td><td>sex</td><td>Male</td><td>NA</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_04_sexe</td><td>sex</td><td>Femelle</td><td>NA</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_05_sexe</td><td>sex</td><td>Femelle</td><td>NA</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST22</td><td>ZIPABC_PLAGE01_2024_ST22_Crangon</td><td>ZIPABC_PLAGE01_2024_ST22_Crangon_01_sexe</td><td>sex</td><td>Male</td><td>NA</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST20</td><td>ZIPABC_PLAGE01_2024_ST20_Gmacro</td><td>ZIPABC_PLAGE01_2024_ST20_Gmacro_01_age</td><td>âge</td><td>Juvenile</td><td>NA</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST20</td><td>ZIPABC_PLAGE01_2024_ST20_Gmacro</td><td>ZIPABC_PLAGE01_2024_ST20_Gmacro_02_age</td><td>âge</td><td>Juvenile</td><td>NA</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_01_age</td><td>âge</td><td>N/D</td><td>NA</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_02_age</td><td>âge</td><td>Adulte</td><td>NA</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_03_age</td><td>âge</td><td>Juvenile</td><td>NA</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_04_age</td><td>âge</td><td>Adulte</td><td>NA</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST21</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus</td><td>ZIPABC_PLAGE01_2024_ST21_Cirroratus_05_age</td><td>âge</td><td>Adulte</td><td>NA</td><td>NA</td></tr>
      <tr><td>ZIPABC_PLAGE01_2024_ST22</td><td>ZIPABC_PLAGE01_2024_ST22_Crangon</td><td>ZIPABC_PLAGE01_2024_ST22_Crangon_01_age</td><td>âge</td><td>N/D</td><td>NA</td><td>NA</td></tr>
    </tbody>
  </table>
</div>
