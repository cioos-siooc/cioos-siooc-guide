# Sensitive Data

## What is sensitive data?

Sensitive data is any information that requires protection from unauthorized access, use, or disclosure because its release could cause harm to individuals, communities, institutions, or ecosystems. 
This need for protection may arise for legal, ethical, privacy, cultural, environmental, or intellectual-property reasons.
Although sensitive data is often associated with human-subject research, it is important to recognize that all disciplines produce sensitive data in different forms and at varying levels of risk. Sensitive data may involve social groups, organizations, wildlife, habitats, or proprietary technologies.

### Common categories of sensitive data:

* Biomedical data: Genetic, physiological, or health-related information from humans, animals, or plants. This can include laboratory measurements, tissue samples, or genetic sequences that could reveal sensitive traits or vulnerabilities.
* Personal data: identifying information linked to an individual, either directly or indirectly. Personal address and phone numbers, state identification number, economic, cultural, or social attributes.
* Confidential data: Information protected by intellectual property rights, trade secrets, internal organizational documents, or any material that could affect competitiveness or security. This may also include data linked to national security.
* Environmental data: Precise locations of endangered species, vulnerable habitats, archaeological sites, or other ecologically or culturally important areas. Exact sampling coordinates, detailed survey timelines, and specimen identification details can also fall into this category.

It is important to note that even when individual datasets appear non-sensitive, the combination of several datasets can create new risks. 
Linking different sources may allow re-identification of research participants or reveal the exact location of species or resources that should remain protected.

## Why be cautious about sharing data?

Sharing sensitive data without appropriate safeguards can create significant risks for individuals, communities, institutions, and ecosystems. 
These risks vary depending on the nature of the data, but they can be grouped into three categories:

* Individual risks, which include reputational harm, discrimination or stigmatization, and emotional or psychological distress. 
* Collective risks, which include endangerment of vulnerable species, habitats, or culturally significant sites and unwanted disclosure of ancestral, traditional, or community knowledge. 
* Institutional risks, which include legal or regulatory penalties for non-compliance, loss of funding or partnerships, and breaches of intellectual property or confidentiality agreements

These risks can also damage trust between researchers, institutions, partners, and the communities or ecosystems involved.
When sensitive data is mismanaged, it can undermine scientific integrity, strain collaborations, and reduce the willingness of participants or communities to engage in future research. For these reasons, it is essential to plan carefully how sensitive data will be collected, stored, processed, and shared, regardless of discipline or research context.

## Determining the level of sensitivity

The responsibility for determining the level of sensitivity lies with the data producer. 
This assessment should be guided by several key elements:

* The respect for any agreements, whether written or verbal, made with participants, communities, or data owners,
* Compliance with institutional policies, national regulations, and relevant legal frameworks,
* Ethical and moral considerations, protecting the privacy, safety and trust of the research participants and their communities, 
* Awareness that sensitivity can evolve over time; for example, once a scientific article is published, certain reputational risks may decrease, while other risks may persist or even increase depending on context.

![Data sensitivity matrix](../assets/images/sensitivitymatrix.png)  
/// caption
Adapted from the risk classification created by Calcul Québec.
///

## How to collect sensitive data

**Informed consent** should guide the collection of sensitive data. 
Consent may take the form of a signed agreement between the researcher and participants, but it can also be obtained through a clear and transparent conversation about how the information will be used. 
At this stage, it is also important to consider the potential for future reuse of the data and to agree with participants on the conditions under which such reuse is acceptable. 
What matters is that participants fully understand the purpose of the research, what data will be collected, how it will be managed, and what potential impacts or risks may arise.

## How to store sensitive data

Storing sensitive data securely is essential to preventing unauthorized access or loss. 
Good storage practices apply to all research data, but sensitive data requires an additional layer of protection to prevent any unwanted or unauthorized access: 

* Encryption: Encoding data so that only individuals with the appropriate decryption key can access it. This adds an important layer of protection, especially when transferring or storing data on shared systems.
* Secure storage locations: Using institutional servers or certified cloud services that meet recognized security standards. These environments typically include strong access controls, audit logs, and regular security updates.
* Access-control mechanisms: Restricting access to only those who need the data to carry out their work. This may involve password protection, multi-factor authentication, or assigning role-specific permissions.
This approach helps ensure that sensitive data remains protected even in the event of hardware failures, accidental deletion, or security breaches.

## How to analyze sensitive data

To reduce identification risks during analysis, researchers can apply different techniques depending on the nature of the data and the level of detail needed. 

* Aggregation: providing summary values rather than individual ones. This can include reporting averages instead of individual measurements, or grouping people into broader categories or communities. For example, grouping species by genus or using the average salary rather than individual one. 
* Generalization: Reducing the precision of certain variables. For example, replacing specific job titles with broader categories such as “manager,” or enlarging geographic areas instead of providing precise coordinates.
* Anonymization (irreversible): Removing all direct and indirect identifiers in a way that makes re-identification impossible. Once anonymized, the data cannot be traced back to its original source.
* Depersonalization (pseudonymization): Replacing identifiers with codes while keeping a secure, separate key that allows re-identification if necessary and ethically justified.

This approach protects privacy while still enabling follow-up analyses or validation when required.
When choosing a data transformation technique, it is important to preserve the variables that are relevant to the research question. For instance, if the goal is to compare environmental attitudes across age groups, it may be necessary to keep age categories while generalizing other details that are less relevant to the analysis and keep the identity of participants hidden.

### Biodiversity data

Several variables can be adjusted to reduce the sensitivity of biodiversity records, including:

* Dates, which can be generalized to the year level (while remaining ISO-compliant).
* Taxonomic identification, which can be reported at a higher rank (e.g., genus or family rather than species).
* Occurrence reporting, where records can be expressed as presence/absence instead of providing exact observation counts.

The precise localization of an observation can be sensitive, especially when it relates vulnerable or endangered species; there are many ways to obscure that information. 
For example, OBIS (Ocean Biodiversity Information System) uses WKT (Well-Known Text) polygons to spatially generalize or obscure sensitive data by defining a geographic area—rather than a precise point location—where a species occurrence is reported.
Instead of publishing exact coordinates the record is associated with a polygon representing a broader area such as a grid cell, protected zone, or custom boundary. 
The WKT format encodes this polygon geometry as a text string, allowing it to be stored, shared, and interpreted consistently across geospatial systems. 
By linking occurrence data to these polygons, OBIS preserves spatial context for ecological analysis while reducing the risk of revealing exact locations of sensitive biodiversity features.

## How to share sensitive data

To be shared publicly safely either through a scientific publication or as a dataset, sensitive data often needs to undergo modifications that reduce or eliminate the possibility of identifying individuals, communities, organisms, or precise locations. 

## Conclusion

Sensitive data must be handled with care at every stage of the research project, from collection to analysis, storage, and sharing. When managed responsibly, these data can also open the door to new insights and research directions. Handling sensitive data correctly requires:

* Assessing risk,
* Applying secure storage and processing methods,
* Using ethical judgment,
* Monitoring data before publication,
* And adapting protection measures over time.

