# Export to SQL Server Using Data Factory

Source: https://v2.support.procore.com/product-manuals/analytics-company/tutorials/export-to-sql-server-using-data-factory

---

## Overview

This document provides step-by-step instructions for setting up a data pipeline in Microsoft Fabric to transfer data from Delta Share to a SQL warehouse. This configuration enables seamless data integration between Delta Lake sources and SQL destinations.

## Prerequisites

- Active Microsoft Fabric account with appropriate permissions.
- Delta Share credentials.
- SQL warehouse credentials.
- Access to Data Flow Gen2 in Fabric.

## Steps

- Access Data Flow Gen2
- Configure Data Source
- Set Up Delta Share Connection
- Configure Data Destination
- Finalize and Deploy
- Verification
- Troubleshooting

### Access Data Flow Gen2

1. Log in to your Microsoft Fabric account.
2. Navigate to the workspace.
3. Select 'Data Flow Gen2' from the available options.

### Configure Data Source

1. Click on 'Data from another source' to begin the configuration.
2. From the Get Data screen do the following:

   - Locate the search bar labeled 'Choose data source'.
   - Type 'delta sharing' in the search field.
   - Select Delta Sharing from the results.

### Set Up Delta Share Connection

1. Enter your Delta Share credentials when prompted.

   - Ensure all required fields are completed accurately.
   - Validate the connection if possible.
2. Click 'Next' to proceed.
3. Review the list of available tables:

   - All tables you have access to will be displayed.
   - Select the desired tables for transfer.

### Configure Data Destination

1. Click 'Add Data Destination'.
2. Select 'SQL warehouse' as your destination.
3. Enter SQL credentials:

   - Server details.
   - Authentication information.
   - Database specifications.
   - Verify the connection settings.

### Finalize and Deploy

1. Review all configurations.
2. Click 'Publish' to deploy the data flow.
3. Wait for the confirmation message.

### Verification

1. Access your SQL warehouse.
2. Verify that the data is available and properly structured.
3. Run test queries to ensure data integrity.

### Troubleshooting

Common issues and solutions:

- Connection failures: Verify credentials and network connectivity.
- Missing tables: Check Delta Share permissions.
- Performance issues: Review resource allocation and optimization settings.