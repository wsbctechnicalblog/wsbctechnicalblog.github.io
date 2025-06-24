Title: Fixing empty Closed Date fields in work items (Part 2)
Date: 2025-06-25
Category: Posts 
Tags: azure-devops
Slug: azure-devops-empty-closed-date-field-fix
Author: Willy-Peter Schaub
Summary: Now that we know what the issue is, how do we resolve it?

As outlined in [Why is the Closed Date field empty in my work items?](/azure-devops-empty-closed-date-field.html), you may have encountered closed work items missing a `Closed Date`. Microsoft acknowledged this long-standing Azure DevOps bug, where custom work item types were not configured to populate the Closed Date field by default, but has never issued a fix.

Fortunately, our own Azure DevOps and PowerShell expert, Daniel Broderick, developed a script that allowed us to efficiently correct hundreds of affected work items. This proactive solution saved us from hours of tedious manual remediation and ensured data integrity across our boards.

We share it here for you to review and potentially help you `automate the mundane` and cleanup your work items.

---

>
> Script update-workitem-closing-date.ps1
> Developed by Daniel Broderick
>

```
<#
    .DESCRIPTION
        Update the workitem closing date for the microsoft but where its closed but does not show.
        Finds work items with no closed date but are closed of type Technical Debt.

#>

#region params
[CmdletBinding()]
param (
  [Parameter(Mandatory = $false)]
  [String]
  $Organisation = "<YOUR-ORG>",
  [Parameter(Mandatory = $false)]
  [String]
  $PAT = $env:pat
)
#endregion params


#region import variables
$FileName = 'bootstrap.ps1'
$FoundFlag = $false
$Path = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition

do {
  try {
    if (Test-Path -path "$Path\$FileName") {
      $FoundFlag = $true
      Write-Debug "Bootstrapping"
      Write-Output "Bootstrap found importing modules"
      . "$Path\$FileName"
    }
    else {
      $Path = Split-Path -Parent -Path $Path
      Write-Debug "Path $Path\$FileName Not found"
    }
  }
  catch {
    $_ 
    Write-Debug "Bootstrap Not found exiting"
    Write-Output "$FileName Not found bootstrap cannot load modules - exiting"
    exit # variables not found	
  }
	
}
Until ($FoundFlag -eq $true)
#endregion import variables

$ProjectName = 'zDEPRECATE - Cloud-WLT'
Set-DevOpsScriptVariables -DevOpsOrganisation $Organisation -DevOpsProject "$ProjectName" -PAT $PAT

$TicketsUpdatedArray = @()
$UpdatedArray = @()
$FailedArray = @()
$TimeStamp = Get-Date -Format "yyyy-MM-dd HHmm"
#region work item dates


#region query
$JSONQuery = '{"query": "select * from 
                                WorkItems
                                where 
                                [System.TeamProject] = ''zDEPRECATE - Cloud-WLT''
                                and [Microsoft.VSTS.Common.ClosedDate] = ''''
                                and [System.WorkItemType] = ''Technical Debt'' 
                                and [System.State] = ''Closed''
                                ORDER BY [id]
                                "
                    }'

$QueryID = '484dc53f-813b-43ca-a567-8474dc8aa470' # get results by Saved Query ID
#endregion query

#region get workitems from query
#$Result = Get-DevOpsWorkItemByWIQLQuery -JSONQuery $JSONQuery -Organisation $Organisation -ProjectName $ProjectName

$Result = Get-DevOpsWorkItemByWIQLQuery -QueryID $QueryID -Organisation $Organisation -ProjectName $ProjectName

#endregion get workitems from query

#region iterate and update
Write-Host " Found $(($Result.workItems).count) tickets with no closed date and are in a closed state"
foreach ($Ticket In $Result.workItems.id) {
  $TicketObject = Get-DevOpsWorkItemByID -Organisation $Organisation -ProjectName $ProjectName -WorkItemID $Ticket


  #region get work item updates to find the actual closed date
  $WorkItemUpdates = Get-DevOpsWorkItemUpdatesByID -Organisation $Organisation -ProjectName $ProjectName -WorkItemID $Ticket

  $WorkItemUpdateWithClosedDate = $WorkItemUpdates.fields | sort-object id  | Where-Object {$_."System.Reason".newValue -eq 'Moved to state Closed' }
  $DateToClose = $WorkItemUpdateWithClosedDate."System.ChangedDate".newValue
  #endregion get work item updates to find the actual closed date

  $TicketsUpdatedArray += $TicketObject
  $TicketObject.fields
  
  $FieldsToUpdate = @(
    @{
      path  = "/fields/Microsoft.VSTS.Common.ClosedDate"
      value = "$DateToClose"
    }
  )
  Write-Host "Update ticket $Ticket closed date to with date $DateToClose"
  $FieldsToUpdate
  start-sleep -Milliseconds 300
  try {
    $UpdatedResult = Update-DevOpsWorkItem -Organisation $Organisation  -WorkItemId $Ticket -FieldsToUpdate $FieldsToUpdate
    Write-Host " Updated ticket"
    $UpdatedResult.fields
    $UpdatedArray += $UpdatedResult
  }
  catch {
    $FailedArray += $TicketObject
  }
  
}
#endregion iterate and update

#endregion work item dates

#region save files
$UpdatedArray | ConvertTo-Json -Depth 100 | Out-File -FilePath "$Home\Downloads\UpdatedWorkItems$($TimeStamp).json"
$TicketsUpdatedArray | ConvertTo-Json -Depth 100 | Out-File -FilePath "$Home\Downloads\TicketsOriginalData$($TimeStamp).json"
$UpdatedArray | ConvertTo-CSV -noTypeInformation -UseQuotes Always | Out-File -FilePath "$Home\Downloads\UpdatedWorkItems$($TimeStamp).csv"
$TicketsUpdatedArray | ConvertTo-CSV -noTypeInformation -UseQuotes Always | Out-File -FilePath "$Home\Downloads\TicketsOriginalData$($TimeStamp).csv"
# output failed array - usually fields missing
$FailedArray | ConvertTo-CSV -noTypeInformation -UseQuotes Always | Out-File -FilePath "$Home\Downloads\FailedWorkItemsUpdate$($TimeStamp).csv"
$FailedArray | ConvertTo-Json -Depth 100 | Out-File -FilePath "$Home\Downloads\FailedWorkItemsUpdate$($TimeStamp).json"
#endregion save files
```

---

>
> Script bootstrap.ps1
> Developed by Daniel Broderick
>

```
<#	
	.DESCRIPTION
		A powershell script to bootstrap variables and modules.

        This script will dyncamically import any modules in the libary\powershell folders

        Other paths can be added if required. 

        Any new modules can be simply added and the bootstrap will dyncamically load them.

        Use the import-module.ps1 header in your scripts to dyncamically call this bootstrap.
#>

try
{
	Write-Debug "$($MyInvocation.MyCommand): Bootstrapping all variables"
	$global:RootScriptPath = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition # Dymanically get Path of script -  # decleared a global for the GUI application 
	
    # add environment variable, this will only be present during script run
    # creating an env variable will make it available in jobs - makes the scope more universal
	$env:RootScriptPath = $RootScriptPath 

	
	$FileTimeStamp = get-date -Format "ddMMyyyy-HHmm" # used in many scripts for time stamping saved files
	
	#region Paths
	$LibraryPath = "$RootScriptPath\Library"  
	$ModulePath = "$LibraryPath\Modules"
    $PowershellModules = "$ModulePath\Powershell"
	#endregion Paths


	#region regex for naming conventions
	# https://wcbbc.sharepoint.com/:w:/s/AzureDevOpsIAWorkgroups/ETGFzaWXGKVEgBPG0lgUJYgBepMwBwOhmNpETORxO4sQdw?e=6OuW7B
	# To use example $Hotfix -match $BranchNamingConventionRegex


	$RepoNamingConventionRegex = '([a-z]{1,50})\.([a-z0-9-]{1,50})\.([a-z0-9-]{1,50})\.([a-z0-9-]{1,50})'
	$BranchNamingConventionRegex = '([a-z]+)(\/)([0-9])([\.0-9])([0-9a-z-]+)'
	$ClassicReleaseNamingConventionRegex = '([a-z]{1,50})\.([a-z0-9-]{1,50})\.([a-z0-9-]{1,50})'
	
	#endregion regex for naming conventions
	
	#region set variable preferences
	if ($env:SetDebugPreference)
	{
		$Global:DebugPreference = $env:SetDebugPreference
	}

	if ($env:SetVerbosePreference)
	{
		$Global:VerbosePreference = $env:SetVerbosePreference
	}

	#endregion set variable preferences
	
	#region import modules and ps1 functions
	if (-not ($env:PSModulePath -like "*$PowershellModules*"))
	{
		Write-Debug "$($MyInvocation.MyCommand): Setting module Path environment variable - adding $PowershellModules"
		$env:PSModulePath = $env:PSModulePath + ";" + $PowershellModules
	}
	
	foreach ($PowershellModuleFile  in (Get-ChildItem -Recurse -Path $PowershellModules -Include *.psm1, *.psd1).FullName)
	{
		Write-Debug "$($MyInvocation.MyCommand): Importing module $PowershellModuleFile"
		Import-Module $PowershellModuleFile -Force -NoClobber -ErrorAction SilentlyContinue
	}	
}
catch
{
	
	Write-Error "$($MyInvocation.MyCommand): Error bootstrapping variables - $($_.Exception)"
}

```

---

Enjoy!