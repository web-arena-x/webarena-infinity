# How to Access Smart Tools Feedback (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731498847770-How-to-Access-Smart-Tools-Feedback-Engage-Legacy

---

When your Agents leave feedback on Smart Tools, you can access that feedback within your S3 environment.

Local Measure cannot access the specifics of the feedback unless you intentionally share it.

Local Measure can see product analytics such as when an Agent gives a 'thumb up' or 'thumb down' in response to a Smart Tool. Local Measure cannot access specific details about the Smart Tool nor the associated Contact (such as the transcript or any PII).

Engage AI feedback data is stored as traces. A trace is a collection of spans, where each span represents a unit of work or operation.

When an Agent uses a Smart Tool, a trace is created to record the operations and their contexts as spans within the trace. When an Agent submits feedback, feedback spans are added to the relevant trace.

To access Smart Tools feedback, follow the steps below:

1. Log into your AWS Console
2. Navigate to S3
3. Within your **General purpose buckets**, search for "engageai"
4. Open the bucket
5. Open the **feedbacks/** folder
6. A list of trace folders will appear

#### Feedback Structure

The feedback data is stored in Amazon S3 using the following structure:

- <trace\_id>.trace.d 
  - <start\_ts>\_<span\_id>\_<end\_ts>.span  - …

Each file is a JSON file. Typically, the feedback span will be the last span in a trace when sorted by name.

#### Key Fields

When analysing the data, the most interesting fields are `attributes` and `events`.

#### Ad-Hoc Analysis

For ad-hoc analysis, it is recommended to use `jq` commands in combination with common command line text processing utilities. For more advanced ad-hoc analysis, simple scripting in any programming language should be sufficient.

For example, the following command filters all the spans for the feedback submission call:

`cat */*.span | jq 'select(.name | contains("collect_feedback"))'`

#### Visualised Analysis

For visualised analysis, most data analysis tools are suitable. As an example, The Elastic Stack (ELK) is a good option for both continuous and ad-hoc analysis.