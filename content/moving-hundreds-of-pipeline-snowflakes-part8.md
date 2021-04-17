Title: Part 8: Pipelines - From CI to CD and beyond in one pipeline
Date: 2021-04-13
Category: Posts
Tags: Azure Pipelines, DevOps, Pipeline as Code
Slug: yaml-pipelines-part8
Author: Willy-Peter Schaub
Summary: Continuous Deployment seems important. It deploys new features, bug and hot fixes, which we can release to our delighted customers on demand.

Welcome back to another installment of pipeline wizardry. In [part 7](/yaml-pipelines-part7.html) we wrapped up our application-type continuous integration (CI) pipeline. OK, we have nailed the build, but what about continuous deployment (CD)?

---

# Why do we care about continuous deployment?

In previous posts we covered the world of Continuous Integration (CI), which builds and validates your latest code in your source control repository. With Continuous Delivery (CD) we deploy the artifact from the CI build to one or more environments. 

In the MSDN article, [Applying DevOps to a Software Development Project](https://docs.microsoft.com/en-us/archive/msdn-magazine/2016/august/devops-applying-devops-to-a-software-development-project), I emphasised the subtle difference between Continuous Delivery (CD) and Continuous Deployment (CD): "_The latter is to a single environment. A small team might only implement Continuous Deployment because each change goes directly to production. Continuous Delivery is moving code through several environments, ultimately ending up in production, which may include automated user interface (UI), load and performance tests and approvals along the way._" 

Note that both have the dreaded TLA (two|three lettered acronym) CD? ... confusing, right? Oh, how I loathe IT (information technology) acronyms q;-(

Back to Continuous Deployment, which seems important. It **deploys** new features, bug and hot fixes, which we can **release** to our delighted customers on demand.

> **NOTE** - The use of "continuous" implies that both the continuous integration and continuous deployment engineering processes embrace the "automate everything automatable" motto!

After being flabbergasted with the innovation, [simplicity and enablement, courtesy of the app-type blueprint-based YAML pipelines](/yaml-pipelines-part7.html), I expected a world of frustration and pain to embrace the blueprints within the context of Continuous Deployment.

Here is the final chapter in our blueprint-based pipeline adventure.

---

# Tweaks to the Application-type CI Blueprints

We continue from where we left off with the app-type CI Blueprint Architecture, comprised of the following key elements:

- [ ] **Starter** template, which configures the continuous integration pipeline. 
- [ ] **App-type** CI template, which **extends** the starter template and abstracts the continuous integration (CI) process.
- [ ] **Example** of the app-type blueprint, for reference.

> App-Type CI Blueprint Architecture
>
> ![CI Blueprint Architecture](/images/moving-hundreds-of-pipeline-snowflakes-part7-2.png)

We add two templates to the CI Blueprint Architecture to create our CICD Blueprint Architecture. 

- [ ] **App-type** CD template, which abstracts and **includes** continuous deployment (CD) process.
- [ ] **Variable** template, which contains all configuration for the various [deployment jobs](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/deployment-jobs) and [environments](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/environments) as key:value pairs.

> App-Type CICD Blueprint Architecture
>
> ![CICD Blueprint Architecture](/images/moving-hundreds-of-pipeline-snowflakes-part8-1.png)

It took us minutes to create a fully functional CICD pipeline using the App-Type CI Blueprint. In fact it is was so painless and quick, that I repeated the exercise to verify the process.

I hope, that you have appreciate the simplicity, power, and prospects that the YAML templates and our app-type blueprints are bringing to the party.

## **Starter** template tweaks

When you include variable groups or variable templates, you need to switch your variable definitions to the sequence syntax. To add the variable template, we changed our **Starter** template from the simple notation ...

> SAMPLE: Variables using simple notation

```yml
variables:
  portfolioName: 'TODO REPLACE WITH PORTFOLIO NAME' 
  productName:   'TODO REPLACE WITH PRODUCT NAME' 
```

... to the key:value notation. The variable template name is assembled from the portfolio and program name, and pulled from the same repository as the other templates.

> SAMPLE: Variables using key:value pair notation and variable template extract

```yml
variables:
- name:  portfolioName
  value: 'TODO 
- name:  'TODO REPLACE WITH PORTFOLIO NAME'
  value: 'TODO REPLACE WITH PROGRAM NAME'
- template: CD/Config/${{variables.portfolioName}}.${{variables.productName}}.config.yml@CeSTemplates
```

## **CI** template tweaks

Changes to the CI template were just as humdrum. An optional parameter allows us to override the app-type CD template, with a custom template on exceptional cases. 

> SAMPLE: CI template extract

```yml
parameters:
...
- name:     customCDTemplate
  type:     string
  default:  'blueprint' 

...

# DEPLOYMENT

- ${{ if ne( parameters.customCDTemplate, 'blueprint' ) }}:
  - template: CD/Custom/${{parameters.customCDTemplate}}.yml@CeSTemplates
- ${{ if eq( parameters.customCDTemplate, 'blueprint' ) }}:
  - template: CD/Blueprints/<appType>CDTemplate.yml@CeSTemplates

# END OF PIPELINE
```

We are experimenting and fine tuning our variable and CD templates and therefore it would be overzealous to include them in entirety. 

As mentioned the variable template is a list of key:value pairs to define configuration for the associated deployment jobs and environments.

> SAMPLE: Variable template extract

```yml
variables:
...
# DEVelopment Stage
- name:  developmentStageEnvName
  value: 'POC_DEV'
- name:  developmentStageVmImage
  value: 'ubuntu-latest'
```

For the CD Blueprint, you should explore [deployment jobs](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/deployment-jobs) and associated strategies. To start, we opted to experiment with the [runOnce](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/deployment-jobs?view=azure-devops#runonce-deployment-strategy) strategy.

> SAMPLE: CD template extract

```yml
stages:

# DEVELOPMENT STAGE

- stage:         'Development'
  dependsOn:
  - ContinuousIntegration
  pool:
    vmImage:     $(developmentStageVmImage)
  jobs:
  - deployment:  'Development'
    environment: $(developmentStageEnvName)
    strategy:
      runOnce:
        preDeploy:
          steps:
          - script: echo Welcome to PREDEPLOY - Development stage running on $(developmentStageVmImage) pool in the $(developmentStageEnvName) environment
        deploy:
          steps:
          - script: echo Welcome to DEPLOY - Development stage running on $(developmentStageVmImage) pool in the $(developmentStageEnvName) environment
        routeTraffic:
          steps:
          - script: echo Welcome to ROUTETAFFIC -  Development stage running on $(developmentStageVmImage) pool in the $(developmentStageEnvName) environment        
        postRouteTraffic:
          steps:
          - script: echo Welcome to POSTROUTETRAFFIC - Development stage running on $(developmentStageVmImage) pool in the $(developmentStageEnvName) environment
        on:
          failure:
            steps:
            - script: echo Welcome to FAILURE -  Development stage running on $(developmentStageVmImage) pool in the $(developmentStageEnvName) environment          
          success:
            steps:
            - script: echo Welcome to SUCCESS -  Development stage running on $(developmentStageVmImage) pool in the $(developmentStageEnvName) environment   
```

OK, the template revisions to include continuous deployment are straightforward. Apart from many upcoming refinements, we now have a functional application-type CICD blueprint-based pipeline.

But, how do they map out at queue time and are our security engineers contempt with the new pipelines?

---

# Making sure our Security Engineers are happy

TBD

> Build Artifact triggered by non-release branch
>
> ![CICD Blueprint Architecture](/images/moving-hundreds-of-pipeline-snowflakes-part8-2.png)

TBD

> Build Artifact triggered by release branch
>
> ![CICD Blueprint Architecture](/images/moving-hundreds-of-pipeline-snowflakes-part8-3.png)

TBD

```yml
# STAGING STAGE
- ${{ if or( eq(variables['Build.SourceBranch'], 'refs/heads/hotfix'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release')) }}:
  - stage:         'Staging'
    dependsOn:
    - SecurityScans
    - SecurityReview
  ...
```

TBD

---

# Mulling over environments and/or service connection approvals

TBD

---

# Are our engineers losing control over their pipeline?

TBD

---

# What is next?

TBD

---

> Series Bread Crumbs | [Part 1, TOC](/why-pipelines-part1.html) | [Part 2](/yaml-pipelines-part2.html) | [Part 3](/yaml-pipelines-part3.html) | [Part 4](/yaml-pipelines-part4.html) | [Part 5](/yaml-pipelines-part5.html) | [Part 6](/yaml-pipelines-part6.html) | [Part 7](/yaml-pipelines-part7.html) | Part 8 |  

