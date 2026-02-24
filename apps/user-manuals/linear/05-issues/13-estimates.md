# Estimates

Show how much effort each issue will take.

![Linear app showing an issue estimate being changed](https://webassets.linear.app/images/ornj730p/production/e1af0f17db6f9c374fb850cfbc0a59e4025f7f47-1114x668.png?q=95&auto=format&dpr=2)

## Overview

Use estimates to describe the complexity or size of an issue. Cycles and projects use estimates to calculate effort and related statistics. You'll opt into estimates on a team level as well as choose which estimate scale to use.

## Configure

Go to _Team Settings > General > Estimates_ to enable the feature. Teams can use different estimate scales and configurations, even if they're working together on the same project.

![estimate settings](https://webassets.linear.app/images/ornj730p/production/15930ec67ceb31085b1f70ccbaa735818560fcea-1400x962.png?q=95&auto=format&dpr=2)

### Scale range options

Scale | | | | | --- | --- | --- | --- | --- | --- Exponential | 1 | 2 | 4 | 8 | 16 Fibonacci | 1 | 2 | 3 | 5 | 8 Linear | 1 | 2 | 3 | 4 | 5 T-Shirt | XS | S | M | L | XL

> [!NOTE]
> When T-Shirt sizes require translation to numerical values (for display in graphs, for instance,) they follow the Fibonacci scale.

### Extended estimate scales

Enable the extended scale to add two additional values to your scale. 

Extended Scale |   | --- | --- | --- Exponential | 32 | 64 Fibonacci | 13 | 21 Linear | 6 | 7 T-shirt | XXL | XXXL

### Zero estimates

Allow zero estimates by toggling this option on in estimate settings. By default, we count unestimated issues as one point but you can disable this in estimate settings as well.

## Add, edit, or remove estimates

Add estimates when creating or updating issues with the keyboard shortcut `Shift` `E`. The same keyboard shortcut can be used to edit or remove the estimate.

## Filter for estimates

Find issues with specific point values by filtering for estimates. The shortcut `F` will open the filter menu and you can select estimates from there. This is especially helpful when creating custom views and searching through the backlog. 

## Analytics

When you see the word effort, that refers to estimate. When estimates are not enabled, we calculate statistics using a default value of 1 estimate point per issue. T-shirt estimates map to the Fibonacci scale.

If you've enabled estimates, we'll use the estimate values to calculate percentage completion and effort in cycle and project graphs. The top bars on most views will show the total issues count or total estimate value next to the view's name. Hover over the number to see both values.

> [!NOTE]
> **When estimates are too large, refine issue scope**   
> Larger estimates usually mean that there is uncertainty about the issue's complexity. We find that breaking up issues into smaller ones is the best approach.
