# Using custom code steps in action flows

Source: https://support.zendesk.com/hc/en-us/articles/9853782610970-Using-custom-code-steps-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

An [action flow](https://support.zendesk.com/hc/en-us/articles/8855513857306) is a user-defined automated workflow. Each
action flow consists of an action flow trigger, which initiates the flow, and one or
more actions.

Custom code steps let you execute custom JavaScript to perform complex data
transformations, formatting, and advanced logic that aren't possible with the predefined
actions and steps. For example, you might use a custom code step to take information to
mask sensitive parts of an email address, validate the format of an email or order ID,
or even calculate future dates for follow-up reminders.

This article contains the following topics:

- [Adding and configuring custom code steps](#topic_j3q_xdb_chc)
- [Supported data types for custom code inputs and outputs](#topic_txg_s3c_chc)
- [AI prompt templates for generating custom JavaScript code for your action flow step](#topic_hmv_ydb_chc)
- [Examples custom code steps](#topic_cvv_tnc_chc)

**Disclaimer:** The example JavaScript for Action Builder’s custom
code step is provided for informational purposes only on an ‘as is’ basis. Zendesk does
not guarantee they will work for your use case and does not provide support for writing
or debugging custom JavaScript. Test in a test environment and do not include secrets or
other sensitive data.

## Adding and configuring custom code steps

If you need to execute code as part of an action flow, you can add a custom code
step. See [Supported data types](#topic_txg_s3c_chc)
to learn which data types are supported for inputs and outputs of custom code
steps.

**To add custom code to an action flow**

1. [Open an action flow.](https://support.zendesk.com/hc/en-us/articles/9052312956570#topic_ant_ttk_t2c)
2. In the action builder, beneath an existing step, click the **Add step**
   icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
3. In the step sidebar, under **Flow control and utilities**, click
   **Custom code**.
4. In the step sidebar, click **Add input** to [add inputs for the custom
   code](#topic_ssr_12b_chc).
5. In the step sidebar, click **Add output** to [add at least one
   output](#topic_qvx_b2b_chc).
6. In the step sidebar, under **Code**, [enter your custom JavaScript code](#topic_m3s_c2b_chc).
7. Click **Save**.

To ensure the custom code is working as expected, [test your action flow](https://support.zendesk.com/hc/en-us/articles/9052312956570#topic_uyj_qsw_3fc). If you run into
issues, see [Troubleshooting custom code steps](https://support.zendesk.com/hc/en-us/articles/9052312956570#topic_obr_cfb_chc).

### Adding inputs to custom code steps

Custom code steps can have a maximum of 50 inputs.

**To add inputs to a custom code step**

1. [Open an action flow](https://support.zendesk.com/hc/en-us/articles/9052312956570#topic_ant_ttk_t2c).
2. In the action builder, click on an existing custom code step or click
   the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)) to [add a custom code
   step](#topic_j3q_xdb_chc).
3. In the step sidebar, click **Add input**.
4. Under **Select variable**, select a variable from a previous step or
   the action flow trigger.

   Note: The input's data type is inferred from the
   selected variable.
5. Verify the input's **Name** value, which is automatically populated
   based on the selected variable but can be edited. Input names must
   adhere to these [requirements](https://support.zendesk.com/hc/en-us/articles/8855601898266#topic_gsd_llc_chc).
6. Click **Save**.

### Adding outputs to custom code steps

Custom code steps must have at least 1 output and up to 50 outputs.

Note: Your
custom code must return a value for each defined output.

**To add outputs to a custom code step**

1. [Open an action flow](https://support.zendesk.com/hc/en-us/articles/9052312956570#topic_ant_ttk_t2c).
2. In the action builder, click on an existing custom code step or click
   the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)) to [add a custom code
   step](#topic_j3q_xdb_chc).
3. In the step sidebar, click **Add output**.
4. Enter a unique **Name** for the output.

   It must adhere to these
   [requirements](https://support.zendesk.com/hc/en-us/articles/8855601898266#topic_gsd_llc_chc).
5. Select the output's data **Type**.
6. Click **Save**.

### Adding your custom code

The JavaScript in custom code steps must export a function that takes an
*inputs* object and returns an *outputs* object. Each time you add
a custom code step to an action flow, it is prepoulated with this framework,
which you can modify, expand upon, or delete and start fresh.

Although the custom code step is designed to be as user-friendly as possible,
admins might still require engineering support when implementing these
steps.

Keep the following requirements, limitations, and restrictions in mind:

- The code for a step can be a maximum of 10,000 characters.
- Your custom code must return a value for each [output](#topic_qvx_b2b_chc) defined for
  the step.
- The code you use in action flows must execute quickly and use a
  reasonable amount of memory.
- The following JavaScript restrictions apply:
  - The function must be synchronous. That means
    `async`, `await`, and
    `promise` aren't supported.
  - Network requests, such as `fetch`,
    `XMLHttpRequest`, and jQuery AJAX arent't
    supported.
  - You can't `import` or `require`
    external libraries or modules.

**To add your custom code**

1. [Open an action flow](https://support.zendesk.com/hc/en-us/articles/9052312956570#topic_ant_ttk_t2c).
2. In the action builder, click on an existing custom code step or click
   the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)) to [add a custom code
   step](#topic_j3q_xdb_chc).
3. Under **Code**, expand upon the provided example, delete the example
   and write your own logic, or use an [AI prompt](#topic_hmv_ydb_chc) to generate custom code for
   you.

   Your code must export a function that takes an *inputs*
   object and returns an *outputs* object. For
   example:

   ```
   // In the Inputs section for this step, add an input named status.
   // In the Outputs section for this step, add a text output named message.

   module.exports = (inputs) => {
   // Access inputs using inputs.<name>
    const msg = 'Your text was ' + inputs.status + '.'

   // This return must include all outputs.
   return {
     message: msg
     }
   }
   ```

   Note: As
   you write your code, the editor offers helpful suggestions for valid
   JavaScript operations. Typos and invalid code are marked with a
   squiggly, red underline. Hover your mouse over the underlined
   section to view the error message.
4. Click **Save**.

## Supported data types for custom code inputs and outputs

The custom code step accepts and returns the following data types, each of which
appears in your code as the equivalent JavaScript type.

| Input type | JavaScript data type | Example |
| --- | --- | --- |
| Text | string | "Hello there!" |
| Number | number | 123, -5, 0 |
| Decimal | number | 12.67, 1.0, 0.0 |
| True/false | boolean | true, false |
| Date\* | string | "2025-10-27" |
| Date and time\* | string | A UTC date and time  "2025-10-27T10:30:00Z"  A date and time with a time zone offset:  "2025-06-22T05:11:28+10:00"  A UTC date and time with milliseconds:  "2025-03-08T06:01:21.415Z" A date and time with a time zone offset and milliseconds:"2025-07-23T13:33:17.031-3:00" |
| Text array | array of strings | ["Hello there!", "How are you"] |
| Number array | array of numbers | [12, 34, 56, 0] |
| Decimal array | array of numbers | [2.1, 6.3, 6.01, 0.1] |
| True/false array | array of booleans | [true, true, false] |
| Date array | array of strings | ["1997-08-29", "2004-07-25", "2011-04-21"] |
| Datetime array | array of strings | ["1977-05-25T12:45Z", "1980-05-21T15:00Z", "1983-05-25T19:30Z"] |

Note: \* Date and datetime inputs are provided to your code as
strings. To perform date operations, convert these values to JavaScript Date objects
first.

The following data types below aren’t supported as outputs. If you need to return one
of these types, convert it to a string before outputting it as a Text or Text
array:

- Object
- Object array
- Mixed array
- Array array

## AI prompt templates for generating custom JavaScript code for your action flow step

The following prompts can be used with AI tools, such as ChatGPT, to generate code
for your custom code step. The pompts include guidance about the supported data
types and the required structure for the code.

### Prompt 1

```
Write a piece of JavaScript code. The code must export a function that takes an inputs object and returns an outputs object, for example:

module.exports = (inputs) => {
let msg = "Your text was " + inputs.inputText + "."
return {
  outputMessage: msg
  }
}

Supported data types:
Strings, numbers, booleans, dates (YY-MM-DD) and datetimes (YY-MM-DDTHH:mm:SSZ) are supported.  Arrays of those are supported too.

Objects, arrays of arrays, and arrays of objects are not supported.  When used as inputs or outputs they must be stringified and passed as strings.

Check for missing or invalid data, and ensure it is handled gracefully by returning a valid output:

for strings, output the empty string ""
for numbers, output -1
for booleans, output false
for arrays, output the empty array []
for objects, output the empty object {}

Comment the code:

Include a comment at the top which briefly describes what the code does.

Include comments directing the reader to create the inputs and outputs, for example: // Make sure to create the following inputs: field_tag (Text).
In comments, refer to variable types with the following friendly names:
string: use "Date" for dates, "Date and time" for datetimes, else use "Text"
number: use "Number” or "Decimal"
boolean: use "True/False"
array: use "Number array", "Text array" etc

The code should... <DESCRIBE WHAT YOU WANT YOUR CODE TO DO HERE>
```

### Prompt 2

```
Write a piece of JavaScript code. The code must export a function that takes an inputs object and returns an outputs object, for example:

module.exports = (inputs) => {
let msg = "Your text was " + inputs.inputText + "."
return {
outputMessage: msg
}
}

Supported input and output data types:
Strings, numbers, booleans, dates (YY-MM-DD) and datetimes (YY-MM-DDTHH:mm:SSZ) are supported.  Arrays of those are supported too.

Objects, arrays of arrays, and arrays of objects are not supported.  When used as inputs or outputs they must be stringified and passed as strings.

Comment the code:

Include a comment at the top which briefly describes what the code does.

Include comments directing the reader to create the inputs and outputs, for example: // Make sure to create the following inputs: field_tag (Text).
In comments, refer to variable types with the following friendly names:
string: use "Date" for dates, "Date and time" for datetimes, else use "Text"
number: use "Number" or "Decimal"
boolean: use "True/False"
array: use "Number array", "Text array" etc

The code should... <DESCRIBE WHAT YOU WANT YOUR CODE TO DO HERE>
```

## Examples custom code steps

The following examples demonstrate how the custom code step can be used to address
common automation scenarios:

- [Formatting basic ticket details into a human-readable comment](#topic_ey3_fpc_chc)
- [Calculating the next hour from now](#topic_htc_3pc_chc)
- [Validating the formatting of an email address](#topic_ysh_lpc_chc)
- [Masking an email address](#topic_rjf_npc_chc)
- [Mapping an internal identifier to a human-readable name](#topic_lrd_qpc_chc)
- [Checking whether any items in a list begin with specific characters](#topic_isp_5pc_chc)
- [Comparing two lists of values](#topic_upl_bqc_chc)
- [Finding an order ID within text](#topic_c3y_fqc_chc)
- [Generating a random number](#topic_pnm_jqc_chc)
- [Generating three random numbers between one and seven](#topic_nzz_mqc_chc)

Note: Zendesk provides these JavaScript examples for instructional purposes only.
Zendesk does not guarantee compatibility with your specific use case and does not
offer support for writing or debugging custom JavaScript. Always test code in a test
environment first, and avoid including sensitive data.

### Formatting basic ticket details into a human-readable comment

```
module.exports = (inputs) => {
  // This code takes text inputs 'status' and 'priority', and a number input 'ticket_id', and outputs a friendly message combining these values.

  // Make sure to create the following inputs:
  // status (Text)
  // priority (Text)
  // ticket_id (Number)

  const message = `Ticket ${inputs.ticket_id} has status ${inputs.status} and priority ${inputs.priority}.`

  // Make sure to create the following outputs:
  // message (Text)
  return {
    message,
  }
}
```

### Calculating the next hour from now

In the example, the time is currently 2025-10-27T09:17:00Z. Therefore, the
following code returns 2025-10-27T10:00:00Z.

```
module.exports = (inputs) => {
  // This code calculates the next full hour from the current UTC time

  // No inputs required

  // Make sure to create the following outputs:
  // nextHour (Date and time)

  // Create a Date object for the current time
  const nextHour = new Date()

  // Round up to the next hour by:
  // 1. Setting minutes, seconds, and milliseconds to 0
  nextHour.setUTCMinutes(0, 0, 0)
  // 2. Adding 1 hour
  nextHour.setUTCHours(nextHour.getUTCHours() + 1)

  return {
    nextHour: nextHour.toISOString(),
  }
}
```

### Validating the formatting of an email address

```
module.exports = (inputs) => {
  // This code takes a text input 'emailAddress',
  // uses regex to do a basic check whether it is a valid email format,
  // and outputs a boolean 'emailIsValid'.

  // Make sure to create the following inputs:
  // emailAddress (Text)

  // Simple email regex pattern
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

  const emailIsValid = emailRegex.test(inputs.emailAddress)

  // Make sure to create the following outputs:
  // emailIsValid (True/False)

  return {
    emailIsValid
  }
}
```

### Masking an email address

This example replaces portions of an email address with asterisk characters. For
example, "Could you please confirm your email address is
d\*\*\*\*\*\*n@zendesk.com?"

```
// This code takes an email address input and returns a masked version where the local part is partially replaced with '*', preserving the first and last characters.

// Make sure to create the following input:
// emailToMask (Text)

// Make sure to create the following output:
// maskedEmail (Text)

module.exports = (inputs) => {
  
  const [emailName, emailDomain] = inputs.emailToMask.split("@")

  let maskedEmailName = emailName

  if (emailName.length > 2) {
    maskedEmailName = emailName[0]
    maskedEmailName += "*".repeat(emailName.length-2)
    maskedEmailName += emailName[emailName.length-1]
  }

  return {
    maskedEmail: `${maskedEmailName}@${emailDomain}`
  }
}
```

### Mapping an internal identifier to a human-readable name

Mappings like this are useful for converting internal ids, such as a dropdown
ticket field’s tag, to more user-friendly names like a value shown in a
dropdown.

You can use this approach for tasks such as:

- Translating Slack channel ids to channel names
- Converting JIRA project ids to project names
- Mapping Zendesk ticket statuses to corresponding JIRA issue
  statuses

```
const optionMap = {
  option_01_ivory: 'ivory',
  option_02_cream: 'cream',
  option_03_white: 'white',
  option_04_bone: 'bone',
}

module.exports = (inputs) => {
  // This code takes a text input 'optionTag',
  // and outputs the corresponding 'optionName' based on a predefined mapping.
  // If the input is missing or does not match any tag, it returns an empty string.

  // Make sure to create the following inputs:
  // optionTag (Text)

  const optionName = optionMap[inputs.optionTag] || ''

  // Make sure to create the following outputs:
  // optionName (Text)

  return {
    optionName,
  }
}
```

### Checking whether any items in a list begin with specific characters

This example checks whether any items in a list begin with specific characters.
For example, if you're searching for items beginning with “customer” and your
list of tags contains [“critical\_bug”, “customer\_24601”, “escalation”], the
result would be `true` because “customer\_24601” begins with
“customer”.

```
module.exports = (inputs) => {
  // This code takes a text array 'tags' and a text string 'searchTerm',
  // and outputs a boolean 'matchFound' indicating whether any tag begins with the searchTerm.

  // Make sure to create the following inputs:
  // tags (Text array)
  // searchTerm (Text)

  const matchFound = inputs.tags.some(tag => tag.startsWith(inputs.searchTerm))

  // Make sure to create the following outputs:
  // matchFound (True/False)

  return {
    matchFound
  }
}
```

### Comparing two lists of values

This example compares two lists and removes all values from the first list that
are also present in the second.

For example, given a list of ticket CCs and a list of disallowed users, any
disallowed users found in the CC list will be excluded from the output list
(`cleanCCs`). This method can also be used to filter out tags
that should be removed from a ticket or user.

```
module.exports = (inputs) => {
  // This code takes two number arrays: ticketCCs and disallowedUsers,
  // and outputs a number array cleanCCs which includes only those items from ticketCCs that are NOT in disallowedUsers.

  // Make sure to create the following inputs:
  // ticketCCs (Number array)
  // disallowedUsers (Number array)

  const cleanCCs = inputs.ticketCCs.filter(cc => !inputs.disallowedUsers.includes(cc))

  // Make sure to create the following outputs:
  // cleanCCs (Number array)

  return {
    cleanCCs,
  }
}
```

### Finding an order ID within text

This example extracts an order ID from a string of text, such as a ticket
comment. You can adjust the regular expression (`/GO-\d{8,9}/`)
as needed to match your specific order ID format.

```
// Regex for order number: "GO-" followed by 8 or 9 digits
const ORDER_NUMBER_REGEX = /GO-\d{8,9}/

// Searches comment for order number and returns it if found.
const findOrderNumber = comment => comment.match(ORDER_NUMBER_REGEX)[0]

module.exports = (inputs) => {
  // This code uses regex to look for an orderNumber with pattern "GO-" followed by 8 or 9 digits

  // Make sure to create the following inputs:
  // commentBody (Text)

  const orderNumber = findOrderNumber(inputs.commentBody)

  // Make sure to create the following outputs:
  // orderNumber (Text)
  // matchFound (True/False)

  return {
    orderNumber,
    matchFound: Boolean(orderNumber),
  }
}
```

### Generating a random number

This example generates a random number within the boundaries you specify. You can
change the value `52` to set your desired upper limit for the
random number.

```
module.exports = (inputs) => {
  // This code outputs a random integer number between 1 and 52 inclusive.

  // No inputs required.

  // Make sure to create the following outputs:
  // randomNumber (Number)

  const randomNumber = Math.floor(Math.random() * 52) + 1

  return {
    randomNumber
  }
}
```

### Generating three random numbers between one and seven

The following example returns three random numbers as individual
outputs:

```
module.exports = (inputs) => {
  // This code outputs three unique random integer numbers between 1 and 7 inclusive.

  // No inputs required.

  // Make sure to create the following outputs:
  // randomNumber1 (Number)
  // randomNumber2 (Number)
  // randomNumber3 (Number)

  const numbers = new Array()
  while (numbers.length < 3) {
    const candidate = Math.floor(Math.random() * 7) + 1
    if (!numbers.includes(candidate)) {
      numbers.push(candidate)
    }
  }

  return {
    randomNumber1: numbers[0],
    randomNumber2: numbers[1],
    randomNumber3: numbers[2]
  }
}
```

This example returns three random numbers in an array rather than
individually:

```
module.exports = (inputs) => {
  // This code outputs an array of three unique random numbers between 1 and 7 inclusive.

  // No inputs required.

  // Make sure to create the following outputs:
  // randomNumbers (Number array)

  const numbers = new Array()
  while (numbers.length < 3) {
    const candidate = Math.floor(Math.random() * 7) + 1
    if (!numbers.includes(candidate)) {
      numbers.push(candidate)
    }
  }

  return {
    randomNumbers: numbers
  }
}
```