# JSONata reference for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357756884250-JSONata-reference-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

JSONata Exerciser: <https://try.jsonata.org/>  
JSONata functions: [String](https://docs.jsonata.org/string-functions), [Number](https://docs.jsonata.org/numeric-functions), [Object](https://docs.jsonata.org/object-functions), [Array](https://docs.jsonata.org/array-functions)

Force string type: $string(Account.Order[0].Product[0].ProductID): "858383"  
Force number type: $number(Account.Order[0].Product[0].SKU): 406654608

## Day & Time

$now() > ISO 8601, e.g. 2022-10-17T09:50:03.163Z  
$millis() > UNIX Epoch in milliseconds, e.g. 1666000139832

**To Millis (UNIX x 1000)** (for any math conversions and comparisons):

$toMillis(date)  
> e.g. 1626335334767

If your date is not in ISO 8601 format, you can still use toMillis by specifying the input format, e.g. $toMillis('2020-09-09 00:00:00 +02:00', '[Y0001]-[M01]-[D01] [H01]:[m01]:[s01] [Z]')

**From Millis (UNIX x 1000)** (human-readable, pass [output pattern](https://www.w3.org/TR/xpath-functions-31/#date-picture-string) as a param:

$fromMillis($toMillis(date), '[M01]/[D01]/[Y0001] [h#1]:[m01][P]')  
> e.g. 07/15/2021 7:48am

Example: Difference between orderDate and now():

($millis() - $toMillis(orderDate))/1000/60 > To minutes  
($millis() - $toMillis(orderDate))/1000/60/60/24 > To days

> e.g. 461 days, which can now be used on Conditional Block number operators: <>=

## Aggregating multiple results: Cards & Carousels

(Keep in mind the [technical limitations](https://support.zendesk.com/hc/en-us/articles/8357749513370-Carousels) when testing on a live CRM widget.)

IMPORTANT: C&Cs in the dialogue builder look for arrays. Unless you define your target output in JSONata as [], it may return an object instead and will throw a technical error.

When output in an AI agent text message, (un-nested) objects will render as [object Object], arrays as [object Object],[object Object].

Basic query to create a new object per entry:

```
Account.Order.Product.{'Quantity': Quantity}
```

Simple C&C:

```
Account.Order.Product[[0..8]].{  
'SKU': $substring(SKU, 0, 50), 'Quantity': Quantity}
```

… [[0..8]] > Range of results with first item being index 0, 10 objects in total being the max. limit for most CRMs  
… $substring(SKU, 0, 50) > Cut off excess string letters with first letter being index 0

Optional Fallback Card in case response body is empty / not found:

```
Account.Order.Product ?   
[Account.Order.Product[[0..8]].{  
'SKU': $substring(SKU, 0, 50), 'Quantity': Quantity}] :  
[{"SKU" : "Product Not Found"}]
```

## Aggregating multiple results: Email

```
$join(Account.Order.Product.(  
"SKU: " & SKU & ", " & "Price: " & Price), '\n')
```

… '\n' > Render a new line to separate results if your CRM supports basic formatting