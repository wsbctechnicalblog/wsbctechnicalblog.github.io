Title: Self-service automation - A dream turns into reality
Date: 2021-07-05
Category: Posts
Tags: automation, azure-devops, pipelines, x-as-code
Slug: yaml-pipelines-part9
Author: Willy-Peter Schaub
Summary: Automate a “hello world in less than 1min”, also referred to as our “walking skeleton”.
Welcome back to another installment of pipeline wizardry. We are changing gears from the nuts and bolts, to the automation we can achieve using the blueprint-based pipelines. Fasten your seat belts!

---

# The dream

Our automation working group had a vision to build an engineering process that could generate a “Hello world in less than 1min”, aka walking skeleton, to decimate engineering process lead lines and enable our engineering teams.

> Option 1 - Manual and humanoid driven engineering process
>
> ![Manual](/images/moving-hundreds-of-pipeline-snowflakes-part9-1.png)

Our engineering process is not unique. It starts with an idea. Engineering creates a new repository for the code artifacts, and a continuous integration and deployment pipeline. As engineers require elevated permissions to generate the repo and pipeline artifacts, other engineers and departments get engaged as part of the process to ensure consistency, security, and alignment with guardrails (governance). 

As frustrating as it may sound, it can take **hours to days**, until the engineering team can finally start adding and building their code.

> Option 2 - Automated and humanoid enabled engineering process
>
> ![Manual](/images/moving-hundreds-of-pipeline-snowflakes-part9-2.png)

Our envisaged engineering process is radically different. Engineering visits a self-service portal, captures data to describe what they need, and the **click a button**. The engineering process should be created through automation, the repo should contain an application-type sample, and by the time the engineering team blinks, the pipelines should be running to validate the setup using the sample code. 

Machines (automation) can do repetitive tasks much better and faster than we can, they stick to the instructions to ensure that we do not have to validate consistency and guardrail alignment.

Our dream, as mentioned, is to enable the engineering team within 1 minute. 

---

# Community View

> Option 2 - Automated and humanoid enabled engineering process
>
> ![Manual](/images/moving-hundreds-of-pipeline-snowflakes-part9-3.png)

We polled the twitter and LinkedIn community and realized that we are not alone. An average of **33**% of users tolerate hours and **36**% of users days to get a basic project environment assembled. 

**That is unacceptable!**

> ![Manual](/images/moving-hundreds-of-pipeline-snowflakes-part9-6.png)

---

# Our drop-the-mic demo

We demonstrated the following engineering process using a recipe of Git, Azure DevOps REST API, and a PowerShell automation script, developed and mob-reviewed by our automation working group:

- Query Azure DevOps Project information
- Create an Azure Repo (Git)
- Clone our AzureDevOps.Automation.Pipeline.Templates and the app-type specific AzureDevOps.Automation.Pipeline.Sample.* repository
- Clone the newly created repository
- Add the app-type *-start.yml template to the new repo
- Add the app-type sample code to the new repo
- Push local changes to the Azure Repo
- Create a new pipeline, linked to the *-start.yml template in the new repo
- Run the new pipeline

When we shared a recording of the demo with engineering, there were a few gob-smacked faces when the penny dropped that our "less 1min dream" could evolve into a "less than 20 seconds engineering process".

> Hello world automation demo
>
> ![Demo](/images/moving-hundreds-of-pipeline-snowflakes-part9-4.png)

Here is our automation script we used for the demo.

```
<# 
  CATEGORY: azure-devops-pipelines
  LAUNCHED: Demo
 #>

[CmdletBinding()]
param (
 [Parameter (Mandatory= $true)]
 [string]    $orgName,
 [Parameter (Mandatory= $true)]
 [string]    $projectName,
 [Parameter (Mandatory= $true)]
 [string]    $portfolioName,
 [Parameter (Mandatory= $true)]
 [string]    $productName,
 [Parameter (Mandatory= $true)]
 [string]    $blueprintName,
 [Parameter (Mandatory= $true)]
 [string]    $patToken
)

# GET START DATE & TIME
$startTime = Get-Date

# Security Header
$basicAuth = ("{0}:{1}" -f "",$patToken)
$basicAuth = [System.Text.Encoding]::UTF8.GetBytes($basicAuth)
$basicAuth = [System.Convert]::ToBase64String($basicAuth)
$headerPAT = @{Authorization=("Basic {0}" -f $basicAuth)}

# Variables
[string]  $nameTemplates       = 'AzureDevOps.Automation.Pipeline.Templates'
[string]  $repoTemplates       = 'https://<SOURCE-ORG>@dev.azure.com/<SOURCE-ORG>/<SOURCE-PROJECT>/_git/' + $nameTemplates
[string]  $nameSamples         = 'AzureDevOps.Automation.Pipeline.Sample.' + $blueprintName
[string]  $repoSamples         = 'https://<SOURCE-ORG>@dev.azure.com/<SOURCE-ORG>/<SOURCE-PROJECT>/_git/' + $nameSamples
[string]  $nameRepo            = $portfolioName + '.' + $productName
[string]  $repoNew             = 'https://' + $orgName + '@dev.azure.com/' + $orgName + '/' + $projectName + '/_git/' + $nameRepo
[string]  $projID              = 'invalid'
[string]  $repoID              = 'invalid'
[string]  $pipeID              = 'invalid'
[string]  $pathWorking         = Get-Location
[string]  $pathTemplates       = $pathWorking        + '\' + $nameTemplates
[string]  $pathSamples         = $pathWorking        + '\' + $nameSamples 
[string]  $pathRepo            = $pathWorking        + '\' + $nameRepo 
[string]  $folderSourceSample  = $pathSamples        + '\src'
[string]  $pathSourceSample    = $folderSourceSample + '\*'
[string]  $folderTargetSample  = $pathRepo           + '\src'
[string]  $folderPipeline      = $pathRepo           + '\pipelines'
[string]  $namePipeline        = $portfolioName      + '-' + $productName + '-start'
[string]  $namePipelineFile    = 'azure-pipeline-'   + $namePipeline + '.yml'
[string]  $startPipeSource     = $pathTemplates      + '\Blueprints\' + $blueprintName + '\azure-pipeline-' + $blueprintName + '-start.yml'
[string]  $startPipeTarget     = $pathRepo           + '\pipelines\' + $namePipelineFile
[string]  $nameConfigFile      = $portfolioName      + '-' + $productName + '-config.yml'
[string]  $startConfigSource   = $pathTemplates      + '\Blueprints\' + $blueprintName + '\azure-pipeline-' + $blueprintName + '-config.yml'
[string]  $startConfigTarget   = $pathTemplates      + '\Operations\Config\' + $nameConfigFile
[string]  $tokenPortfolio      = '__TODO_PORTFOLIO__'
[string]  $tokenProduct        = '__TODO_PRODUCT__'
[Boolean] $debugMode           = $true

try {
  ##################################################################################################################
  # 1.1 Get project ID
  Write-Host ''
  Write-Host '1.1 - Get ID for project: ' $projectName
  $uriGetProject = 'https://dev.azure.com/' + $orgName + '/_apis/projects/' +$projectName + '?api-version=6.0'
  try {
    $projResult  = Invoke-RestMethod -Uri $uriGetProject -ContentType "application/json" -Headers $headerPAT
    $projID      = $projResult.id
    if ( $true -eq $debugMode ) {
      Write-Host 'ID: ' $projID
    }
  }
  catch {
    Write-Host 'STEP 1.1 <GET PROJECT ID> FAILURE: ' $_
    # eject
    throw $_.Exception
  }

  ##################################################################################################################
  # 1.2 Create repo Y.Z in AzDO project X and create local clone.
  Write-Host ''
  Write-Host '1.2 - Create New Repository: ' $repoNew
  $uriCreateRepo  = 'https://dev.azure.com/' + $orgName + '/_apis/git/repositories?api-version=6.1-preview.1'
  $jsonCreateRepo = 
  '{
    "name": "' + $nameRepo +'",
    "project": {
    "id": "' + $projID + '"
    }
  }'
  try {
    $repoResult = Invoke-RestMethod -Uri $uriCreateRepo -Body $jsonCreateRepo -Method Post -ContentType "application/json" -Headers $headerPAT
    if ( $true -eq $debugMode ) {
      Write-Host 'Create Repo Result: ' $repoResult
    }
  }
  catch {
    Write-Host 'STEP 1.2 <CREATE REPO> FAILURE: ' $_
    # eject
    throw $_.Exception  
  }

  ##################################################################################################################
  # 2. Clone repositories 
  Write-Host ''
  Write-Host '2.1 Clone repo ' $repoTemplates ' to local path'
  git clone $repoTemplates
  Set-Location -Path $pathTemplates
  git pull
  Set-Location -Path $pathWorking

  Write-Host ''
  Write-Host '2.2 Clone repo ' $repoSamples ' to local path'
  git clone $repoSamples
  Set-Location -Path $pathSamples
  git pull
  Set-Location -Path $pathWorking
  
  Write-Host ''
  Write-Host '2.3 Clone repo ' $repoNew ' to local path'
  git clone $repoNew
  Set-Location -Path $pathRepo
  git pull
  Set-Location -Path $pathWorking

  ##################################################################################################################
  # 3. Add *-start.yml from templates repo
  Write-Host ''
  Write-Host '3.1 Add app-type start template to new repo'
  New-Item -Path $folderPipeline -ItemType Directory
  Copy-Item $startPipeSource $startPipeTarget
  Write-Host ''
  Write-Host '3.2 Add config template to templates repo'
  New-Item -Path $pathTemplates -ItemType Directory -Force
  Copy-Item $startConfigSource $startConfigTarget

  ##################################################################################################################
  # 4. Add src\* from AzureDevOps.Automation.Pipeline.Sample.azure-function repo to local repo.
  Write-Host ''
  Write-Host '4.1 Add src folder and sample solution'
  New-Item -Path $folderTargetSample -ItemType Directory
  Copy-Item $pathSourceSample $folderTargetSample -recurse
  Write-Host '4.2 Replace tokens with variables'
  $rawFile = Get-Content -path $startPipeTarget -raw
  $step1File = $rawFile.Replace($tokenPortfolio, $portfolioName)
  $step2File = $step1File.Replace($tokenProduct, $productName)
  Set-Content $startPipeTarget $step2File

  ##################################################################################################################
  # 5. Push local changes to X.Y repo.
  Write-Host ''
  Write-Host '5.1 Push all new changes to new repo'
  Set-Location -Path $pathRepo
  git add --all
  git commit -m 'Automation: Sample source & app-type blueprint pipeline.' 
  git push
  Set-Location -Path $pathWorking
  Write-Host ''
  Write-Host '5.2 Push all new changes to new repo'
  Set-Location -Path $pathTemplates
  git add --all
  git commit -m 'Automation: Add new product configuration.' 
  git push
  Set-Location -Path $pathWorking

  ##################################################################################################################
  # 6. Create new pipeline based on the *-start.yml file we committed
  Write-Host ''
  Write-Host '6.1 Query repo ID'
  $uriGetRepo = 'https://dev.azure.com/'+ $orgName + '/' + $projectName + '/_apis/git/repositories/' + $nameRepo + '?api-version=6.0'
  try {
    $repoResult = Invoke-RestMethod -Uri $uriGetRepo -ContentType "application/json" -Headers $headerPAT
    $repoID     = $repoResult.id
    if ( $true -eq $debugMode ) {
      Write-Host 'ID: ' $repoID
    }
  }
  catch {
    Write-Host 'STEP 6.1 <GET REPO ID> FAILURE: ' $_
    # eject
    throw $_.Exception
  }

  Write-Host ''
  Write-Host '6.2 Create new pipeline'
  $uriCreatePipe = 'https://dev.azure.com/'+ $orgName + '/' + $projectName + '/_apis/pipelines?api-version=6.0-preview.1'
  $jsonCreatePipe = 
'{
  "folder" : "' + $portfolioName + '",
  "name": "' + $namePipeline + '",
  "configuration": {
      "type" : "yaml",
      "path" : "/pipelines/' + $namePipelineFile + '",
      "repository" : {
        "id" : "' + $repoID + '",
        "name" : "' + $nameRepo + '",
        "type" : "azureReposGit"
      }
    }
}'  
  try {
    $pipeResult  = Invoke-RestMethod -Uri $uriCreatePipe -Body $jsonCreatePipe -Method Post -ContentType "application/json" -Headers $headerPAT
    $pipeID = $pipeResult.id
    if ( $true -eq $debugMode ) {
      Write-Host 'ID: ' $pipeID
    }
  }
  catch {
    Write-Host 'STEP 6.2 <LINK PIPELINE> FAILURE: ' $_
    # eject
    throw $_.Exception
  }

  ##################################################################################################################
  # 7. Run new pipeline.
  # https://docs.microsoft.com/en-us/rest/api/azure/devops/pipelines/runs/run%20pipeline?view=azure-devops-rest-6.1
  Write-Host ''
  Write-Host '7.1 Run pipeline'
  $uriRunPipe = 'https://dev.azure.com/'+ $orgName + '/' + $projectName + '/_apis/pipelines/' + $pipeID + '/runs?api-version=6.0-preview.1'
  $jsonRunPipe =
'{ "variables": {      
      "customVariable": {
      }
    },
    "process": {
      "yamlFilename": "' + $namePipelineFile + '",
      "type":  2
     },
    "repository": {
      "id": "' + $repoID + '",
      "type": "TfsGit",
      "name": "' + $nameRepo + '",
      "defaultBranch": "refs/heads/master",
      "clean":  null,
      "checkoutSubmodules":  false
    },
    "name": "' + $namePipeline + '",
    "path": "' + $portfolioName + '",
    "type": "build",
    "queueStatus": "enabled",
    "project":  {
      "id": "' + $projID + '",
      "name": "' + $projectName + '"
    }
}'

  try {
    $pipeResult  = Invoke-RestMethod -Uri $uriRunPipe -Body $jsonRunPipe -Method Post -ContentType "application/json" -Headers $headerPAT
    $pipeID = $pipeResult.id
    if ( $true -eq $debugMode ) {
      Write-Host 'ID: ' $pipeID
    }
  }
  catch {
    Write-Host 'STEP 6.2 <LINK PIPELINE> FAILURE: ' $_
    # eject
    throw $_.Exception
  }
}
catch {
  Write-Host 'OH, OH - FATAL ERROR! ' $_.Exception.Message
  Write-Host $_
}

# GET END DATE & TIME
$endTime = Get-Date
$micTime = New-Timespan -seconds $(($endTime - $startTime).TotalSeconds)
Write-Host ''
Write-Host 'From zero to hello world in >>' $micTime.TotalSeconds '<< seconds q;)'
```

> COPY-PASTE and REUSE at your own risk. This was a demo script and will be going through extensive mob-reviews and mob-programming to turn it into a production-ready automation.

---

# Gob-smacked?

> gob-smacked (excited) yet?
>
> ![Gobsmacked](/images/moving-hundreds-of-pipeline-snowflakes-part9-5.png)

---

# What is next?

We need to expand our library of application-type blueprints and in parallel expand the automation script to support the new app-types. In parallel we need to move the automation script to be run by Azure Pipelines to support queueing, and add a user-friendly service portal to "click the button."

Watch this space for more exiting progress.

---

> Series Bread Crumbs | [Part 1, TOC](/why-pipelines-part1.html) | [Part 2](/yaml-pipelines-part2.html) | [Part 3](/yaml-pipelines-part3.html) | [Part 4](/yaml-pipelines-part4.html) | [Part 5](/yaml-pipelines-part5.html) | [Part 6](/yaml-pipelines-part6.html) | [Part 7](/yaml-pipelines-part7.html) | [Part 8](/yaml-pipelines-part8.html) | Part 9 |

