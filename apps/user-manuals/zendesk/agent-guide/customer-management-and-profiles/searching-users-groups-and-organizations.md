# Searching users, groups, and organizations

Source: https://support.zendesk.com/hc/en-us/articles/4408883318554-Searching-users-groups-and-organizations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Data in the end users, team members, group, and organization objects can be searched on their respective pages.

This article covers the following topics:

- [About searching](#topic_4bz_kng_vt)
- [The user and type keywords](#topic_ipy_bxi_vc)
- [Searching users](#topic_duj_sbb_vc)
- [Searching for users by email domain](#topic_nei_edv_uc)
- [Searching groups](#topic_qei_edv_uc)
- [Searching organizations](#topic_vgx_pcb_vc)
- [Searching custom user and organization fields](#topic_pyt_m1s_vk)

## About searching

At the top of each page related to managing and organizing users, there is a search bar. Searches on these pages are limited in scope to the page. That means a search on the Team members page only returns team members that meet the search criteria and, likewise, a search on the Organizations page only returns organizations that meet the search criteria.

If you search using the global search tool, you need to use the `type` keyword if you want to restrict results to specific types of data. If you don't, your search results will include matches from the data in your Zendesk Support instance.

```
type:organization tags:premium
```

For more information about using search, see [Searching the data in your Zendesk](https://support.zendesk.com/hc/en-us/articles/4408894221594). All the user data properties you can search are described in the tables below. All of the searchable data in your Zendesk Support instance (including ticket data) is described in [Zendesk search reference](https://support.zendesk.com/hc/en-us/articles/4408886879258).

## The user and type keywords

To search for a user's profile data, you have the following two options.

Using the `user` keyword:

```
user:amy
```

Or, using the `type:user` keyword:

```
type:user amy
```

What's the difference between the two? The keyword `user` when not combined with `type` is just a shortcut for finding users by ID, name, and email address. The `user` keyword, like the ticket user role keywords (assignee, requester, submitter), accepts the ID, name, and email address as valid user identifiers.

```
user:52789480
user:amy
user:"amy moore"
user:amy@mondocam.com
```

If you want to search for additional user data, such as the user's phone number, the organization they belong to, and so on, you need to use `type:user`.

```
type:user tags:beta_user organization:customers
```

This example also illustrates the usefulness of `type` keyword. With it you can search for user data that is shared by more than one user. You can search for users that are in the same organization or group or any of the other searchable user data. For more information about the `type` keyword, see [Using the type keyword](https://support.zendesk.com/hc/en-us/articles/4408886879258#topic_qtr_avw_ld).

The `type` keyword is also used to search the group and organization data objects. For example:

- ```
 type:group name:"level 2"
 ```
- ```
 type:organization name:customers
 ```

## Searching users

The user data object contains all of the user properties that you can set in the user profile for end users and team members. Not all of the user profile data is searchable; those properties that are searchable are described in the following table.

Table 1. User property keywords

   | Keyword | Description |
| --- | --- |
| `name` | The user's partial or full name. ``` name:"alex anderson" ``` |
| `role` | The user's designated role. ``` role:admin ``` |
| `email` | Specify the user's email address, or specify none to search for users without an email address. ``` email:alex@mondocam.com ``` ``` email:"none" ```   Tip: Wildcards do not work for email address searches. For example, the following search returns no results: ``` email:dwight* ``` |
| `group` | The user's group name. This only applies to admin and agent users. ``` group:"Level 2" ``` |
| `organization` | Specify the user's organization name or ID, or specify `none` to search for users without an organization. If the user belongs to more than one organization, searching on any of those organizations will return their profile. ``` organization:mondocam ``` |
| `created` | The date the user was added to your Zendesk. ``` created<2011-05-01 ```   For more information on using date and time in your search, see [Searching by date and time](https://support.zendesk.com/hc/en-us/articles/4408835086106#topic_gbg_dvw_ld). |
| `notes` | All text in the notes field in the user's profile. ``` notes:"manager" ``` |
| `details` | All text in the details field in the user's profile. ``` details:"madison, wi" ``` |
| `external_id` | Specify the user's external ID, if used, or specify`none` to search for users without an external ID. ``` external_id:0098884412 ``` |
| `phone` | Specify the user's phone number, or specify `none` to search for users without a phone number. ``` phone:555-111-2222 ``` |
| `tags` | Specify tags on the user's profile, or specify `none` to search for users without tags. ``` tags:premium tags:wholesale ``` For more information about tagging users and organizations, see [Adding tags to users and organizations](https://support.zendesk.com/hc/en-us/articles/4408881573658). |
| `customfield` | Custom user fields. ``` plan_type:platinum ``` For more information, see [Searching custom user and organization fields](#topic_pyt_m1s_vk). |
| `is_verified` | Indicates whether the user’s primary email address has been verified. - **is\_verified:false Sunita** returns all users named Sunita with an unverified primary email address - **is\_verified:true** returns all users with a verified primary email address |
| `is_suspended` | Indicates whether the user has been suspended. - **is\_suspended:true Sunita** returns all users named Sunita who have been suspended. - **is\_suspended:true** returns all users who have been suspended. |
| whatsapp | Search for users based on a WhatsApp phone number. For more information see [Searching for tickets by WhatsApp number](https://support.zendesk.com/hc/en-us/articles/5869718332954). |

## Searching for users by email domain

All users belonging to the same email domain can be returned with this search statement:

```
type:user mondocam.com
```

To search for more than one email domain at a time, you just add more email domains to the search separated by a space:

```
type:user mondocam.com zendesk.com
```

## Searching groups

Here are the group properties that can be searched.

Table 2. Group property keywords

   | Keyword | Description |
| --- | --- |
| `name` | The group's name. ``` name:"level 2" ``` |
| `created` | The date the group was added. ``` created<2011-05-01 ``` For more information on using date and time in your search, see [Searching by date and time](https://support.zendesk.com/hc/en-us/articles/4408835086106#topic_gbg_dvw_ld). |

## Searching organizations

Here are the organization properties that can be searched.

Table 3. Organization property keywords

   | Keyword | Description |
| --- | --- |
| `name` | The organization's partial or full name. ``` name:mondocam ``` |
| `created` | The date the organization was added. ``` created<2011-05-01 ```   For more information on using date and time in your search, see [Searching by date and time](https://support.zendesk.com/hc/en-us/articles/4408835086106#topic_gbg_dvw_ld). |
| `notes` | All text in the notes field in the user's profile. ``` notes:EMEA ``` |
| `details` | All text in the details field in the organization's profile. ``` details:london ``` |
| `tags` | Specify tags that have been added to the organization, or specify `none` to search for organizations without tags. ``` tags:premium ```   For more information about tagging users and organizations, see [Adding tags to users and organizations](https://support.zendesk.com/hc/en-us/articles/4408881573658). |
| `customfield` | Custom organization fields. ``` plan_type:platinum ``` For more information, see [Searching custom user and organization fields](#topic_pyt_m1s_vk). |
| `external_id` | The external ID of the organization or specify **none** to search for users without an external ID. ``` external_id:00112345 ``` |

## Searching custom user and organization fields

You can search for data in custom user fields and custom organization fields by using the key that identifies the custom field.

**To locate the key for a custom field**

1. Navigate to the list of custom fields:
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **People** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)) in the sidebar, then select **Configuration > Organization fields**.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **People** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)) in the sidebar, then select **Configuration > User fields**.
2. Click the name of a custom field.

   The field key appears in the properties panel on the right.

You can search for users and organizations that have no value in a specific custom field, by using none as the search term, along with the custom field key. For instance, if you have a custom field key *foo*, a search for *foo:none* returns all users or organizations with the empty custom field *foo*.

Note: You cannot search for data in custom ticket fields the same way that you can for custom user and custom org fields. For custom ticket fields you can search for data in drop-down and checkbox fields based on their tags. For more information, see [Searching custom ticket fields](https://support.zendesk.com/hc/en-us/articles/4408882086298#topic_wly_fev_uc).

| Field type | Operators | Examples |
| --- | --- | --- |
| Drop-down list | : | Find users or organizations where **plan\_type** is platinum: ``` plan_type:platinum ``` Find users or organizations where **plan\_type** is platinum or gold: ``` plan_type:platinum plan_type:gold ``` |
| Text Multi-line text | : | Find users or organizations where **product\_name** contains widget: ``` product_name:widget ``` |
| Regular expression | : | Find users or organizations where **product\_name** contains the multi-word phrase "red widget:" ``` product_name:"red widget" ``` |
| Numeric | >, <, >=, <=, : | Find users or organizations where **num\_agents** is exactly 5: ``` num_agents:5 ``` Find users or organizations where **num\_agents** is between 4 and 10, inclusive: ``` num_agents>4 num_agents<10 ``` |
| Decimal | >, <, >=, <=, : | Find users or organizations where **avg\_score** is greater than 14.5: ``` avg_score>14.5 ``` Find users or organizations where avg\_score is between 10.1 and 15.3, exclusive: ``` avg_score>10.1 avg_score<15.3 ``` |
| Check box | : | Find users or organizations where **is\_active** is true: ``` is_active:true ``` |
| Date | >, <, >=, <=, : | Find users or organizations where **subscription\_date** is before 2013-06-23: ``` subscription_date<2013-06-23 ``` Find users or organizations where **subscription\_date** is between 2012-05-23 and 2013-06-23, exclusive ``` subscription_date>2012-05-23 subscription_date<2013-06-23 ``` |
| Lookup relationship | | Searching by lookup relationship field values is not supported. |