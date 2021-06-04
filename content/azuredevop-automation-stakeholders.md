Title: Manage your Azure DevOps User Access Levels through automation
Date: 2021-06-02
Category: Posts
Tags: AzDO, Automation
Slug: azuredevop-automation-stakeholders
Author: Willy-Peter Schaub
Summary: Quick overview how our Azure DevOps access level audits and management automation using PowerShell, REST APIs, and Richard's WIKI Updater task.

Three of my top irritations in software engineering are **complexity**, **inconsistency**, and **waste**. They lead to engineering rot, the infamous 2AM calls, and rapid evaporation of funds that could have beeen re-invested in innovation and learning.

![Agent 13](../images/azuredevop-automation-stakeholders-13.png)

As Agent #13, I made this declaration in [Navigating DevOps through Waterfalls](https://www.tactec.ca/ndtw-resources/):

> To remain competitive and respond to rapidly changing business and 
technology trends, as well as regulatory and compliance 
requirements, you must find ways to:
>
> - Ship value! – Increase the delivery of value to customers. 
> - Ship value faster! – Shorten the delivery cycle. 
> - Ship the right value faster! – Monitor, learn, adapt, and pivot. 
> - Ship the right and better value faster! – Improve quality! 
> - Ship the right and better value faster while reducing cost and efficiency! – Reduce cost and simplify through automation.”
>

---

# Context 
As part of our common engineering system we performed regular user audits to identify **inactive** users, assigned with **Basic** and the expensive **Basic + Test** access levels. You can find details on the Azure DevOps access levels [here](https://docs.microsoft.com/en-us/azure/devops/organizations/security/access-levels?view=azure-devops).

Why?

- Identify inactive users and downgrade them to free stakeholder access level
- Downgrade helps us **reduce unnecessary costs**
- Downgrade supports **security** by reducing access and limiting features

---

# The "ding" moment

After doing the painstaking and mind-numbing manual audit a few times, a faithful background thread triggered at the back of my head: "_you have followed the boring audit checklist more than twice - automate!_"

![Idea](../images/azuredevop-automation-stakeholders-3.png)

What followed was collaboration with the community, such as the former ALM/DevOps Rangers and our automation guru, aka Rodney. We agreed to the following automation requirements:

- Automate the manual audit using PowerShell Core
- Schedule the audit weekly using Azure Pipelines
- Identify users who have been inactive for X months and based on parameters:
  - Only report the inactive users
  - Downgrade the inactive users to stakeholder access level
- Inactive users are defined as:
  - Users who have logged on to Azure DevOps, but have not used any of its services for X months
  - Users who have been assigned an access level, but have never logged on to Azure DevOps for X months
- Write the weekly report to our knowledgebase wiki

# Automation solution

And voila, here is the PowerShell script that has been running weekly for more than a year.

```
[CmdletBinding()]
param(
  [string]   $orgName       = "experimentation-sandbox",
  [int]      $months        = "-2",
  [int]      $actionSet     = 0,
  [int]      $purgeUnknown  = 0,
  [string]   $patToken      = "<PAT>,
  [string]   $outputfile    = "Reset-Idle-Users-To-Stakeholders.md"
)

Write-Host ""
Write-Host ">>> QUERY MEMBER ENTITLEMENTS"
Write-Host ""

# Initialise outputfile
#$logFile = ("{0}-{1}" -f [DateTime]::Now.ToString("yyyyMMdd"), $outputfile)
$logFile  = $outputfile;
"|{0}|{1}|{2}|" -f "Organsation", "Months", "Actionset" | add-content -path $logFile
"|---|:-:|:-:|"                                         | add-content -path $logFile
"|{0}|{1}|{2}|" -f $orgName, $months, $actionSet        | add-content -path $logFile
"---"                                                   | add-content -path $logFile
"|{0}|{1}|{2}|{3}|{4}|" -f "Name", "Last Access", "License", "License Name", "Action" | add-content -path $logFile
"|---|---|---|---|---|"                                 | add-content -path $logFile

# Authentication header
$basicAuth = ("{0}:{1}" -f "",$patToken)
$basicAuth = [System.Text.Encoding]::UTF8.GetBytes($basicAuth)
$basicAuth = [System.Convert]::ToBase64String($basicAuth)
$headers   = @{Authorization=("Basic {0}" -f $basicAuth)}

# Requests
$request_GetEntitlements         = "https://vsaex.dev.azure.com/" + $orgName + "/_apis/userentitlements?top=10000&api-version=5.1-preview.2";
$request_UpdateEntitlementsPre   = "https://vsaex.dev.azure.com/" + $orgName + "/_apis/userentitlements/";
$request_UpdateEntitlementsPost  = "?api-version=5.1-preview.2";
$json                            = '[{"from": "","op": "replace","path": "/accessLevel","value": {"accountLicenseType": "stakeholder","licensingSource": "account"}}]';
  
# Data
$members              = New-Object System.Collections.ArrayList
[int] $count          = 0;
[string] $basic       = "Basic";
[string] $basicTest   = "Basic + Test Plans";
[string] $stakeholder = "Stakeholder"; 

# Get Entitlements
$response          = Invoke-RestMethod -Uri $request_GetEntitlements -headers $headers -Method Get
$response.items | ForEach-Object { $members.add($_.id) | out-null }

# List Members 
Write-Host ""
Write-Host ">>> LIST ENTITLEMENTS "
Write-Host ""

$response.items | ForEach-Object {
  $name    = [string]$_.user.displayName;
  $date    = [DateTime]$_.lastAccessedDate;
  $expired = Get-Date;
  $expired = $expired.AddMonths($months);
  $license = [string]$_.accessLevel.AccountLicenseType;
  $licenseName = [string]$_.accessLevel.LicenseDisplayName;
  $count++;

  # Forcefully remove never activated users
  if ( $purgeUnknown -eq 1 )
  {
    if ( $date.Year -eq 1 ) {
      $date    = [DateTime]$_.dateCreated;
    }
  }

  if ( $expired -gt $date ) {

    # Prepare request for the expired user
    $request = $request_UpdateEntitlementsPre + $_.id + $request_UpdateEntitlementsPost;

    # NEVER ACTIVATED
    if ( $date.Year -eq 1 )
    {
      if ( $licenseName -ne $stakeholder ) {
        Write-Host " ** IGNORE NEVER ACCESSED - ** " " Name: " $name " Date Created: " $_.dateCreated " Last Access: " $date "License: " $license " - " $licenseName
      }
    }
    # BASIC
    elseif ( $licenseName -eq $basic ) {
      if ( $actionSet -ne 0 ) {
        try {
            Write-Host " ** RESET TO STAKEHOLDER - ** " " Name: " $name " Last Access: " $date "License: " $license " - " $licenseName
            $response = Invoke-RestMethod -Uri $request -headers $headers -Method Patch -Body $json -ContentType 'application/json-patch+json'
            "|{0}|{1}|{2}|{3}|{4}|" -f $name, $date, $license, $licenseName, "Reset to Stakeholder" | add-content -path $logFile
        }
        catch {
          Write-Host Error updating entitlements
          Write-Host $_.Exception|format-list -force
        }
      }
      else {
        Write-Host " ** EXPIRED ** " " Name: " $name " Last Access: " $date "License: " $license " - " $licenseName
        "|{0}|{1}|{2}|{3}|{4}|" -f $name, $date, $license, $licenseName, "Expired" | add-content -path $logFile
      }
    }
    # BASIC + TEST
    elseif ( $licenseName -eq $basicTest ) {
      if ( $actionSet -ne 0 ) {
        try {
            Write-Host " ** RESET TO STAKEHOLDER - ** " " Name: " $name " Last Access: " $date "License: " $license " - " $licenseName
            $response = Invoke-RestMethod -Uri $request -headers $headers -Method Patch -Body $json -ContentType 'application/json-patch+json'
            "|{0}|{1}|{2}|{3}|{4}|" -f $name, $date, $license, $licenseName, "Reset to Stakeholder" | add-content -path $logFile
        }
        catch {
          Write-Host Error updating entitlements
          Write-Host $_.Exception|format-list -force
        }
      }
      else {
        Write-Host " ** EXPIRED ** " " Name: " $name " Last Access: " $date "License: " $license " - " $licenseName
        "|{0}|{1}|{2}|{3}|{4}|" -f $name, $date, $license, $licenseName, "Expired" | add-content -path $logFile
      }
    }
  }
}
```

> REFERENCE INFORMATION
>
> - [Azure DevOps Services REST API Reference](https://docs.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-6.1)
> - [WIKI Updater Tasks](https://marketplace.visualstudio.com/items?itemName=richardfennellBM.BM-VSTS-WIKIUpdater-Tasks)
>

---

# Azure DevOps Pipeline

And here is the Azure Pipeline definition, whereby I replace our organization and project with <ORG> and <PROJECT> placeholders:

```
schedules:
- cron: 30 15 * * 0
  branches:
    include:
    - refs/heads/master
  always: true
name: $(Date:yyyyMMdd)$(Rev:.r)

jobs:
- job: Weekly_Audit
  displayName: Agent Weekly Audit
  pool:
    name: <AGENT>
  steps:
  - checkout: self
    clean: False
    persistCredentials: True

  - task: AzureKeyVault@1
    displayName: 'Azure Key Vault: <RROJECT>-KV'
    inputs:
      ConnectedServiceName: <GUID>
      KeyVaultName: <PROJECT>-KV

  - task: PowerShell@2
    displayName: PowerShell
    inputs:
      filePath: Member Entitlement Management/Reset-Idle-Users-To-Stakeholders.ps1
      arguments: -patToken $(PAT-MemberEntitlementManagement) -orgName "<ORG>" -months -3 -actionSet 1 -outputFile $(Build.ArtifactStagingDirectory)/Reset-Idle-Users-To-Stakeholders.md
      failOnStderr: true
      pwsh: true

  - task: WikiUpdaterTask@1
    displayName: Git based WIKI
    inputs:
      repo: <ORG>.visualstudio.com/<PROJECT>/_git/Common-Engineering-System.wiki
      filename: <PROJECT>/Knowledgebase/Logs/InactiveUsers/wcbbc/$(Build.BuildNumber)_Reset_Idle_User_Licenses.md
      dataIsFile: true
      sourceFile: $(Build.ArtifactStagingDirectory)/Reset-Idle-Users-To-Stakeholders.md
      message: Automated Idle Users Report Job
      gitname: $(Build.QueuedBy)
      gitemail: $(Build.QueuedBy)
      useAgentToken: true
```

# Positive ending

The audit is now performed weekly (not ad-hoc), in minutes (not hours), and consistently (not flawed by boredom or context switching). In fact, I completely forgot about the automation until my colleague, Dennis, asked me whether we can run the same automation in another organization. Response was an easy one, "_yes we can and already have been for the past X months. Checkout the weekly reports in our knowledgebase wiki._"

![Robots](../images/azuredevop-automation-stakeholders-1.png)

Hope you will join us on our quest to **automate everything automatable** to move the repetitive, mind-numbing, and therefore error-prone tasks that our digital colleagues can perform consistently and efficiently. 

![Humanoids](../images/azuredevop-automation-stakeholders-2.png)

Do not see it as the world of robotics taking over humanity, but as robotic colleagues enabling us to focus on other responsibilities, such as ensuring we continuously ship value to our **delighted customers**.

