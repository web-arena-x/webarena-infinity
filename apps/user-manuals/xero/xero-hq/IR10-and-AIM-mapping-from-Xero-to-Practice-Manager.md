# IR10 and AIM mapping from Xero to Practice Manager

Source: https://central.xero.com/s/article/IR10-and-AIM-mapping-from-Xero-to-Practice-Manager

---

## Overview

- Understand how Practice Manager maps data from Xero to your client's IR10 and AIM.
- If you've connected your client in Practice Manager to their organisation in Xero, Practice Manager populates the client's IR10 and AIM with data directly from Xero.

Warning

We no longer support AIM returns for clients with foreign exchange transactions. AIM returns still support clients without foreign exchange transactions.

How it works

- If you've connected your client in Practice Manager to their organisation in Xero, Practice Manager populates the client's IR10 and AIM with data directly from Xero.
- Practice Manager populates the IR10 and AIM based on [report codes in Xero](Report-codes-for-practices-using-report-templates.md). It’s important to use the correct report codes so your IR10 and AIM populates correctly. You can edit report code mapping to suit your client's circumstances
- You can overwrite the data on the IR10 and AIM, however we recommend you make changes to your client's data in Xero and then [refresh the connection between Practice Manager and Xero](Connect-your-client-to-their-Xero-organisation.md) to preserve the audit trail.
- Practice Manager sends this schedule to Inland Revenue when you submit your client's associated return.

Positive value indicator

Practice Manager shows a number in the IR10 and AIM boxes. If the number has a positive value, use the table below to see if it refers to a credit or debit.

| IR10 description | Box # | Positive value |
| --- | --- | --- |
| Gross income from sales and/or services | 2 | Credit |
| Opening stock (includes work in progress) | 3 | Debit |
| Purchases | 4 | Debit |
| Closing stock (includes work in progress) | 5 | Credit |
| Gross profit | 6 | Credit |
| Interest received | 7 | Credit |
| Dividends received | 8 | Credit |
| Rental, lease and licence income | 9 | Credit |
| Other income | 10 | Credit |
| Total income | 11 | Credit |
| Bad debts | 12 | Debit |
| Accounting depreciation and amortisation | 13 | Debit |
| Insurance (excludes ACC levies) | 14 | Debit |
| Interest expense | 15 | Debit |
| Professional and consulting fees | 16 | Debit |
| Rates | 17 | Debit |
| Rental, lease and licence payments | 18 | Debit |
| Repairs and maintenance | 19 | Debit |
| Research and development | 20 | Debit |
| Related party remuneration | 21 | Debit |
| Salaries and wages paid to employees | 22 | Debit |
| Contractor and sub-contractor payments | 23 | Debit |
| Other expenses | 24 | Debit |
| Total expenses | 25 | Debit |
| Exceptional items | 26 | Debit |
| Net profit/loss before tax | 27 | Credit |
| Tax adjustments | 28 | Debit |
| Current year taxable profit/loss | 29 | Credit |
| Accounts receivable (debtors) | 30 | Debit |
| Cash and deposits | 31 | Debit |
| Other current assets | 32 | Debit |
| Vehicles | 33 | Debit |
| Plant and machinery | 34 | Debit |
| Furniture and fittings | 35 | Debit |
| Land | 36 | Debit |
| Buildings | 37 | Debit |
| Other fixed assets | 38 | Debit |
| Intangibles | 39 | Debit |
| Shares/ownership interests | 40 | Debit |
| Term deposits | 41 | Debit |
| Other non-current assets | 42 | Debit |
| Total assets | 43 | Debit |
| Provisions | 44 | Credit |
| Accounts payable | 45 | Credit |
| Current loans | 46 | Credit |
| Other current liabilities | 47 | Credit |
| Total current liabilities | 48 | Credit |
| Non-current liabilities (as at balance date) | 49 | Credit |
| Total liabilities | 50 | Credit |
| Owners' equity | 51 | Credit |
| Tax depreciation | 52 | Debit |
| Untaxed realised gains/receipts | 53 | Credit |
| Additions to fixed assets | 54 | Debit |
| Disposals of fixed assets | 55 | Credit |
| Dividends paid | 56 | Debit |
| Drawings | 57 | Credit |
| Current account year-end balances | 58 | Credit |
| Tax-deductible loss on disposal of fixed assets | 59 | Debit |

Income statement mapping – Box 2 to Box 29

**Gross income from sales and/or services – Box 2**

| Xero report code | Xero report code name |
| --- | --- |
| REV.TRA | Trading revenue |
| REV.TRA.MAN | Manufactured goods and services |
| REV.TRA.CON | Construction contracts |
| REV.TRA.RET | Retail goods and services |

**Cost of goods sold – Box 3 to Box 5**

| IR10 Description | Box # | Xero report code | Xero report code name |
| --- | --- | --- | --- |
| Opening stock | 3 | EXP.COS.OPE EXP.COS.WPO | Opening inventory Opening work in progress |
| Purchases | 4 | EXP.COS EXP.COS.PUR | Cost of goods sold Purchases |
| Closing stock | 5 | EXP.COS.CLO EXP.COS.WPC | Closing inventory Closing work in progress |

**Gross profit – Box 6**

- Box 2 - Box 3 - Box 4 + Box 5

**Other gross income – Box 7 to Box 10**

| IR10 Description | Box # | Xero report code | Xero report code name |
| --- | --- | --- | --- |
| Interest received | 7 | REV.INV.INT | Interest |
| Dividends received | 8 | REV.INV.DIV | Dividends |
| Rental, lease and licence income | 9 | REV.TRA.OPE REV.INV.REN | Operating leases Rents |
| Other income | 10 | REV.\* | All revenue codes not otherwise used |

**Total income – Box 11**

- Box 6 + Box 7 + Box 8 + Box 9 + Box 10

**Expenses – Box 12 to Box 24**

| IR10 Description | Box # | Xero report code | Xero report code name |
| --- | --- | --- | --- |
| Bad debts | 12 | EXP.BAD | Bad debts |
| Accounting depreciation and amortisation | 13 | EXP.DEP EXP.AMO | Depreciation Amortisation of intangibles |
| Insurance (excludes ACC levies) | 14 | EXP.INS | Insurance |
| Interest expense | 15 | EXP.INT | Interest and finance charges |
| Professional and consulting fees | 16 | EXP.LEG | Professional and consulting fee(s) |
| Rates | 17 | EXP.RAT | Rates |
| Rental, lease and licence payments | 18 | EXP.REN | Rental and lease payments |
| Repairs and maintenance | 19 | EXP.REP | Repairs and maintenance |
| Research and development | 20 | EXP.RES | Research and development |
| Related party remuneration | 21 | EXP.DIR | Directors/trustees and related party fees |
| Salaries and wages paid to employees | 22 | EXP.WAG | Wages and salaries |
| Contractor and sub-contractor payments | 23 | EXP.CON | Contractor payments |
| Other expenses | 24 | EXP.\* | All expense codes not otherwise used, except EXP.TAX and EXP.EXT |

**Total expenses – Box 25**

- Sum of Box 12 to Box 24

**Exceptional items – Box 26**

| Xero report code | Xero report code name |
| --- | --- |
| EXP.EXT | Non-recurring items |

**Net profit/loss before tax – Box 27**

- Box 11 - Box 25 - Box 26

**Tax adjustments – Box 28**

| Xero report code | Xero report code name |
| --- | --- |
| EXP.ENT.NON | Non-deductible entertainment |
| EXP.LEG.NON | Non-deductible legal fees |
| EXP.NON | Other non-deductible items |
| REV.NON | Non-taxable income |
| REV.OTH.GAI.CAP | Capital gain on disposal of property, plant and equipment |

**Current year taxable profit/loss – Box 29**

- Box 27 - Box 28

Balance sheet mapping – Box 30 to Box 51

**Current assets (as at balance date) – Box 30 to Box 32**

| Description | Box # | Xero report code | Xero report code name |
| --- | --- | --- | --- |
| Accounts receivable (debtors) | 30 | ASS.CUR.REC ASS.CUR.REC.TRA | Trade and other receivables Trade receivables |
| Cash and deposits | 31 | ASS.CUR.BAN (where account has debit balance at end of reporting period) | Bank and cash/(bank overdraft) |
| Other current assets | 32 | ASS.CUR.\* | Other current assets not otherwise used, except ASS.CUR.BAN with credit balance (used in Box 46) |

**Fixed assets (closing accounting value) – Box 33 to Box 38**

| IR10 Description | Box # | Xero report code | Xero report code name |
| --- | --- | --- | --- |
| Vehicles | 33 | ASS.NCA.FIX.OWN.VEH ASS.NCA.FIX.OWN.VEH.ACC ASS.NCA.FIX.LEA.VEH ASS.NCA.FIX.LEA.VEH.ACC | Vehicles owned Accumulated depreciation - vehicles owned Vehicles leased Accumulated depreciation - vehicles leased |
| Plant and machinery | 34 | ASS.NCA.FIX.OWN.PLA ASS.NCA.FIX.OWN.PLA.ACC ASS.NCA.FIX.LEA.PLA ASS.NCA.FIX.LEA.PLA.ACC | Plant and machinery owned Accumulated depreciation - plant and machinery owned Plant and machinery leased Accumulated depreciation - plant and machinery leased |
| Furniture and fittings | 35 | ASS.NCA.FIX.OWN.FUR ASS.NCA.FIX.OWN.FUR.ACC ASS.NCA.FIX.LEA.FUR ASS.NCA.FIX.LEA.FUR.ACC | Furniture and fittings owned Accumulated depreciation - furniture and fittings owned Furniture and fittings leased Accumulated depreciation - furniture and fittings leased |
| Land | 36 | ASS.NCA.FIX.OWN.LAC ASS.NCA.FIX.OWN.LAR | Land at cost Land revaluation |
| Buildings | 37 | ASS.NCA.FIX.OWN.BUC ASS.NCA.FIX.OWN.BUR ASS.NCA.FIX.OWN.BUC.ACC | Buildings at cost Buildings revaluation Accumulated depreciation - buildings |
| Other fixed assets | 38 | ASS.NCA.FIX.\* | Other fixed assets not otherwise used |

**Other non-current assets (as at balance date) – Box 39 to Box 42**

| Description | Box # | Xero report code | Xero report code name |
| --- | --- | --- | --- |
| Intangibles | 39 | ASS.NCA.INT.\* | All intangible assets |
| Shares/ownership interests | 40 | ASS.NCA.INV.PRE ASS.NCA.INV.SHA | Preference shares Shares and debentures |
| Term deposits | 41 | ASS.NCA.INV.TER | Term deposits |
| Other non-current assets | 42 | ASS.NCA.\* ASS.\* | Other non-current assets not otherwise used Other assets not otherwise used |

**Total assets – Box 43**

- Sum of Box 30 to Box 42

**Current liabilities (as at balance date) – Box 44 to Box 48**

| Description | Box # | Xero report code | Xero report code name |
| --- | --- | --- | --- |
| Provisions | 44 | LIA.CUR.PRO.\* | All current provisions |
| Accounts payable (creditors) | 45 | LIA.CUR.PAY.TRA LIA.CUR.PAY LIA.CUR.PAY.PAY LIA.CUR.PAY.FBT LIA.CUR.PAY.EMP | Trade payables Trade and other payables PAYE Fringe Benefit tax Employee entitlements (wages, annual leave, etc) |
| Current loans | 46 | ASS.CUR.BAN (where account has credit balance at end of reporting period) LIA.CUR.LOA | Bank and cash/(bank overdraft) Loans |
| Other current liabilities | 47 | LIA.CUR.\* EQU.OWN\* | Other current liabilities not otherwise used Only net credit amounts for EQU.OWN\* will be displayed |
| Total current liabilities | 48 | | Sum of Box 44 to Box 47 |

**Non-current liabilities (as at balance date) – Box 49**

| Xero report code | Xero report code name |
| --- | --- |
| LIA.NCL.\* | Non-current liabilities not otherwise used, except LIA.NCL.ADV.\* (Proprietor/shareholder advances and drawings) |

**Total liabilities – Box 50**

Box 48 + Box 49

**Owners' equity – Box 51**

Box 43 - Box 50

Other information – Box 52 to Box 59

**Tax depreciation – Box 52**

| Xero report code | Xero report code name |
| --- | --- |
| EXP.DEP | Depreciation |

**Untaxed realised gains/receipts - Box 53**

- This box reuses report codes which have been reported previously on the IR10 and AIM.

| Xero report code | Xero report code name |
| --- | --- |
| REV.NON | Non-taxable income |
| REV.OTH.GAI.CAP | Capital gain on disposal of property, plant and equipment |

**Additions to fixed assets – Box 54**

- This box reuses report codes which have been reported previously on the IR10 and AIM.
- This box shows movement in accounts. It only reports on the debits posted to accounts using the following report codes in the reporting period.

| Xero report code | Xero report code name |
| --- | --- |
| ASS.NCA.FIX.LEA | Leased fixed assets |
| ASS.NCA.FIX.LEA.FUR | Furniture and fittings leased |
| ASS.NCA.FIX.LEA.PLA | Plant and machinery leased |
| ASS.NCA.FIX.LEA.VEH | Vehicles leased |
| ASS.NCA.FIX.OWN | Owned fixed assets |
| ASS.NCA.FIX.OWN.BUC | Buildings at cost |
| ASS.NCA.FIX.OWN.FUR | Furniture and fittings owned |
| ASS.NCA.FIX.OWN.LAC | Land at cost |
| ASS.NCA.FIX.OWN.PLA | Plant and machinery owned |
| ASS.NCA.FIX.OWN.VEH | Vehicles owned |

**Disposals of fixed assets – Box 55**

- This box reuses report codes which have been reported previously on the IR10 and AIM.
- This box shows movement in accounts. It only reports on the credits posted to accounts using the following report codes in the reporting period.

| Xero report code | Xero report code name |
| --- | --- |
| ASS.NCA.FIX.LEA | Leased fixed assets |
| ASS.NCA.FIX.LEA.FUR | Furniture and fittings leased |
| ASS.NCA.FIX.LEA.PLA | Plant and machinery leased |
| ASS.NCA.FIX.LEA.VEH | Vehicles leased |
| ASS.NCA.FIX.OWN | Owned fixed assets |
| ASS.NCA.FIX.OWN.BUC | Buildings at cost |
| ASS.NCA.FIX.OWN.FUR | Furniture and fittings owned |
| ASS.NCA.FIX.OWN.LAC | Land at cost |
| ASS.NCA.FIX.OWN.PLA | Plant and machinery owned |
| ASS.NCA.FIX.OWN.VEH | Vehicles owned |

**Dividends paid – Box 56**

- This box shows movement in accounts using this report code for the reporting period, not the closing balances.

| Xero report code | Xero report code name |
| --- | --- |
| EQU.RET.DIV | Dividends paid |

**Drawings – Box 57**

- This box shows movement in accounts using these report codes for the reporting period, not the closing balances.

| Xero report code | Xero report code name |
| --- | --- |
| LIA.NCL.ADV.DRA | Drawings |
| EQU.OWN.DRA | Owner/partner drawings |

**Current account year-end balances - Box 58**

- This box reuses report codes which have been reported previously on the IR10 and AIM.
- For individuals completing an AIM return, the value in Box 58 is set to equal the amount in Box 51.

| Xero report code | Xero report code name |
| --- | --- |
| LIA.NCL.ADV | Proprietor/shareholder advance accounts |
| EQU.OWN | Owner/partner funds introduced |

**Tax-deductible loss on disposal of fixed assets - Box 59**

| Xero report code | Xero report code name |
| --- | --- |
| EXP.LOS | Loss on disposal of property, plant and equipment |

## What's next?

[Resolve common errors](https://central.xero.com/s/article/Troubleshoot-common-IR10-or-AIM-mapping-errors) you might come across when you import data from Xero to your IR10 or AIM.