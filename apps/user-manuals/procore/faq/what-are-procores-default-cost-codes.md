# What are Procore's default cost codes? - Procore

Source: https://support.procore.com/faq/what-are-procores-default-cost-codes

---

## Background

In Procore, a *cost code* defines the specific type of work being completed on a construction project. It is also one (1) of Procore's default segments in a [budget code](../references/construction-management/glossary-of-terms.md#Budget_Code "Glossary of Terms"). To learn more, see [What is a budget code in Procore's WBS?](https://support.procore.com/faq/what-is-a-budget-code-in-procores-wbs "What is a budget code in Procore's WBS?")

## Answer

One of the first steps as the [Procore Administrator](https://support.procore.com/procore-learning-paths/general-contractor/procore-administrator "Procore Administrator") for your company's Procore account is to define the cost code and cost type lists for your company's Work Breakdown Structure (WBS).

Choose one of these options:

- **Use the Cost Code Segment in Procore's Work Breakdown Structure** In Procore, the 'Cost Code' segment is available by default and aligns with the [MasterFormat](../references/construction-management/glossary-of-terms.md#MasterFormat "Glossary of Terms") from the [Construction Specifications Institute (CSI)](../references/construction-management/glossary-of-terms.md#Construction_Specifications_Institute "Glossary of Terms"). See [Default Cost Code List](#Default_Cost_Code_List "What are Procore's Default Cost Codes?") below. To learn more about segments, see:
 - [Create Your Company's Default Work Breakdown Structure](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-your-companys-default-work-breakdown-structure "Create Your Company's Default Work Breakdown Structure")
 - [Create Your Project's Work Breakdown Structure](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/create-your-projects-work-breakdown-structure "Create Your Project's Work Breakdown Structure")
- **Import Cost Codes Segment Items using the Procore Imports app** You can use the Procore Imports app to import segment items to the Company or Project level Admin tool. See [Procore Import Templates](https://support.procore.com/references/procore-import-templates "Procore Import Templates") and the links below for more information:
 - [Import Segment Items into your Company Level Admin Tool](https://support.procore.com/products/procore-imports/company-admin/tutorials/import-segment-items-into-your-company-level-admin-tool-procore-imports "Import Segment Items into your Company Level Admin Tool (Procore Imports)")
 - [Import Segment Items into your Project Level Admin Tool](https://support.procore.com/products/procore-imports/project-admin/tutorials/import-segment-items-into-your-project-level-admin-tool-with-procore-imports "Import Segment Items into your Project Level Admin Tool (Procore Imports)")

##### Note

If your company is using the ERP Integrations tool or Procore's ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14) [Resource Tracking](https://www.procore.com/field-productivity "https://www.procore.com/field-productivity") tools, see [Why can't I create WBS custom segments?](https://support.procore.com/faq/why-cant-i-create-wbs-custom-segments "Why can't I create WBS custom segments?")

### Default Cost Code Segment

The following table details the default 'Cost Code' segment in Procore, which is based on the 17 Division CSI MasterFormat. In the table below, the rows with a gray background denote the MasterFormat's divisions and the rows with the white background shows the individual cost code segment items within each of the MasterFormat's divisions.

##### Tips

**Why is there no 'Division' concept in Procore?** In Procore's WBS, the 'Cost Code' segment is a tiered segment and there is no concept of 'Divison'. Instead, a 'Division' is treated as a tier in a tiered segment. Tiers within a segment are always delimited by a dash (-).  Procore's default cost code list has two (2) tiers. However, your environment might have one, two, or multiple tiers. To learn more, see [Where is the 'Division' in the 'Cost Code' segment in Procore's WBS?](https://support.procore.com/faq/where-is-the-division-in-the-cost-code-segment-in-procores-wbs "Where is the 'Division' in the 'Cost Code' segment in Procore's WBS?")

**Can I get a copy of the default cost code list?** To download a copy of the default cost code names for your reference, click **[Procore\_Default\_Cost\_Codes.csv](https://support.procore.com/@api/deki/files/14617/Procore_Default_Cost_Codes.csv?revision=2 "Procore_Default_Cost_Codes.csv")**. 
*Note:* This CSV file is for reference only and not formatted for imports into Procore.

| Cost Code Number | Cost Code Description |
| --- | --- |
| Division 01- | General Requirements |
| 000 | Purpose |
| 002 | Instructions |
| 010 | Project Manager |
| 011 | Project Engineer |
| 012 | Superintendent |
| 013 | Project Coordinator |
| 014 | Project Executive |
| 500 | Temporary Facilities and Controls |
| 510 | Temporary Utilities |
| 511 | Temporary Electricity |
| 514 | Temporary Heating, Cooling, and Ventilation |
| 515 | Temporary Lighting |
| 517 | Temporary Telephone |
| 520 | Construction Facilities |
| 523 | Sanitary Facilities |
| 530 | Temporary Construction |
| 540 | Construction Aids |
| 542 | Construction Scaffolding and Platforms |
| 550 | Vehicular Access and Parking |
| 560 | Temporary Barriers and Enclosures |
| 570 | Temporary Controls |
| 580 | Project Identification |
| 600 | Product Requirements (Scope of Work) |
| 630 | Product Substitution Procedures |
| 640 | Owner Furnished Products |
| 700 | Execution Requirements |
| 712 | Local Conditions |
| 740 | Cleaning |
| 760 | Protecting Installed Construction |
| 903 | Hazardous Materials Abatement |
| 904 | Hazardous Materials Removal and Disposal |

| Division 02- | Site Construction |
| --- | --- |
| 000 | General |
| 200 | Site Preparation |
| 220 | Site Demolition |
| 230 | Site Clearing |
| 240 | Dewatering |
| 250 | Shoring and Underpinning |
| 260 | Excavation Support and Protection |
| 300 | Earthwork |
| 310 | Grading |
| 311 | Final Grading |
| 312 | Rough Grading |
| 315 | Excavation |
| 316 | Backfilling |
| 317 | Select Borrow |
| 320 | Excavation and Fill |
| 362 | Termite Control |
| 370 | Erosion and Sedimentation Control |
| 500 | Utility Services |
| 540 | Septic Tank |
| 621 | Foundation Drainage Piping |
| 625 | Retaining Wall Drainage Piping |
| 740 | Flexible Pavement Asphalt Pavement |
| 750 | Concrete Pads and Walks |
| 770 | Curb and Gutters |
| 780 | Clay Unit Pavers |
| 781 | Asphalt Pavers |
| 782 | Brick Pavers |
| 783 | Interlocking Concrete Unit Paving |
| 784 | Stone Unit Pavers |
| 790 | Athletic Surfacing |
| 795 | Porous Paving |
| 800 | Site Amenities |
| 812 | Drip Irrigation |
| 813 | Lawn Sprinkling and Irrigation |
| 815 | Fountains |
| 820 | Fences and Gates |
| 821 | Chain Link Fences |
| 822 | Ornamental Metal Fences and Gates |
| 823 | PVC Fences and Gates |
| 824 | Wire Fences and Gates |
| 825 | Wood Fences and Gates |
| 830 | Retaining Walls |
| 850 | Bridges/Footbridges |
| 870 | Sculpture/Ornamental |
| 900 | Landscaping |
| 915 | Mulch |
| 917 | Soil Preparation |
| 919 | Topsoil |
| 923 | Seeding and Soil Supplements |
| 924 | Sodding |
| 930 | Exterior Plants |
| 932 | Plants and Bulbs |
| 935 | Plant Maintenance |
| 936 | Fertilizer |

| Division 03- | Concrete |
| --- | --- |
| 000 | General |
| 050 | Concrete Subcontractor |
| 100 | Concrete Reinforcement |
| 210 | Cast-In-Place Concrete |
| 230 | Anchor Bolts |
| 300 | Footings |
| 310 | Expansion Joints |
| 320 | Slab Foundations |
| 330 | Poured Concrete Basement Walls |
| 350 | Concrete Finishing |
| 400 | Precast Concrete |
| 500 | Cementitious Decks and Underlayments |
| 600 | Grouts |

| Division 04- | Masonry |
| --- | --- |
| 050 | Basic Masonry Materials and Methods |
| 200 | Masonry Units |
| 400 | Stone |
| 500 | Refractories |
| 600 | Corrosion-Resistant Masonry |
| 700 | Simulated Masonry |
| 800 | Masonry Assemblies |
| 900 | Masonry Restoration and Cleaning |

| Division 05- | Metals |
| --- | --- |
| 050 | Basic Metal Materials and Method |
| 100 | Structural Metals |
| 200 | Metal Joists |
| 300 | Metal Deck |
| 400 | Cold-Formed Metal Framing |
| 500 | Metal Fabrications |
| 600 | Hydraulic Fabrications |
| 700 | Ornamental Metal |
| 800 | Erosion Control |
| 900 | Metal Restoration and Cleaning |

| Division 06- | Wood and Plastics |
| --- | --- |
| 050 | Basic Wood and Plastic Materials and Methods |
| 100 | Rough Carpentry |
| 200 | Finish Carpentry |
| 400 | Architectural Woodwork |
| 500 | Structural Plastics |
| 600 | Plastic Fabrications |
| 900 | Wood and Plastic Restoration and Cleaning |

| Division 07- | Thermal and Moisture Protection |
| --- | --- |
| 050 | Basic Thermal and Moisture Protection Materials and Methods |
| 100 | Damproofing and Waterproofing |
| 200 | Thermal Protection - Insulation |
| 300 | Shingles, Roof Tiles, and Roof Coverings |
| 400 | Roofing and Siding Panels |
| 500 | Membrane Roofing |
| 600 | Flashing and Sheet Metal |
| 700 | Roof Specialties and Accessories |
| 800 | Fire and Smoke Protection |
| 900 | Joint Sealers |

| Division 08- | Doors and Windows |
| --- | --- |
| 050 | Basic Door and Window Materials and Methods |
| 100 | Doors |
| 200 | Wood and Plastic Doors |
| 300 | Specialty Doors |
| 400 | Entrances and Storefronts |
| 500 | Windows |
| 600 | Skylights |
| 700 | Hardware |
| 800 | Glazing |
| 900 | Glazed Curtain Wall |

| Division 09- | Finishes |
| --- | --- |
| 050 | Basic Finish Materials and Methods |
| 100 | Metal Support Assemblies |
| 250 | Gypsum Wallboard |
| 300 | Tile |
| 400 | Terrazzo |
| 500 | Ceilings |
| 600 | Flooring |
| 680 | Carpet |
| 700 | Wall Finishes |
| 800 | Acoustical Treatment |
| 900 | Paints and Coatings |

| Division 10- | Specialties |
| --- | --- |
| 100 | Visual Display Boards |
| 150 | Compartments and Cubicles |
| 200 | Louvers and Vents |
| 240 | Grilles and Screens |
| 250 | Service Walls |
| 260 | Wall and Corner Guards |
| 270 | Access Flooring |
| 290 | Pest Control |
| 300 | Fireplaces and Stoves |
| 340 | Manufactured Exterior Specialties |
| 350 | Flagpoles |
| 400 | Identification Devices |
| 450 | Pedestrian Control Devices |
| 500 | Lockers |
| 520 | Fire Protection Specialties |
| 530 | Protective Covers |
| 550 | Postal Specialties |
| 600 | Partitions |
| 670 | Storage Shelving |
| 700 | Exterior Protection |
| 750 | Telephone Specialties |
| 800 | Toilet, Bath, and Laundry Specialties |
| 820 | Bathroom Accessories |
| 880 | Scales |
| 900 | Wardrobe and Closet Specialties |

| Division 11- | Equipment |
| --- | --- |
| 010 | Maintenance Equipment |
| 020 | Security and Vault Equipment |
| 030 | Teller and Service Equipment |
| 040 | Ecclesiastical Equipment |
| 050 | Library Equipment |
| 060 | Theater and Stage Equipment |
| 070 | Instrumental Equipment |
| 080 | Registration Equipment |
| 090 | Checkroom Equipment |
| 100 | Mercantile Equipment |
| 110 | Commercial Laundry and Dry Cleaning Equipment |
| 120 | Vending Equipment |
| 130 | Audio-Visual Equipment |
| 140 | Vehicle Service Equipment |
| 150 | Parking Control Equipment |
| 160 | Loading Dock Equipment |
| 170 | Solid Waste Handling Equipment |
| 190 | Detention Equipment |
| 200 | Water Supply and Treatment Equipment |
| 280 | Hydraulic Gates and Valves |
| 300 | Fluid Waste Treatment and Disposal Equipment |
| 400 | Food Service Equipment |
| 450 | Residential Equipment |
| 460 | Unit Kitchens |
| 470 | Darkroom Equipment |
| 480 | Athletic, Recreational, and Therapeutic Equipment |
| 500 | Industrial and Process Equipment |
| 600 | Laboratory Equipment |
| 650 | Planetarium Equipment |
| 660 | Observatory Equipment |
| 680 | Office Equipment |
| 700 | Medical Equipment |
| 850 | Navigation Equipment |
| 870 | Agricultural Equipment |
| 900 | Exhibit Equipment |

| Division 12- | Furnishing |
| --- | --- |
| 050 | Fabrics |
| 100 | Art |
| 300 | Manufactured Casework |
| 400 | Furnishing and Accessories |
| 500 | Furniture |
| 600 | Multiple Seating |
| 700 | Systems Furniture |
| 800 | Interior Plants and Planters |
| 900 | Furnishing Restoration and Repair |

| Division 13- | Special Construction |
| --- | --- |
| 010 | Air-Supported Structures |
| 020 | Building Modules |
| 030 | Special Purpose Rooms |
| 090 | Radiation Protection |
| 100 | Lightning Protection |
| 110 | Cathodic Protection |
| 120 | Pre-Engineered Structures |
| 150 | Swimming Pools |
| 160 | Aquariums |
| 165 | Aquatic Park Facilities |
| 170 | Tubs and Pools |
| 175 | Ice Rinks |
| 185 | Kennels and Animal Shelters |
| 190 | Site-Constructed Incinerators |
| 200 | Storage Tanks |
| 220 | Filter Underdrains and Media |
| 230 | Digester Covers and Appurtenances |
| 240 | Oxygenation Systems |
| 260 | Sludge Conditioning Systems |
| 280 | Hazardous Material Remediation |
| 400 | Measurement and Control Instrumentation |
| 500 | Recording Instrumentation |
| 550 | Transportatin Control Instrumentation |
| 600 | Solar and Wind Energy Equipment |
| 700 | Security Access and Surveillance |
| 800 | Building Automation and Control |
| 850 | Detection and Alarm |
| 900 | Fire Suppression |

| 14- | Conveying Systems |
| --- | --- |
| 100 | Dumbwaiters |
| 200 | Elevators |
| 300 | Escalators and Moving Walks |
| 400 | Lifts |
| 500 | Material Handling |
| 600 | Hoists and Cables |
| 700 | Turntables |
| 800 | Scaffolding |
| 900 | Transportation |

| 15- | Mechanical |
| --- | --- |
| 050 | Basic Mechanical Materials and Methods |
| 100 | Plumbing |
| 200 | Process Piping |
| 300 | Fire Protection Piping |
| 400 | Plumbing Fixtures and Equipment |
| 500 | Heat-Generation Equipment |
| 600 | Refrigeration Equipment |
| 700 | Heating, Venting, and Air Conditioning |
| 800 | Air Distribution |
| 900 | HVAC Instruments and Controls |
| 950 | Testing, Adjusting, and Balancing |

| 16 | Electrical |
| --- | --- |
| 050 | Basic Electrical Materials and Methods |
| 100 | Electrical |
| 200 | Electrical Power |
| 300 | Transmission and Distribution |
| 400 | Low-Voltage Distribution |
| 500 | Lighting |
| 700 | Communications |
| 800 | Sound and Video |

| 17- | Markup and Contingency |
| --- | --- |
| 010 | Contingency |
| 020 | Insurance |
| 030 | Bond |
| 040 | Profit |

## See Also

- [Add Company Cost Codes](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/add-company-cost-codes "Add Company Cost Codes")
- [Configure Cost Code Preferences for ERP Integrations](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/configure-cost-code-preferences-for-erp-integrations "Configure Cost Code Preferences for ERP Integrations")
- [What are Procore's default cost types?](https://support.procore.com/faq/what-are-procores-default-cost-types "What are Procore's default cost types?")

## 

If you would like to learn more about Procore's cost management software and how it can help your business, please visit our [construction cost management software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/construction-financials/cost-management "https://www.procore.com/construction-financials/cost-management").