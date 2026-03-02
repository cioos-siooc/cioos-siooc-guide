# Appendices

## Biodiversity Data and Definition of Terms  

This appendix is ​​intended to provide information on the DarwinCore format.  

The DarwinCore format structure is based on the principles of Event Cores, which are associated with Occurrence Extension tables and, where applicable, Extended Measurements (or Facts) derived from occurrences and events (Occurrence and Event EMoF). Unique identifiers (eventID, occurrenceID, measurementID) are used to link these tables.  

## Event Table (Event Core)  

* The Event Table is part of the Darwin Core data structure, contained in a separate spreadsheet (e.g., an .xlsx file), which contains information about collection or observation events associated with specimens or occurrences.
* This table allows us to document the contextual details surrounding the collection or observation of species, which is crucial for understanding, interpreting, and comparing biodiversity data.   

An Event Table therefore provides information about where and when specimen observations were made and where abiotic measurements were taken to characterize the environments where the observations took place. The essential variables that must be included include:  

- Date and time (at least the year);  
- Geographic coordinates;  
- Geographic coordinate reference system;  
- A brief description of the sampling protocol (a few words are sufficient).  

## Occurrence Table (Occurrence Extension)

* The occurrence table is another part of the Darwin Core data structure, also included in a separate spreadsheet, which allows you to indicate **which specimens** were observed and their abundance during different events;  
* It constitutes a kind of **inventory of the biodiversity** observed (or not observed) based on the events.  

The variables to include are:  

- The scientific name of the observed species;  
- The occurrence status;  
- The "BasisOfRecord".  

**Occurrence Table Structure**  

When biodiversity data is collected, such as for an inventory, it is required to create a spreadsheet specifically dedicated to marking observations, i.e., occurrences.   

![Structure minimale d’une structure d’archivage répondant aux normes du Darwin Core.](../assets/images/Structure_minimale_du_Darwin_Core.png)  
/// caption
Minimal structure of an archiving structure meeting Darwin Core standards.
///  

## Occurrence Measurements Table (EMoF Occurrence)  

* The occurrence measurements table is an extension file associated with the occurrences table;  
* It allows you to record specific measurements, such as length, weight, sex, etc., associated with individual species occurrences;  
* Each record in the occurrence measurements table is linked to a specific occurrence and contains information about the measurement taken, as well as other relevant metadata such as the measurement method, unit of measurement, etc.;  
* This table complements the occurrence data by providing additional quantitative or qualitative details about each specimen, allowing for more in-depth biodiversity analysis based on data collected in the field or in other collection contexts.  

In the figure below, there is a fourth table corresponding to the extended measurements taken on occurrences. However, this guide will not focus on this table. Physicochemical measurements taken during events (Event EMoF), such as water temperature, marine substrate qualification, water level, etc. can be integrated directly into the event table (Event Core).  

![Tableaux relationnels du Darwin Core.](../assets/images/Tableaux_relationels_du_Darwin_Core.png)  
/// caption
Darwin Core relational tables.
///

## Unique Identifiers   

First, it's important to note that **each line in a data file must have its own unique identifier**. There are different names for the variable that refers to the unique identifier. OBIS and Darwin Core define several types, but the ones this guide focuses on are:  

- EventID  
- OccurrenceID  
- MeasurementID  

**eventID**  

* The eventID refers to a specific **event**, such as an observation or a field collection;  
* This identifier is assigned to a set of occurrences that were collected simultaneously during the same field operation;  
* For example, during a quadrat inventory of herbaceous plants, each quadrat could have its own eventID. Each occurrence, each species observed in the same quadrat, would therefore share this eventID.  

**occurrenceID**  

* The occurrenceID is a unique identifier assigned to each occurrence;  
* It allows tracking and referencing **each distinct observation** made during an event;  
* For example, if ten specimens of the same species are observed during the same event, a row containing the required variables and the number of specimens observed (10) will be noted in the spreadsheet, and a unique occurrenceID will be assigned to this observation.  

**measurementID**  

* The measurementID is used to uniquely identify **each measurement or observation associated with an occurrence**.  
* It is typically used in the context of data associated with specific measurements, such as a specimen's length, weight, etc.  
* For example, if multiple measurements are taken on a specimen (such as length, width, etc.), each measurement could be individually identified by a unique measurementID.  

Essentially, when building an occurrence table from an event table, the goal is to use this structure to indicate which specimen observations were made during a particular event. The same principle applies to the measurement table for occurrences or events. Thus, each measurement is grouped into an occurrence and each occurrence into an event using identifiers.  

**How ​​to create a unique identifier:**  

First, you should know that each identifier must be globally unique, meaning it must not exist in any other database anywhere else in the world. The more information you add to the unique identifier, the closer you get to this theoretical goal of making it globally unique. To create a unique identifier for the event, you can use information already contained in the spreadsheet: the quadrat number, an abbreviation of the site name, the year the observation was made, etc. You can also add information such as the name of the organization that collected the data, as well as other specific information that could make the identifier truly unique. Subsequently, to create an occurrence identifier, you can simply add a code or abbreviation referring to the observed species. Using the same logic, you can then add an abbreviation of the measurement to create a measurement identifier.  

## Occurrence Status  

The **occurrenceStatus** variable refers to the presence or absence of an organism in a given location at a given time. This variable is used to describe whether a specimen or observation of a particular species was observed or collected in a specific location at a given time.  

There are only two possible values ​​that can be entered under the occurrenceStatus variable: ***present*** and ***absent***. The OGSL provides definitions for each value:  

* Present: When the occurrenceStatus is defined as "present," it means that the organism in question was observed or collected in the study area or at the specified location. Presence can be confirmed by direct detection of the organism itself or by indirect methods such as acoustic recordings or DNA traces.   
* Absent: When the occurrence status is defined as "absent," it indicates that the organism in question has not been observed or collected in the study area or at the specified location. This can mean that an exhaustive search was conducted and no trace of the organism was found, or that the organism is known to be absent from that specific geographic area or habitat.  

It is important to note that determining whether a species is absent can be influenced by a variety of factors, including data collection techniques, seasons, environmental conditions, and observer skill. Absence can essentially mean two distinct facts: (1) in a given place and time, the specimen was not observed, but it is not possible to say that it does not exist at that given location; or (2) the specimen is absent because it does not exist at that given location. These two interpretations can lead to completely different conclusions.  

Therefore, it is recommended to provide information on data collection methods and the reliability of observations when using the occurrenceStatus variable. Therefore, if you notice the absence of a specimen, also note the *absence*, as this information will be relevant to include in the metadata.  

The **samplingProtocol** variable, which must appear in the Event Core table, allows you to clarify the notion of absence, if applicable.  
## The Basis of Record

In the context of the Darwin Core standard, the ***basisOfRecord*** variable describes the origin of the observation. It provides information on how the data were obtained and the form in which they are stored.  

The possible values are standardized, meaning you must select one of the values defined by Darwin Core. We present here the 6 most frequently used values. The definitions we provide are intended to make it easier to determine which value to choose. Be sure to respect uppercase and lowercase characters!  

**HumanObservation:** Indicates that the data were collected through the direct observation of a human observer. For example, observations of animal behavior in nature, field surveys conducted by scientists or amateur naturalists, etc. This is the most commonly used term for field inventories, especially when species identification is carried out in the field.

**MachineObservation:** Indicates that the observation was made using a device, such as a passive bat detector (e.g., Anabat), a trail camera, or an autonomous recorder (e.g., an SM4). Even if a human performs the identification, the actual observation was made by the device.

**MaterialSample:** Applies to occurrences identified in a laboratory setting. A sample (e.g., sediment) is collected, stored in a container, likely preserved with ethanol, and the organisms within it are identified later in the lab. After identification, organisms may be stored long-term and added to a collection, or simply discarded.

**PreservedSpecimen, LivingSpecimen, and FossilSpecimen:** These three terms apply to organisms in a collection that are, respectively, preserved, living, or fossilized. **PreservedSpecimen** refers to data collected from a specimen stored in a museum, collection, or similar institution. Preserved specimens may include taxidermied animals, dried plant samples, DNA samples, organisms stored in ethanol, etc. **LivingSpecimen** refers to data collected from a living organism not in the wild, such as in an aquarium, zoo, or botanical garden. FossilSpecimen applies to fossil organisms.
If one of these last three terms is used, it is recommended to also include the columns **institutionCode**, **collectionCode**, and **catalogNumber** to identify, respectively: the institution that holds the collection, the collection identifier, and the specimen identifier within that collection.

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

<h4>The following table summarizes these terms and the contexts in which they may be used:</h4>
<div class="table-container">
  <table>
    <thead>
      <tr>
        <th></th>
        <th>HumanObservation</th>
        <th>MachineObservation</th>
        <th>MaterialSample</th>
        <th>PreservedSpecimen</th>
        <th>FossilSpecimen</th>
        <th>LivingSpecimen</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Direct observation</td>
        <td>yes</td>
        <td>no</td>
        <td>yes</td>
        <td>yes</td>
        <td>yes</td>
        <td>yes</td>
      </tr>
      <tr>
        <td>Indirect observation</td>
        <td>no</td>
        <td>yes</td>
        <td>no</td>
        <td>no</td>
        <td>no</td>
        <td>no</td>
      </tr>
      <tr>
        <td>Laboratory identification</td>
        <td>no</td>
        <td>yes</td>
        <td>yes</td>
        <td>yes</td>
        <td>yes</td>
        <td>yes or no</td>
      </tr>
	  <tr>
	    <td>Observation in nature</td>
        <td>yes</td>
        <td>yes</td>
        <td>yes</td>
        <td>no</td>
        <td>no</td>
        <td>no</td>
	  </tr>
      <tr>
        <td>Observation in captivity, in culture, in cultivation, etc</td>
        <td>no</td>
        <td>no</td>
        <td>no</td>
        <td>yes</td>
        <td>yes</td>
        <td>yes</td>
      </tr>		
	  <tr>
	    <td>Living organism</td>
        <td>yes or no</td>
        <td>yes</td>
        <td>no</td>
        <td>no</td>
        <td>no</td>
        <td>yes</td>
	  </tr>		
	  <tr>
	    <td>Possibility to confirm identification later</td>
        <td>no</td>
        <td>yes, as long as the images or recordings are preserved</td>
        <td>yes, if the specimens are not discarded</td>
        <td>no</td>
        <td>yes</td>
        <td>yes</td>
	  </tr>		
    </tbody>
  </table>
</div>

</body>
</html>

<div style="margin-left: 20px;">
<small>In Darwin Core, there is a variable (column) “vitality” which should not be confused with “LivingSpecimen”, a possible value of the “basisOfRecord” variable. “vitality” is used to indicate whether the organism was alive or not at the time of observation. If this variable is included, its value would be “alive|vivant” in the case of a basisOfRecord with the value “LivingSpecimen”, or “dead|mort” for PreservedSpecimen, FossilSpecimen, and MaterialSample. </small><br>
</div>  



## The Sampling Protocol  

The **samplingProtocol** variable must appear in the Event Core table. The Event Core table is used to record information about sampling or observation events, i.e., occasions when biological samples were collected or observations were made.  

![](../assets/images/SamplingProtocol.png)  

In this table, each row represents a distinct sampling or observation event. The samplingProtocol variable is used to record the specific protocol or method used during this event to collect biological samples or observe organisms.  

If multiple sampling protocols were applied during the same event, Darwin Core recommends separating values ​​using a space-pipe-space character (“ | “).  


Ex: Lobster trap | Modified lobster trap  

