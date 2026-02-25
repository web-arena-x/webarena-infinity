# Analytics - Data Change Log

Source: https://v2.support.procore.com/product-manuals/analytics-company/reference-data-change-log

---

Below are the notable changes to the Procore data and intelligence layer accessible via the Analytics 2.0 Cloud Connector.

#### Recent Changes

##### Analytics 2.0 Data Updates (02/17/2026)

**Procore added the following models (tables):**

**Show/Hide**

- contacts:

 - Added job\_title
- project\_contacts:

 - Added job\_title
- projects:

 - Added store\_number
- commitments:

 - Added invoice\_contacts\_list
- payments\_manual\_holds:

 - Added vendor\_id
- daily\_log\_accident:

 - Added location\_id
 - Added vendor\_id
- daily\_log\_construction\_reports:

 - Added location\_id
- daily\_log\_delay:

 - Added vendor\_id
 - Added vendor\_name
- daily\_log\_delivery:

 - Added location\_id
 - Added vendor\_id
 - Added vendor\_name
- daily\_log\_dumpster:

 - Added location\_id
- daily\_log\_equipment:

 - Added vendor\_id
 - Added vendor\_name
- daily\_log\_inspection:

 - Added vendor\_id
 - Added vendor\_name
- daily\_log\_note:

 - Added vendor\_id
 - Added vendor\_name
- daily\_log\_observed\_weather\_condition:

 - Added location\_id
 - Added vendor\_id
 - Added vendor\_name
- daily\_log\_phone\_call:

 - Added location\_id
 - Added vendor\_id
 - Added vendor\_name
- daily\_log\_plan\_revision:

 - Added location\_id
 - Added vendor\_id
 - Added vendor\_name
- daily\_log\_productivity:

 - Added location\_id
- daily\_log\_quantity:

 - Added vendor\_id
 - Added vendor\_name
- daily\_log\_safety\_violation:

 - Added location\_id
 - Added vendor\_id
- daily\_log\_scheduled\_work:

 - Added location\_id
 - Added vendor\_id
 - Added vendor\_name
- daily\_log\_visitor:

 - Added location\_id
 - Added vendor\_id
 - Added vendor\_name
- daily\_log\_waste:

 - Added location\_id
- scheduling\_activity:

 - Added audit\_transaction\_timestamp
 - Added calendar\_id
 - Added calendar\_name
 - Added category\_data
 - Added company\_id
 - Added constraint\_date
 - Added constraint\_type
 - Added created\_at
 - Added created\_by
 - Added deadline\_date
 - Added deadline\_variance
 - Added duration
 - Added duration\_display\_unit
 - Added duration\_unit
 - Added finish\_date
 - Added is\_actual\_finish
 - Added is\_actual\_start
 - Added is\_critical
 - Added is\_placeholder
 - Added note
 - Added sibling\_position
 - Added parent\_id
 - Added percent\_done
 - Added project\_id
 - Added resource\_data
 - Added crew\_size
 - Added schedule\_activity\_id
 - Added schedule\_id
 - Added start\_date
 - Added activity\_name
 - Added total\_float
 - Added updated\_at
 - Added vendor\_id
 - Added vendor\_name
- scheduling\_activity\_custom\_fields:

 - Added activity\_category\_assignment\_id
 - Added alias\_project\_custom\_field\_id
 - Added company\_id
 - Added custom\_field\_data\_type
 - Added custom\_field\_definitions\_id
 - Added custom\_field\_name
 - Added custom\_field\_value
 - Added custom\_field\_value\_id
 - Added project\_id
 - Added schedule\_activity\_id
 - Added schedule\_id
 - Added scheduling\_activity\_custom\_field\_id
- scheduling\_relationship:

 - Added audit\_transaction\_timestamp
 - Added company\_id
 - Added created\_at
 - Added created\_by
 - Added dependency\_type
 - Added from\_activity
 - Added is\_active
 - Added lag
 - Added lag\_display\_unit
 - Added project\_id
 - Added schedule\_id
 - Added schedule\_relationship\_id
 - Added to\_activity
 - Added updated\_at
- scheduling\_type:

 - Added audit\_transaction\_timestamp
 - Added calendar\_id
 - Added company\_id
 - Added created\_at
 - Added created\_by
 - Added imported\_data\_date
 - Added is\_active
 - Added name
 - Added parent\_schedule\_id
 - Added project\_id
 - Added schedule\_id
 - Added start\_date
 - Added type
 - Added updated\_at
- employees:

 - Added contact\_id
- labor\_allocations:

 - Added audit\_transaction\_timestamp
 - Added created\_by
- scheduling\_activity:

 - Added display\_id
- budget\_view\_standard\_columns:

 - Added original\_budget\_amount\_project\_currency
 - Added original\_budget\_amount\_company\_currency
 - Added budget\_modifications\_project\_currency
 - Added budget\_modifications\_company\_currency
 - Added forecast\_to\_complete\_automatic\_sum\_project\_currency
 - Added forecast\_to\_complete\_automatic\_sum\_company\_currency
 - Added forecast\_to\_complete\_manual\_sum\_project\_currency
 - Added forecast\_to\_complete\_manual\_sum\_company\_currency
 - Added forecast\_to\_complete\_aggregate\_sum\_project\_currency
 - Added forecast\_to\_complete\_aggregate\_sum\_company\_currency
 - Added approved\_co\_amount\_sum\_project\_currency
 - Added approved\_co\_amount\_sum\_company\_currency
 - Added approved\_budget\_changes\_amount\_sum\_project\_currency
 - Added approved\_budget\_changes\_amount\_sum\_company\_currency
 - Added committed\_costs\_sum\_project\_currency
 - Added committed\_costs\_sum\_company\_currency
 - Added direct\_cost\_total\_amount\_sum\_project\_currency
 - Added direct\_cost\_total\_amount\_sum\_company\_currency
 - Added pending\_cost\_changes\_sum\_project\_currency
 - Added pending\_cost\_changes\_sum\_company\_currency
 - Added subcontractor\_invoice\_sum\_project\_currency
 - Added subcontractor\_invoice\_sum\_company\_currency
 - Added projected\_costs\_sum\_project\_currency
 - Added projected\_costs\_sum\_company\_currency
 - Added estimated\_cost\_at\_completion\_project\_currency
 - Added estimated\_cost\_at\_completion\_company\_currency
 - Added job\_to\_date\_costs\_sum\_project\_currency
 - Added job\_to\_date\_costs\_sum\_company\_currency
 - Added pending\_co\_sum\_project\_currency
 - Added pending\_co\_sum\_company\_currency
 - Added revised\_budget\_sum\_project\_currency
 - Added revised\_budget\_sum\_company\_currency
 - Added projected\_budget\_sum\_project\_currency
 - Added projected\_budget\_sum\_company\_currency
 - Added projected\_over\_under\_sum\_project\_currency
 - Added projected\_over\_under\_sum\_company\_currency

**Procore removed** **the following models (tables):**

**Show/Hide**

- contract
- Estimates:

 - Removed other\_adjustment1
 - Removed other\_adjustment1\_amount
 - Removed other\_adjustment1\_name
 - Removed other\_adjustment1\_percentage
 - Removed other\_adjustment2
 - Removed other\_adjustment2\_amount
 - Removed other\_adjustment2\_name
 - Removed other\_adjustment2\_percentage
 - Removed other\_adjustment3
 - Removed other\_adjustment3\_amount
 - Removed other\_adjustment3\_name
 - Removed other\_adjustment3\_percentage
 - Removed other\_adjustment4
 - Removed other\_adjustment4\_amount
 - Removed other\_adjustment4\_name
 - Removed other\_adjustment4\_percentage
- field\_productivity:

 - Removed is\_budgeted
- requests:

 - Removed job\_title\_id\_2

**Procore updated the data type for the following models (tables):**

**Show/Hide**

- incident\_record\_custom\_fields:

 - Changed custom\_field\_definitions\_id from bigint to string
- incident\_record\_custom\_field\_configs:

 - Changed custom\_field\_definition\_id from bigint to string
- budget\_change\_adjustment\_line\_items:

 - Changed unit\_cost\_project\_currency from decimal(23,4) to decimal(38,5)
 - Changed unit\_cost\_company\_currency from decimal(30,4) to decimal(38,5)
 - Changed amount\_project\_currency from decimal(21,2) to decimal(38,5)
 - Changed amount\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed budget\_changes\_approved\_amount\_project\_currency from decimal(21,2) to decimal(38,5)
 - Changed budget\_changes\_approved\_amount\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed budget\_changes\_under\_review\_amount\_project\_currency from decimal(21,2) to decimal(38,5)
 - Changed budget\_changes\_under\_review\_amount\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed budget\_changes\_draft\_amount\_project\_currency from decimal(21,2) to decimal(38,5)
 - Changed budget\_changes\_draft\_amount\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed changes\_to\_budgeted\_amount\_project\_currency from decimal(21,2) to decimal(38,5)
 - Changed changes\_to\_budgeted\_amount\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed pending\_changes\_to\_budgeted\_amount\_project\_currency from decimal(21,2) to decimal(38,5)
 - Changed pending\_changes\_to\_budgeted\_amount\_company\_currency from decimal(28,2) to decimal(38,5)
- budget\_forecast\_line\_items:

 - Changed amount\_project\_currency from decimal(21,2) to decimal(38,5)
 - Changed amount\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed unit\_cost\_project\_currency from decimal(21,2) to decimal(38,5)
 - Changed unit\_cost\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed forecast\_to\_complete\_project\_currency from decimal(21,2) to decimal(38,5)
 - Changed forecast\_to\_complete\_company\_currency from decimal(28,2) to decimal(38,5)
- budget\_line\_items:

 - Changed original\_budget\_amount\_project\_currency from decimal(21,2) to decimal(38,5)
 - Changed original\_budget\_amount\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed unit\_cost\_project\_currency from decimal(23,4) to decimal(38,5)
 - Changed unit\_cost\_company\_currency from decimal(30,4) to decimal(38,5)
- budget\_modifications:

 - Changed transfer\_amount\_project\_currency from decimal(23,2) to decimal(38,5)
 - Changed transfer\_amount\_company\_currency from decimal(30,2) to decimal(38,5)
- change\_event\_line\_item\_with\_markups:

 - Changed cost\_rom\_project\_currency from decimal(22,2) to decimal(38,5)
 - Changed cost\_rom\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed cost\_rom\_unit\_cost\_project\_currency from decimal(24,4) to decimal(38,5)
 - Changed cost\_rom\_unit\_cost\_company\_currency from decimal(30,4) to decimal(38,5)
 - Changed revenue\_rom\_unit\_cost\_project\_currency from decimal(24,4) to decimal(38,5)
 - Changed revenue\_rom\_unit\_cost\_company\_currency from decimal(30,4) to decimal(38,5)
- change\_event\_line\_items:

 - Changed cost\_rom\_project\_currency from decimal(22,2) to decimal(38,5)
 - Changed cost\_rom\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed cost\_rom\_unit\_cost\_project\_currency from decimal(24,4) to decimal(38,5)
 - Changed cost\_rom\_unit\_cost\_company\_currency from decimal(30,4) to decimal(38,5)
 - Changed revenue\_rom\_unit\_cost\_project\_currency from decimal(24,4) to decimal(38,5)
 - Changed revenue\_rom\_unit\_cost\_company\_currency from decimal(30,4) to decimal(38,5)
- commitment\_change\_order\_line\_items:

 - Changed unit\_cost\_project\_currency from decimal(29,4) to decimal(38,5)
 - Changed unit\_cost\_company\_currency from decimal(36,4) to decimal(38,5)
 - Changed manual\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed manual\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed total\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed total\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed approximate\_bottom\_line\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed approximate\_bottom\_line\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed extended\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed extended\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed amount\_including\_markup\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed amount\_including\_markup\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed change\_order\_committed\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed change\_order\_committed\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_pendings\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_pendings\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_approved\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_approved\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_draft\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_draft\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_not\_pricing\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_not\_pricing\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_pricing\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_pricing\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_pending\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_pending\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_revised\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_revised\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_proceeding\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_proceeding\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_not\_proceeding\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_not\_proceeding\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_no\_charge\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_no\_charge\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_rejected\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_rejected\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_void\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_void\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_pending\_billable\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_pending\_billable\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_pendings\_amount\_including\_markup\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_pendings\_amount\_including\_markup\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_approved\_amount\_including\_markup\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_approved\_amount\_including\_markup\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_draft\_amount\_including\_markup\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_draft\_amount\_including\_markup\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_not\_pricing\_amount\_including\_markup\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_not\_pricing\_amount\_including\_markup\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_pricing\_amount\_including\_markup\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_pricing\_amount\_including\_markup\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_pending\_amount\_including\_markup\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_pending\_amount\_including\_markup\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_revised\_amount\_including\_markup\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_revised\_amount\_including\_markup\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_proceeding\_amount\_including\_markup\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_proceeding\_amount\_including\_markup\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_not\_proceeding\_amount\_including\_markup\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_not\_proceeding\_amount\_including\_markup\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_no\_charge\_amount\_including\_markup\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_no\_charge\_amount\_including\_markup\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_rejected\_amount\_including\_markup\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_rejected\_amount\_including\_markup\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_void\_amount\_including\_markup\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_void\_amount\_including\_markup\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_pending\_billable\_amount\_including\_markup\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed potential\_change\_order\_pending\_billable\_amount\_including\_markup\_company\_currency from decimal(36,2) to decimal(38,5)
- commitment\_change\_order\_requests:

 - Changed amount\_without\_markup\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed amount\_without\_markup\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed grand\_total\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed grand\_total\_company\_currency from decimal(38,2) to decimal(38,5)
- commitment\_change\_orders:

 - Changed amount\_without\_markup\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed amount\_without\_markup\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed grand\_total\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed grand\_total\_company\_currency from decimal(38,2) to decimal(38,5)
- commitment\_line\_items:

 - Changed unit\_cost\_project\_currency from decimal(29,4) to decimal(38,5)
 - Changed unit\_cost\_company\_currency from decimal(36,4) to decimal(38,5)
 - Changed manual\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed manual\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed total\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed total\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed approximate\_bottom\_line\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed approximate\_bottom\_line\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed extended\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed extended\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed contracts\_approved\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed contracts\_approved\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed contracts\_draft\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed contracts\_draft\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed contracts\_out\_for\_signature\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed contracts\_out\_for\_signature\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed contracts\_complete\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed contracts\_complete\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
- commitment\_potential\_change\_orders:

 - Changed extended\_total\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed extended\_total\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed grand\_total\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed grand\_total\_company\_currency from decimal(34,2) to decimal(38,5)
- commitments:

 - Changed total\_payments\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed total\_payments\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed line\_items\_total\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed line\_items\_total\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed line\_items\_extended\_total\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed line\_items\_extended\_total\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed grand\_total\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed grand\_total\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed revised\_contract\_amount\_project\_currency from decimal(35,2) to decimal(38,5)
 - Changed revised\_contract\_amount\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed remaining\_balance\_project\_currency from decimal(35,2) to decimal(38,5)
 - Changed remaining\_balance\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed pending\_change\_orders\_project\_currency from decimal(35,2) to decimal(38,5)
 - Changed pending\_change\_orders\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed approved\_change\_orders\_project\_currency from decimal(35,2) to decimal(38,5)
 - Changed approved\_change\_orders\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed draft\_change\_orders\_project\_currency from decimal(35,2) to decimal(38,5)
 - Changed draft\_change\_orders\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed invoiced\_project\_currency from decimal(29,2) to decimal(38,5)
 - Changed invoiced\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed pending\_revised\_contract\_amount\_project\_currency from decimal(35,2) to decimal(38,5)
 - Changed pending\_revised\_contract\_amount\_company\_currency from decimal(35,2) to decimal(38,5)
- direct\_cost\_line\_items:

 - Changed unit\_cost\_project\_currency from decimal(29,4) to decimal(38,5)
 - Changed unit\_cost\_company\_currency from decimal(36,4) to decimal(38,5)
 - Changed manual\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed manual\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed extended\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed extended\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed approved\_total\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed approved\_total\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed payroll\_unit\_cost\_project\_currency from decimal(29,4) to decimal(38,5)
 - Changed payroll\_unit\_cost\_company\_currency from decimal(36,4) to decimal(38,5)
 - Changed amount\_total\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed amount\_total\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed amount\_grand\_total\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed amount\_grand\_total\_company\_currency from decimal(34,2) to decimal(38,5)
- erp\_job\_costs:

 - Changed job\_to\_date\_cost\_project\_currency from decimal(19,2) to decimal(38,5)
 - Changed job\_to\_date\_cost\_company\_currency from decimal(26,2) to decimal(38,5)
 - Changed commitment\_invoiced\_project\_currency from decimal(19,2) to decimal(38,5)
 - Changed commitment\_invoiced\_company\_currency from decimal(26,2) to decimal(38,5)
- direct\_costs:

 - Changed amount\_total\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed amount\_total\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed amount\_grand\_total\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed amount\_grand\_total\_company\_currency from decimal(34,2) to decimal(38,5)
- monitoring\_resources:

 - Changed unit\_cost\_project\_currency from decimal(23,4) to decimal(38,5)
 - Changed unit\_cost\_company\_currency from decimal(30,4) to decimal(38,5)
- owner\_invoice\_line\_item\_with\_markups:

 - Changed previous\_materials\_retainage\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed scheduled\_value\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed scheduled\_value\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed approved\_changes from decimal(20,2) to decimal(38,5)
 - Changed approved\_changes\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed approved\_changes\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed unit\_price\_project\_currency from decimal(29,4) to decimal(38,5)
 - Changed unit\_price\_company\_currency from decimal(36,4) to decimal(38,5)
 - Changed previous\_work\_completed\_value\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed previous\_work\_completed\_value\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed work\_completed\_this\_period\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed work\_completed\_this\_period\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed gross\_amount\_project\_currency from decimal(29,2) to decimal(38,5)
 - Changed gross\_amount\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed materials\_presently\_stored\_project\_currency from decimal(28,2) to decimal(38,5)
 - Changed materials\_presently\_stored\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed total\_completed\_and\_stored\_to\_date\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed total\_completed\_and\_stored\_to\_date\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed balance\_to\_finish\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed balance\_to\_finish\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed work\_retainage\_from\_previous\_application\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed work\_retainage\_from\_previous\_application\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed total\_retainage\_from\_previous\_application\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed total\_retainage\_from\_previous\_application\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed work\_retainage\_retained\_this\_period\_project\_currency from decimal(35,2) to decimal(38,5)
 - Changed work\_retainage\_retained\_this\_period\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed materials\_retainage\_retained\_this\_period\_project\_currency from decimal(20,2) to decimal(38,5)
 - Changed materials\_retainage\_retained\_this\_period\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed work\_retainage\_released\_this\_period\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed work\_retainage\_released\_this\_period\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed total\_retainage\_released\_this\_period\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed total\_retainage\_released\_this\_period\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed work\_retainage\_currently\_retained\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed work\_retainage\_currently\_retained\_company\_currency from decimal(37,2) to decimal(38,5)
 - Changed materials\_retainage\_currently\_retained\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed materials\_retainage\_currently\_retained\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed total\_retainage\_currently\_retained\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed total\_retainage\_currently\_retained\_company\_currency from decimal(37,2) to decimal(38,5)
 - Changed from\_previous\_application\_total\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed from\_previous\_application\_total\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed work\_retainage\_this\_period\_project\_currency from decimal(34,2) to decimal(38,5)
 - Changed work\_retainage\_this\_period\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed materials\_retainage\_from\_previous\_application\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed materials\_retainage\_from\_previous\_application\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed materials\_previously\_stored\_project\_currency from decimal(29,2) to decimal(38,5)
 - Changed materials\_previously\_stored\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed materials\_retainage\_released\_this\_period\_project\_currency from decimal(10,0) to decimal(38,5)
 - Changed materials\_retainage\_released\_this\_period\_company\_currency from decimal(10,0) to decimal(38,5)
 - Changed new\_materials\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed new\_materials\_company\_currency from decimal(34,2) to decimal(38,5)
- owner\_invoice\_line\_items:

 - Changed previous\_materials\_retainage\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed scheduled\_value\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed scheduled\_value\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed approved\_changes from decimal(20,2) to decimal(38,5)
 - Changed approved\_changes\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed approved\_changes\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed unit\_price\_project\_currency from decimal(29,4) to decimal(38,5)
 - Changed unit\_price\_company\_currency from decimal(36,4) to decimal(38,5)
 - Changed previous\_work\_completed\_value\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed previous\_work\_completed\_value\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed work\_completed\_this\_period\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed work\_completed\_this\_period\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed gross\_amount\_project\_currency from decimal(29,2) to decimal(38,5)
 - Changed gross\_amount\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed materials\_presently\_stored\_project\_currency from decimal(28,2) to decimal(38,5)
 - Changed materials\_presently\_stored\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed total\_completed\_and\_stored\_to\_date\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed total\_completed\_and\_stored\_to\_date\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed balance\_to\_finish\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed balance\_to\_finish\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed work\_retainage\_from\_previous\_application\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed work\_retainage\_from\_previous\_application\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed total\_retainage\_from\_previous\_application\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed total\_retainage\_from\_previous\_application\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed work\_retainage\_retained\_this\_period\_project\_currency from decimal(35,2) to decimal(38,5)
 - Changed work\_retainage\_retained\_this\_period\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed materials\_retainage\_retained\_this\_period\_project\_currency from decimal(20,2) to decimal(38,5)
 - Changed materials\_retainage\_retained\_this\_period\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed work\_retainage\_released\_this\_period\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed work\_retainage\_released\_this\_period\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed total\_retainage\_released\_this\_period\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed total\_retainage\_released\_this\_period\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed work\_retainage\_currently\_retained\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed work\_retainage\_currently\_retained\_company\_currency from decimal(37,2) to decimal(38,5)
 - Changed materials\_retainage\_currently\_retained\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed materials\_retainage\_currently\_retained\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed total\_retainage\_currently\_retained\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed total\_retainage\_currently\_retained\_company\_currency from decimal(37,2) to decimal(38,5)
 - Changed from\_previous\_application\_total\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed from\_previous\_application\_total\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed work\_retainage\_this\_period\_project\_currency from decimal(34,2) to decimal(38,5)
 - Changed work\_retainage\_this\_period\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed materials\_retainage\_from\_previous\_application\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed materials\_retainage\_from\_previous\_application\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed materials\_previously\_stored\_project\_currency from decimal(29,2) to decimal(38,5)
 - Changed materials\_previously\_stored\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed materials\_retainage\_released\_this\_period\_project\_currency from decimal(10,0) to decimal(38,5)
 - Changed materials\_retainage\_released\_this\_period\_company\_currency from decimal(10,0) to decimal(38,5)
 - Changed new\_materials\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed new\_materials\_company\_currency from decimal(34,2) to decimal(38,5)
- owner\_invoice\_markup\_line\_items:

 - Changed previous\_materials\_retainage\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed scheduled\_value\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed scheduled\_value\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed approved\_changes from decimal(20,2) to decimal(38,5)
 - Changed approved\_changes\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed approved\_changes\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed unit\_price\_project\_currency from decimal(29,4) to decimal(38,5)
 - Changed unit\_price\_company\_currency from decimal(36,4) to decimal(38,5)
 - Changed previous\_work\_completed\_value\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed previous\_work\_completed\_value\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed work\_completed\_this\_period\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed work\_completed\_this\_period\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed gross\_amount\_project\_currency from decimal(29,2) to decimal(38,5)
 - Changed gross\_amount\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed materials\_presently\_stored\_project\_currency from decimal(28,2) to decimal(38,5)
 - Changed materials\_presently\_stored\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed total\_completed\_and\_stored\_to\_date\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed total\_completed\_and\_stored\_to\_date\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed balance\_to\_finish\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed balance\_to\_finish\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed work\_retainage\_from\_previous\_application\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed work\_retainage\_from\_previous\_application\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed total\_retainage\_from\_previous\_application\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed total\_retainage\_from\_previous\_application\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed work\_retainage\_retained\_this\_period\_project\_currency from decimal(35,2) to decimal(38,5)
 - Changed work\_retainage\_retained\_this\_period\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed materials\_retainage\_retained\_this\_period\_project\_currency from decimal(20,2) to decimal(38,5)
 - Changed materials\_retainage\_retained\_this\_period\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed work\_retainage\_released\_this\_period\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed work\_retainage\_released\_this\_period\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed total\_retainage\_released\_this\_period\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed total\_retainage\_released\_this\_period\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed work\_retainage\_currently\_retained\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed work\_retainage\_currently\_retained\_company\_currency from decimal(37,2) to decimal(38,5)
 - Changed materials\_retainage\_currently\_retained\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed materials\_retainage\_currently\_retained\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed total\_retainage\_currently\_retained\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed total\_retainage\_currently\_retained\_company\_currency from decimal(37,2) to decimal(38,5)
 - Changed from\_previous\_application\_total\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed from\_previous\_application\_total\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed work\_retainage\_this\_period\_project\_currency from decimal(34,2) to decimal(38,5)
 - Changed work\_retainage\_this\_period\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed materials\_retainage\_from\_previous\_application\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed materials\_retainage\_from\_previous\_application\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed materials\_previously\_stored\_project\_currency from decimal(29,2) to decimal(38,5)
 - Changed materials\_previously\_stored\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed materials\_retainage\_released\_this\_period\_project\_currency from decimal(10,0) to decimal(38,5)
 - Changed materials\_retainage\_released\_this\_period\_company\_currency from decimal(10,0) to decimal(38,5)
 - Changed new\_materials\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed new\_materials\_company\_currency from decimal(34,2) to decimal(38,5)
- owner\_invoices:

 - Changed tax\_applicable\_to\_this\_payment\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed tax\_applicable\_to\_this\_payment\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed taxable\_amount\_project\_currency from decimal(35,2) to decimal(38,5)
 - Changed taxable\_amount\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed net\_change\_by\_change\_orders\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed net\_change\_by\_change\_orders\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed contract\_sum\_to\_date\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed contract\_sum\_to\_date\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed total\_completed\_and\_stored\_to\_date\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed total\_completed\_and\_stored\_to\_date\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed total\_retainage\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed less\_previous\_certificates\_for\_payment\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed less\_previous\_certificates\_for\_payment\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed net\_amount\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed net\_amount\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed gross\_amount\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed gross\_amount\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed total\_changes\_approved\_previous\_months\_by\_owner\_client\_additions\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed total\_changes\_approved\_previous\_months\_by\_owner\_client\_additions\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed total\_changes\_approved\_previous\_months\_by\_owner\_client\_deductions\_project\_currency from decimal(36,2) to decimal(38,5)
 - Changed total\_changes\_approved\_previous\_months\_by\_owner\_client\_deductions\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed total\_approved\_this\_month\_additions\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed total\_approved\_this\_month\_additions\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed total\_approved\_this\_month\_deductions\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed total\_approved\_this\_month\_deductions\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed total\_changes\_approved\_additions\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed total\_changes\_approved\_additions\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed total\_changes\_approved\_deductions\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed total\_changes\_approved\_deductions\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed retainage\_work\_completed\_to\_date\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed retainage\_work\_completed\_to\_date\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed retainage\_materials\_presently\_stored\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed retainage\_materials\_presently\_stored\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed materials\_presently\_stored\_project\_currency from decimal(30,2) to decimal(38,5)
 - Changed materials\_presently\_stored\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed paid\_amount\_project\_currency from decimal(35,2) to decimal(38,5)
 - Changed paid\_amount\_company\_currency from decimal(35,2) to decimal(38,5)
- payments\_issued:

 - Changed amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed amount\_company\_currency from decimal(34,2) to decimal(38,5)
- payments\_received:

 - Changed amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed amount\_company\_currency from decimal(34,2) to decimal(38,5)
- prime\_contract\_change\_order\_line\_items:

 - Changed unit\_cost\_project\_currency from decimal(29,4) to decimal(38,5)
 - Changed unit\_cost\_company\_currency from decimal(36,4) to decimal(38,5)
 - Changed manual\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed manual\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed extended\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed extended\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_approved\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_approved\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_draft\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_draft\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_not\_pricing\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_not\_pricing\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_pricing\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_pricing\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_pending\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_pending\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_revised\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_revised\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_proceeding\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_proceeding\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_not\_proceeding\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_not\_proceeding\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_no\_charge\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_no\_charge\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_rejected\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_rejected\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_void\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_void\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_pending\_billable\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_pending\_billable\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed potential\_change\_order\_pendings\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed potential\_change\_order\_pendings\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
- prime\_contract\_change\_order\_requests:

 - Changed amount\_without\_markup\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed amount\_without\_markup\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed grand\_total\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed grand\_total\_company\_currency from decimal(38,2) to decimal(38,5)
- prime\_contract\_change\_orders:

 - Changed amount\_without\_markup\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed amount\_without\_markup\_company\_currency from decimal(38,2) to decimal(38,5)
 - Changed grand\_total\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed grand\_total\_company\_currency from decimal(38,2) to decimal(38,5)
- prime\_contract\_line\_items:

 - Changed unit\_cost\_project\_currency from decimal(29,4) to decimal(38,5)
 - Changed unit\_cost\_company\_currency from decimal(36,4) to decimal(38,5)
 - Changed amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed amount\_company\_currency from decimal(34,2) to decimal(38,5)
- prime\_contract\_potential\_change\_orders:

 - Changed extended\_total\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed extended\_total\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed grand\_total\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed grand\_total\_company\_currency from decimal(34,2) to decimal(38,5)
- prime\_contracts:

 - Changed line\_items\_total\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed line\_items\_total\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed line\_item\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed line\_item\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed total\_payments\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed total\_payments\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed grand\_total\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed grand\_total\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed approved\_change\_orders\_grand\_total\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed approved\_change\_orders\_grand\_total\_company\_currency from decimal(38,2) to decimal(38,5)
- request\_for\_quote\_quotes:

 - Changed cost\_project\_currency from decimal(35,2) to decimal(38,5)
 - Changed cost\_company\_currency from decimal(35,2) to decimal(38,5)
- request\_for\_quotes:

 - Changed estimated\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed estimated\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed original\_quote\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed original\_quote\_company\_currency from decimal(34,2) to decimal(38,5)
- subcontractor\_invoice\_line\_items:

 - Changed unit\_price\_project\_currency from decimal(29,4) to decimal(38,5)
 - Changed unit\_price\_company\_currency from decimal(36,4) to decimal(38,5)
 - Changed scheduled\_value\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed scheduled\_value\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed work\_completed\_from\_previous\_application\_project\_currency from decimal(20,2) to decimal(38,5)
 - Changed work\_completed\_from\_previous\_application\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed work\_completed\_this\_period\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed work\_completed\_this\_period\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed total\_completed\_and\_stored\_to\_date\_value\_project\_currency from decimal(29,2) to decimal(38,5)
 - Changed total\_completed\_and\_stored\_to\_date\_value\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed balance\_to\_finish\_project\_currency from decimal(30,2) to decimal(38,5)
 - Changed balance\_to\_finish\_company\_currency from decimal(37,2) to decimal(38,5)
 - Changed work\_retainage\_currently\_retained\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed work\_retainage\_currently\_retained\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed materials\_retainage\_currently\_retained\_project\_currency from decimal(20,2) to decimal(38,5)
 - Changed materials\_retainage\_currently\_retained\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed total\_currently\_retained\_project\_currency from decimal(28,2) to decimal(38,5)
 - Changed total\_currently\_retained\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed total\_retainage\_project\_currency from decimal(32,2) to decimal(38,5)
 - Changed total\_retainage\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed proposed\_this\_period\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed proposed\_this\_period\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed materials\_presently\_stored\_project\_currency from decimal(20,2) to decimal(38,5)
 - Changed materials\_presently\_stored\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed materials\_previously\_stored\_project\_currency from decimal(20,2) to decimal(38,5)
 - Changed materials\_previously\_stored\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed materials\_previously\_stored\_from\_project\_currency from decimal(20,2) to decimal(38,5)
 - Changed materials\_previously\_stored\_from\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed work\_retainage\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed work\_retainage\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed work\_retainage\_previous\_application\_amount\_project\_currency from decimal(20,2) to decimal(38,5)
 - Changed work\_retainage\_previous\_application\_amount\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed materials\_retainage\_previous\_application\_amount\_project\_currency from decimal(20,2) to decimal(38,5)
 - Changed materials\_retainage\_previous\_application\_amount\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed total\_retainage\_previous\_application\_amount\_project\_currency from decimal(21,2) to decimal(38,5)
 - Changed total\_retainage\_previous\_application\_amount\_company\_currency from decimal(29,2) to decimal(38,5)
 - Changed work\_retainage\_released\_this\_period\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed work\_retainage\_released\_this\_period\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed materials\_retainage\_released\_this\_period\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed materials\_retainage\_released\_this\_period\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed new\_materials\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed new\_materials\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed total\_completed\_and\_stored\_to\_date\_from\_previous\_project\_currency from decimal(29,2) to decimal(38,5)
 - Changed total\_completed\_and\_stored\_to\_date\_from\_previous\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed net\_amount\_project\_currency from decimal(32,2) to decimal(38,5)
 - Changed net\_amount\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed gross\_amount\_project\_currency from decimal(28,2) to decimal(38,5)
 - Changed gross\_amount\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed retainage\_new\_materials\_from\_percent\_project\_currency from decimal(34,2) to decimal(38,5)
 - Changed retainage\_new\_materials\_from\_percent\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed adjusted\_materials\_retained\_previously\_project\_currency from decimal(28,2) to decimal(38,5)
 - Changed adjusted\_materials\_retained\_previously\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed adjusted\_materials\_previously\_stored\_project\_currency from decimal(28,2) to decimal(38,5)
 - Changed adjusted\_materials\_previously\_stored\_company\_currency from decimal(35,2) to decimal(38,5)
- subcontractor\_invoices:

 - Changed total\_proposed\_amount\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed total\_proposed\_amount\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed total\_retainage\_project\_currency from decimal(21,2) to decimal(38,5)
 - Changed total\_retainage\_company\_currency from decimal(29,2) to decimal(38,5)
 - Changed total\_earned\_less\_retainage\_project\_currency from decimal(22,2) to decimal(38,5)
 - Changed total\_earned\_less\_retainage\_company\_currency from decimal(30,2) to decimal(38,5)
 - Changed current\_payment\_due\_project\_currency from decimal(23,2) to decimal(38,5)
 - Changed current\_payment\_due\_company\_currency from decimal(31,2) to decimal(38,5)
 - Changed original\_payment\_due\_project\_currency from decimal(23,2) to decimal(38,5)
 - Changed original\_payment\_due\_company\_currency from decimal(31,2) to decimal(38,5)
 - Changed balance\_to\_finish\_project\_currency from decimal(29,2) to decimal(38,5)
 - Changed balance\_to\_finish\_company\_currency from decimal(36,2) to decimal(38,5)
 - Changed net\_change\_by\_change\_orders\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed net\_change\_by\_change\_orders\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed contract\_sum\_to\_date\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed contract\_sum\_to\_date\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed total\_contract\_amount\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed total\_contract\_amount\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed total\_completed\_and\_stored\_to\_date\_project\_currency from decimal(20,2) to decimal(38,5)
 - Changed total\_completed\_and\_stored\_to\_date\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed retainage\_work\_completed\_to\_date\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed retainage\_work\_completed\_to\_date\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed retainage\_materials\_presently\_stored\_project\_currency from decimal(20,2) to decimal(38,5)
 - Changed retainage\_materials\_presently\_stored\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed total\_changes\_approved\_in\_previous\_months\_by\_owner\_client\_additions\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed total\_changes\_approved\_in\_previous\_months\_by\_owner\_client\_additions\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed total\_changes\_approved\_in\_previous\_months\_by\_owner\_client\_deductions\_project\_currency from decimal(37,2) to decimal(38,5)
 - Changed total\_changes\_approved\_in\_previous\_months\_by\_owner\_client\_deductions\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed total\_changes\_approved\_this\_month\_additions\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed total\_changes\_approved\_this\_month\_additions\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed total\_changes\_approved\_this\_month\_deductions\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed total\_changes\_approved\_this\_month\_deductions\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed total\_changes\_approved\_additions\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed total\_changes\_approved\_additions\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed total\_changes\_approved\_deductions\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed total\_changes\_approved\_deductions\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed less\_certificates\_for\_payment\_project\_currency from decimal(20,2) to decimal(38,5)
 - Changed less\_certificates\_for\_payment\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed completed\_work\_retainage\_amount\_project\_currency from decimal(38,2) to decimal(38,5)
 - Changed completed\_work\_retainage\_amount\_company\_currency from decimal(28,2) to decimal(38,5)
 - Changed gross\_amount\_project\_currency from decimal(21,2) to decimal(38,5)
 - Changed gross\_amount\_company\_currency from decimal(29,2) to decimal(38,5)
 - Changed net\_amount\_project\_currency from decimal(23,2) to decimal(38,5)
 - Changed net\_amount\_company\_currency from decimal(31,2) to decimal(38,5)
 - Changed paid\_amount\_project\_currency from decimal(35,2) to decimal(38,5)
 - Changed paid\_amount\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed total\_tax\_project\_currency from decimal(27,2) to decimal(38,5)
 - Changed total\_tax\_company\_currency from decimal(34,2) to decimal(38,5)
 - Changed total\_payments\_amount\_project\_currency from decimal(35,2) to decimal(38,5)
 - Changed total\_payments\_amount\_company\_currency from decimal(35,2) to decimal(38,5)
 - Changed early\_pay\_fee\_amount\_company\_currency from decimal(26,2) to decimal(38,5)
- wp\_roles:

 - Changed company\_id from string to bigint
 - Changed project\_id from string to bigint

##### Analytics 2.0 Data Updates (01/20/2026)

**Procore updated the following models (tables):**

- bid\_Package:

 - Added bid\_Manager
 - Added bid\_submission\_notifications
- timecard\_entries:

 - Added clock\_in\_gps\_onsite
 - Added clock\_out\_gps\_onsite
 - Added lunch\_clock\_in\_gps\_onsite
 - Added lunch\_clock\_out\_gps\_onsite
- equipment\_timecard\_entry:

 - Added idle\_hours
- labor\_allocations:

 - Added created\_at
 - Added updated\_at
- budget\_change\_adjustment\_line\_items:

 - Added change\_event\_line\_item\_id
 - Added vendor\_id
- budget\_change\_custom\_fields:

 - Added audit\_transaction\_timestamp
 - Added budget\_change\_custom\_field\_id
 - Added budget\_change\_id
 - Added company\_id
 - Added custom\_field\_data\_type
 - Added custom\_field\_definitions\_id
 - Added custom\_field\_name
 - Added custom\_field\_value
 - Added custom\_field\_value\_id
 - Added project\_id
- budget\_forecast\_line\_items:

 - Added wbs\_code\_id
- commitment\_change\_order\_line\_items:

 - Added vendor\_id
- commitment\_line\_items:

 - Added prime\_contract\_line\_item\_id
 - Added vendor\_id
- contract\_compliance\_documents:

 - Added vendor\_id
- direct\_cost\_line\_items:

 - Added employee\_id
 - Added vendor\_id
- owner\_invoices:

 - Added vendor\_id
- payments\_issued:

 - Added disbursement\_id
 - Added vendor\_id
- payments\_lien\_waivers:

 - Added commitment\_id
 - Added vendor\_id
- payments\_received:

 - Added vendor\_id
- payments\_requirements:

 - Added commitment\_id
- prime\_contract\_workflow\_responses:

 - Added vendor\_id
- prime\_contract\_workflow\_steps:

 - Added vendor\_id
- wbs\_codes:

 - Added wbs\_code\_status
- submittal\_approver\_attachments:

 - Added submittal\_approver\_attachment\_id
 - Added company\_id
 - Added company\_type
 - Added content\_type
 - Added submittal\_approver\_id
 - Added submittal\_id
 - Added created\_at
 - Added created\_by
 - Added created\_by\_id
 - Added created\_by\_login
 - Added filename
 - Added name
 - Added project\_id
 - Added prostore\_file\_id
 - Added updated\_at
 - Added viewable\_type
- inspection\_item\_attachments:

 - Added inspection\_item\_attachment\_id
 - Added company\_id
 - Added company\_type
 - Added content\_type
 - Added inspection\_item\_id
 - Added created\_at
 - Added created\_by
 - Added created\_by\_id
 - Added created\_by\_login
 - Added filename
 - Added name
 - Added project\_id
 - Added prostore\_file\_id
 - Added updated\_at
 - Added viewable\_type

##### Analytics 2.0 Data Updates (12/16/2025)

**Procore updated the following models (tables):**

- invoice\_compliance:

 - Added vendor\_id
- subcontractor\_invoices:

 - Added early\_pay\_fee\_amount\_company\_currency
 - Added early\_pay\_fee\_amount\_project\_currency
 - Added total\_contract\_amount\_company\_currency
 - Added total\_contract\_amount\_project\_currency
- commitment\_line\_items:

 - Added allow\_these\_users\_to\_see\_sov\_items
 - Added contract\_assignee\_id
 - Added contract\_created\_by\_id
 - Added contract\_private
 - Added contract\_user\_id\_list
- prime\_contract\_line\_items:

 - Added allow\_these\_users\_to\_see\_sov\_items
 - Added contract\_assignee\_id
 - Added contract\_created\_by\_id
 - Added contract\_private
 - Added contract\_status
 - Added contract\_type
 - Added contract\_user\_id\_list
- daily\_log\_accident:

 - Added area
- daily\_log\_construction\_reports:

 - Added area
- daily\_log\_delay:

 - Added area
- daily\_log\_delivery:

 - Added area
- action\_plan:

 - Added approver\_party\_id\_list
- coordination\_issue\_custom\_fields:

 - Added audit\_transaction\_timestamp
 - Added company\_id
 - Added coordination\_issue\_custom\_field\_id
 - Added coordination\_issue\_id
 - Added custom\_field\_data\_type
 - Added custom\_field\_definitions\_id
 - Added custom\_field\_name
 - Added custom\_field\_value
 - Added custom\_field\_value\_id
 - Added project\_id
- daily\_log\_dumpster:

 - Added area
- daily\_log\_equipment:

 - Added area
- daily\_log\_inspection:

 - Added segment
- daily\_log\_manpower:

 - Added area
- daily\_log\_note:

 - Added area
- daily\_log\_observed\_weather\_condition:

 - Added area
- daily\_log\_phone\_call:

 - Added area
- daily\_log\_plan\_revision:

 - Added area
- daily\_log\_productivity:

 - Added area
- daily\_log\_quantity:

 - Added area
- daily\_log\_safety\_violation:

 - Added area
- daily\_log\_scheduled\_work:

 - Added area
- daily\_log\_visitor:

 - Added area
- daily\_log\_waste:

 - Added area
- equipment\_telematic:

 - Added provider\_name
 - Added provider\_id
- equipment\_telematics\_daily\_summary:

 - Added active\_regeneration\_hours
 - Added date
 - Added distance
 - Added equipment\_telematics\_daily\_summary\_id
 - Added fuel\_used
 - Added fuel\_used\_last\_24
 - Added identification\_number
 - Added idle\_hours
 - Added idle\_non\_operating\_hours
 - Added load\_count
 - Added maximum\_speed\_last\_24
 - Added operating\_hours
 - Added power\_take\_off\_hours
 - Added company\_id
 - Added equipment\_id
- incident:

 - Added assignee\_id\_list
 - Added assignee\_list
 - Added global\_status
- incident\_assignee:

 - Added audit\_transaction\_timestamp
 - Added company\_id
 - Added incident\_assignee\_id
 - Added incident\_id
 - Added login
 - Added project\_id
 - Added assignee\_id
 - Added company\_name
 - Added created\_at
 - Added name
 - Added updated\_at
- commitments:

 - Added bid\_id
 - Added bid\_vendor\_id
 - Added bid\_package\_id
 - Added bid\_form\_id
- punch\_item\_activities:

 - Added audit\_transaction\_timestamp
 - Added company\_id
 - Added created\_by\_id
 - Added created\_by\_login
 - Added project\_id
 - Added punch\_item\_id
 - Added attachments\_count
 - Added comment
 - Added created\_at
 - Added created\_by\_name
 - Added punch\_item\_activity\_id
 - Added status
 - Added updated\_at
- rfi\_responses:

 - Added rfi\_project\_id
- site\_instruction\_attentions:

 - Added user\_id
 - Added name
- incident\_record:

 - Added equipment\_identification\_number
 - Added equipment\_id
 - Added equipment\_name
- site\_instruction\_distribution\_members:

 - Added user\_id
 - Added name
- specification\_sections:

 - Added created\_by\_id
- bid\_package:

 - Added require\_nda
- labor\_equipment\_productivity:

 - Added cost\_code
 - Added wbs\_code\_flat\_code
 - Added labor\_estimated\_hours
 - Added labor\_reported\_hours
 - Added labor\_reported\_cost
 - Added labor\_percent\_completion
 - Added equipment\_estimated\_hours
 - Added equipment\_reported\_hours
 - Added equipment\_reported\_cost
 - Added equipment\_percent\_completion
 - Added total\_estimated\_hours
 - Added total\_reported\_hours
 - Added total\_reported\_cost
 - Added labor\_equipment\_productivity\_id
 - Added company\_id
 - Added project\_id
 - Added cost\_code\_id
 - Added wbs\_code\_id
- timecard\_entries:

 - Added wp\_people\_id
- labor\_allocations:

 - Added labor\_allocation\_id
 - Added allocation\_date
 - Added wbs\_code\_id
 - Added allocation\_hours
 - Added company\_id
 - Added project\_id
 - Added created\_by\_id
- prime\_contract:

 - Added pending\_change\_orders
 - Added invoiced
 - Added approved\_change\_orders
 - Added pending\_revised\_contract\_amount
 - Added remaining\_balance
 - Added revised\_contract\_amount
 - Added draft\_change\_orders
 - Added pending\_change\_orders\_project\_currency
 - Added invoiced\_project\_currency
 - Added approved\_change\_orders\_project\_currency
 - Added pending\_revised\_contract\_amount\_project\_currency
 - Added remaining\_balance\_project\_currency
 - Added revised\_contract\_amount\_project\_currency
 - Added draft\_change\_orders\_company\_currency
 - Added pending\_change\_orders\_company\_currency
 - Added invoiced\_company\_currency
 - Added approved\_change\_orders\_company\_currency
 - Added pending\_revised\_contract\_amount\_company\_currency
 - Added remaining\_balance\_company\_currency
 - Added revised\_contract\_amount\_company\_currency
 - Added draft\_change\_orders\_company\_currency
- rfis:

 - Added attachment\_count

##### Analytics 2.0 Data Updates (11/18/2025)

**Procore added the following models (tables):**

- budget\_forecasts

**Procore removed** **the following models (tables):**

- budget\_change\_custom\_field\_configs
- change\_event\_custom\_field\_configs
- commitment\_co\_custom\_field\_configs
- commitment\_custom\_field\_configs
- commitment\_pco\_custom\_field\_configs
- prime\_contract\_co\_custom\_field\_configs
- prime\_contract\_pco\_custom\_field\_configs
- prime\_contract\_custom\_field\_configs
- subcontractor\_invoice\_custom\_field\_configs
- action\_plan\_custom\_field\_configs
- correspondence\_custom\_field\_configs
- daily\_log\_construction\_report\_custom\_field\_configs
- daily\_log\_equipment\_custom\_field\_configs
- daily\_log\_manpower\_custom\_field\_configs
- inspection\_custom\_field\_configs
- observation\_custom\_field\_configs
- punch\_item\_custom\_field\_configs
- rfi\_custom\_field\_configs
- submittal\_custom\_field\_configs
- time\_and\_material\_entry\_custom\_field\_configs
- time\_and\_material\_equipment\_custom\_field\_configs
- time\_and\_material\_labors\_custom\_field\_configs
- time\_and\_material\_material\_custom\_field\_configs
- time\_and\_material\_entry\_subcontractor\_field\_configs
- timecard\_entry\_custom\_field\_configs:
- bid\_item:

 - Removed bidding\_vendor\_id
- bid\_vendor:

 - Removed bidding\_vendor\_id
- bid:

 - Removed bidding\_vendor\_id
- contracts:

 - Removed bidding\_vendor\_id
- wp\_people:

 - Removed tags
 - Removed tag\_instance\_id
 - Removed wp\_people\_project\_tag\_id
 - Removed wp\_project\_id
- wp\_projects:

 - Removed tags
 - Removed tag\_instance\_id
 - Removed wp\_project\_tag\_id

**Procore updated the data type for the following models (tables):**

- action\_plan\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- budget\_change\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- change\_event\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- commitment\_co\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- commitment\_custom\_fields

 - Changed custom\_field\_value\_id from int to string
- commitment\_pco\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- company\_folder\_documents\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- correspondence\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_accident\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_construction\_report\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_delay\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_delivery\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_dumpster\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_equipment\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_inspection\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_manpower\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_note\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_phone\_call\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_plan\_revision\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_productivity\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_quantity\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_safety\_violation\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_scheduled\_work\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_visitor\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- daily\_log\_waste\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- drawing\_revision\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- folder\_documents\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- incident\_action\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- incident\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- incident\_record\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- incident\_witness\_statement\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- inspection\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- observation\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- prime\_contract\_co\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- prime\_contract\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- prime\_contract\_pco\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- project\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- punch\_item\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- rfi\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- subcontractor\_invoice\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string
- submittal\_custom\_fields:

 - Changed custom\_field\_value\_id from int to string

**Procore updated the following models (tables):**

- submittal\_approvers:

 - Added variance\_at\_end
- Bid:

 - Added invitation\_first\_sent\_at
- projects:

 - Added budget\_locked
 - Added actual\_completion\_date
- form\_template:

 - Added company\_id
 - Added created\_by\_id
 - Added prostore\_file\_id
 - Added audit\_transaction\_timestamp
 - Added form\_template\_id
 - Added name
 - Added description
 - Added created\_at
 - Added updated\_at
 - Added archived\_at
- commitments:

 - Added draft\_change\_orders\_company\_currency
 - Added invoiced\_company\_currency
 - Added pending\_change\_orders\_company\_currency
 - Added pending\_revised\_contract\_amount\_company\_currency
 - Added approved\_change\_orders\_company\_currency
 - Added approved\_change\_orders\_project\_currency
 - Added contract\_user\_id\_list
 - Added draft\_change\_orders\_project\_currency
 - Added invoiced\_project\_currency
 - Added pending\_change\_orders\_project\_currency
 - Added pending\_revised\_contract\_amount\_project\_currency
 - Added remaining\_balance\_project\_currency
 - Added revised\_contract\_amount\_project\_currency
 - Added workflow\_distribution\_member\_id\_list
 - Added workflow\_role\_user\_id\_list
 - Added pending\_revised\_contract\_amount\_company\_currency
- commitment\_change\_order\_workflow\_responses:

 - Added current\_step\_response
- commitment\_pco\_workflow\_responses:

 - Added current\_step\_response
- correspondence\_workflow\_responses:

 - Added current\_step\_response
- drawing\_revision:

 - Added current\_revision
 - Added reviewed\_by\_id
 - Added status\_id
- prime\_contracts:

 - Added contract\_user\_id\_list
 - Added workflow\_distribution\_member\_id\_list
 - Added workflow\_role\_user\_id\_list
- budget\_change\_workflow\_responses:

 - Added current\_step\_response
 - Added remaining\_balance\_company\_currency
 - Added revised\_contract\_amount\_company\_currency
- bid\_item:

 - Added bid\_vendor\_id
- bid\_vendor:

 - Added bid\_form\_id
- estimate\_adjustment:

 - Added procore\_project\_id
- estimate\_budget\_item:

 - Added procore\_project\_id
- estimate\_budget\_item\_included\_item:

 - Added procore\_project\_id
- estimate\_layer\_groups:

 - Added procore\_project\_id
- estimate\_layers:

 - Added procore\_project\_id
- estimates:

 - Added procore\_project\_id
- estimating\_project\_custom\_fields:

 - Added procore\_project\_id
- action\_plan:

 - Added assignee\_party\_id\_list
 - Added completed\_plan\_receiver\_party\_id\_list
- correspondence\_assignees:

 - Added user\_id
- correspondence\_distributions:

 - Added user\_id
- correspondences:

 - Added assignee\_id\_list
 - Added composite\_provider\_key
 - Added distribution\_member\_id\_list
- daily\_log\_accident:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_construction\_reports:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_delay:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_delivery:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_dumpster:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_equipment:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_inspection:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_manpower:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_note:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_observed\_weather\_condition:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_phone\_call:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_plan\_revision:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_productivity:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_quantity:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_safety\_violation:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_scheduled\_work:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_visitor:

 - Added created\_by\_collaborator
 - Added raw\_status
- daily\_log\_waste:

 - Added created\_by\_collaborator
 - Added raw\_status
- inspection\_items:

 - Added date\_value\_timestamp
- incident:

 - Added distribution\_member\_id\_list
 - Added recipient\_id\_list
- incident\_alert:

 - Added permission\_recipient\_id
 - Added recipient\_name
- site\_instruction\_attentions:

 - Added member\_name
 - Added audit\_transaction\_timestamp
 - Added company\_id
 - Added site\_instruction\_attention\_id
 - Added member\_id
 - Added project\_id
 - Added site\_instruction\_id
- site\_instruction\_distribution\_members:

 - Added member\_name
 - Added site\_instruction\_distribution\_member\_id
 - Added audit\_transaction\_timestamp
 - Added company\_id
 - Added member\_id
 - Added project\_id
 - Added site\_instruction\_id
- site\_instructions:

 - Added attention\_user\_id\_list
 - Added distribution\_member\_id\_list
- inspections:

 - Added assignee\_id\_list
 - Added distribution\_member\_id\_list
 - Added signature\_id\_list
- meeting:

 - Added assignee\_id\_list
- meeting\_attendee:

 - Added person\_id
- observation:

 - Added distribution\_member\_ids
- observation\_distribution\_member:

 - Added user\_id
- punch\_item:

 - Added assignee\_id\_list
 - Added distribution\_member\_id\_list
 - Added permission\_workflow\_status
- rfi\_responses:

 - Added assignee\_id\_list
 - Added distribution\_member\_id\_list
 - Added rfi\_created\_by\_id
 - Added rfi\_draft
 - Added rfi\_hidden
 - Added rfi\_manager\_id
 - Added rfi\_private
- rfis:

 - Added assignee\_id\_list
 - Added distribution\_member\_id\_list
- schedule\_calendar\_item:

 - Added assigned\_id
- schedule\_lookahead:

 - Added created\_by\_id
- schedule\_lookahead\_task:

 - Added created\_by\_id
- schedule\_task:

 - Added created\_by\_id
- maintenance\_record:

 - Added type
 - Added duration
 - Added start\_date
 - Added issue
 - Added notes
 - Added maintenance\_record\_id
 - Added company\_id
 - Added equipment\_id
- owner\_invoice\_workflow\_responses:

 - Added current\_step\_response
- task:

 - Added assignee\_user\_id\_list
 - Added created\_by\_id
 - Added task\_item\_distribution\_member\_id\_list
- task\_assignee:

 - Added assignee\_id
- task\_distribution\_member:

 - Added user\_id
- prime\_contract\_workflow\_responses:

 - Added current\_step\_response
- prime\_contract\_change\_order\_workflow\_responses:

 - Added current\_step\_response
- prime\_contract\_pco\_workflow\_responses:

 - Added current\_step\_response
- submittals:

 - Added approvers\_ids
 - Added distribution\_id\_list
- specification\_sections:

 - Added current\_revision
 - Added issued\_date
 - Added received\_date
 - Added revision
- Estimate:

 - Added include\_in\_primary\_estimate
- equipment\_timecard\_entry\_custom\_fields:

 - Added batch\_id
 - Added partition\_company\_id
 - Added equipment\_timecard\_entry\_id
 - Added equipment\_timecard\_entry\_custom\_field\_id
 - Added custom\_field\_value
 - Added custom\_field\_value\_id
 - Added custom\_field\_definitions\_id
 - Added custom\_field\_name
 - Added custom\_field\_data\_type
 - Added company\_id
 - Added project\_id
- estimating\_projects:

 - Added primary\_contact\_full\_address
- subcontractor\_invoice\_workflow\_responses:

 - Added current\_step\_response
- assignments:

 - Added percent\_allocation
- wp\_wage\_overrides:

 - Added wp\_project\_id
 - Added wp\_wage\_override\_id
 - Added job\_title\_id
 - Added company\_id
 - Added job\_title
 - Added wage\_override\_rate
 - Added project\_id
- tags:

 - Added wp\_people\_id
 - Added wp\_project\_id
- commitment\_workflow\_response\_occurrences:

 - Added current\_step\_response

##### Analytics 2.0 Data Updates (10/28/2025)

**Procore updated the following models (tables):**

- inspection\_items:

 - Added attachment\_count
- correspondences\_workflow\_responses:

 - Added current\_step\_response

##### Analytics 2.0 Data Updates (10/21/2025)

**Procore updated the following models (tables):**

- action\_plan:

 - Added status\_id
- actual\_production\_quantities:

 - Added description
- bid\_vendor:

 - Added audit\_transaction\_timestamp
- assembly\_part:

 - Added difficulty\_factor
 - Added labor\_margin
 - Added total\_cost
 - Added total\_labor\_sales
 - Added unit\_labor\_mins
 - Added unit\_sales
- bid\_package:

 - Added require\_

    nda
- bid\_vendor:

 - Added bid\_form\_id
 - Added bid\_id
 - Added bid\_package\_id
 - Added bid\_vendor\_id
 - Added company\_id
 - Added created\_at
 - Added jobsite\_proximity\_in\_miles
 - Added project\_id
 - Added updated\_at
 - Added vendor\_address
 - Added vendor\_affirmative\_action
 - Added vendor\_african\_american\_business
 - Added vendor\_asian\_american\_business
 - Added vendor\_authorized\_bidder
 - Added vendor\_avg\_company\_rating
 - Added vendor\_business\_phone
 - Added vendor\_certified\_business\_enterprise
 - Added vendor\_city
 - Added vendor\_country
 - Added vendor\_disadvantaged\_business
 - Added vendor\_eight\_a\_business\_enterprise
 - Added vendor\_hispanic\_business
 - Added vendor\_historically\_underutlized\_business
 - Added vendor\_id
 - Added vendor\_minority\_business\_enterprise
 - Added vendor\_name
 - Added vendor\_native\_american\_business
 - Added vendor\_service\_disabled\_veteran\_owned\_small\_business
 - Added vendor\_small\_business
 - Added vendor\_state
 - Added vendor\_trades
 - Added vendor\_womens\_business
 - Added vendor\_zip
- bid:

 - Added bid\_vendor\_id
 - Added nda\_activity
- change\_event\_line\_item\_with\_markups:

 - Added non\_committed\_cost
 - Added non\_committed\_cost\_company\_currency
 - Added non\_committed\_cost\_project\_currency
- commitment\_change\_orders:

 - Added change\_reason
- company\_granular\_permissions:

 - Added audit\_transaction\_timestamp
 - Added company\_granular\_permission\_id
 - Added company\_id
 - Added login\_information\_id
 - Added tool\_bid\_board\_can\_access\_projects\_for\_all\_users
 - Added tool\_bid\_board\_can\_add\_notes
 - Added tool\_bid\_board\_can\_edit\_docs
 - Added tool\_bid\_board\_can\_edit\_project\_details
 - Added tool\_bid\_board\_can\_export\_bid
 - Added tool\_directory\_add\_user\_to\_project
 - Added tool\_directory\_assign\_to\_future\_projects
 - Added tool\_directory\_create\_users
 - Added tool\_directory\_create\_vendors
 - Added tool\_directory\_remove\_user\_from\_project
 - Added tool\_directory\_view\_user\_details
 - Added tool\_directory\_view\_vendor\_details
- company\_permissions:

 - Added permission\_template\_id
- contract:

 - Added bid\_vendor\_id
- daily\_log\_types:

 - Added audit\_transaction\_timestamp
 - Added company\_id
 - Added created\_at
 - Added daily\_log\_type\_id
 - Added enabled
 - Added label
 - Added name
 - Added updated\_at
- equipment:

 - Added daily\_logs\_count\_l7
 - Added engine\_hours\_changes\_count\_l7
 - Added inspections\_count\_l7
 - Added is\_idle\_last\_7\_days
 - Added last\_activity
 - Added last\_activity\_date
 - Added last\_daily\_log\_date
 - Added last\_engine\_hours\_activity\_date
 - Added last\_inspection\_date
 - Added last\_location\_activity\_date
 - Added last\_timecard\_date
 - Added location\_changes\_count\_l7
 - Added timecards\_count\_l7
- form:

 - Added template\_archived\_date
- inspections:

 - Added group
 - Added reinspected\_by\_id
 - Added reinspected\_by\_name
 - Added reinspected\_from\_id
 - Added reinspected\_from\_name
- meeting:

 - Added distributed\_at
 - Added distributed\_by\_id
 - Added distributed\_by\_name
 - Added last\_distributed\_event
- observation:

 - Added group
- project\_granular\_permissions:

 - Added audit\_transaction\_timestamp
 - Added company\_id
 - Added login\_information\_id
 - Added pk\_user\_id
 - Added project\_granular\_permission\_id
 - Added project\_id
 - Added tool\_action\_plans\_act\_as\_approver
 - Added tool\_action\_plans\_act\_as\_receiver
 - Added tool\_action\_plans\_create\_and\_edit\_plan
 - Added tool\_action\_plans\_create\_test\_records\_as\_assignee
 - Added tool\_action\_plans\_delete\_plan
 - Added tool\_action\_plans\_edit\_due\_date
 - Added tool\_action\_plans\_edit\_item\_notes\_as\_assignee
 - Added tool\_action\_plans\_edit\_item\_status\_as\_assignee
 - Added tool\_action\_plans\_edit\_notifications
 - Added tool\_action\_plans\_edit\_project\_templates
 - Added tool\_action\_plans\_link\_record
 - Added tool\_action\_plans\_sign\_as\_any\_assignee
 - Added tool\_action\_plans\_sign\_as\_same\_company\_approver
 - Added tool\_action\_plans\_sign\_as\_same\_company\_assignee
 - Added tool\_action\_plans\_sign\_as\_same\_company\_receiver
 - Added tool\_action\_plans\_sign\_as\_self\_assignee
 - Added tool\_action\_plans\_unlink\_record
 - Added tool\_admin\_manage\_locations
 - Added tool\_admin\_manage\_wbs\_codes
 - Added tool\_admin\_update\_active\_tabs
 - Added tool\_admin\_update\_cost\_codes
 - Added tool\_admin\_update\_general\_settings
 - Added tool\_budget\_create\_edit\_delete\_budget\_changes
 - Added tool\_budget\_delete\_budget\_line\_items
 - Added tool\_budget\_import\_line\_items\_from\_csv
 - Added tool\_budget\_lock\_budget
 - Added tool\_budget\_modify\_original\_budget\_amount
 - Added tool\_budget\_send\_and\_retrieve\_from\_erp
 - Added tool\_budget\_view\_budget\_insights
 - Added tool\_budget\_view\_direct\_cost\_details
 - Added tool\_change\_events\_can\_export\_to\_pdf\_or\_csv
 - Added tool\_change\_events\_can\_view\_change\_history
 - Added tool\_commitments\_create\_purchase\_order\_contract
 - Added tool\_commitments\_create\_work\_order\_contract
 - Added tool\_commitments\_select\_out\_of\_scope\_wbs\_codes\_on\_commitment\_change\_orders
 - Added tool\_commitments\_update\_contract\_currency\_exchange\_rate
 - Added tool\_commitments\_update\_purchase\_order\_contract
 - Added tool\_commitments\_update\_work\_order\_contract
 - Added tool\_commitments\_view\_private\_purchase\_order\_contract
 - Added tool\_commitments\_view\_private\_work\_order\_contract
 - Added tool\_daily\_log\_copy
 - Added tool\_daily\_log\_log\_restrictively
 - Added tool\_daily\_log\_update\_own\_entries
 - Added tool\_daily\_log\_view\_company\_entries
 - Added tool\_data\_extracts\_can\_create
 - Added tool\_data\_extracts\_can\_delete\_drafts
 - Added tool\_data\_extracts\_can\_download
 - Added tool\_data\_extracts\_can\_edit\_drafts
 - Added tool\_data\_extracts\_can\_extract\_data
 - Added tool\_data\_extracts\_can\_view
 - Added tool\_direct\_costs\_create\_direct\_cost
 - Added tool\_direct\_costs\_delete\_direct\_cost
 - Added tool\_direct\_costs\_update\_direct\_cost
 - Added tool\_direct\_costs\_update\_exchange\_rate
 - Added tool\_directory\_add\_user
 - Added tool\_directory\_assign\_project\_role
 - Added tool\_directory\_create\_distribution\_group
 - Added tool\_directory\_create\_person
 - Added tool\_directory\_create\_user
 - Added tool\_directory\_create\_vendor
 - Added tool\_directory\_manage\_permission\_templates
 - Added tool\_directory\_manage\_vendor\_insurances
 - Added tool\_directory\_remove\_user
 - Added tool\_directory\_remove\_vendor
 - Added tool\_directory\_request\_imports
 - Added tool\_directory\_see\_vendor\_insurances
 - Added tool\_directory\_update\_person
 - Added tool\_documents\_access\_private
 - Added tool\_documents\_destroy\_files\_and\_folders
 - Added tool\_documents\_move\_files\_and\_folders
 - Added tool\_documents\_rename\_files\_and\_folders
 - Added tool\_documents\_see\_recycle\_bin
 - Added tool\_documents\_set\_permissions
 - Added tool\_drawings\_upload\_and\_review\_drawings
 - Added tool\_drawings\_upload\_drawings
 - Added tool\_inspections\_can\_bulk\_create\_inspections
 - Added tool\_inspections\_can\_reinspect
 - Added tool\_inspections\_create\_edit\_inspection\_schedules
 - Added tool\_meetings\_add\_comment
 - Added tool\_meetings\_create
 - Added tool\_meetings\_delete\_own\_comment
 - Added tool\_meetings\_distribute
 - Added tool\_meetings\_edit
 - Added tool\_meetings\_manage\_meeting\_categories
 - Added tool\_meetings\_manage\_meeting\_items
 - Added tool\_meetings\_manage\_related\_items
 - Added tool\_meetings\_send\_emails
 - Added tool\_observations\_assign\_standard\_user
 - Added tool\_observations\_respond\_to\_vendor\_observation\_items
 - Added tool\_observations\_view\_vendor\_observation\_items
 - Added tool\_photos\_create\_photo\_album
 - Added tool\_photos\_delete\_photo\_album
 - Added tool\_photos\_reorder\_photo\_albums
 - Added tool\_photos\_view\_private\_photo\_album
 - Added tool\_prime\_contracts\_can\_import\_markups
 - Added tool\_prime\_contracts\_create\_prime\_contract
 - Added tool\_prime\_contracts\_delete\_prime\_contract
 - Added tool\_prime\_contracts\_update\_contract\_currency\_exchange\_rate
 - Added tool\_prime\_contracts\_update\_prime\_contract
 - Added tool\_prime\_contracts\_view\_payment\_application\_detail
 - Added tool\_punch\_list\_respond\_to\_vendor\_punch\_items
 - Added tool\_punch\_list\_view\_vendor\_punch\_items
 - Added tool\_rfis\_act\_as\_rfi\_manager
 - Added tool\_rfis\_mark\_official\_responses
 - Added tool\_rfis\_view\_private\_rfis
 - Added tool\_rfis\_view\_project\_rfi\_insights
 - Added tool\_schedule\_lookahead\_create
 - Added tool\_schedule\_lookahead\_delete
 - Added tool\_schedule\_lookahead\_task\_create
 - Added tool\_schedule\_lookahead\_task\_delete
 - Added tool\_schedule\_lookahead\_task\_update
 - Added tool\_schedule\_lookahead\_view
 - Added tool\_schedule\_lookahead\_view\_change\_history
 - Added tool\_schedule\_task\_update\_percent\_complete
 - Added tool\_specifications\_can\_configure
 - Added tool\_specifications\_can\_create
 - Added tool\_specifications\_can\_create\_specification\_set
 - Added tool\_specifications\_can\_delete\_pending\_specification\_uploads
 - Added tool\_specifications\_can\_destroy
 - Added tool\_specifications\_can\_download\_specification
 - Added tool\_specifications\_can\_email
 - Added tool\_specifications\_can\_export\_specification
 - Added tool\_specifications\_can\_manually\_create\_divisions
 - Added tool\_specifications\_can\_manually\_create\_spec\_sections
 - Added tool\_specifications\_can\_publish
 - Added tool\_specifications\_can\_relate\_items
 - Added tool\_specifications\_can\_review
 - Added tool\_specifications\_can\_show
 - Added tool\_specifications\_can\_show\_uploads
 - Added tool\_specifications\_can\_update
 - Added tool\_specifications\_can\_view\_all\_revision
 - Added tool\_specifications\_can\_view\_change\_history
 - Added tool\_specifications\_can\_view\_deleted\_specifications
 - Added tool\_submittals\_apply\_submittal\_workflow\_template
 - Added tool\_submittals\_create\_submittal
 - Added tool\_submittals\_create\_submittal\_package
 - Added tool\_submittals\_view\_private\_submittals
 - Added tool\_submittals\_view\_project\_submittal\_insights
 - Added tool\_timesheets\_review\_timesheets
 - Added tool\_transmittals\_view\_private\_transmittals"
- project\_permissions:

 - Added permission\_template\_id
- project\_role\_memberships:

 - Added updated\_at
- invoice\_compliance:

 - Added invoice\_compliance\_id
 - Added name
 - Added type
 - Added status
 - Added notes
 - Added attachment\_count
 - Added effective\_date
 - Added expiration\_date
 - Added last\_modified\_by
 - Added last\_modified\_date
- observation\_custom\_field\_configs:

 - Changed the Custom\_field\_definitions\_id format (e.g., 0\_60128 to 12345\_60128)
- observation\_custom\_fields:

 - Changed the Custom\_field\_definitions\_id format (e.g., 0\_60128 to 12345\_60128)

##### Analytics 2.0 Bug Fix (09/02/2025)

**Procore updated the following models (tables):**

- Estimate\_budget\_item\_included\_item:

 - Added wbs\_code\_id
- Estimate\_budget\_item:

 - Added wbs\_code\_id

##### Analytics 2.0 Data Updates (08/19/2025)

**Procore added the following models (tables):**

- Bid
- Bid\_form
- Bid\_item
- Bid\_package
- company\_permissions
- contact
- project\_contacts
- Project\_note
- project\_permissions
- Project\_task
- Project\_document
- assembly\_part
- estimating\_project\_custom\_field\_configs

**Procore updated the following models (tables):**

- observation\_custom\_fields:

 - Changed type\_id from int to bigint
- payments\_subtier\_waivers:

 - Changed payment\_subtier\_waiver\_id from bigint to string
- incident\_record:

 - Changed incident\_environmental\_type from boolean to string
- commitment\_change\_order\_line\_items:

 - Added commitment\_change\_order\_line\_items.quantity
 - Added commitment\_change\_order\_line\_items.tax\_code
 - Added commitment\_change\_order\_line\_items.uom
- commitments:

 - Added commitments.approved\_change\_orders
 - Added commitments.draft\_change\_orders
 - Added commitments.invoiced
 - Added commitments.pending\_change\_orders
 - Added commitments.pending\_revised\_contract\_amount
- owner\_invoice\_line\_item\_with\_markups:

 - Added owner\_invoice\_line\_item\_with\_markups.materials\_retainage\_released\_this\_period
 - Added owner\_invoice\_line\_item\_with\_markups.materials\_retainage\_released\_this\_period\_company\_currency
 - Added owner\_invoice\_line\_item\_with\_markups.materials\_retainage\_released\_this\_period\_project\_currency
- owner\_invoice\_line\_items:

 - Added owner\_invoice\_line\_items.materials\_retainage\_released\_this\_period
 - Added owner\_invoice\_line\_items.materials\_retainage\_released\_this\_period\_company\_currency
 - Added owner\_invoice\_line\_items.materials\_retainage\_released\_this\_period\_project\_currency
- owner\_invoice\_markup\_line\_items:

 - Added owner\_invoice\_markup\_line\_items.materials\_retainage\_released\_this\_period
 - Added owner\_invoice\_markup\_line\_items.materials\_retainage\_released\_this\_period\_company\_currency
 - Added owner\_invoice\_markup\_line\_items.materials\_retainage\_released\_this\_period\_project\_currency
- owner\_invoices:

 - Added owner\_invoices.created\_by\_id
- payments\_subtier\_waivers:

 - Added payments\_subtier\_waivers.waiver\_required
- subcontractor\_invoices:

 - Added subcontractor\_invoices.created\_by\_id
 - Added subcontractor\_invoices.total\_contract\_amount
- photo:

 - Added photo.uploaded\_by\_id
- assignments:

 - Added assignments.employee\_id
- time\_and\_material\_equipments:

 - Added time\_and\_material\_equipments.equipment\_id
 - Added time\_and\_material\_equipments.equipment\_identification\_number
 - Added time\_and\_material\_equipments.equipment\_name\_legacy
- time\_off:

 - Added time\_off.employee\_id
- timecard\_entries:

 - Added timecard\_entries.party\_employee\_id
 - Added timesheet\_id
- wp\_people:

 - Added wp\_people.party\_id
- wp\_role:

 - Added wp\_roles.audit\_transaction\_timestamp
 - Added wp\_roles.employee\_id
- Vendor:

 - Added avg\_company\_rating
- Estimating Project:

 - Added created\_by\_id
 - Added primary\_contact\_full\_address
- budget\_snapshot\_line\_item\_headers:

 - Added line\_items
- requests:

 - Added status
- wp\_people:

 - Added customer\_employee\_id
 - Added user\_id
- incident\_records:

 - Added affected\_user\_id

##### Analytics 2.0 Data Updates (07/22/2025)

**Procore added the following models (tables):**

- company\_project\_currency\_configurations
- assignment\_custom\_fields
- request\_custom\_fields
- wp\_people\_custom\_fields
- folder\_documents\_custom\_field\_configs
- folder\_documents\_custom\_fields
- task\_distribution\_member

**Procore updated the following models (tables):**

- project\_vendors:

 - Added project\_vendors.avg\_company\_rating
 - Added project\_vendors.invoice\_contact\_email\_address
 - Added project\_vendors.invoice\_contact\_full\_name
- vendors:

 - Added vendors.avg\_company\_rating
 - Added vendors.invoice\_contact\_email\_address
 - Added vendors.invoice\_contact\_full\_name
- direct\_costs:

 - Added direct\_costs.created\_by\_id
- payments\_subtiers:

 - Added payments\_subtiers.hired\_by\_company\_name
 - Added payments\_subtiers.tier
 - Added payments\_subtiers.tiering
- subcontractor\_invoices:

 - Added subcontractor\_invoices.early\_pay\_fee\_amount\_calculated
- incident\_record:

 - Added incident\_record.affected\_party\_id
 - Added incident\_record.affected\_party\_name
- inspection\_items:

 - Added inspection\_items.respondable
- inspection\_signature\_requests:

 - Added inspection\_signature\_requests.requested
 - Added inspection\_signature\_requests.requested\_login
- submittals:

 - Added submittals.source\_submittal\_id
 - Added submittals.specification\_area\_name
- actual\_production\_quantities:

 - Added actual\_production\_quantities.created\_by\_id
- budgeted\_production\_quantities:

 - Added budgeted\_production\_quantities.created\_by\_id
- equipment:

 - Added equipment.project\_id
- time\_and\_material\_entries:

 - Added time\_and\_material\_entries.created\_by\_id
- timecard\_entries:

 - Added timecard\_entries.created\_by\_id

##### Analytics 2.0 Data Updates (06/17/2025)

**Procore added the following models (tables):**

- Company\_folder\_documents
- Folder\_documents
- Folder\_watchers
- Equipment\_telematic
- wp\_project\_custom\_fields
- estimating\_project\_custom\_field\_configs

**Procore updated the following models (tables):**

- **Changes in subcontractor\_invoice\_line\_items:**

 - Added subcontractor\_invoice\_line\_items.adjusted\_materials\_previously\_stored
 - Added subcontractor\_invoice\_line\_items.adjusted\_materials\_previously\_stored\_company\_currency
 - Added subcontractor\_invoice\_line\_items.adjusted\_materials\_previously\_stored\_project\_currency
 - Added subcontractor\_invoice\_line\_items.adjusted\_materials\_retained\_previously
 - Added subcontractor\_invoice\_line\_items.adjusted\_materials\_retained\_previously\_company\_currency
 - Added subcontractor\_invoice\_line\_items.adjusted\_materials\_retained\_previously\_project\_currency
 - Added subcontractor\_invoice\_line\_items.gross\_amount
 - Added subcontractor\_invoice\_line\_items.gross\_amount\_company\_currency
 - Added subcontractor\_invoice\_line\_items.gross\_amount\_project\_currency
 - Added subcontractor\_invoice\_line\_items.net\_amount
 - Added subcontractor\_invoice\_line\_items.net\_amount\_company\_currency
 - Added subcontractor\_invoice\_line\_items.net\_amount\_project\_currency
 - Added subcontractor\_invoice\_line\_items.retainage\_new\_materials\_from\_percent
 - Added subcontractor\_invoice\_line\_items.retainage\_new\_materials\_from\_percent\_company\_currency
 - Added subcontractor\_invoice\_line\_items.retainage\_new\_materials\_from\_percent\_project\_currency
 - Added subcontractor\_invoice\_line\_items.total\_completed\_and\_stored\_to\_date\_from\_previous
 - Added subcontractor\_invoice\_line\_items.total\_completed\_and\_stored\_to\_date\_from\_previous\_company\_currency
 - Added subcontractor\_invoice\_line\_items.total\_completed\_and\_stored\_to\_date\_from\_previous\_project\_currency
 - Added subcontractor\_invoice\_line\_items.commitment\_line\_item\_id
 - Added subcontractor\_invoice\_line\_items.prime\_contract\_line\_item\_id
- **Changes in submittals:**

 - Added submittals.anticipated\_delivery\_date\_at\_close
 - Added submittals.remaining\_buffer\_time\_at\_close
 - Added submittals.workflow\_progress\_at\_close
 - Changes in wp\_people:
 - Added wp\_people.custom\_fields
- **Changes in wp\_projects:**

 - Added wp\_projects.custom\_fields
- **Changes in budget\_view\_details:**

 - Added budget\_view\_details.infojson\_currency\_conversion

##### Analytics 2.0 Data Updates (05/20/2025)

**Procore added the following models (tables):**

- project\_company\_comments
- tags

**Procore updated the following models (tables):**

- Changes in company\_comments:

 - Added company\_comments.audit\_transaction\_timestamp
 - Added company\_comments.rating
- Changes in company\_distribution\_groups:

 - Added company\_distribution\_groups.audit\_transaction\_timestamp
 - Added company\_distribution\_groups.project\_id
- Changes in project\_distribution\_groups:

 - Added project\_distribution\_groups.audit\_transaction\_timestamp
 - Added project\_distribution\_groups.company\_id
- Changes in project\_tools:

 - Added project\_tools.audit\_transaction\_timestamp
 - Added project\_tools.is\_active
- Changes in budget\_codes:

 - Added budget\_codes.production\_quantity\_code\_description
- Changes in drawing\_attachment:

 - Added drawing\_attachment.folder\_document\_id
- Changes in inspections:

 - Added inspections.closed\_at
- Changes in equipment:

 - Added equipment.status\_type
- Changes in field\_productivity:

 - Added field\_productivity.hours\_utilization\_enrp
 - Added field\_productivity.projected\_hours\_at\_completion\_enrp

##### Analytics 2.0 Data Updates (04/22/2025)

**Procore added the following models (tables):**

- early\_pay\_program
- early\_pay\_program\_enrollment
- task\_distribution\_member
- wp\_roles
- estimate\_budget\_item
- estimate\_budget\_item\_WBS\_value
- estimate\_budget\_included\_item
- procore\_analytics\_metadata

**Procore updated the following models (tables):**

- Changes in project\_role\_memberships:

 - Added: project\_role\_memberships.employee\_id
- Changes in project\_vendors:

 - Added: project\_vendors.cost\_codes
 - Added: project\_vendors.trades
- Changes in projects:

 - Added: projects.schedule\_last\_updated
 - Added: projects.schedule\_percent\_completion
- Changes in vendors:

 - Added: vendors.cost\_codes
 - Added: vendors.trades
- Changes in budget\_change\_adjustment\_line\_items:

 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_approved\_amount
 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_approved\_amount\_company\_currency
 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_approved\_amount\_project\_currency
 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_draft\_amount
 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_draft\_amount\_company\_currency
 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_draft\_amount\_project\_currency
 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_under\_review\_amount
 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_under\_review\_amount\_company\_currency
 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_under\_review\_amount\_project\_currency
- Changes in budget\_columns:

 - Added: budget\_columns.budget\_column\_id
- Changes in budget\_snapshot\_line\_item\_forecasts:

 - Added: budget\_snapshot\_line\_item\_forecasts.approval\_status
 - Added: budget\_snapshot\_line\_item\_forecasts.snapshot\_type
- Changes in budget\_snapshot\_line\_item\_headers:

 - Added budget\_snapshot\_line\_item\_headers.approval\_status
 - Added: budget\_snapshot\_line\_item\_headers.audit\_transaction\_timestamp
 - Added: budget\_snapshot\_line\_item\_headers.snapshot\_type
- Changes in budget\_snapshot\_line\_items:

 - Added budget\_snapshot\_line\_items.approval\_status
 - Added: budget\_snapshot\_line\_items.audit\_transaction\_timestamp
 - Added: budget\_snapshot\_line\_items.snapshot\_type
- Changes in change\_event\_line\_item\_with\_markups:

 - Added: change\_event\_line\_item\_with\_markups.links\_commitment\_contract\_cost
 - Added: change\_event\_line\_item\_with\_markups.links\_commitment\_pco\_cost
 - Added: change\_event\_line\_item\_with\_markups.links\_contract
 - Added: change\_event\_line\_item\_with\_markups.links\_edit
 - Added: change\_event\_line\_item\_with\_markups.links\_prime\_pco\_cost
 - Added: change\_event\_line\_item\_with\_markups.links\_rfq\_amount
 - Added: change\_event\_line\_item\_with\_markups.links\_rom
 - Added: change\_event\_line\_item\_with\_markups.links\_view
- Changes in commitment\_line\_items:

 - Added: commitment\_line\_items.contracts\_approved\_amount
 - Added: commitment\_line\_items.contracts\_approved\_amount\_company\_currency
 - Added: commitment\_line\_items.contracts\_approved\_amount\_project\_currency
 - Added: commitment\_line\_items.contracts\_complete\_amount
 - Added: commitment\_line\_items.contracts\_complete\_amount\_company\_currency
 - Added: commitment\_line\_items.contracts\_complete\_amount\_project\_currency
 - Added: commitment\_line\_items.contracts\_draft\_amount
 - Added: commitment\_line\_items.contracts\_draft\_amount\_company\_currency
 - Added: commitment\_line\_items.contracts\_draft\_amount\_project\_currency
 - Added: commitment\_line\_items.contracts\_out\_for\_signature\_amount
 - Added: commitment\_line\_items.contracts\_out\_for\_signature\_amount\_company\_currency
 - Added: commitment\_line\_items.contracts\_out\_for\_signature\_amount\_project\_currency
- Changes in commitments:

 - Added: commitments.global\_insurance\_compliance
 - Added: commitments.project\_insurance\_compliance
 - Added: commitments.remaining\_balance
 - Added: commitments.revised\_contract\_amount
- Changes in payments\_issued:

 - Added: payments\_issued.early\_pay\_fee\_amount
- Changes in payments\_project\_controls:

 - Added payments\_project\_controls.assigned\_early\_pay\_program
 - Added: payments\_project\_controls.audit\_transaction\_timestamp
 - Added: payments\_project\_controls.early\_pay\_program\_id
- Changes in payments\_subtier\_waivers:

 - Added: payments\_subtier\_waivers.joint\_check\_requisition
- Changes in payments\_subtiers:

 - Added payments\_subtiers.additional\_address\_information
 - Added: payments\_subtiers.address
 - Added: payments\_subtiers.amount\_billed\_to\_date
 - Added: payments\_subtiers.city
 - Added: payments\_subtiers.country
 - Added: payments\_subtiers.joint\_check\_future\_requisitions
 - Added: payments\_subtiers.kind\_of\_work
 - Added: payments\_subtiers.phone
 - Added: payments\_subtiers.state
 - Added: payments\_subtiers.subtier\_type
 - Added: payments\_subtiers.waiver\_contact\_email
 - Added: payments\_subtiers.zip
- Changes in prime\_contract\_change\_order\_requests:

 - Added: prime\_contract\_change\_order\_requests.schedule\_impact\_days
- Changes in prime\_contract\_change\_orders:

 - Added: prime\_contract\_change\_orders.schedule\_impact\_days
- Changes in prime\_contract\_potential\_change\_orders:

 - Added: prime\_contract\_potential\_change\_orders.schedule\_impact\_days
- Changes in subcontractor\_invoices:

 - Added: subcontractor\_invoices.early\_pay\_fee\_amount
 - Added: subcontractor\_invoices.early\_pay\_fee\_rate
 - Added: subcontractor\_invoices.early\_pay\_status
 - Added: subcontractor\_invoices.missed\_payment\_due\_date
 - Added: subcontractor\_invoices.original\_payment\_due
 - Added: subcontractor\_invoices.original\_payment\_due\_company\_currency
 - Added: subcontractor\_invoices.original\_payment\_due\_project\_currency
 - Added: subcontractor\_invoices.payment\_due\_date
- Changes in correspondence\_types:

 - Added: correspondence\_types.created\_at
- Changes in correspondence\_workflow\_steps:

 - Added: correspondence\_workflow\_steps.current\_step\_due\_date
- Changes in daily\_log\_accident\_custom\_fields:

 - Added: daily\_log\_accident\_custom\_fields.type\_id
- Changes in daily\_log\_completion:

 - Added: daily\_log\_completion.created\_at
- Changes in daily\_log\_construction\_report\_custom\_fields:

 - Added: daily\_log\_construction\_report\_custom\_fields.type\_id
- Changes in daily\_log\_delay\_custom\_fields:

 - Added: daily\_log\_delay\_custom\_fields.type\_id
- Changes in daily\_log\_delivery\_custom\_fields:

 - Added: daily\_log\_delivery\_custom\_fields.type\_id
- Changes in daily\_log\_dumpster\_custom\_fields:

 - Added: daily\_log\_dumpster\_custom\_fields.type\_id
- Changes in daily\_log\_equipment:

 - Added: daily\_log\_equipment.equipment\_id
 - Added: daily\_log\_equipment.equipment\_identification\_number
 - Added: daily\_log\_equipment.equipment\_name\_beta
- Changes in daily\_log\_equipment\_custom\_fields:

 - Added: daily\_log\_equipment\_custom\_fields.type\_id
- Changes in daily\_log\_inspection\_custom\_fields:

 - Added: daily\_log\_inspection\_custom\_fields.type\_id
- Changes in daily\_log\_manpower\_custom\_fields:

 - Added: daily\_log\_manpower\_custom\_fields.type\_id
- Changes in daily\_log\_plan\_revision\_custom\_fields:

 - Added: daily\_log\_plan\_revision\_custom\_fields.type\_id
- Changes in daily\_log\_productivity\_custom\_fields:

 - Added: daily\_log\_productivity\_custom\_fields.type\_id
- Changes in daily\_log\_scheduled\_work\_task:

 - Added: daily\_log\_scheduled\_work\_task.created\_at
- Changes in drawing\_revision:

 - Added: drawing\_revision.created\_at
- Changes in incident\_alert:

 - Added: incident\_alert.created\_at
 - Added: incident\_alert.updated\_at
- Changes in inspection\_distribution\_list:

 - Added: inspection\_distribution\_list.created\_at
 - Added: inspection\_distribution\_list.updated\_at
- Changes in inspection\_item\_signature\_requests:

 - Added: inspection\_item\_signature\_requests.created\_at
 - Added: inspection\_item\_signature\_requests.updated\_at
- Changes in inspection\_schedule\_assignees:

 - Added: inspection\_schedule\_assignees.created\_at
 - Added: inspection\_schedule\_assignees.updated\_at
- Changes in inspection\_schedule\_distribution\_list:

 - Added: inspection\_schedule\_distribution\_list.created\_at
 - Added: inspection\_schedule\_distribution\_list.updated\_at
- Changes in inspection\_schedules:

 - Added: inspection\_schedules.created\_at
 - Added: inspection\_schedules.equipment\_id
 - Added: inspection\_schedules.equipment\_identification\_number
 - Added: inspection\_schedules.equipment\_name
 - Added: inspection\_schedules.updated\_at
- Changes in meeting\_attendee:

 - Added: meeting\_attendee.created\_at
 - Added: meeting\_attendee.updated\_at
- Changes in meeting\_item\_assignee:

 - Added: meeting\_item\_assignee.updated\_at
- Changes in observation\_distribution\_member:

 - Added: observation\_distribution\_member.created\_at
- Changes in punch\_item:

 - Added: punch\_item.audit\_transaction\_timestamp
- Changes in punch\_item\_bic:

 - Added punch\_item\_bic.audit\_transaction\_timestamp
 - Added: punch\_item\_bic.ball\_in\_court\_role
- Changes in punch\_item\_custom\_fields:

 - Added: punch\_item\_custom\_fields.type\_id
- Changes in punch\_item\_distribution\_member:

 - Added punch\_item\_distribution\_member.audit\_transaction\_timestamp
- Changes in rfi\_assignees:

 - Added: rfi\_assignees.audit\_transaction\_timestamp
- Changes in rfi\_distributions:

 - Added rfi\_distributions.audit\_transaction\_timestamp
- Changes in rfi\_responses:

 - Added rfi\_responses.audit\_transaction\_timestamp
- Changes in rfis:

 - Added: rfis.audit\_transaction\_timestamp
 - Added: rfis.current\_revision
 - Added: rfis.revision
- Changes in rfis\_bic:

 - Added rfis\_bic.audit\_transaction\_timestamp
 - Added: rfis\_bic.ball\_in\_court\_role
- Changes in schedule\_calendar\_item:

 - Added: schedule\_calendar\_item.audit\_transaction\_timestamp
- Changes in schedule\_lookahead:

 - Added schedule\_lookahead.audit\_transaction\_timestamp
- Changes in schedule\_lookahead\_task:

 - Added: schedule\_lookahead\_task.audit\_transaction\_timestamp
- Changes in schedule\_task:

 - Added: schedule\_task.audit\_transaction\_timestamp
- Changes in schedule\_task\_changes:

 - Added: schedule\_task\_changes.audit\_transaction\_timestamp
- Changes in schedule\_task\_requests:

 - Added schedule\_task\_requests.audit\_transaction\_timestamp
- Changes in site\_instructions:

 - Added: site\_instructions.audit\_transaction\_timestamp
- Changes in specification\_sections:

 - Added specification\_sections.audit\_transaction\_timestamp
- Changes in submittal\_approvers:

 - Added submittal\_approvers.audit\_transaction\_timestamp
 - Added: submittal\_approvers.comments
- Changes in submittal\_ball\_in\_courts:

 - Added submittal\_ball\_in\_courts.audit\_transaction\_timestamp
 - Added: submittal\_ball\_in\_courts.response\_required
- Changes in submittal\_distributions:
- Added submittal\_distributions.audit\_transaction\_timestamp
- Changes in submittals:

 - Added: submittals.audit\_transaction\_timestamp
 - Added: submittals.closed\_at
- Changes in task:

 - Added: task.audit\_transaction\_timestamp
- Changes in task\_activity:

 - Added: task\_activity.audit\_transaction\_timestamp
- Changes in task\_assignee:

 - Added: task\_assignee.audit\_transaction\_timestamp
- Changes in equipment:

 - Added: equipment.rental\_end\_date
 - Added: equipment.rental\_start\_date
 - Added: equipment.vendor\_name
- Changes in field\_productivity:

 - Added: field\_productivity.cost\_code\_id
 - Added: field\_productivity.production\_quantity\_code

##### Analytics 2.0 Data Updates (03/18/2025)

**Procore added the following models (tables):**

- Budget Code Segments
- Layer WBS Values
- Layer Group WBS Values
- Estimate Adjustment

**Procore updated the following models (tables):**

- Changes in correspondence\_workflow\_steps

 - Added current\_step\_due\_date
 - Added current\_step\_name
- Changes in payments\_disbursements

 - Added owner\_invoices.tax\_applicable\_to\_this\_payment\_company\_currency
 - Added owner\_invoices.tax\_applicable\_to\_this\_payment\_project\_currency
- Changes in subcontractor\_invoice\_line\_items

 - Added payments\_disbursements.number
 - Added subcontractor\_invoice\_line\_items.total\_retainage\_company\_currency
 - Added subcontractor\_invoice\_line\_items.total\_retainage\_project\_currency
- Changes in action\_plan

 - Added action\_plan.audit\_transaction\_timestamp
- Changes in action\_plan\_approver

 - Added action\_plan\_approver.audit\_transaction\_timestamp
- Changes in action\_plan\_completed\_receiver

 - Added action\_plan\_completed\_receiver.audit\_transaction\_timestamp
- Changes in action\_plan\_line\_item

 - Added action\_plan\_line\_item.audit\_transaction\_timestamp
- Changes in action\_plan\_line\_item\_assignee

 - Added action\_plan\_line\_item\_assignee.audit\_transaction\_timestamp
- Changes in action\_plan\_line\_item\_record

 - Added action\_plan\_line\_item\_record.audit\_transaction\_timestamp
- Changes in action\_plan\_line\_item\_record\_request

 - Added action\_plan\_line\_item\_record\_request.audit\_transaction\_timestamp
- Changes in action\_plan\_line\_item\_reference

 - Added action\_plan\_line\_item\_reference.audit\_transaction\_timestamp
- Changes in drawing\_revision

 - Added drawing\_revision.is\_connected\_drawing
- Changes in incident\_record

 - Added incident\_record.affected\_person\_id
- Changes in observation

 - Added observation.created\_by\_company
- Changes in rfi\_responses

 - Added rfi\_responses.is\_most\_recent
- Changes in rfis\_bic

 - Added rfis\_bic.response\_required
- Changes in schedule\_task

 - Added schedule\_task.predecessor\_wbs\_list
 - Added schedule\_task.successor\_wbs\_list
- Changes in specification\_sections

 - `Added specification\_sections.specification\_area\_description
 - Added specification\_sections.specification\_area\_name
- Changes in submittal\_approvers

 - Added submittal\_approvers.previous\_due\_date
 - Added submittal\_approvers.previous\_returned\_date
 - Added submittal\_approvers.previous\_sent\_date
- Changes in wp\_projects

 - Added wp\_projects.categories
- Added users.audit\_transaction\_timestamp
- Added estimate\_layer\_groups.profit

##### Analytics 2.0 Data Updates (02/18/2025)

**Procore added the following models (tables):**

- Financial

 - payments\_permissions
 - payments\_disbursements
 - pay\_requirement\_settings
 - payments\_project\_controls
 - payments\_invites
 - payments\_agreements
 - payments\_received
- Project Management

 - connected\_rfi\_responses
 - connected\_rfis
 - daily\_log\_accident\_custom\_field\_configs
 - daily\_log\_accident\_custom\_fields
 - daily\_log\_delay\_custom\_field\_configs
 - daily\_log\_delay\_custom\_fields
 - daily\_log\_delivery\_custom\_field\_configs
 - daily\_log\_delivery\_custom\_fields
 - daily\_log\_dumpster\_custom\_field\_configs
 - daily\_log\_dumpster\_custom\_fields
 - daily\_log\_inspection\_custom\_field\_configs
 - daily\_log\_inspection\_custom\_fields
 - daily\_log\_phone\_call\_custom\_field\_configs
 - daily\_log\_phone\_call\_custom\_fields
 - daily\_log\_plan\_revision\_custom\_field\_configs
 - daily\_log\_plan\_revision\_custom\_fields
 - daily\_log\_productivity\_custom\_field\_configs
 - daily\_log\_productivity\_custom\_fields
 - daily\_log\_quantity\_custom\_field\_configs
 - daily\_log\_quantity\_custom\_fields
 - daily\_log\_safety\_violation\_custom\_field\_configs
 - daily\_log\_safety\_violation\_custom\_fields
 - daily\_log\_scheduled\_work\_custom\_field\_configs
 - daily\_log\_scheduled\_work\_custom\_fields
 - daily\_log\_waste\_custom\_field\_configs
 - daily\_log\_waste\_custom\_fields
 - inspection\_item\_references
 - schedule\_task\_changes
- Resource Planning

 - assignments
 - job titles
 - requests
 - time off
 - wp people
 - wp projects
 - groups
- Equipment

 - equipment
 - equipment project log
 - equipment timecard entry
- Estimating

 - estimating projects
 - estimate layers
 - estimate layer groups
 - estimating project custom fields

**Procore updated the following models (tables):**

- Changes in project\_vendor\_insurances.sql:

 - Added project\_vendor\_insurances.external\_origin\_data
 - Added project\_vendor\_insurances.external\_origin\_id
- Changes in projects.sql:

 - Added projects.code
 - Added projects.delivery\_method
 - Added projects.external\_origin\_data
 - Added projects.external\_origin\_id
 - Added projects.sector
 - Added projects.work\_scope
- Changes in users.sql:

 - Added users.abbreviated\_name
 - Added users.can\_push\_to\_accounting
 - Added users.company\_name
 - Added users.company\_permission\_template
 - Added users.external\_origin\_data
 - Added users.external\_origin\_id
 - Added users.login\_information\_id
 - Added users.origin\_id
 - Added users.origin\_name
- Changes in budget\_changes.sql:

 - Added budget\_changes.external\_origin\_data
 - Added budget\_changes.external\_origin\_id
- Changes in budget\_line\_items.sql:

 - Added budget\_line\_items.budget\_notes
- Changes in change\_events.sql:

 - Added change\_events.external\_origin\_data
 - Added change\_events.external\_origin\_id
- Changes in commitment\_change\_orders.sql:

 - Added commitment\_change\_orders.external\_origin\_data
 - Added commitment\_change\_orders.external\_origin\_id
- Changes in commitment\_line\_items.sql:

 - Added commitment\_line\_items.external\_origin\_data
 - Added commitment\_line\_items.external\_origin\_id
- Changes in direct\_cost\_line\_items.sql:

 - Added direct\_cost\_line\_items.external\_origin\_data
 - Added direct\_cost\_line\_items.external\_origin\_id
- Changes in direct\_costs.sql:

 - Added direct\_costs.external\_origin\_data
 - Added direct\_costs.external\_origin\_id
- Changes in owner\_invoice\_line\_item\_with\_markups.sql:

 - Added owner\_invoice\_line\_item\_with\_markups.external\_origin\_data
 - Added owner\_invoice\_line\_item\_with\_markups.external\_origin\_id
 - Added owner\_invoice\_line\_item\_with\_markups.materials\_presently\_stored\_qty
 - Added owner\_invoice\_line\_item\_with\_markups.name
 - Added owner\_invoice\_line\_item\_with\_markups.new\_materials\_stored\_qty
 - Added owner\_invoice\_line\_item\_with\_markups.previous\_materials\_stored\_qty
 - Added owner\_invoice\_line\_item\_with\_markups.prime\_contract\_id
- Changes in owner\_invoice\_line\_items.sql:

 - Added owner\_invoice\_line\_items.external\_origin\_data
 - Added owner\_invoice\_line\_items.external\_origin\_id
 - Added owner\_invoice\_line\_items.line\_type
 - Added owner\_invoice\_line\_items.markup\_id
 - Added owner\_invoice\_line\_items.materials\_presently\_stored\_qty
 - Added owner\_invoice\_line\_items.name
 - Added owner\_invoice\_line\_items.new\_materials\_stored\_qty
 - Added owner\_invoice\_line\_items.owner\_invoice\_line\_item\_with\_markup\_id
 - Added owner\_invoice\_line\_items.owner\_invoice\_markup\_line\_item\_id
 - Added owner\_invoice\_line\_items.previous\_materials\_stored\_qty
- Changes in owner\_invoice\_markup\_line\_items.sql:

 - Added owner\_invoice\_markup\_line\_items.approved\_changes
 - Added owner\_invoice\_markup\_line\_items.approved\_changes\_company\_currency
 - Added owner\_invoice\_markup\_line\_items.approved\_changes\_project\_currency
 - Added owner\_invoice\_markup\_line\_items.balance\_to\_finish
 - Added owner\_invoice\_markup\_line\_items.company\_id\_2
 - Added owner\_invoice\_markup\_line\_items.external\_origin\_data
 - Added owner\_invoice\_markup\_line\_items.external\_origin\_id
 - Added owner\_invoice\_markup\_line\_items.line\_type
 - Added owner\_invoice\_markup\_line\_items.materials\_presently\_stored\_qty
 - Added owner\_invoice\_markup\_line\_items.name
 - Added owner\_invoice\_markup\_line\_items.new\_materials\_stored\_qty
 - Added owner\_invoice\_markup\_line\_items.owner\_invoice\_line\_item\_id
 - Added owner\_invoice\_markup\_line\_items.owner\_invoice\_line\_item\_with\_markup\_id
 - Added owner\_invoice\_markup\_line\_items.previous\_materials\_stored\_qty
 - Added owner\_invoice\_markup\_line\_items.prime\_contract\_id
- Changes in owner\_invoices.sql:

 - Added owner\_invoices.external\_origin\_data
 - Added owner\_invoices.external\_origin\_id
 - Added owner\_invoices.tax\_applicable\_to\_this\_payment
- Changes in payments\_issued.sql:

 - Added payments\_issued.external\_origin\_data
 - Added payments\_issued.external\_origin\_id
- Changes in prime\_contract\_change\_order\_line\_items.sql:

 - Added prime\_contract\_change\_order\_line\_items.external\_origin\_data
 - Added prime\_contract\_change\_order\_line\_items.external\_origin\_id
- Changes in prime\_contract\_change\_order\_requests.sql:

 - Added prime\_contract\_change\_order\_requests.external\_origin\_data
 - Added prime\_contract\_change\_order\_requests.external\_origin\_id
- Changes in prime\_contract\_change\_orders.sql:

 - Added prime\_contract\_change\_orders.external\_origin\_data
 - Added prime\_contract\_change\_orders.external\_origin\_id
- Changes in prime\_contract\_line\_items.sql:

 - Added prime\_contract\_line\_items.external\_origin\_data
 - Added prime\_contract\_line\_items.external\_origin\_id
 - Added prime\_contract\_line\_items.vendor\_id
- Changes in prime\_contract\_potential\_change\_orders.sql:

 - Added prime\_contract\_potential\_change\_orders.external\_origin\_data
 - Added prime\_contract\_potential\_change\_orders.external\_origin\_id
- Changes in prime\_contracts.sql:

 - Added prime\_contracts.external\_origin\_data
- Added prime\_contracts.external\_origin\_id
- Changes in subcontractor\_invoice\_line\_items.sql:

 - Added subcontractor\_invoice\_line\_items.materials\_presently\_stored\_qty
 - Added subcontractor\_invoice\_line\_items.materials\_previously\_stored\_qty
 - Added subcontractor\_invoice\_line\_items.new\_materials\_qty
- Changes in subcontractor\_invoices.sql:

 - Added subcontractor\_invoices.external\_origin\_data
 - Added subcontractor\_invoices.external\_origin\_id
- Changes in inspections.sql:

 - Added inspections.equipment\_identification\_number
- Changes in rfi\_assignees.sql:

 - Added rfi\_assignees.forwarded\_by
- Changes in submittal\_approvers.sql:

 - Added submittal\_approvers.is\_last\_step
- Changes in equipment\_timecard\_entry.sql:

 - Added equipment\_timecard\_entry.equipment\_identification\_number
 - Added equipment\_timecard\_entry.equipment\_name

##### Analytics 2.0 Data Updates (01/21/2025)

**Procore has added the following models (tables):**

- inspection\_item\_references
- schedule\_task\_changes
- equipment
- equipment\_project\_log
- equipment\_timecard\_entry
- payments\_project\_controls
- payments\_invites
- payments\_agreements
- pay\_requirement\_settings

**Procore has updated the following models (tables):**

- company\_vendor\_insurances:

 - Added company\_vendor\_insurances.template\_name
- project\_role\_memberships:

 - Added project\_role\_memberships.user\_id
- budget\_change\_workflow\_steps:

 - Added budget\_change\_workflow\_steps.current\_step\_due\_date
- budget\_codes:

 - Deleted SELECT budget\_codes.budget\_code
 - Added SELECT budget\_codes.attribute\_1\_line\_item
 - Added budget\_codes.attribute\_1\_name
 - Added budget\_codes.attribute\_2\_line\_item
 - Added budget\_codes.attribute\_2\_name
 - Added budget\_codes.attribute\_3\_line\_item
 - Added budget\_codes.attribute\_3\_name
 - Added budget\_codes.budget\_code
- budget\_columns:

 - Added budget\_columns.created\_at
 - Added budget\_columns.updated\_at
- change\_event\_line\_item\_with\_markups:

 - Deleted SELECT change\_event\_line\_item\_with\_markups.budget\_days\_in\_stage
 - Added SELECT change\_event\_line\_item\_with\_markups.biller\_id
 - Added change\_event\_line\_item\_with\_markups.biller\_model\_name
 - Added change\_event\_line\_item\_with\_markups.biller\_name
 - Added change\_event\_line\_item\_with\_markups.budget\_days\_in\_stage
 - Added change\_event\_line\_item\_with\_markups.change\_event\_events\_id
 - Added change\_event\_line\_item\_with\_markups.change\_event\_status
 - Added change\_event\_line\_item\_with\_markups.change\_event\_title
 - Added change\_event\_line\_item\_with\_markups.contract\_id
 - Added change\_event\_line\_item\_with\_markups.contract\_number
 - Added change\_event\_line\_item\_with\_markups.contract\_title
 - Added change\_event\_line\_item\_with\_markups.estimated\_budget\_amount
 - Added change\_event\_line\_item\_with\_markups.estimated\_budget\_transfer\_amount
 - Added change\_event\_line\_item\_with\_markups.estimated\_cost\_amount
 - Added change\_event\_line\_item\_with\_markups.estimated\_cost\_amount\_company\_currency
 - Added change\_event\_line\_item\_with\_markups.estimated\_cost\_amount\_project\_currency
 - Added change\_event\_line\_item\_with\_markups.event\_scope
 - Added change\_event\_line\_item\_with\_markups.proposed\_contract\_id
 - Added change\_event\_line\_item\_with\_markups.proposed\_vendor\_id
 - Added change\_event\_line\_item\_with\_markups.source
 - Added change\_event\_line\_item\_with\_markups.vendor\_name
 - Added change\_event\_line\_item\_with\_markups.wbs\_code\_id
- commitment\_change\_order\_line\_items:

 - Added commitment\_change\_order\_line\_items.commitment\_change\_order\_request\_id
 - Added commitment\_change\_order\_line\_items.commitment\_potential\_change\_order\_id
- commitment\_change\_order\_workflow\_steps:

 - Added commitment\_change\_order\_workflow\_steps.current\_step\_due\_date
- commitment\_custom\_field\_configs:

 - Added commitment\_custom\_field\_configs.name
- commitment\_pco\_workflow\_steps:

 - Added commitment\_pco\_workflow\_steps.current\_step\_due\_date
- commitment\_workflow\_step\_occurrences:

 - Added commitment\_workflow\_step\_occurrences.current\_step\_due\_date
- contract\_compliance\_documents:

 - Added contract\_compliance\_documents.template\_name
- owner\_invoice\_workflow\_steps:

 - Added owner\_invoice\_workflow\_steps.current\_step\_due\_date
- owner\_invoices:

 - Added owner\_invoices.erp\_latest\_status
 - Added owner\_invoices.erp\_updated\_at
 - Added owner\_invoices.erp\_user\_name
 - Added owner\_invoices.synced\_with\_accounting
- payments\_beneficiaries:

 - Added payments\_beneficiaries.early\_pay\_classification
- prime\_contract\_change\_order\_line\_items:

 - Added prime\_contract\_change\_order\_line\_items.name
 - Added prime\_contract\_change\_order\_line\_items.prime\_contract\_change\_order\_request\_id
 - Added prime\_contract\_change\_order\_line\_items.prime\_contract\_potential\_change\_order\_id
- prime\_contract\_change\_order\_workflow\_steps:

 - Added prime\_contract\_change\_order\_workflow\_steps.current\_step\_due\_date
- prime\_contract\_pco\_workflow\_steps:

 - Added prime\_contract\_pco\_workflow\_steps.current\_step\_due\_date
- prime\_contract\_workflow\_steps:

 - Added prime\_contract\_workflow\_steps.current\_step\_due\_date
- subcontractor\_invoice\_line\_items:

 - Added subcontractor\_invoice\_line\_items.total\_retainage
- subcontractor\_invoice\_workflow\_steps:

 - Added subcontractor\_invoice\_workflow\_steps.current\_step\_due\_date
- action\_plan\_custom\_fields:

 - Added action\_plan\_custom\_fields.type\_id
- action\_plan\_line\_item\_record:

 - Added action\_plan\_line\_item\_record.action\_plan\_line\_item\_record\_resource\_url
- correspondence\_custom\_fields:

 - Added correspondence\_custom\_fields.type\_id
- correspondence\_response\_attachments:

 - Added correspondence\_response\_attachments.type\_id
- correspondence\_schedule\_tasks:

 - Added correspondence\_schedule\_tasks.type\_id
- correspondence\_workflow\_responses:

 - Added correspondence\_workflow\_responses.type\_id
- correspondence\_workflow\_steps:

 - Added correspondence\_workflow\_steps.type\_id
- daily\_log\_accident:

 - Added daily\_log\_accident.daily\_log\_completion\_id
- daily\_log\_construction\_reports:

 - Added daily\_log\_construction\_reports.daily\_log\_completion\_id
- daily\_log\_delay:

 - Added daily\_log\_delay.daily\_log\_completion\_id
- daily\_log\_delivery:

 - Added daily\_log\_delivery.daily\_log\_completion\_id
- daily\_log\_dumpster:

 - Added daily\_log\_dumpster.daily\_log\_completion\_id
- daily\_log\_equipment:

 - Added daily\_log\_equipment.daily\_log\_completion\_id
- daily\_log\_inspection:

 - Added daily\_log\_inspection.daily\_log\_completion\_id
- daily\_log\_manpower:

 - Added daily\_log\_manpower.daily\_log\_completion\_id
- daily\_log\_note:

 - Added daily\_log\_note.daily\_log\_completion\_id
- daily\_log\_observed\_weather\_condition:

 - Added daily\_log\_observed\_weather\_condition.daily\_log\_completion\_id
- daily\_log\_phone\_call:

 - Added daily\_log\_phone\_call.daily\_log\_completion\_id
- daily\_log\_plan\_revision:

 - Added daily\_log\_plan\_revision.daily\_log\_completion\_id
- daily\_log\_productivity:

 - Added daily\_log\_productivity.daily\_log\_completion\_id
- daily\_log\_quantity:

 - Added daily\_log\_quantity.daily\_log\_completion\_id
- daily\_log\_safety\_violation:

 - Added daily\_log\_safety\_violation.daily\_log\_completion\_id
- daily\_log\_scheduled\_work:

 - Added daily\_log\_scheduled\_work.daily\_log\_completion\_id
- daily\_log\_scheduled\_work\_task:

 - Added daily\_log\_scheduled\_work\_task.daily\_log\_completion\_id
 - Added daily\_log\_scheduled\_work\_task.schedule\_task\_id
- daily\_log\_visitor:

 - Added daily\_log\_visitor.daily\_log\_completion\_id
- daily\_log\_waste:

 - Added daily\_log\_waste.daily\_log\_completion\_id
- inspection\_custom\_fields:
- Added inspection\_custom\_fields.type\_id
- inspection\_item\_signature\_requests:

 - Added inspection\_item\_signature\_requests.inspection\_schedule\_id
- inspection\_items:

 - Added inspection\_items.position\_number
- inspection\_schedules:

 - Added inspection\_schedules.ends\_at
 - Added inspection\_schedules.starts\_at
- inspections:

 - Added inspections.equipment\_id
 - Added inspections.equipment\_name
- observation\_custom\_field\_configs:

 - Added observation\_custom\_field\_configs.observation\_type\_id
 - Added observation\_custom\_field\_configs.type\_id
- observation\_custom\_fields:

 - Added observation\_custom\_fields.type\_id
- punch\_item\_bic:

 - Added punch\_item\_bic.punch\_item\_bic\_id
- rfis\_bic:

 - Added rfis\_bic.rfi\_bic\_id
- schedule\_lookahead\_task:

 - Added schedule\_lookahead\_task.task\_id\_comp
- schedule\_task:

 - Added schedule\_task.task\_id
- submittal\_ball\_in\_courts:

 - Added submittal\_ball\_in\_courts.company\_name
 - Added submittal\_ball\_in\_courts.role
- submittals:

 - Added submittals.ball\_in\_court\_role
 - Added submittals.paused
- actual\_production\_quantities:

 - Added actual\_production\_quantities.wbs\_code\_id
- budget\_change\_production\_quantities:

 - Deleted SELECT budget\_change\_production\_quantities.budget\_change\_production\_quantity\_id
 - Added SELECT budget\_change\_production\_quantities.budget\_change\_id
 - Added budget\_change\_production\_quantities.budget\_change\_production\_quantity\_id
 - Added budget\_change\_production\_quantities.wbs\_code\_id
- prime\_potential\_change\_order\_production\_quantities:

 - Added prime\_potential\_change\_order\_production\_quantities.prime\_contract\_change\_order\_id
 - Added prime\_potential\_change\_order\_production\_quantities.wbs\_code\_id
- project:

 - Added project.code
- owner\_invoices:

 - Added owner\_invoices.Tax\_Applicable\_To\_This\_Payment
- timecard\_entries:

 - Added timecard\_entries.user\_id

##### Analytics 2.0 Data Updates (12/17/2024)

**Procore has added (current\_step\_due\_date) to the following models (tables):**

- budget\_change\_workflow\_steps
- commitment\_change\_order\_workflow\_steps
- commitment\_pco\_workflow\_responses
- commitment\_workflow\_step\_occurrences
- owner\_invoice\_workflow\_steps
- prime\_contract\_change\_order\_workflow\_steps
- prime\_contract\_pco\_workflow\_steps
- prime\_contract\_workflow\_steps
- subcontractor\_invoice\_workflow\_steps

**Procore has added the following fields:**

- actual\_production\_quantities.wbs\_code\_id
- timecard\_entries.user\_id

## Recent Changes

#### Procore Analytics 2.0 Data Updates (08/19/2025)

**Procore added the following models (tables):**

- Bid
- Bid\_form
- Bid\_item
- Bid\_package
- company\_permissions
- contact
- project\_contacts
- Project\_note
- project\_permissions
- Project\_task
- Project\_document
- assembly\_part
- estimating\_project\_custom\_field\_configs

**Procore updated the following models (tables):**

- observation\_custom\_fields:

 - Changed type\_id from int to bigint
- payments\_subtier\_waivers:

 - Changed payment\_subtier\_waiver\_id from bigint to string
- incident\_record:

 - Changed incident\_environmental\_type from boolean to string
- commitment\_change\_order\_line\_items:

 - Added commitment\_change\_order\_line\_items.quantity
 - Added commitment\_change\_order\_line\_items.tax\_code
 - Added commitment\_change\_order\_line\_items.uom
- commitments:

 - Added commitments.approved\_change\_orders
 - Added commitments.draft\_change\_orders
 - Added commitments.invoiced
 - Added commitments.pending\_change\_orders
 - Added commitments.pending\_revised\_contract\_amount
- owner\_invoice\_line\_item\_with\_markups:

 - Added owner\_invoice\_line\_item\_with\_markups.materials\_retainage\_released\_this\_period
 - Added owner\_invoice\_line\_item\_with\_markups.materials\_retainage\_released\_this\_period\_company\_currency
 - Added owner\_invoice\_line\_item\_with\_markups.materials\_retainage\_released\_this\_period\_project\_currency
- owner\_invoice\_line\_items:

 - Added owner\_invoice\_line\_items.materials\_retainage\_released\_this\_period
 - Added owner\_invoice\_line\_items.materials\_retainage\_released\_this\_period\_company\_currency
 - Added owner\_invoice\_line\_items.materials\_retainage\_released\_this\_period\_project\_currency
- owner\_invoice\_markup\_line\_items:

 - Added owner\_invoice\_markup\_line\_items.materials\_retainage\_released\_this\_period
 - Added owner\_invoice\_markup\_line\_items.materials\_retainage\_released\_this\_period\_company\_currency
 - Added owner\_invoice\_markup\_line\_items.materials\_retainage\_released\_this\_period\_project\_currency
- owner\_invoices:

 - Added owner\_invoices.created\_by\_id
- payments\_subtier\_waivers:

 - Added payments\_subtier\_waivers.waiver\_required
- subcontractor\_invoices:

 - Added subcontractor\_invoices.created\_by\_id
 - Added subcontractor\_invoices.total\_contract\_amount
- photo:

 - Added photo.uploaded\_by\_id
- assignments:

 - Added assignments.employee\_id
- time\_and\_material\_equipments:

 - Added time\_and\_material\_equipments.equipment\_id
 - Added time\_and\_material\_equipments.equipment\_identification\_number
 - Added time\_and\_material\_equipments.equipment\_name\_legacy
- time\_off:

 - Added time\_off.employee\_id
- timecard\_entries:

 - Added timecard\_entries.party\_employee\_id
 - Added timesheet\_id
- wp\_people:

 - Added wp\_people.party\_id
- wp\_role:

 - Added wp\_roles.audit\_transaction\_timestamp
 - Added wp\_roles.employee\_id
- Vendor:

 - Added avg\_company\_rating
- Estimating Project:

 - Added created\_by\_id
 - Added primary\_contact\_full\_address
- budget\_snapshot\_line\_item\_headers:

 - Added line\_items
- requests:

 - Added status
- wp\_people:

 - Added customer\_employee\_id
 - Added user\_id
- incident\_records:

 - Added affected\_user\_id

#### Procore Analytics 2.0 Data Updates (07/22/2025)

**Procore added the following models (tables):**

- company\_project\_currency\_configurations
- assignment\_custom\_fields
- request\_custom\_fields
- wp\_people\_custom\_fields
- folder\_documents\_custom\_field\_configs
- folder\_documents\_custom\_fields
- task\_distribution\_member

**Procore updated the following models (tables):**

- project\_vendors:

 - Added project\_vendors.avg\_company\_rating
 - Added project\_vendors.invoice\_contact\_email\_address
 - Added project\_vendors.invoice\_contact\_full\_name
- vendors:

 - Added vendors.avg\_company\_rating
 - Added vendors.invoice\_contact\_email\_address
 - Added vendors.invoice\_contact\_full\_name
- direct\_costs:

 - Added direct\_costs.created\_by\_id
- payments\_subtiers:

 - Added payments\_subtiers.hired\_by\_company\_name
 - Added payments\_subtiers.tier
 - Added payments\_subtiers.tiering
- subcontractor\_invoices:

 - Added subcontractor\_invoices.early\_pay\_fee\_amount\_calculated
- incident\_record:

 - Added incident\_record.affected\_party\_id
 - Added incident\_record.affected\_party\_name
- inspection\_items:

 - Added inspection\_items.respondable
- inspection\_signature\_requests:

 - Added inspection\_signature\_requests.requested
 - Added inspection\_signature\_requests.requested\_login
- submittals:

 - Added submittals.source\_submittal\_id
 - Added submittals.specification\_area\_name
- actual\_production\_quantities:

 - Added actual\_production\_quantities.created\_by\_id
- budgeted\_production\_quantities:

 - Added budgeted\_production\_quantities.created\_by\_id
- equipment:

 - Added equipment.project\_id
- time\_and\_material\_entries:

 - Added time\_and\_material\_entries.created\_by\_id
- timecard\_entries:

 - Added timecard\_entries.created\_by\_id

#### Procore Analytics 2.0 Data Updates (06/17/2025)

**Procore added the following models (tables):**

- Company\_folder\_documents
- Folder\_documents
- Folder\_watchers
- Equipment\_telematic
- wp\_project\_custom\_fields
- estimating\_project\_custom\_field\_configs

**Procore updated the following models (tables):**

- **Changes in subcontractor\_invoice\_line\_items:**

 - Added subcontractor\_invoice\_line\_items.adjusted\_materials\_previously\_stored
 - Added subcontractor\_invoice\_line\_items.adjusted\_materials\_previously\_stored\_company\_currency
 - Added subcontractor\_invoice\_line\_items.adjusted\_materials\_previously\_stored\_project\_currency
 - Added subcontractor\_invoice\_line\_items.adjusted\_materials\_retained\_previously
 - Added subcontractor\_invoice\_line\_items.adjusted\_materials\_retained\_previously\_company\_currency
 - Added subcontractor\_invoice\_line\_items.adjusted\_materials\_retained\_previously\_project\_currency
 - Added subcontractor\_invoice\_line\_items.gross\_amount
 - Added subcontractor\_invoice\_line\_items.gross\_amount\_company\_currency
 - Added subcontractor\_invoice\_line\_items.gross\_amount\_project\_currency
 - Added subcontractor\_invoice\_line\_items.net\_amount
 - Added subcontractor\_invoice\_line\_items.net\_amount\_company\_currency
 - Added subcontractor\_invoice\_line\_items.net\_amount\_project\_currency
 - Added subcontractor\_invoice\_line\_items.retainage\_new\_materials\_from\_percent
 - Added subcontractor\_invoice\_line\_items.retainage\_new\_materials\_from\_percent\_company\_currency
 - Added subcontractor\_invoice\_line\_items.retainage\_new\_materials\_from\_percent\_project\_currency
 - Added subcontractor\_invoice\_line\_items.total\_completed\_and\_stored\_to\_date\_from\_previous
 - Added subcontractor\_invoice\_line\_items.total\_completed\_and\_stored\_to\_date\_from\_previous\_company\_currency
 - Added subcontractor\_invoice\_line\_items.total\_completed\_and\_stored\_to\_date\_from\_previous\_project\_currency
 - Added subcontractor\_invoice\_line\_items.commitment\_line\_item\_id
 - Added subcontractor\_invoice\_line\_items.prime\_contract\_line\_item\_id
- **Changes in submittals:**

 - Added submittals.anticipated\_delivery\_date\_at\_close
 - Added submittals.remaining\_buffer\_time\_at\_close
 - Added submittals.workflow\_progress\_at\_close
 - Changes in wp\_people:
 - Added wp\_people.custom\_fields
- **Changes in wp\_projects:**

 - Added wp\_projects.custom\_fields
- **Changes in budget\_view\_details:**

 - Added budget\_view\_details.infojson\_currency\_conversion

#### Procore Analytics 2.0 Data Updates (05/20/2025)

**Procore added the following models (tables):**

- project\_company\_comments
- tags

**Procore updated the following models (tables):**

- Changes in company\_comments:

 - Added company\_comments.audit\_transaction\_timestamp
 - Added company\_comments.rating
- Changes in company\_distribution\_groups:

 - Added company\_distribution\_groups.audit\_transaction\_timestamp
 - Added company\_distribution\_groups.project\_id
- Changes in project\_distribution\_groups:

 - Added project\_distribution\_groups.audit\_transaction\_timestamp
 - Added project\_distribution\_groups.company\_id
- Changes in project\_tools:

 - Added project\_tools.audit\_transaction\_timestamp
 - Added project\_tools.is\_active
- Changes in budget\_codes:

 - Added budget\_codes.production\_quantity\_code\_description
- Changes in drawing\_attachment:

 - Added drawing\_attachment.folder\_document\_id
- Changes in inspections:

 - Added inspections.closed\_at
- Changes in equipment:

 - Added equipment.status\_type
- Changes in field\_productivity:

 - Added field\_productivity.hours\_utilization\_enrp
 - Added field\_productivity.projected\_hours\_at\_completion\_enrp

#### Procore Analytics 2.0 Data Updates (04/22/2025)

**Procore added the following models (tables):**

- budget\_forecasts
- early\_pay\_program
- early\_pay\_program\_enrollment
- task\_distribution\_member
- wp\_roles
- estimate\_budget\_item
- estimate\_budget\_item\_WBS\_value
- estimate\_budget\_included\_item
- procore\_analytics\_metadata

**Procore updated the following models (tables):**

- Changes in project\_role\_memberships:

 - Added: project\_role\_memberships.employee\_id
- Changes in project\_vendors:

 - Added: project\_vendors.cost\_codes
 - Added: project\_vendors.trades
- Changes in projects:

 - Added: projects.schedule\_last\_updated
 - Added: projects.schedule\_percent\_completion
- Changes in vendors:

 - Added: vendors.cost\_codes
 - Added: vendors.trades
- Changes in budget\_change\_adjustment\_line\_items:

 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_approved\_amount
 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_approved\_amount\_company\_currency
 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_approved\_amount\_project\_currency
 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_draft\_amount
 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_draft\_amount\_company\_currency
 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_draft\_amount\_project\_currency
 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_under\_review\_amount
 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_under\_review\_amount\_company\_currency
 - Added: budget\_change\_adjustment\_line\_items.budget\_changes\_under\_review\_amount\_project\_currency
- Changes in budget\_columns:

 - Added: budget\_columns.budget\_column\_id
- Changes in budget\_snapshot\_line\_item\_forecasts:

 - Added: budget\_snapshot\_line\_item\_forecasts.approval\_status
 - Added: budget\_snapshot\_line\_item\_forecasts.snapshot\_type
- Changes in budget\_snapshot\_line\_item\_headers:

 - Added budget\_snapshot\_line\_item\_headers.approval\_status
 - Added: budget\_snapshot\_line\_item\_headers.audit\_transaction\_timestamp
 - Added: budget\_snapshot\_line\_item\_headers.snapshot\_type
- Changes in budget\_snapshot\_line\_items:

 - Added budget\_snapshot\_line\_items.approval\_status
 - Added: budget\_snapshot\_line\_items.audit\_transaction\_timestamp
 - Added: budget\_snapshot\_line\_items.snapshot\_type
- Changes in change\_event\_line\_item\_with\_markups:

 - Added: change\_event\_line\_item\_with\_markups.links\_commitment\_contract\_cost
 - Added: change\_event\_line\_item\_with\_markups.links\_commitment\_pco\_cost
 - Added: change\_event\_line\_item\_with\_markups.links\_contract
 - Added: change\_event\_line\_item\_with\_markups.links\_edit
 - Added: change\_event\_line\_item\_with\_markups.links\_prime\_pco\_cost
 - Added: change\_event\_line\_item\_with\_markups.links\_rfq\_amount
 - Added: change\_event\_line\_item\_with\_markups.links\_rom
 - Added: change\_event\_line\_item\_with\_markups.links\_view
- Changes in commitment\_line\_items:

 - Added: commitment\_line\_items.contracts\_approved\_amount
 - Added: commitment\_line\_items.contracts\_approved\_amount\_company\_currency
 - Added: commitment\_line\_items.contracts\_approved\_amount\_project\_currency
 - Added: commitment\_line\_items.contracts\_complete\_amount
 - Added: commitment\_line\_items.contracts\_complete\_amount\_company\_currency
 - Added: commitment\_line\_items.contracts\_complete\_amount\_project\_currency
 - Added: commitment\_line\_items.contracts\_draft\_amount
 - Added: commitment\_line\_items.contracts\_draft\_amount\_company\_currency
 - Added: commitment\_line\_items.contracts\_draft\_amount\_project\_currency
 - Added: commitment\_line\_items.contracts\_out\_for\_signature\_amount
 - Added: commitment\_line\_items.contracts\_out\_for\_signature\_amount\_company\_currency
 - Added: commitment\_line\_items.contracts\_out\_for\_signature\_amount\_project\_currency
- Changes in commitments:

 - Added: commitments.global\_insurance\_compliance
 - Added: commitments.project\_insurance\_compliance
 - Added: commitments.remaining\_balance
 - Added: commitments.revised\_contract\_amount
- Changes in payments\_issued:

 - Added: payments\_issued.early\_pay\_fee\_amount
- Changes in payments\_project\_controls:

 - Added payments\_project\_controls.assigned\_early\_pay\_program
 - Added: payments\_project\_controls.audit\_transaction\_timestamp
 - Added: payments\_project\_controls.early\_pay\_program\_id
- Changes in payments\_subtier\_waivers:

 - Added: payments\_subtier\_waivers.joint\_check\_requisition
- Changes in payments\_subtiers:

 - Added payments\_subtiers.additional\_address\_information
 - Added: payments\_subtiers.address
 - Added: payments\_subtiers.amount\_billed\_to\_date
 - Added: payments\_subtiers.city
 - Added: payments\_subtiers.country
 - Added: payments\_subtiers.joint\_check\_future\_requisitions
 - Added: payments\_subtiers.kind\_of\_work
 - Added: payments\_subtiers.phone
 - Added: payments\_subtiers.state
 - Added: payments\_subtiers.subtier\_type
 - Added: payments\_subtiers.waiver\_contact\_email
 - Added: payments\_subtiers.zip
- Changes in prime\_contract\_change\_order\_requests:

 - Added: prime\_contract\_change\_order\_requests.schedule\_impact\_days
- Changes in prime\_contract\_change\_orders:

 - Added: prime\_contract\_change\_orders.schedule\_impact\_days
- Changes in prime\_contract\_potential\_change\_orders:

 - Added: prime\_contract\_potential\_change\_orders.schedule\_impact\_days
- Changes in subcontractor\_invoices:

 - Added: subcontractor\_invoices.early\_pay\_fee\_amount
 - Added: subcontractor\_invoices.early\_pay\_fee\_rate
 - Added: subcontractor\_invoices.early\_pay\_status
 - Added: subcontractor\_invoices.missed\_payment\_due\_date
 - Added: subcontractor\_invoices.original\_payment\_due
 - Added: subcontractor\_invoices.original\_payment\_due\_company\_currency
 - Added: subcontractor\_invoices.original\_payment\_due\_project\_currency
 - Added: subcontractor\_invoices.payment\_due\_date
- Changes in correspondence\_types:

 - Added: correspondence\_types.created\_at
- Changes in correspondence\_workflow\_steps:

 - Added: correspondence\_workflow\_steps.current\_step\_due\_date
- Changes in daily\_log\_accident\_custom\_fields:

 - Added: daily\_log\_accident\_custom\_fields.type\_id
- Changes in daily\_log\_completion:

 - Added: daily\_log\_completion.created\_at
- Changes in daily\_log\_construction\_report\_custom\_fields:

 - Added: daily\_log\_construction\_report\_custom\_fields.type\_id
- Changes in daily\_log\_delay\_custom\_fields:

 - Added: daily\_log\_delay\_custom\_fields.type\_id
- Changes in daily\_log\_delivery\_custom\_fields:

 - Added: daily\_log\_delivery\_custom\_fields.type\_id
- Changes in daily\_log\_dumpster\_custom\_fields:

 - Added: daily\_log\_dumpster\_custom\_fields.type\_id
- Changes in daily\_log\_equipment:

 - Added: daily\_log\_equipment.equipment\_id
 - Added: daily\_log\_equipment.equipment\_identification\_number
 - Added: daily\_log\_equipment.equipment\_name\_beta
- Changes in daily\_log\_equipment\_custom\_fields:

 - Added: daily\_log\_equipment\_custom\_fields.type\_id
- Changes in daily\_log\_inspection\_custom\_fields:

 - Added: daily\_log\_inspection\_custom\_fields.type\_id
- Changes in daily\_log\_manpower\_custom\_fields:

 - Added: daily\_log\_manpower\_custom\_fields.type\_id
- Changes in daily\_log\_plan\_revision\_custom\_fields:

 - Added: daily\_log\_plan\_revision\_custom\_fields.type\_id
- Changes in daily\_log\_productivity\_custom\_fields:

 - Added: daily\_log\_productivity\_custom\_fields.type\_id
- Changes in daily\_log\_scheduled\_work\_task:

 - Added: daily\_log\_scheduled\_work\_task.created\_at
- Changes in drawing\_revision:

 - Added: drawing\_revision.created\_at
- Changes in incident\_alert:

 - Added: incident\_alert.created\_at
 - Added: incident\_alert.updated\_at
- Changes in inspection\_distribution\_list:

 - Added: inspection\_distribution\_list.created\_at
 - Added: inspection\_distribution\_list.updated\_at
- Changes in inspection\_item\_signature\_requests:

 - Added: inspection\_item\_signature\_requests.created\_at
 - Added: inspection\_item\_signature\_requests.updated\_at
- Changes in inspection\_schedule\_assignees:

 - Added: inspection\_schedule\_assignees.created\_at
 - Added: inspection\_schedule\_assignees.updated\_at
- Changes in inspection\_schedule\_distribution\_list:

 - Added: inspection\_schedule\_distribution\_list.created\_at
 - Added: inspection\_schedule\_distribution\_list.updated\_at
- Changes in inspection\_schedules:

 - Added: inspection\_schedules.created\_at
 - Added: inspection\_schedules.equipment\_id
 - Added: inspection\_schedules.equipment\_identification\_number
 - Added: inspection\_schedules.equipment\_name
 - Added: inspection\_schedules.updated\_at
- Changes in meeting\_attendee:

 - Added: meeting\_attendee.created\_at
 - Added: meeting\_attendee.updated\_at
- Changes in meeting\_item\_assignee:

 - Added: meeting\_item\_assignee.updated\_at
- Changes in observation\_distribution\_member:

 - Added: observation\_distribution\_member.created\_at
- Changes in punch\_item:

 - Added: punch\_item.audit\_transaction\_timestamp
- Changes in punch\_item\_bic:

 - Added punch\_item\_bic.audit\_transaction\_timestamp
 - Added: punch\_item\_bic.ball\_in\_court\_role
- Changes in punch\_item\_custom\_fields:

 - Added: punch\_item\_custom\_fields.type\_id
- Changes in punch\_item\_distribution\_member:

 - Added punch\_item\_distribution\_member.audit\_transaction\_timestamp
- Changes in rfi\_assignees:

 - Added: rfi\_assignees.audit\_transaction\_timestamp
- Changes in rfi\_distributions:

 - Added rfi\_distributions.audit\_transaction\_timestamp
- Changes in rfi\_responses:

 - Added rfi\_responses.audit\_transaction\_timestamp
- Changes in rfis:

 - Added: rfis.audit\_transaction\_timestamp
 - Added: rfis.current\_revision
 - Added: rfis.revision
- Changes in rfis\_bic:

 - Added rfis\_bic.audit\_transaction\_timestamp
 - Added: rfis\_bic.ball\_in\_court\_role
- Changes in schedule\_calendar\_item:

 - Added: schedule\_calendar\_item.audit\_transaction\_timestamp
- Changes in schedule\_lookahead:

 - Added schedule\_lookahead.audit\_transaction\_timestamp
- Changes in schedule\_lookahead\_task:

 - Added: schedule\_lookahead\_task.audit\_transaction\_timestamp
- Changes in schedule\_task:

 - Added: schedule\_task.audit\_transaction\_timestamp
- Changes in schedule\_task\_changes:

 - Added: schedule\_task\_changes.audit\_transaction\_timestamp
- Changes in schedule\_task\_requests:

 - Added schedule\_task\_requests.audit\_transaction\_timestamp
- Changes in site\_instructions:

 - Added: site\_instructions.audit\_transaction\_timestamp
- Changes in specification\_sections:

 - Added specification\_sections.audit\_transaction\_timestamp
- Changes in submittal\_approvers:

 - Added submittal\_approvers.audit\_transaction\_timestamp
 - Added: submittal\_approvers.comments
- Changes in submittal\_ball\_in\_courts:

 - Added submittal\_ball\_in\_courts.audit\_transaction\_timestamp
 - Added: submittal\_ball\_in\_courts.response\_required
- Changes in submittal\_distributions:
- Added submittal\_distributions.audit\_transaction\_timestamp
- Changes in submittals:

 - Added: submittals.audit\_transaction\_timestamp
 - Added: submittals.closed\_at
- Changes in task:

 - Added: task.audit\_transaction\_timestamp
- Changes in task\_activity:

 - Added: task\_activity.audit\_transaction\_timestamp
- Changes in task\_assignee:

 - Added: task\_assignee.audit\_transaction\_timestamp
- Changes in equipment:

 - Added: equipment.rental\_end\_date
 - Added: equipment.rental\_start\_date
 - Added: equipment.vendor\_name
- Changes in field\_productivity:

 - Added: field\_productivity.cost\_code\_id
 - Added: field\_productivity.production\_quantity\_code

#### Procore Analytics 2.0 Data Updates (03/18/2025)

**Procore added the following models (tables):**

- Budget Code Segments
- Layer WBS Values
- Layer Group WBS Values
- Estimate Adjustment

**Procore updated the following models (tables):**

- Changes in correspondence\_workflow\_steps

 - Added current\_step\_due\_date
 - Added current\_step\_name
- Changes in payments\_disbursements

 - Added owner\_invoices.tax\_applicable\_to\_this\_payment\_company\_currency
 - Added owner\_invoices.tax\_applicable\_to\_this\_payment\_project\_currency
- Changes in subcontractor\_invoice\_line\_items

 - Added payments\_disbursements.number
 - Added subcontractor\_invoice\_line\_items.total\_retainage\_company\_currency
 - Added subcontractor\_invoice\_line\_items.total\_retainage\_project\_currency
- Changes in action\_plan

 - Added action\_plan.audit\_transaction\_timestamp
- Changes in action\_plan\_approver

 - Added action\_plan\_approver.audit\_transaction\_timestamp
- Changes in action\_plan\_completed\_receiver

 - Added action\_plan\_completed\_receiver.audit\_transaction\_timestamp
- Changes in action\_plan\_line\_item

 - Added action\_plan\_line\_item.audit\_transaction\_timestamp
- Changes in action\_plan\_line\_item\_assignee

 - Added action\_plan\_line\_item\_assignee.audit\_transaction\_timestamp
- Changes in action\_plan\_line\_item\_record

 - Added action\_plan\_line\_item\_record.audit\_transaction\_timestamp
- Changes in action\_plan\_line\_item\_record\_request

 - Added action\_plan\_line\_item\_record\_request.audit\_transaction\_timestamp
- Changes in action\_plan\_line\_item\_reference

 - Added action\_plan\_line\_item\_reference.audit\_transaction\_timestamp
- Changes in drawing\_revision

 - Added drawing\_revision.is\_connected\_drawing
- Changes in incident\_record

 - Added incident\_record.affected\_person\_id
- Changes in observation

 - Added observation.created\_by\_company
- Changes in rfi\_responses

 - Added rfi\_responses.is\_most\_recent
- Changes in rfis\_bic

 - Added rfis\_bic.response\_required
- Changes in schedule\_task

 - Added schedule\_task.predecessor\_wbs\_list
 - Added schedule\_task.successor\_wbs\_list
- Changes in specification\_sections

 - `Added specification\_sections.specification\_area\_description
 - Added specification\_sections.specification\_area\_name
- Changes in submittal\_approvers

 - Added submittal\_approvers.previous\_due\_date
 - Added submittal\_approvers.previous\_returned\_date
 - Added submittal\_approvers.previous\_sent\_date
- Changes in wp\_projects

 - Added wp\_projects.categories
- Added users.audit\_transaction\_timestamp
- Added estimate\_layer\_groups.profit

#### Procore Analytics 2.0 Data Updates (02/18/2025)

**Procore added the following models (tables):**

- Financial

 - payments\_permissions
 - payments\_disbursements
 - pay\_requirement\_settings
 - payments\_project\_controls
 - payments\_invites
 - payments\_agreements
 - payments\_received
- Project Management

 - connected\_rfi\_responses
 - connected\_rfis
 - daily\_log\_accident\_custom\_field\_configs
 - daily\_log\_accident\_custom\_fields
 - daily\_log\_delay\_custom\_field\_configs
 - daily\_log\_delay\_custom\_fields
 - daily\_log\_delivery\_custom\_field\_configs
 - daily\_log\_delivery\_custom\_fields
 - daily\_log\_dumpster\_custom\_field\_configs
 - daily\_log\_dumpster\_custom\_fields
 - daily\_log\_inspection\_custom\_field\_configs
 - daily\_log\_inspection\_custom\_fields
 - daily\_log\_phone\_call\_custom\_field\_configs
 - daily\_log\_phone\_call\_custom\_fields
 - daily\_log\_plan\_revision\_custom\_field\_configs
 - daily\_log\_plan\_revision\_custom\_fields
 - daily\_log\_productivity\_custom\_field\_configs
 - daily\_log\_productivity\_custom\_fields
 - daily\_log\_quantity\_custom\_field\_configs
 - daily\_log\_quantity\_custom\_fields
 - daily\_log\_safety\_violation\_custom\_field\_configs
 - daily\_log\_safety\_violation\_custom\_fields
 - daily\_log\_scheduled\_work\_custom\_field\_configs
 - daily\_log\_scheduled\_work\_custom\_fields
 - daily\_log\_waste\_custom\_field\_configs
 - daily\_log\_waste\_custom\_fields
 - inspection\_item\_references
 - schedule\_task\_changes
- Resource Planning

 - assignments
 - job titles
 - requests
 - time off
 - wp people
 - wp projects
 - groups
- Equipment

 - equipment
 - equipment project log
 - equipment timecard entry
- Estimating

 - estimating projects
 - estimate layers
 - estimate layer groups
 - estimating project custom fields

**Procore updated the following models (tables):**

- Changes in project\_vendor\_insurances.sql:

 - Added project\_vendor\_insurances.external\_origin\_data
 - Added project\_vendor\_insurances.external\_origin\_id
- Changes in projects.sql:

 - Added projects.code
 - Added projects.delivery\_method
 - Added projects.external\_origin\_data
 - Added projects.external\_origin\_id
 - Added projects.sector
 - Added projects.work\_scope
- Changes in users.sql:

 - Added users.abbreviated\_name
 - Added users.can\_push\_to\_accounting
 - Added users.company\_name
 - Added users.company\_permission\_template
 - Added users.external\_origin\_data
 - Added users.external\_origin\_id
 - Added users.login\_information\_id
 - Added users.origin\_id
 - Added users.origin\_name
- Changes in budget\_changes.sql:

 - Added budget\_changes.external\_origin\_data
 - Added budget\_changes.external\_origin\_id
- Changes in budget\_line\_items.sql:

 - Added budget\_line\_items.budget\_notes
- Changes in change\_events.sql:

 - Added change\_events.external\_origin\_data
 - Added change\_events.external\_origin\_id
- Changes in commitment\_change\_orders.sql:

 - Added commitment\_change\_orders.external\_origin\_data
 - Added commitment\_change\_orders.external\_origin\_id
- Changes in commitment\_line\_items.sql:

 - Added commitment\_line\_items.external\_origin\_data
 - Added commitment\_line\_items.external\_origin\_id
- Changes in direct\_cost\_line\_items.sql:

 - Added direct\_cost\_line\_items.external\_origin\_data
 - Added direct\_cost\_line\_items.external\_origin\_id
- Changes in direct\_costs.sql:

 - Added direct\_costs.external\_origin\_data
 - Added direct\_costs.external\_origin\_id
- Changes in owner\_invoice\_line\_item\_with\_markups.sql:

 - Added owner\_invoice\_line\_item\_with\_markups.external\_origin\_data
 - Added owner\_invoice\_line\_item\_with\_markups.external\_origin\_id
 - Added owner\_invoice\_line\_item\_with\_markups.materials\_presently\_stored\_qty
 - Added owner\_invoice\_line\_item\_with\_markups.name
 - Added owner\_invoice\_line\_item\_with\_markups.new\_materials\_stored\_qty
 - Added owner\_invoice\_line\_item\_with\_markups.previous\_materials\_stored\_qty
 - Added owner\_invoice\_line\_item\_with\_markups.prime\_contract\_id
- Changes in owner\_invoice\_line\_items.sql:

 - Added owner\_invoice\_line\_items.external\_origin\_data
 - Added owner\_invoice\_line\_items.external\_origin\_id
 - Added owner\_invoice\_line\_items.line\_type
 - Added owner\_invoice\_line\_items.markup\_id
 - Added owner\_invoice\_line\_items.materials\_presently\_stored\_qty
 - Added owner\_invoice\_line\_items.name
 - Added owner\_invoice\_line\_items.new\_materials\_stored\_qty
 - Added owner\_invoice\_line\_items.owner\_invoice\_line\_item\_with\_markup\_id
 - Added owner\_invoice\_line\_items.owner\_invoice\_markup\_line\_item\_id
 - Added owner\_invoice\_line\_items.previous\_materials\_stored\_qty
- Changes in owner\_invoice\_markup\_line\_items.sql:

 - Added owner\_invoice\_markup\_line\_items.approved\_changes
 - Added owner\_invoice\_markup\_line\_items.approved\_changes\_company\_currency
 - Added owner\_invoice\_markup\_line\_items.approved\_changes\_project\_currency
 - Added owner\_invoice\_markup\_line\_items.balance\_to\_finish
 - Added owner\_invoice\_markup\_line\_items.company\_id\_2
 - Added owner\_invoice\_markup\_line\_items.external\_origin\_data
 - Added owner\_invoice\_markup\_line\_items.external\_origin\_id
 - Added owner\_invoice\_markup\_line\_items.line\_type
 - Added owner\_invoice\_markup\_line\_items.materials\_presently\_stored\_qty
 - Added owner\_invoice\_markup\_line\_items.name
 - Added owner\_invoice\_markup\_line\_items.new\_materials\_stored\_qty
 - Added owner\_invoice\_markup\_line\_items.owner\_invoice\_line\_item\_id
 - Added owner\_invoice\_markup\_line\_items.owner\_invoice\_line\_item\_with\_markup\_id
 - Added owner\_invoice\_markup\_line\_items.previous\_materials\_stored\_qty
 - Added owner\_invoice\_markup\_line\_items.prime\_contract\_id
- Changes in owner\_invoices.sql:

 - Added owner\_invoices.external\_origin\_data
 - Added owner\_invoices.external\_origin\_id
 - Added owner\_invoices.tax\_applicable\_to\_this\_payment
- Changes in payments\_issued.sql:

 - Added payments\_issued.external\_origin\_data
 - Added payments\_issued.external\_origin\_id
- Changes in prime\_contract\_change\_order\_line\_items.sql:

 - Added prime\_contract\_change\_order\_line\_items.external\_origin\_data
 - Added prime\_contract\_change\_order\_line\_items.external\_origin\_id
- Changes in prime\_contract\_change\_order\_requests.sql:

 - Added prime\_contract\_change\_order\_requests.external\_origin\_data
 - Added prime\_contract\_change\_order\_requests.external\_origin\_id
- Changes in prime\_contract\_change\_orders.sql:

 - Added prime\_contract\_change\_orders.external\_origin\_data
 - Added prime\_contract\_change\_orders.external\_origin\_id
- Changes in prime\_contract\_line\_items.sql:

 - Added prime\_contract\_line\_items.external\_origin\_data
 - Added prime\_contract\_line\_items.external\_origin\_id
 - Added prime\_contract\_line\_items.vendor\_id
- Changes in prime\_contract\_potential\_change\_orders.sql:

 - Added prime\_contract\_potential\_change\_orders.external\_origin\_data
 - Added prime\_contract\_potential\_change\_orders.external\_origin\_id
- Changes in prime\_contracts.sql:

 - Added prime\_contracts.external\_origin\_data
- Added prime\_contracts.external\_origin\_id
- Changes in subcontractor\_invoice\_line\_items.sql:

 - Added subcontractor\_invoice\_line\_items.materials\_presently\_stored\_qty
 - Added subcontractor\_invoice\_line\_items.materials\_previously\_stored\_qty
 - Added subcontractor\_invoice\_line\_items.new\_materials\_qty
- Changes in subcontractor\_invoices.sql:

 - Added subcontractor\_invoices.external\_origin\_data
 - Added subcontractor\_invoices.external\_origin\_id
- Changes in inspections.sql:

 - Added inspections.equipment\_identification\_number
- Changes in rfi\_assignees.sql:

 - Added rfi\_assignees.forwarded\_by
- Changes in submittal\_approvers.sql:

 - Added submittal\_approvers.is\_last\_step
- Changes in equipment\_timecard\_entry.sql:

 - Added equipment\_timecard\_entry.equipment\_identification\_number
 - Added equipment\_timecard\_entry.equipment\_name

#### Procore Analytics 2.0 Data Updates (01/21/2025)

**Procore has added the following models (tables):**

- inspection\_item\_references
- schedule\_task\_changes
- equipment
- equipment\_project\_log
- equipment\_timecard\_entry
- payments\_project\_controls
- payments\_invites
- payments\_agreements
- pay\_requirement\_settings

**Procore has updated the following models (tables):**

- company\_vendor\_insurances:

 - Added company\_vendor\_insurances.template\_name
- project\_role\_memberships:

 - Added project\_role\_memberships.user\_id
- budget\_change\_workflow\_steps:

 - Added budget\_change\_workflow\_steps.current\_step\_due\_date
- budget\_codes:

 - Deleted SELECT budget\_codes.budget\_code
 - Added SELECT budget\_codes.attribute\_1\_line\_item
 - Added budget\_codes.attribute\_1\_name
 - Added budget\_codes.attribute\_2\_line\_item
 - Added budget\_codes.attribute\_2\_name
 - Added budget\_codes.attribute\_3\_line\_item
 - Added budget\_codes.attribute\_3\_name
 - Added budget\_codes.budget\_code
- budget\_columns:

 - Added budget\_columns.created\_at
 - Added budget\_columns.updated\_at
- change\_event\_line\_item\_with\_markups:

 - Deleted SELECT change\_event\_line\_item\_with\_markups.budget\_days\_in\_stage
 - Added SELECT change\_event\_line\_item\_with\_markups.biller\_id
 - Added change\_event\_line\_item\_with\_markups.biller\_model\_name
 - Added change\_event\_line\_item\_with\_markups.biller\_name
 - Added change\_event\_line\_item\_with\_markups.budget\_days\_in\_stage
 - Added change\_event\_line\_item\_with\_markups.change\_event\_events\_id
 - Added change\_event\_line\_item\_with\_markups.change\_event\_status
 - Added change\_event\_line\_item\_with\_markups.change\_event\_title
 - Added change\_event\_line\_item\_with\_markups.contract\_id
 - Added change\_event\_line\_item\_with\_markups.contract\_number
 - Added change\_event\_line\_item\_with\_markups.contract\_title
 - Added change\_event\_line\_item\_with\_markups.estimated\_budget\_amount
 - Added change\_event\_line\_item\_with\_markups.estimated\_budget\_transfer\_amount
 - Added change\_event\_line\_item\_with\_markups.estimated\_cost\_amount
 - Added change\_event\_line\_item\_with\_markups.estimated\_cost\_amount\_company\_currency
 - Added change\_event\_line\_item\_with\_markups.estimated\_cost\_amount\_project\_currency
 - Added change\_event\_line\_item\_with\_markups.event\_scope
 - Added change\_event\_line\_item\_with\_markups.proposed\_contract\_id
 - Added change\_event\_line\_item\_with\_markups.proposed\_vendor\_id
 - Added change\_event\_line\_item\_with\_markups.source
 - Added change\_event\_line\_item\_with\_markups.vendor\_name
 - Added change\_event\_line\_item\_with\_markups.wbs\_code\_id
- commitment\_change\_order\_line\_items:

 - Added commitment\_change\_order\_line\_items.commitment\_change\_order\_request\_id
 - Added commitment\_change\_order\_line\_items.commitment\_potential\_change\_order\_id
- commitment\_change\_order\_workflow\_steps:

 - Added commitment\_change\_order\_workflow\_steps.current\_step\_due\_date
- commitment\_custom\_field\_configs:

 - Added commitment\_custom\_field\_configs.name
- commitment\_pco\_workflow\_steps:

 - Added commitment\_pco\_workflow\_steps.current\_step\_due\_date
- commitment\_workflow\_step\_occurrences:

 - Added commitment\_workflow\_step\_occurrences.current\_step\_due\_date
- contract\_compliance\_documents:

 - Added contract\_compliance\_documents.template\_name
- owner\_invoice\_workflow\_steps:

 - Added owner\_invoice\_workflow\_steps.current\_step\_due\_date
- owner\_invoices:

 - Added owner\_invoices.erp\_latest\_status
 - Added owner\_invoices.erp\_updated\_at
 - Added owner\_invoices.erp\_user\_name
 - Added owner\_invoices.synced\_with\_accounting
- payments\_beneficiaries:

 - Added payments\_beneficiaries.early\_pay\_classification
- prime\_contract\_change\_order\_line\_items:

 - Added prime\_contract\_change\_order\_line\_items.name
 - Added prime\_contract\_change\_order\_line\_items.prime\_contract\_change\_order\_request\_id
 - Added prime\_contract\_change\_order\_line\_items.prime\_contract\_potential\_change\_order\_id
- prime\_contract\_change\_order\_workflow\_steps:

 - Added prime\_contract\_change\_order\_workflow\_steps.current\_step\_due\_date
- prime\_contract\_pco\_workflow\_steps:

 - Added prime\_contract\_pco\_workflow\_steps.current\_step\_due\_date
- prime\_contract\_workflow\_steps:

 - Added prime\_contract\_workflow\_steps.current\_step\_due\_date
- subcontractor\_invoice\_line\_items:

 - Added subcontractor\_invoice\_line\_items.total\_retainage
- subcontractor\_invoice\_workflow\_steps:

 - Added subcontractor\_invoice\_workflow\_steps.current\_step\_due\_date
- action\_plan\_custom\_fields:

 - Added action\_plan\_custom\_fields.type\_id
- action\_plan\_line\_item\_record:

 - Added action\_plan\_line\_item\_record.action\_plan\_line\_item\_record\_resource\_url
- correspondence\_custom\_fields:

 - Added correspondence\_custom\_fields.type\_id
- correspondence\_response\_attachments:

 - Added correspondence\_response\_attachments.type\_id
- correspondence\_schedule\_tasks:

 - Added correspondence\_schedule\_tasks.type\_id
- correspondence\_workflow\_responses:

 - Added correspondence\_workflow\_responses.type\_id
- correspondence\_workflow\_steps:

 - Added correspondence\_workflow\_steps.type\_id
- daily\_log\_accident:

 - Added daily\_log\_accident.daily\_log\_completion\_id
- daily\_log\_construction\_reports:

 - Added daily\_log\_construction\_reports.daily\_log\_completion\_id
- daily\_log\_delay:

 - Added daily\_log\_delay.daily\_log\_completion\_id
- daily\_log\_delivery:

 - Added daily\_log\_delivery.daily\_log\_completion\_id
- daily\_log\_dumpster:

 - Added daily\_log\_dumpster.daily\_log\_completion\_id
- daily\_log\_equipment:

 - Added daily\_log\_equipment.daily\_log\_completion\_id
- daily\_log\_inspection:

 - Added daily\_log\_inspection.daily\_log\_completion\_id
- daily\_log\_manpower:

 - Added daily\_log\_manpower.daily\_log\_completion\_id
- daily\_log\_note:

 - Added daily\_log\_note.daily\_log\_completion\_id
- daily\_log\_observed\_weather\_condition:

 - Added daily\_log\_observed\_weather\_condition.daily\_log\_completion\_id
- daily\_log\_phone\_call:

 - Added daily\_log\_phone\_call.daily\_log\_completion\_id
- daily\_log\_plan\_revision:

 - Added daily\_log\_plan\_revision.daily\_log\_completion\_id
- daily\_log\_productivity:

 - Added daily\_log\_productivity.daily\_log\_completion\_id
- daily\_log\_quantity:

 - Added daily\_log\_quantity.daily\_log\_completion\_id
- daily\_log\_safety\_violation:

 - Added daily\_log\_safety\_violation.daily\_log\_completion\_id
- daily\_log\_scheduled\_work:

 - Added daily\_log\_scheduled\_work.daily\_log\_completion\_id
- daily\_log\_scheduled\_work\_task:

 - Added daily\_log\_scheduled\_work\_task.daily\_log\_completion\_id
 - Added daily\_log\_scheduled\_work\_task.schedule\_task\_id
- daily\_log\_visitor:

 - Added daily\_log\_visitor.daily\_log\_completion\_id
- daily\_log\_waste:

 - Added daily\_log\_waste.daily\_log\_completion\_id
- inspection\_custom\_fields:
- Added inspection\_custom\_fields.type\_id
- inspection\_item\_signature\_requests:

 - Added inspection\_item\_signature\_requests.inspection\_schedule\_id
- inspection\_items:

 - Added inspection\_items.position\_number
- inspection\_schedules:

 - Added inspection\_schedules.ends\_at
 - Added inspection\_schedules.starts\_at
- inspections:

 - Added inspections.equipment\_id
 - Added inspections.equipment\_name
- observation\_custom\_field\_configs:

 - Added observation\_custom\_field\_configs.observation\_type\_id
 - Added observation\_custom\_field\_configs.type\_id
- observation\_custom\_fields:

 - Added observation\_custom\_fields.type\_id
- punch\_item\_bic:

 - Added punch\_item\_bic.punch\_item\_bic\_id
- rfis\_bic:

 - Added rfis\_bic.rfi\_bic\_id
- schedule\_lookahead\_task:

 - Added schedule\_lookahead\_task.task\_id\_comp
- schedule\_task:

 - Added schedule\_task.task\_id
- submittal\_ball\_in\_courts:

 - Added submittal\_ball\_in\_courts.company\_name
 - Added submittal\_ball\_in\_courts.role
- submittals:

 - Added submittals.ball\_in\_court\_role
 - Added submittals.paused
- actual\_production\_quantities:

 - Added actual\_production\_quantities.wbs\_code\_id
- budget\_change\_production\_quantities:

 - Deleted SELECT budget\_change\_production\_quantities.budget\_change\_production\_quantity\_id
 - Added SELECT budget\_change\_production\_quantities.budget\_change\_id
 - Added budget\_change\_production\_quantities.budget\_change\_production\_quantity\_id
 - Added budget\_change\_production\_quantities.wbs\_code\_id
- prime\_potential\_change\_order\_production\_quantities:

 - Added prime\_potential\_change\_order\_production\_quantities.prime\_contract\_change\_order\_id
 - Added prime\_potential\_change\_order\_production\_quantities.wbs\_code\_id
- project:

 - Added project.code
- owner\_invoices:

 - Added owner\_invoices.Tax\_Applicable\_To\_This\_Payment
- timecard\_entries:

 - Added timecard\_entries.user\_id

#### Procore Analytics 2.0 Data Updates (12/17/2024)

**Procore has added (current\_step\_due\_date) to the following models (tables):**

- budget\_change\_workflow\_steps
- commitment\_change\_order\_workflow\_steps
- commitment\_pco\_workflow\_responses
- commitment\_workflow\_step\_occurrences
- owner\_invoice\_workflow\_steps
- prime\_contract\_change\_order\_workflow\_steps
- prime\_contract\_pco\_workflow\_steps
- prime\_contract\_workflow\_steps
- subcontractor\_invoice\_workflow\_steps

**Procore has added the following fields:**

- actual\_production\_quantities.wbs\_code\_id
- timecard\_entries.user\_id