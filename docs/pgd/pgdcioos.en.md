# CIOOS DMP

This template is intended for individual and government supported researchers, research organizations, institutions, NGOs and agencies within Canada that are interested in making ocean data more discoverable and accessible. The questions provided below are intended to help these data providers evaluate their research project data management practices, document expected research outputs, identify gaps, and assess whether data deposit and access through CIOOS RAs can benefit their data discovery and integration at a global level.   

This DMP (“Data and Research Output Management Plan”) is adopted from the [Portage Standard Template](https://dmp-pgd.ca/), and modified to address the requirements for data discovery and integration put forward by CIOOS. While data is considered a research output, these terms will be used interchangeably throughout the template. If the intention is to have your data be discoverable through CIOOS, it is strongly recommended to fill out this Data and Research Output Management Plan prior to starting your research project or publishing your data.  

Reach out to info@cioos.ca to learn more about CIOOS and get help working through this template and have your data be discoverable through CIOOS.   

## I. Project Outputs  

**Q1.** What data will you collect, and what research outputs will you create, derive, link to, acquire and/or record?   

**Q1. Guidance**   
Following the definition from DataCite, research outputs cover a wide range of resources produced throughout the research project, including for example: datasets, software, code, samples, theses, images, video, graphs, models, publications, etc.    

**Q2.** Do your research outputs contain Essential Ocean Variables (EOVs) or Essential Climate Variable (ECVs)?   
Oui/Non, si oui précisez

**Q2. Guidance**   
For ingestion into CIOOS, it is preferred that your research output contains at least one EOV. A list of the EOVs supported by CIOOS can be found [here](https://cioos.ca/essential-ocean-variables/). The Global Ocean Observing System (GOOS) Expert Panels have identified the EOVs based on their impact and feasibility, and a list of EOVs can be found [here](https://goosocean.org/what-we-do/framework/essential-ocean-variables/), and a list of ECV [here](https://gcos.wmo.int/site/global-climate-observing-system-gcos/essential-climate-variables).  
Please note that there is overlap between the EOVs and the ECVs, and both contain sub-variables and derived products as well in their specification sheets. 
  

**Q3.** What file formats will your research outputs be in? Will these formats allow for data re-use, sharing and long-term access to the data?    

**Q3. Guidance**   
File formats preferred for CIOOS are non-proprietary (open file) formats, e.g. .csv, .netCDF, tab-delimited, GeoTiff, .kmz, etc. Additional information on proprietary vs open file formats can be found from the [UBC library](https://ubc-library-rc.github.io/rdm/content/02_file_formats.html). 
Proprietary file formats requiring specialized software or hardware to use are not recommended, but may be necessary for certain data collection or analysis methods. 



## II. Documentation and Metadata    

**Q1.** What documentation will be needed for the research outputs to be read and interpreted correctly in the future? Describe how the documentation is captured or updated consistently throughout the active phase of the project.  

**Q1. Guidance**  
Good documentation includes referenced supplemental material and information about the study and other contextual information required to make the research outputs (re)usable by others. Development of a [README](https://ubc-library-rc.github.io/rdm/content/03_create_readme.html)/Codebook throughout the project lifecycle can include elements such as: description of data capture and collection methods (e.g. SOPs, lab procedures, instruments), processing steps, description of data granularity (e.g. taxa were identified to the lowest taxonomic rank practical, spatial resolution), variable definitions (e.g. through a data dictionary), units of measurement, assumptions and limitations to the study, and types of analyses performed (for each sample type).    
For documenting model data, please provide a description of the model planned and (references to) intended input data sources. If applicable and available, consider providing code, tools and/or links to existing publications describing the intended model.   

**Q2.** If you are using a data or metadata standard and/or tools to document and describe your data, please list here. 

**Q2. Guidance**  
For CIOOS, the most relevant schemas are [ISO-19115](https://www.iso.org/standard/53798.html) (metadata), [Climate and Forecast (CF) Conventions](https://cfconventions.org/) (often used for physical or biogeochemical oceanography data) and the [Darwin Core](https://dwc.tdwg.org/) standard (often used for marine biological occurrence data). Dataset documentation provided in one of these standard, machine-readable, openly-accessible formats enables effective exchange of information between users and systems. 

Dataset documentation may also include a controlled vocabulary, which is a standardized list of terminology for describing information. Examples of controlled vocabularies include the [NERC vocabulary](https://www.bodc.ac.uk/resources/products/web_services/vocab/) or [NASA’s Global Change Master Directory (GCMD) Keywords](https://www.earthdata.nasa.gov/earth-observation-data/find-data/idn/gcmd-keywords).  

**Q3.** What processes currently exist to continuously improve data quality (reviews, quality flags, testing, verification, etc) throughout and beyond the active phase of the project? Who has the executive responsibility for the quality of the data?  

**Q3. Guidance** 
Some common issues found with data are e.g. duplicates, missing values, spikes or outliers in the data, incorrect format type (character, numeric). Please describe the processes, feedback mechanisms, tools or software in place to identify these issues and continuously improve data quality throughout and beyond the active phase of your project (e.g. QARTOD, etc.). If applicable, please link to scripts used to clean the data.   

## III. Storage and Backup    

**Q1.** What are the anticipated storage requirements throughout the active phase of the project, in terms of storage space (in megabytes, gigabytes, terabytes, etc.) and the length of time you will be storing it?

**Q1. Guidance**  
Storage-space estimates should take into account requirements for file versioning, backups, and growth over time. If you are collecting data over a long period (e.g. several months or years), your data storage and backup strategy should accommodate data growth throughout the active project.   

**Q2.** How and where will your research outputs be stored and backed up during the active phase of the research project?  

**Q2. Guidance**  
The risk of losing data due to human error, natural disasters, or other mishaps should be considered, an option for mitigating this can include, but is not limited to, the 3-2-1 backup rule: 
- Have at least three copies of your data.  
- Store the copies on two different media.  
- Keep one backup copy offsite.  
  
Further information on storage and backup practice is available from the [Digital Research Alliance of Canada](https://docs.alliancecan.ca/wiki/Storage_and_file_management).  

**Q3.** What collaboration environment and procedures will the research team use to access, modify and contribute data or other research outputs throughout the active phase of the project? How will you organize, name and version-control files in a (shared) directory?    

**Q3. Guidance**  
An ideal collaborative environment is one that facilitates cooperation and ensures data security, yet is able to be adopted by project participants with minimal training. It is important to keep track of different copies or versions of files, files held in different formats or locations, and information cross-referenced between files. To facilitate tracking of file versions, it is strongly recommended to agree on a collaboration environment (e.g. Google Drive, GitHub, Sharepoint, etc.) to use throughout the active phase of the project, and to describe the hierarchies and naming conventions used when organizing and sharing data files. Logical file structures, informative file and folder naming conventions, clear indications of file versions, etc., all contribute to better use of your data during and after your research project.   
These practices will help ensure that you and your research team are using the appropriate version of your data, and minimize confusion regarding copies on different computers and/or on different media. For research outputs that are ongoing, please describe how new data is being added (e.g. to minimize duplication, reconciling delayed and real-time data). For examples and to read more about file naming and version control: [UBC Library](https://researchdata.library.ubc.ca/plan/organize-your-data/).  

Please contact info@cioos.ca to determine the best solution for your research project.    

## IV. Preservation  

**Q1.** Où et pendant combien de temps allez-vous déposer ou archiver vos données et matériels supplémentaires (c'est-à-dire les protocoles) pour leur préservation à long terme et leur accès à la fin de votre projet de recherche ?   

**Q1. Guidance**  
Data archiving or preservation is different from data storage. Archiving is the practice of moving data to a long-term data storage system (i.e. repository) where it can be located and retrieved as needed. This decision can be driven by external policies (e.g. funding agencies, journal publishers, etc.). Recommended repositories for CIOOS are the Ocean Biodiversity Information System (OBIS) for biological data, and ERDDAP for physical and geochemical oceanography data. Alternatively, data can be archived in public repositories such as as [Federated Research Data Repository](https://www.frdr-dfdr.ca/repo/?locale=en) (FRDR), [DRYAD Digital Repository](https://datadryad.org/), [Zenodo](https://zenodo.org/) and [Open Science Framework](https://osf.io/). An overview of research data repositories can be found at [Registry of research Data Repositories](https://www.re3data.org/)(re3data) website. 

For protocols, these can be archived on generalist repositories, or more specific repositories such as [protocols.io](https://www.protocols.io/), the [Ocean Best Practice system](https://www.oceanbestpractices.org/), or [Aquadocs](https://aquadocs.org/). Some CIOOS regional associations may also provide storage space. 

If you need assistance locating a suitable data repository or archive, please reach out to info@cioos.ca.    


## V. Sharing and Reuse  

**Q1.** What research outputs will be shared and in what form? (e.g. raw, processed, analyzed, and model).    

**Q1. Guidance** 
Raw data are the data directly obtained from the instrument, simulation or survey. Processed data result from some manipulation of the raw data in order to eliminate errors or outliers, to prepare the data for analysis, to derive new variables, or to de-identify the human participants. Analyzed data are the results of qualitative, statistical, or mathematical analysis of the processed data. They can be presented as graphs, charts or statistical tables. Model data are data products used to simulate real-world conditions to predict a future instance.  

Consider which data or other research outputs may need to be shared in order to meet institutional or funding requirements, and which may be restricted because of confidentiality/privacy/intellectual property considerations.  

**Q2.** Vos données et résultats de recherche peuvent-ils être partagés avec une licence ouverte ?   

**Q2. Guidance**  
For data sharing through CIOOS, it is recommended to apply an open license such as the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), open government licenses (e.g. [Open Government Licence - Canada](https://open.canada.ca/en/open-government-licence-canada)) or a public domain license (e.g. [CC0](https://creativecommons.org/public-domain/cc0/)). 
Licenses determine what uses can be made of your data. Funding agencies and/or data repositories may have end-user license requirements in place; if not, they may still be able to guide you in what license to attach. Note that only the intellectual property rights holder(s) can issue a license, so it is crucial to clarify who owns those rights (see Section VII).  

**Q3.** Quelles mesures seront prises pour aider la communauté de recherche à savoir que vos résultats de recherche existent ?

**Q3. Guidance** 
Describe how CIOOS helps meet funder requirements for openly accessible data, and is a community resource. Possibilities include: data registries, metadata catalogues, repositories, indexes, word of mouth, publications, social media. CIOOS recommends each data record to have a unique digital object identifier (DOI). CIOOS RAs can assist with minting of new DOIs, or link to existing DOIs. It is recommended that collaborators and affiliated organizations have persistent identifiers (e.g. ORCID and ROR).   

**_An example answer for funding agencies_**
CIOOS leverages persistent identifiers (PIDs) such as DOIs, Open Researcher and Contributor ID (ORCIDs), and Research Organization Registry ID (RORs) to allow for easy programmatic linkages between research outputs. CIOOS creates recommended data citations for each data record following the ISO 19115 and DataCite standards/best practices, ensuring adherence to the FAIR Principles. The metadata schema used in CIOOS facilitates machine-readability and allows for the harvesting of metadata records by other data/metadata catalogues and data access points, such as FRDR and Google Dataset Search. Finally, CIOOS provides additional value through the use of controlled vocabularies and media and social media coverage.  

## VI. Responsibilities and Resources  

**Q1.** Who will be responsible for managing this project's research outputs during and after the project? Please list the data management-specific tasks for which project contributors will be responsible.  

**Q1. Guidance**   
Your data and research output management plan has identified important data activities in your project. Identify who will be responsible (individuals or organizations) for carrying out these activities. This could also include the time frame associated with these staff responsibilities and any training needed to prepare staff for these duties.   

**Q2.** How will responsibilities for managing data activities be handled if substantive changes happen in the personnel overseeing the project's data, including a change of Principal Investigator?  

**Q2. Guidance** 
Indicate a succession strategy, or contingency plan, for these research outputs in the event that one or more people responsible for the management of the outputs leaves (e.g. a graduate student leaving after graduation, or a Principal Investigator leaving the project.  

**Q3.** What resources will you require to implement the management of your research outputs? What do you estimate the overall cost for this to be?  

**Q3. Guidance** 
This estimate should incorporate research outputs management costs incurred during the project as well as those required for the longer-term support for the data after the project is finished. Items to consider in the latter category of expenses include the costs of documenting, curating and providing long-term access to the data. Some funding agencies state explicitly the support that they will provide to meet the cost of preparing data for deposit. This might include technical aspects of data management, training requirements, file storage and backup, and contributions of non-project staff.    

## VII. Ethics and Legal Compliance  

_Note: This data and research output management plan template focuses on openly accessible data intended for public discovery and accessibility through CIOOS. As a result, it might not currently be applicable to all oceanographic data, such as sensitive/restricted data. To facilitate data discovery through CIOOS for these research outputs, data providers might want to either obfuscate data (through data generalization, anonymization, omittance, or de-identification), place an embargo on sensitive data, or consider developing a metadata-only record to allow for discovery._  

_If you need assistance understanding if (part of) your data is sensitive and requires restricted access, or creating a metadata-only record, please reach out to info@cioos.ca._

**Q1.** Who owns the intellectual property of the research outputs, and how will that person or institution manage legal, ethical, and intellectual property issues? 

**Q1. Guidances**
Include here a description concerning ownership, licensing, and intellectual property rights of the research outputs. Terms of reuse must be clearly stated, in line with the relevant legal and ethical requirements where applicable (e.g., subject consent, permissions, restrictions, etc.).   

Compliance with privacy legislation and laws that may impose content restrictions in the data should be discussed with your institution's privacy officer or research services office. Research Ethics Boards are central to the research process.  
  
**Q2.** Does your project include Indigenous partner involvement, and if so, does it follow the CARE and OCAP Principles?   

**Q2. Guidance**  
Consider how your research may impact or benefit local communities in the respective area. Any research involving Indigenous Partners necessitates education about Indigenous Data Sovereignty through the [CARE](https://www.gida-global.org/care) and [OCAP](https://fnigc.ca/ocap-training/) Principles. These resources will help non-Indigenous researchers begin to understand the requirements inherent in data collection in collaboration with Indigenous Partners, allowing them to proceed appropriately before, during, and after the project completion. In addition to these resources, the Indigenous community(ies) should be engaged in how to properly support their data sovereignty and CARE Principles.  

**Q3.** If your research project includes sensitive or restricted data, how will you ensure intellectual property rights are protected and that sensitive or restricted data is securely managed and accessible only to approved members of the project, during the active phase of the research?    

**Q3. Guidance** 
Consider where, how, and to whom sensitive data with acknowledged long-term value should be made available, and how long it should be archived. Cases may include, but are not limited to marine protected areas (MPAs), Indigenous Community data, endangered species, etc. Sensitive and restricted data considerations should be discussed with the appropriate parties (i.e., Indigenous community partners) and data managers, as well as align with funding requirements.  

Outline problems anticipated in sharing data, and possible measures to mitigate these. Problems may include confidentiality, lack of consent agreements, or concerns about Intellectual Property Rights, among others. In some instances, an embargo period may be justified; these may be defined by a funding agency's policy on research data.  

Restrictions can be imposed by limiting physical access to storage devices, by placing data on computers that do not have external network access (i.e. access to the Internet), through password protection, and by encrypting files. Sensitive data should never be shared via email or cloud storage services such as Dropbox.   

**Q3.** If applicable, what strategies will you undertake to address secondary uses of sensitive data?   

**Q3. Guidance**  
Obtaining the appropriate consent from research participants is an important step in assuring that the data may be shared with researchers outside your project. The consent statement (e.g. an MoU or Research Agreement) may identify certain conditions clarifying the uses of the data (both beyond and throughout the active phase of the project) by other researchers, or whether the data is only available upon request, and who will provide that access.   