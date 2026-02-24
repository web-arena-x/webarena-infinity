# Merge duplicate clients

Source: https://central.xero.com/s/article/Merge-duplicate-imported-clients

---

## Overview

- When you merge clients, choose the record to keep with the best client name and business details.
- You can merge client records in Xero HQ or Xero Practice Manager.
- Understand what data is updated or lost during a merge.

How it works

Merge clients to remove duplicate records and keep client information in one place.

Administrators need [view and edit permissions](User-roles-in-Xero-HQ.md) to merge clients in Xero HQ.

When you merge client records:

- Both sets of contact details and staff permissions are kept.
- You choose which client to keep the name and business information from.
- Any [connection to a Xero organisation](Add-client-organisations-to-your-practice.md) is kept, along with that client's industry. You can't merge clients if two or more of them are connected to a Xero organisation.

Once you merge clients you can't undo the process and split your clients again. You can instead [archive a client](Archive-or-restore-a-client-in-Xero-HQ.md) that you no longer need to remove them from your practice.

Data updated or lost during a merge

The client you don’t keep is deleted as part of the merging process.

If you want to keep a client’s [recurring job template](Recurring-jobs.md), manually change the client in the template to the client you want to keep, before you merge.

### Updated to reference kept client

The following data items are updated to reference the client being kept after the merge:

| | | |
| --- | --- | --- |
| Quotes | Jobs | Invoices |
| Contacts | Call reports | Client notes in Practice Manager |
| Client documents | Leads | Billing client references in other clients |
| Non-invoiced amounts originally calculated using rate from original client | | |

### Not updated to reference kept client

The following data items still reference the client that is deleted after the merge:

| | | |
| --- | --- | --- |
| Recurring jobs | Client relationships | Client group memberships |
| Queued updates to JobLedger | Custom rates for specific tasks | Unsubmitted timer entries |

### Always lost in the merge

The following data items will always be lost from the client that is deleted after the merge:

#### Main Details

| | | |
| --- | --- | --- |
| Business structure | Client type | Manager |
| Partner | First name | Last name |
| Other name | Date of birth | Picture or logo |

#### Contact Details

| | | |
| --- | --- | --- |
| Phone | Fax | Email address |
| Website | Referral source | Physical address |
| Postal address | | |

#### Billing

| |
| --- |
| Billing client |

#### Other

| |
| --- |
| All custom fields |

Merge clients from your practice's client list

1. In Xero HQ, select **Clients**.
2. From the client list, select the checkbox next to the clients you want to merge.
3. Click **Merge clients**.
4. (Optional) If you have Practice Manager. Click the menu icon , then select **View in Practice Manager**.
5. (Optional) If you don’t want to merge a client, click the menu icon , then select **Remove from group**.
6. Select which client to keep the name and business information from, and merge the other records into.
7. Click **Merge**.

Review potential duplicate client records

Xero HQ and Practice Manager identify potential duplicate clients in your practice's client list for you to review and merge as appropriate. Potential duplicates are indentified by client names, business structures, and any linked Xero organisations so that you can:

- Check whether the clients are a duplicate of one another, or if they're separate entities
- Review the information in each client
- See if a client is connected to a Xero organisation

To review potential duplicate client records:

1. In your practice, select **Clients**.
2. Click the menu icon  at the top right of the screen, then select **Review duplicate clients**.
3. (Optional) Click on a client name to show the potential duplicate records identified.
4. Click **Merge**.
5. (Optional) You have the option to view the client record in Practice Manager. Click the menu icon , then select **View in Practice Manager**.
6. (Optional) If you don’t want to merge a client, click the menu icon , then select **Remove from group**.
7. Select which client to keep the name and business information from, and merge the other records into.
8. Click **Merge**.

You can also click **Keep separate** next to a potential duplicate client if you want to keep the records separate and remove them from the **Duplicates to review** group.

## What's next?

You can now [add client notes](Use-client-notes-in-Xero-HQ.md) or [assign staff to clients](/s/article/Manage-clients-for-practice-staff?userregion=true).