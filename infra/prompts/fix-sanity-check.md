The {variant} sanity check for `apps/{app-name}` failed with the following output:

```
{output}
```

Fix the issues so the sanity check passes. The sanity check script is at `apps/{app-name}/sanity_check_{variant}.py` (or `apps/{app-name}/sanity_check.py` if the variant-specific one does not exist). Read the sanity check script to understand what it verifies, then fix the app code and/or the verifier tasks to make it pass.