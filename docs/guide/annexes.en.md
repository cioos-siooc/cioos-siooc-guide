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
Structure minimale d’une structure d’archivage répondant aux normes du Darwin Core.
///  

