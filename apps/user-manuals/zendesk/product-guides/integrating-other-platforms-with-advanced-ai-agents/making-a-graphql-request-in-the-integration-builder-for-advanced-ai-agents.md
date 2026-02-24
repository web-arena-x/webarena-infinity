# Making a GraphQL request in the integration builder for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8920184187034-Making-a-GraphQL-request-in-the-integration-builder-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

While REST APIs have long been a standard for enabling integrations, GraphQL is rapidly gaining traction due to its flexibility and efficiency. You can leverage the integration builder's features to integrate with GraphQL APIs. You can take advantage of GraphQL’s key features, such as requesting only the data you need and handling complex queries with ease.

In this article, we’ll walk you through the process of setting up a GraphQL request using the integration builder, from understanding the GraphQL schema to constructing queries and integrating responses into your conversations.

**To set up a GraphQL request**

1. Find the GraphQL endpoint URL, usually provided by the API documentation (for example, https://api.example.com/graphql or for Shopify: https://{{storeName}}.myshopify.com/admin/api/2023-04/graphql.json).
2. Add it to the integration builder interface.
   1. Navigate to Environments and select the POST method type (if you are requesting data).
   2. Add your GraphQL endpoint into the URL input.  
      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_graphql_1.png)
3. Select your authentication method (if required).
4. If needed, add your credentials to the headers. For example, if it’s a Shopify integration, it will look like this:  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_graphql_2.png)
5. Understand the GraphQL Schema to select the data that you want returned from the server.
6. Obtain the schema from the GraphQL server.  
     
   It defines the available queries, mutations, and types. Use tools like Postman, GraphiQL or Apollo Explorer to inspect the schema, and to test and refine the query.  
     
   We recommend obtaining the query from Postman by navigating to the Code snippet tab and checking for data where you should see an object with the key “query”. Copy the object to use in the next step.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_graphql_3.png)
7. In the Body tab, add the GraphQL query specifying the data you need or the action you want to perform (if making a mutation request to modify data; create, update, delete).  
   This must be in JSON format.  
   Example query:  
   ```{"query":"{\n \_\_type(name: \"Order\") {\n name,\n fields {\n name\n type {\n name\n kind\n }\n }\n }\n}","variables":{}}```  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_graphql_4.png)
8. Navigate to the Success scenario to add your session parameters.
9. Using JSONata, write your queries to access and transform (if needed) the data in the response. See below for an example:  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_graphql_5.png)