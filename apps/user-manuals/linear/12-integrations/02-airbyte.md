# Airbyte

> [!NOTE]
> Available to workspaces on our [Enterprise](https://linear.app/pricing) plan

Connect with Airbyte to consolidate data in data warehouses, lakes, and databases.

![Linear and Airbyte logos](https://webassets.linear.app/images/ornj730p/production/01f331e6f28947dc5304640abb8cf844ea0ff280-2880x1620.png?q=95&auto=format&dpr=2)

## Overview

With the Airbyte integration you can load your Linear data into any data warehouse, lakes or databases in minutes. Create custom analytics and dashboards for your company and update it on any schedule through Airbyte.

We support Airbyte Open Source environments, and do not support Airbyte Cloud.

## Configure

Configuration requires workspace admin permissions to navigate to [Settings > Features > Integrations > Airbyte](https://linear.app/settings/integrations/airbyte) and click the **Enable** button.

Copy the one time Airbyte API key as you will need this later. With this key the integration receives read access to all data in supported tables. There is no way to _exclude_ access to private team access at this time.

### Set up Airbyte locally

Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) and launch it.

Clone the Airbyte repo and run Docker using the following command in Terminal:

```sh
git clone https://github.com/airbytehq/airbyte.git
cd airbyte
docker-compose up
```

Now you can open Airbyte in your browser at http://localhost:8000.

### Set up Linear Source

* In the Airbyte dashboard, click "Settings" on the bottom left.
* Click "Sources" on the left sidebar.
* Click the "New connector" button > enter the following:   
**- Connector display name:** `Linear` **- Docker repository name:** `gcr.io/linear-public-registry/linear-airbyte-source` **- Docker image tag:** `latest` **- Connector Documentation URL:** `https://github.com/linear/linear-airbyte-source/blob/main/readme.md`


![Settings page in Airbyte for adding a new connector](https://webassets.linear.app/images/ornj730p/production/411c6aec9ef601e16ae5a157da4dbbf1b133e114-804x719.png?q=95&auto=format&dpr=2)

### **Connect your destination**

With the connection complete, you can now choose your destination.

* Click "Connections" in the sidebar and the "New connection" button.
* In the "Source type" box search for "Linear".
* You can give a custom name to your source or leave it as Linear.
* Paste the API key you generated in the Linear integration page for Airbyte and click "Set up source".
* On the next page, you can select an existing destination or set up your destination service, their instructions will be provided there if you have not yet created a destination with them before.
* Save the connection.

![Airbyte settings page where you paste your API key ](https://webassets.linear.app/images/ornj730p/production/e55fd4eaa74ab6d7ba2f40af3ad9eb490e12721b-901x512.png?q=95&auto=format&dpr=2)

### **Choose your sync frequency**

Next, you need to choose how often you want to sync your Linear data to this destination:

* Click on Connections and your chosen Connection in the list
* Click on the "Replication" tab and choose your Replication frequency
* Select the data you want to sync. You should see a list of table names. You can select all or choose which ones to sync individually.
* Choose what type of sync mode you'd like to use for each source table. [Full Refresh](https://docs.airbyte.com/understanding-airbyte/connections/full-refresh-overwrite) and [Append](https://docs.airbyte.com/understanding-airbyte/connections/full-refresh-append/) are the options you can choose from. Incremental is not supported at this time. Linear data can sync every 12 hours, it cannot sync sooner than this.
* Click "Save changes"

Everything is now configured to extract, transform, load (ETL) your Linear data into Airbyte and sync it to the selected destination on the schedule you chose. 

> [!NOTE]
> The following models will be synced:
> 
> * Organization
> * Teams
> * Team Key
> * Team Membership
> * User
> * Milestone
> * Project
> * Project Updates
> * Project Link
> * Issues
> * Issue History
> * Issue Label
> * Issue Relation
> * Integration Resource
> * Attachment
> * Audit Entry
> * Comment
> * Cycle
> * Workflow State
> * Document
> * documentContent

## Remove connection

You can disable any incremental or full syncs by going to the _Connection_ settings page and clicking _Delete this connection._

## FAQ

<details>
<summary>Does Airbyte cost an extra fee? </summary>
Airbyte Open Source is free to use, only the cloud version is paid — which we don’t currently support.
</details>

<details>
<summary>Which databases or data warehouses does Airbyte connect to?</summary>
Airbyte offers many services you can connect your Linear workspace data to, you can view the full list here: https://docs.airbyte.com/integrations/
</details>
