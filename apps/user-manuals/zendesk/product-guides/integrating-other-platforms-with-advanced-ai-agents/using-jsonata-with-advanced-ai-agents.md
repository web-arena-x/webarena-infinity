# Using JSONata with advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357756877466-Using-JSONata-with-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

JSONata is an open-source query and transformation language designed for JSON data which we will use to access and parse data from an API-returned JSON response body.

You can easily test your queries using <https://try.jsonata.org/> or, if one prefers some fancier Javascript-esque format, <https://www.stedi.com/jsonata/playground>. Let’s stick to JSONata’s own Exerciser for this introduction.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_f9I36Xn-BRywAHTklHjZHZOAYXh7XZbaAGIjp7mysSB9AXtJBP5Ow5JsqEwBH_rTW4DQNdgExYjtibEITccFDlPaL8dqYVjdLXOZZs5VZr8t1rr-YezX4lsTwCSjZvEBn9iZ0KgoIDHibVw9h0-CzA.png)

The exerciser will launch its Invoice dummy object which we will be using as a point of reference. The raw input data is on the left, the JSONata expression query is on the top right, and the result found by that expression will be rendered on the bottom right.

To re-align the JSON object use the little indent tool on the very right of the dummy object and save any current expression using the share functionality on the top right.

That’s all you need to know about the Exerciser for now! Next up, use a query within the default Invoice template.

#### If you're just looking for the key learnings or a point of reference after the enablement - check out our [cheatsheet.](https://support.zendesk.com/hc/en-us/articles/8357756884250)

## Mapping Data

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_Csi8VEb0rx7PRIT104I-sUfXv83fjioHS9Dld9R_yTNporVEnmxEt3tm9zKRHgdga-R0Nwf5C-CVp-dwp1Ih_FA_DLsqnaOqlnpu4apA2Kk96ITwi2z8idgjodTXIAkggeEd1Ot5zJeH8PoUkfpEYg.png)

Root-level field: Account Nested field in root object: Account.'Account Name' If it finds another JSON structure, you can use dot notation to enter the below fields.

**Nested field in a root level array****:**

First order in this account:

```
Account.Order[0]
```

Reminder: Array indexing starts at [0] for the first item. The shortcut to the last item in an array is [-1].

First product’s colour in this same object:

```
Account.Order[0].Product[0].Description.Colour
```

**Retrieve an array of items from a root level array****:**

If multiple values match a query, JSONata will automatically aggregate them.

Check the entire object Account.Order and retrieve all OrderIDs in it:

```
Account.Order.OrderID
```

## Filtering Data

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_2X105D1eJi9AIEGi0ImPIU8Kk6YFxKZEQet-02uOpgPHvT-5xidyVMQGLHMxd8_TgGdn3iIhnRyrI_3bUW4T3Rcc1_zz5AOF-v_mB0q503WyrnL0QZOUcyh_3hMp6qw0UzCK6VO3m07ScEpV2XNWuA.png)

Define the target that is being accessed, e.g.

```
Account.Order.OrderID
```

Now add the condition in the matching place - for every run through an array, add a pair of [] brackets:

e.g. only include Orders with Products with a price higher than 30 which were ordered only once and show the respective  Product Name:

```
Account.Order.Product[Price > 30 and Quantity = 1].'Product Name'
```

e.g. only include Orders with Products with a Description.Weight of more than 1 and show the respective OrderID:

```
Account.Order[Product[Description.Weight > 1]].OrderID
```

Alternatively, you can also check for a truthy statement, e.g.

```
Account.Order[Product["Purple" in Description.Colour]].OrderID
```

Additionally, this can be combined with wildcard searches if you want to check multiple keys, e.g.

```
Account.Order[Product["Purple" in Description.*]].OrderID
```

## Other Path Operators

(<https://docs.jsonata.org/path-operators>)

**^( ... ) (Order-by)**

Sort by descending OrderID:

```
Account.Order^(>OrderID)
```

Sort by cheapest to most expensive product:

```
Account.Order.Product^(Price)
```

**\* (Wildcard)**

Access any SKU regardless of direct parent naming:

```
Account.Order.*.SKU
```

Access any Product Name, regardless of any parent naming:

```
**.'Product Name'
```

**% (Parent)**

Searches backwards in current data structure:

```
Account.Order.Product.{ 
 'Account': %.%.`Account Name`, 
 'Order': %.OrderID, 
 'Product': `Product Name` 
}
```

**# (Positional variable binding)**

Creates an index, starting at 0:

```
Account.Order#$i[Product.[Quantity > 0]].{ 
 'Order ID': OrderID, 
 'Order Number': $i + 1 
}
```

**@ (Context variable binding)**

Temporarily assigns new data structure, allowing cross-object mappings:

```
Account@$A.Account.Order@$O.{   
 "Account Name": $A.'Account Name', 
 "OrderID": $O.OrderID 
}
```

## Conditionals

### 

Similar to the ternary operator in JS, you can use ? for if and : for else statements. Boolean operators and/or can be used to create chain conditions.

IF CONDITION IS TRUTHY ? DO THIS (ELSE DO NOTHING)

IF CONDITION IS TRUTHY ? DO THIS : ELSE DO THIS

```
$count(Account.Order) > 1 ? "REPEAT CUSTOMER"
```

```
Account.Order[0].Product[0].Price <= 100 or Account.Order[0].Product[1].Price <= 100 ? "Bargain" : "VIP" = "Bargain"
```

## Manipulating Data

### Supported Operators

| | | |
| --- | --- | --- |
| Operator | Priority | Description |
| Multiply (\*) | 5 | Multiplies two numbers |
| Divide (/) | 5 | Divides two numbers |
| Modulus (%) | 5 | Returns the remainder when dividing two numbers |
| Concatenate (&) | 4 | Concatenates two strings |
| Add (+) | 4 | Adds two numbers |
| Subtract (-) | 4 | Subtracts two numbers |
| Equal (=) | 3 | Tests whether two values are equal |
| Not Equal (!=) | 3 | Tests whether two values are not equal |
| Greater Than (>) | 3 | Returns true if the left value is greater than the right value |
| Greater Than or Equal to (>=) | 3 | Returns true if the left value is greater than or equal to the right value |
| Less Than (<) | 3 | Returns true if the left value is less than the right value |
| Less Than or Equal to (<=) | 3 | Returns true if the left value is less than or equal to the right value |
| Logical AND (and) | 2 | Returns true if both the left and right values are true |
| Logical OR (or) | 1 | Returns true if either left value is true, or the right value is true |

e.g. concatenating strings:

```
Account.Order[0].Product[0].Description.Colour & " " & Account.Order[0].Product[0].'Product Name'
```

### Built-In Functions

Please note that these have been heavily abridged for readability's sake, complete documentation can be found here: <https://docs.jsonata.org/overview.html>

Note: a multi-line expression needs to be wrapped in ()

Force string type: $string(Account.Order[0].Product[0].ProductID): "858383"

Force number type: $number(Account.Order[0].Product[0].SKU): 406654608

Uppercase string: $uppercase(Account.Order[0].OrderID): "ORDER103"

Lowercase string: $lowercase(Account.Order[0].Product[0].Description.Colour): "purple"

Output random number between 0 and 1: $random()

Count objects in an array: $count(Account.Order)

Count objects in an array which match a condition:  $count(Account.Order.Product[Price > 30])

Number of characters in a string: $length(Account.'Account Name')

Replace / Remove certain characters in a string: $replace(Account.Order[0].Product[0].'Product Name', "Bowler ", ""): "Hat"

Cut of a string on specific character count: $substring($string(Account.Order[0].Product[0].ProductID), 1, 2)

Cut off a string on a specific pattern: $substringAfter(Account.Order[0].OrderID, "order")

Similar result using split + join:

$join($split(Account.Order[0].Product[0].'Product Name', " "), '\_')

Can also be written as a ~> function:

$split(Account.Order[0].Product[0].'Product Name', " ") ~> $join('\_')

Check if a string contains a specific pattern - pattern can be an exact string or regex:

$contains(Account.Order[0].Product[0].'Product Name', "Hat")

## Dates & Times

Most dates will be passed in the international standard of ISO 8601 and will look like this 2023-04-20T13:09:39+00:00 (carrying time zone information) or 2023-04-20T13:09:39Z (keyed to milliseconds offset from UTC). These are nicely human readable, but can’t be natively manipulated by JSONata.

Oftentimes, you will therefore have to transform them into UNIX time, which is the literal number of seconds that have elapsed since 00:00:00 UTC on 1 January 1970 (Unix Epoch) - which is not humanly readable anymore, but as an integer can be added / subtracted / compared to other UNIX dates. JSONata natively works with Millis, which are the MILLISECONDS since the Unix Epoch (so UNIX \* 1000).

$now(): "2023-04-20T13:39:58.216Z"

$millis(): 1681998518175

These millis can now be re-transformed into a date format of your choice by defining a picture (your target pattern) in a string: <https://www.w3.org/TR/xpath-functions-31/#date-picture-string>

Example patterns: <https://www.w3.org/TR/xpath-functions-31/#date-time-examples>

| | |
| --- | --- |
| Specifier | Meaning |
| Y | Year (absolute value) |
| M | Month in Year |
| D | Day in Month |
| F | Day in Week |
| H | Hour in day (24 hours) |
| h | Hour in half day (12 hours) |
| P | AM/PM marker |
| m | Minute in hour |
| s | Second in minute |
| Z | Timezone |

e.g. $fromMillis($millis(), '[M]/[D]/[Y01]') will return "4/20/23",

$fromMillis($millis(), '[D01].[M01].[Y0001] [H#1]:[m01]') will return "20.04.2023 13:51".

Putting this into practice - let’s say you have two dates in your response data, and you want to check how many days it’s been since TODAY.

"2023-04-20T00:00:00.000Z"

"20.04.2023"

Transform both of them into Milis - the second date is not in standard ISO 8601 pattern, so you’ll need to provide the picture in order for JSONata to know which value is your day, your month, your year as well as any time information you may have available.

$toMillis('2023-04-20T00:00:00.000Z') : 1681948800000

$toMillis('20.04.2023', '[D01].[M01].[Y0001]'): 1681948800000

You also have the current time in Milis via the standard function $millis(): 1681999968402

You can now simply subtract one from the other and receive the difference between the two dates in milliseconds: 1681999968402 - 1681948800000 = 51296367

Using common time conversion:

1000 milliseconds = 1 second

60 sec = 1 minute

60 min = 1 hour

And rounding down the result, you receive a total of 14 hours that passed between now and your provided timestamp:

$round(51296367 / 1000 / 60 / 60) = 14

**Combined into one line, you’re looking at an operation of:**

```
$round(($millis() - $toMillis('20.04.2023', '[D01].[M01].[Y0001]')) / 1000 / 60 / 60)
```

## Special Outputs

### Ticket “Oneliners”

Because you might only have one shot at a reply, you'll want to pass as much information in one single param as you can. JSONata handles the aggregation for you so you can freely play with the text copy.

Let’s say you want to render the SKUs and Prices of all products in your order:

```
Account.Order.Product
```

Since you ultimately just want to have one big line of text with all products considered, you can simply create one shared array with all the information required:

```
Account.Order.Product.(SKU & Price)
```

Now you just need to combine them into one big string with a line break character as a separator:

```
$join(Account.Order.Product.("SKUs: " & SKU & ", " & "Price: " & Price), "\n")
```

Note: Consider your CRMs limitations - Zendesk Support offers some basic formatting, so a \n will correctly translate into a line break when rendering in a reply email, but this might not be the case for all systems.

### Cards & Carousels

Cards and Carousels are the true strength of JSONata since it handles the data query and aggregation natively, as long as your response follows the same schema. A C&C consists of an array of objects in which each object represents one of your cards. A very simple example of a C&C structure with 2 cards could look something like this:

```
[ 
 { 
   "imageURL": data.url1, 
   "title": data.title1, 
   "description": data.description1 
 }, 
 { 
   "imageURL": data.url2, 
   "title": data.title2, 
   "description": data.description2 
 } 
]
```

Important is that all objects in the array follow the same structure so they may be accessed through the same shared key. Also be sure to keep your [CRM's limitations](https://support.zendesk.com/hc/en-us/articles/8357749513370) in mind.

For a straightforward example, let’s construct a C&C on the invoice sample data again. Let’s start with an array from the get-go - any query result with more than one response object will automatically convert to an array, but it’s good to have this failsafe in case your result only carries one object by itself.

```
[Account.Order.Product.'Product Name']
```

```
[Account.Order.Product.SKU]
```

```
[Account.Order.Product.Description.Colour]
```

These are some of the fields we’re interested in. Let’s combine them into one object - be sure to give each key in your target object a name:

```
[ 
 Account.Order.Product. 
 { 
   "name": 'Product Name',   
   "sku": SKU,   
   "colour": Description.Colour 
 } 
]
```

If you need a value a level higher, you can simply start your query a level higher. If you also want to include [Account.Order.OrderID] in your array:

```
[ 
 Account.Order. 
 { 
   "orderId": OrderID,   
   "name": Product.'Product Name',   
   "sku": Product.SKU,   
   "Colour": Product.Description.Colour 
 } 
]
```

You will notice that there is no direct 1:1 match anymore since each order can carry multiple items within, which is why this response creates seemingly random arrays of strings. You can solve this by accessing the parent object indirectly (see parent binding), temporarily assigning a different object structure in JSONata (see context variable binding), adding a secondary C&C which cycles through the items in the chosen order, or transforming data further, depending on your ideal UX. Here’s for example a transformed example:

```
[ 
 Account.Order. 
 { 
   "orderId": OrderID,   
   "name": $join(Product.'Product Name', ", "),   
   "totalPrice": $sum(Product.Price) 
 } 
]
```

If you want to bulletproof your query further, let’s add some fail safes in case you don’t have the expected response data (to cover e.g. a 404) and a cutoff in case the response returns more results than your CRM can support (e.g. 10 for SunCo widgets):

```
Account.Order ?   
 [Account.Order[[0..9]]. 
 { 
   "orderId": OrderID,   
   "name": $join(Product.'Product Name', ", "),   
   "totalPrice": $sum(Product.Price)}]   
: [{"orderId": "???", "name": "Cannot find your item?"}]
```

IMPORTANT: Make sure all C&C keys follow **camelCase** convention, **\_** param names are not supported.

Now all of those keys, e.g. orderId, name, totalPrice will be available to your Carousel. Change your Carousel type to dynamic on the UI and add the param name that hosts your query above, e.g. **orderList**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_DuUKVtv3PGQ9SOgC6nK0U96GJc2ZgE7j6JX6juy6BNYp1yi9RUDj9u3BbpifHKF7BLsH3hxQz8AcbH4ZiSnAX9xBKO_ifm6Q3Llaoq0r4eVinqTr8KRrm49hu09SNqUYlw5mA5cUIaWNROwH2ZAxtA.png)

You can now access any key in your array’s objects by adding a % shorthand - either by outputting them directly in chat on your cards:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_6aZUCEQ6C0mWuadybf1SYBEY_znS-puiqZXymR-qhcyc0vRXR15coNrnQY4aqBhQ1f_UPQ1Cltu25OxLWCYAs8EW9RVLxI4ggPBUtgIHOfVK2bKrPynAhnSU4UpBMJmM3yLLzKuZkS_WicL_VM8p_A.png)

Or by storing them to the session by populating your card of choice with an action referencing your chosen object’s key into a param name of your choice, e.g.:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_awNHNGi4u2c0GvWHA8HmIIwpLgMhhuSW4-j6vdiTucScBHllMLSR8o0jgFEG6opXBh1Dy9098bp5zbxp-rcSM1BbID6679LV8tVYwuTpxAGG7XGydWVPnXwp8Tl-jo4rcvK1KC2nw1xUdJq7ZtLTbg.png)

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_9ZphUE128n1hifw6Yg_az_t9ojX7zu_Ve9ps6s6ioWSxcdCcxL18o4_AB929yYQeWyFkx-oz4DOVOsv32Sb3780QRqcyitFKnmODju-B3gLLWSikISPW91KyzQx93sHwl55TZCxjiCzFIHlXTZUWrw.png)