# Distributing leads, contacts, and deals across your Sell team (round robin)

Source: https://support.zendesk.com/hc/en-us/articles/4408821347226-Distributing-leads-contacts-and-deals-across-your-Sell-team-round-robin

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on Suite Professional plans and above](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_suite_pee.png)

![Available on Sell Growth plans and above](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_pee.png)

Using [Distribution pools](https://support.zendesk.com/hc/en-us/articles/4408839201178), you can automatically assign leads, contacts, or deals to the team members in the pool.

When you set up a distribution pool, the users you include are allocated records (leads, contacts, or deals), using a *round robin* mechanism. This means that the first user added to the distribution pool receives the first record, and each subsequent record is allocated to each subsequent user in the list until all the users have one record. The distribution starts again, allocating the next record to the first user, and so on.

There are certain rules that apply when using distribution pools:

1. All users can see distribution pools.
2. If a user has reassign permissions, the user can reassign leads, contacts and deals to distribution pools.
3. Only admins can create and manage distribution pools.
4. You can assign a distribution pool anywhere in Sell that you assign an owner for a lead, contact, or deal.
5. You can set up a distribution pool for leads, for contacts, or for deals. You can't combine these types of records within a distribution pool.

In this example, there is a lead distribution pool that contains three users (User A, User B, and User C). After you assign the lead distribution pool:

1. The first lead that is created is allocated to User A.
2. The second lead that is created is allocated to User B.
3. The third lead that is created is allocated to User C.
4. The fourth lead that is created is allocated to User A.
5. If the Owner field of an existing lead is then edited to specify the distribution pool, the lead is allocated to User B (because User B is the next user in the distribution pool).

The distribution pool is held centrally in Sell, so that any method that uses it (for example, the Lead Capture Form, Import, or API) allocates records equally among the users in the distribution pool.

You can't define the order of users in the distribution pool.

If the distribution pool is modified to include a new user, the new user moves to the end of the distribution pool. If the distribution pool is modified to delete a user, the pool continues without that user.

The next user in the distribution pool receives a notification (based on their settings), and the lead, contact, or deal is assigned to them.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_dist_lead_assigned.png)

You can allocate and view distribution pools for leads from the following places:

- Lead details page: **Owner** field, on web and mobile
- Lead Capture Form: **Assign leads to** field
- Import: **Owner** field
- Lead conversion: **Owner** field
- Sell REST API and any supported integrations

You can allocate and view distribution pools for contacts from these places:

- Contact details page: **Owner** field
- Import: **Owner** field
- Lead conversion: **Owner** field
- Sell REST API and any supported integrations

You can allocate and view distribution pools for deals from these places:

- Deals details page: **Owner** field
- Import: **Owner** field
- Lead conversion: **Owner** field
- Deal created from an existing contact
- Sell REST API and any supported integrations

See [Assigning distribution pools](https://support.zendesk.com/hc/en-us/articles/4408823875354) for more information.