# Use expressions in prototypes

Source: https://help.figma.com/hc/en-us/articles/15253194385943-Use-expressions-in-prototypes

---

Before you start

Who can use this feature

 

Available on [any paid plan](https://help.figma.com/hc/en-us/articles/360040328273).

Anyone with `can edit` access to a file can create prototypes.

Anyone with `can view` or `can view prototypes only` access to a file can view prototypes.

Prototyping with variables allows you to create realistic prototypes that change based on user selection, using only a few simple frames and interactions.

Expressions can help make your prototypes even more powerful. With expressions, you can generate dynamic string or number values, or even evaluate boolean expressions.

Prototyping with expressions makes it possible to do things such as:

- Create a shopping cart that calculates purchase total
- Build objects that scale in size, like volume or progress bars
- Combine and build new text strings based on user selection

New to variables? Learn more here:

- [Guide to variables →](https://help.figma.com/hc/en-us/articles/15339657135383)
- [Use variables in prototypes →](https://help.figma.com/hc/en-us/articles/14506587589399)

Want to get more hands-on practice?

Check out the [advanced prototyping playground file →](https://www.figma.com/community/file/1234939241273272375)

Looking for more examples of how you can use variables in prototypes? Check out some more [advanced prototyping examples →](advanced-prototyping-examples.md)

## Where to use expressions

Expressions provide a way to manipulate the values of variables with basic operations. They can be used in:

- The **Set variable** prototype action, if the selected variable is a number, string, or boolean type
- The **Conditional** prototype action, as a part of a [conditional statement](https://help.figma.com/hc/en-us/articles/15253220891799)

You can write expressions directly in the following fields on the **Interaction details** modal:

![1: An interaction details panel, with a Set Variable action setting the itemCount variable to itemCount + 1. 2: An interaction details modal, with a Conditional action evaluating IF itemCount == 0.](https://help.figma.com/hc/article_attachments/15262846249879)

1. **[Set variable] to**: Enter an expression to represent the new value of the selected variable
2. **[Conditional] if**: Enter a boolean expression to represent the condition required for the action

To build expressions in your prototype, you can either write them directly in the available fields using supported syntax, or use the selection panel to choose from suggested variables and operators.

![1. Interaction details modal. User clicks suggested variables and operators from the dropdown to build an expression. 2. Interaction details modal. User manually types in variables and operators to build an expression.](https://help.figma.com/hc/article_attachments/15308370542231)

Once your expression is complete, press `Enter` or `Return`. Only expressions written with supported operations and syntax will work. Invalid expressions will be outlined in red.

## Write expressions

Expressions are made up of values and operators.

- **Operators** represent the function you are performing or evaluating (such as addition or subtraction)
- **Values** are the items that the operators are performing on or evaluating

For example, take a look at the following expression:

```
variableName + 2
```

In this example, the operator is addition, represented by the + plus symbol. The values are `variableName` and `2`.

The expression type determines which values and operators are available.

### Numerical expressions

Numerical expressions can be written with the following value types:

- Number variables
- Number literals (such as 0.5, 1, 10)

The following operators can be used in numerical expressions:

|  |  |
| --- | --- |
| **Operation** | **Symbol** |
| Addition | + |
| Subtraction | - |
| Multiplication | \* |
| Division | / |

![An interaction on an Add to Cart button. The interaction is setting the number totalCost variable to subTotal multiplied by salesTax.](https://help.figma.com/hc/article_attachments/15282183782167)

### String expressions

String expressions can be written with the following value types:

- String literals (such as "John Doe”, “item 2”, “5”)
- Number literals
- String and number variables

String literals must be contained in quotations. Number values can be added on to a string value.

The following operator can be used in string expressions:

|  |  |
| --- | --- |
| **Operation** | **Symbol** |
| Add to string | + |

![An interaction on an avator selection frame. The interaction is setting the value of the string userName variable to Ernie, then setting the value of the string welcomeMessage variable to Welcome back + userName.](https://help.figma.com/hc/article_attachments/15282183788055)

### Boolean expressions

Boolean expressions can be written with the following value types:

- Boolean literals (true, false)
- Number literals
- String literals
- Boolean, string, and number variables

The following operators can be used in boolean expressions:

|  |  |
| --- | --- |
| **Operation** | **Symbol** |
| Equal to | == |
| Not equal to | != |
| And | and |
| Or | or |
| Greater than | > |
| Less than | < |
| Greater than or equal to | >= |
| Less than or equal to | <= |
| *Addition\*\** | + |
| *Subtraction\*\** | - |
| *Multiplication\*\** | \* |
| *Division\*\** | / |
| *Add to string\*\** | + |

\*\* Numerical and string operators are not used to evaluate boolean expressions, but can be used as supporting operators in [complex expressions](https://help.figma.com/hc/en-us/articles/15253194385943#Complex_expressions_and_order_of_operations).

![A design of a cake making checklist. On the final step, there is an interaction:
  Set boolean variable cakeComplete to cakeVisibility == true and frostingVisibility
  == true and sprinkleVisibility == true.](https://help.figma.com/hc/article_attachments/15307169876247)

Boolean expressions must resolve to a `true` or `false` value. When setting a boolean variable with an expression, the result of the expression is evaluated to have either a true or false value—therefore setting the new value of the boolean variable.

For example, take a look at the simple interaction and expression below:

```
Set itemCount to 0  
itemCount > 5
```

The value of `itemCount` is `0`, which is not greater than `5`. Therefore, the value of this expression is `false`. However, now take a look at the following example:

```
Set itemCount to 6  
itemCount > 5
```

The value of `itemCount` is `6`, which is greater than `5`. Therefore, the value of this expression is `true`.

Examples of boolean expressions are listed in the tabs below. For these examples, the following statements are true:

```
numberVariable1 ==  1  
numberVariable2 ==  2  
stringVariable1 ==  red  
stringVariable2 ==  blue
```

Equal to (==) Not equal to (!=) And (and) Or (or)

- Returns `true` when the values are equal.
- Returns `false` when the values are not equal.

**Examples:**

```
Set booleanVariable to:  
numberVariable1 == numberVariable2
```

**Answer:** Since `1` does not equal `2`, `booleanVariable` is set to `false`.

```
Set booleanVariable to:  
numberVariable1 + 1 == numberVariable2
```

**Answer:** Since `1` + `1` does equal `2`, `booleanVariable` is set to `true`.

- Returns `true` when the values are not equal.
- Returns `false` when the values are equal.

**Examples:**

```
Set booleanVariable to:  
stringVariable1 != stringVariable2
```

**Answer:** Since `red` does not equal `blue`, `booleanVariable` is set to `true`.

```
Set booleanVariable to:  
numberVariable1 + 1 != numberVariable2
```

**Answer:** Since `2` does equal `2`, `booleanVariable` is set to `false`.

- Returns `true` when both values are true.
- Returns `false` if one or both values are false.

**Examples:**

```
Set booleanVariable to:  
numberVariable1 == 1 and numberVariable2 == 2
```

**Answer:** Since `1` equals `1` *and* `2` equals `2`, `booleanVariable` is set to `true`.

```
Set booleanVariable to:  
numberVariable1 > 5 and numberVariable2 == 2
```

**Answer:** Since `1` is not greater than `5`, `booleanVariable` is set to `false`.

- Returns `true` when one or both values are true.
- Returns `false` when both values are false.

**Examples:**

```
Set booleanVariable to:  
stringVariable1 == red or stringVariable2 == purple
```

**Answer:** Since `red` does equal `red`, `booleanVariable` is set to `true`.

```
Set booleanVariable to:  
stringVariable1 == green or stringVariable2 == orange
```

**Answer:** Since `red` does not equal `green` *or* `orange`, `booleanVariable` is set to `false`.

Note: Boolean expressions are also used to evaluate [conditional statements](https://help.figma.com/hc/en-us/articles/15253220891799).

## Complex expressions and order of operations

Complex expressions are built by using multiple operators within a single expression. Use parentheses to group expressions.

In complex expressions, basic math operations are performed in the following order:

1. Parentheses
2. Multiplication/Division
3. Addition/Subtraction

Boolean expression operators are performed in the following order:

1. Parentheses
2. Comparisons (==, !=, >, <, etc.)
3. And
4. Or

All operations are performed from left to right.

For example, in the following expression:

```
x + y * z
```

First, multiply `y` by `z`. Then, add `x`.

In the following boolean expression:

```
x == (y > z)
```

First, evaluate if `y` is greater than `z`. Then, evaluate if `x` is equal to the solution of `y > z`.

## Concepts in expressions

### Negative numbers

You can use negative numbers in expressions. To represent a negative number, use a `-` minus sign.

### Negate boolean values

Negating a boolean value means flipping its logical state. Negating a true boolean value would make it false, and negating a false boolean value would make it true.

Negating boolean values can be valuable when buildings objects that have two opposing states—such as toggles, buttons, or other settings.

In order to negate a boolean value, enter `!` or `not` before the boolean variable.

For example, consider the following expression: `! boolVar`

- If the `boolVar` value is `true`, the statement is overall evaluated to be `false`.
- If the `boolVar` value is `false`, the statement, is overall evaluated to be `true`.