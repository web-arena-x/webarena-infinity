# Why do awarded bids create commitments with an O - Other cost type? - Procore

Source: https://support.procore.com/faq/Why-do-awarded-bids-create-commitments-with-an-O-Other-cost-type

---

## Background

Users can specify which cost codes bidders are allowed to submit pricing for when setting up a bid package, which applies to both Bidding 1.0 (Legacy) and Bidding 2.0 (Beta). However, it's important to note that *cost types* cannot be selected during this setup.

## Answer

Once a bid is awarded and converted into a contract, Procore requires both a cost code and a cost type for each line item to function properly within the Budget tool. To prevent issues during this transition, Procore automatically assigns the default **O – Other** cost type to each line item in the new contract.

Problems may arise if a company has changed the code or description of the **O – Other** cost type to better fit internal workflows. While the visual label may be different, Procore continues to recognize the original **cost type ID**, which is still linked to **O – Other**. As a result, line items in awarded contracts may display an unintended or confusing cost type.

Currently, there is no way to configure a different default cost type during bid conversion. The only solution is to **manually update the cost type** on the affected line items after the contract has been created.

### How to Tell O - Other has been Updated

While there is no direct way within Procore to identify whether a cost type was originally **O – Other**, there is a useful workaround. If you hover over the delete icon for a particular cost type and see a message indicating it cannot be deleted, that’s a strong indicator it’s a system default cost type rather than a custom one added manually.

![bid-faq.png](https://support.procore.com/@api/deki/files/542018/bid-faq.png?revision=1)

## See Also

Beta: [Award a Bid and Convert it to a Subcontract or Purchase Order](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/award-a-bid-and-convert-it-to-a-subcontract-or-purchase-order "Award a Bid and Convert it to a Subcontract or Purchase Order")  
Legacy: [Award a Winning Bid and Convert it into a Purchase Order](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/award-a-winning-bid-and-convert-it-into-a-purchase-order "Award a Winning Bid and Convert it into a Purchase Order")  
Legacy: [Award a Winning Bid and Convert it into a Subcontract](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/award-a-winning-bid-and-convert-it-into-a-subcontract "Award a Winning Bid and Convert it into a Subcontract")