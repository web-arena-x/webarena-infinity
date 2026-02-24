# Releases: Beta

Connect your CI/CD tool to Linear to know which issues ship in each release and to each environment.

![A scheduled release showing its issues in the main view, and a details sidebar](https://webassets.linear.app/images/ornj730p/production/c709f84b6e2fc4c9aaa99c7c0519cc88d424bda7-2880x1600.png?q=95&auto=format&dpr=2)

# Overview

By modeling each environment as a release pipeline and syncing builds from your CI/CD system, your issues are automatically grouped into releases whether you deploy continuously or on a scheduled release cycle.

This gives your organization a source of truth to know what issues are available in each environment, and helps you plan and track your releases directly in Linear. This functionality is available on Business and Enterprise plans.

## Release pipelines

A release pipeline is a container that holds releases for a specific product/environment combination. If your product supports a web app and Android app for instance, you might have a continuous release pipeline for your web app, and scheduled pipelines for Android Internal and Android Production. 

Each pipeline is defined as **continuous** or **scheduled**. In continuously deployed environments, pipelines use a specialized interface to better show the constant flow of changes as changes land. Releases in scheduled pipelines have properties like stage, start date, and release date, and also allow adding links and documents to support planning needs.

When defining a release pipeline, you can add repository path filters like `mobile-ios/**` to only include commits affecting the provided folders. This can be particularly helpful to avoid including unintended issues in your pipeline if you use a monorepo. 

<details>
<summary>What pipelines does Linear use internally?</summary>
We support iOS and Android apps with scheduled production releases as well as more frequent internal builds, as well as our main app which is continuously deployed.

We use a monorepo, and make use of path filters in the pipeline settings to define which commits should be included in each pipeline.

Here are the pipelines we’re using today:

Name | Type --- | --- Android (production) | Scheduled Android Internal | Continuous iOS (production) | Scheduled iOS Nightly | Continuous iOS Internal | Continuous Linear App | Continuous
</details>

## Releases

A release is a single unit within a pipeline. Each release is named, contains a reference to the commit SHA, and has a list of associated issues.

If we detect that semantic versioning is being used, we will automatically increment subsequent release names. We recommend explicitly providing both a release name and version from your CI when possible, since automatic naming is best-effort. 

### Viewing an issue’s release and pipeline

You can filter issues by their release, release stage type, or release pipeline. In display options in issue views, choose to display an issue’s release to see that information at the top level. Each issue in a release indicates the release’s name in its properties sidebar.

![ios, nightly, and internal releases on an issue's sidebar](https://webassets.linear.app/images/ornj730p/production/2e73115a4cd2cc1bb7a73cd65e087f54b5a3a96f-1746x422.png?q=95&auto=format&dpr=2)

# Configure

1. This feature is currently in beta. If you do not have see releases in [Settings](https://linear.app/settings/releases), or require further support in setup, please contact your account manager.
2. Open [Settings > Releases](https://linear.app/settings/releases) and create the pipelines you need for each product/environment combination you support. 
3. Reference the [README](https://github.com/linear/linear-release?tab=readme-ov-file) of our open-source tool for a link to the pre-built binary for your platform. We also include a sample GitHub Action for ease, though you can integrate with any CI/CD system that can execute command line tools.
