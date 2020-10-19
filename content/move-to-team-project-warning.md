Title: Use the move to team project feature with cuation!
Date: 2020-10-20 13:13
Category: Posts
Tags: AzDO, Azure Boards
Slug: the-move-to-team-project-feature
Author: Willy-Peter Schaub
Summary: The "Move to Team Project" feature nukes your work item state and dates

There are two valuable features in the Azure Boards service, one to change the work item type and the other to move work items between projects. But ... there is always a but ... the second comes with a few gotchas that turned a simple migration into a mind-numbing slog.

![Move to Team project featute](/images/move-to-team-project-warning-1.png)

The "**Move to team project**" allows you to select one, more, or all of the work items on a backlog or from a work item query language (WIQL) result set and move them to another Azure DevOps project, within the same Azure DevOps organization.

> Quick and simple!

But ... here we go again ... when you look at the migrated data you will notice two things:

- The work item state is reset to New
- The Change Date is set to the migration date and time

Why? Do not know, but would love to understand the reasoning behind the state and date changes. If you have not planned your migration you will not have to single step through hundreds to thousands of work items to determine the correct state and dates - mind numbing!

# Pre-migration planning

After staring at the updated work item data in disbelief a few times, we have created a simple pre-migration checklist:

- Export all work items to an Excel workbook to have a reference snapshot.
- Tag the work items with the state, iteration, board column, and board lane.
- Verify that target has all of the work item types for the set of items  you need to migrate
- Grab a can of your favourite brew ... you will need it!

# Post-migration grooming

After using the "Move to team project" feature to migrate all of the work items, we process the post-migration checklist:

- Set the correct state of the work items, based on the state tag. Once done, remove tag.
- Set the correct Iteration Path, based on the state tag. Once done, remove tag.
- Move cards to the correct column and swim lane, based on the column and lane tags. Once done, remove tags.


If needed, set the correct Activated and Closed dates, which are now set to the date and time when you corrected the work item state :(
PowerShell Script to the Rescue

# Samples

Here are two sample scripts we added to our ever growing library of automation and maintenance scripts to update the read-only Closed Date field. We want to change the dates back to the post migration dates, which we can extract from the Excel workbook we created in pre-migration step 1, so that the data on boards and the backlog looks valid.

## Set Changed Date Script

```
[CmdletBinding()]
param(
  [string]   $orgName       = "<ORG>",
  [string]   $patToken      = "<PAT>",
  [string]   $workItemID    = "<invalid>",
  [string]   $dateTime      = "<invalid>"
)

# Authentication header
$basicAuth = ("{0}:{1}" -f "",$patToken)
$basicAuth = [System.Text.Encoding]::UTF8.GetBytes($basicAuth)
$basicAuth = [System.Convert]::ToBase64String($basicAuth)
$headers   = @{Authorization=("Basic {0}" -f $basicAuth)}

# Setup Request
$request   = "https://dev.azure.com/" + $orgName + "/" + "_apis/wit/workitems/" + $workItemID + "?bypassRules=true&api-version=6.0"

# Setup Body
$json = 
'[
{"op":"add","path":"/fields/Microsoft.VSTS.Common.ClosedDate","value":"' + $dateTime + '"},
{"op":"add","path":"/fields/System.History","value":"Post-migration Closed Date correction to reflect original, not migration, date."}
]'

# Call Request
try
{
  Write-Host "Updating work item: $workItemID"
  $response = Invoke-RestMethod -Uri $request -headers $headers -Method PATCH -Body $json -ContentType 'application/json-patch+json'
}
catch 
{
    Write-Host "Error setting date - " $PSItem.Exception.Message
    Write-Host  $_.Exception|format-list -force
}
```

## Calling Script

```
# Batch 1
..\Scripts\Update_Work_Item_ClosedDate.ps1 -orgName "<ORG>" -patToken "<PAT>" -workItemID "<WI #>" -dateTime "<DATE FROM EXCEL WORKBOOK>T13:00:00.00-08:00"
..\Scripts\Update_Work_Item_ClosedDate.ps1 -orgName "<ORG>" -patToken "<PAT>" -workItemID "<WI #>" -dateTime "<DATE FROM EXCEL WORKBOOK>T13:00:00.00-08:00"
```

Migrating data is not an easy task, especially if you also need to migrate Test Plans, Suites, and Cases ... that is another turbulent topic for another day. 

![Migration Tools for Azure DevOps](/images/move-to-team-project-warning-2.png)

We are busy investigating the open source Migration Tools for Azure DevOps, by Martin Hinshelwood, which will hopefully allow us to further automate and reduce the number of state changes during work item migrations. I will be back with an update!