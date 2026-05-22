Title: AI Assisted Automation - From “How Many Azure Repos?” to “Here Is the Report”
Date: 2026-05-22
Category: Posts 
Tags: ai, engineering, azure devops, automation
Slug: ai-assisted-repo-report
Author: Agent Ubuntu
Summary: A small working-group question, a forgotten automation, and a fresh reminder that our centre of gravity is shifting from writing code to writing instructions.

I was sitting in a working group when a perfectly reasonable question landed on the table:

>
> **“How many Azure Repos do we have?”**
>
> ![question](../images/ai-assisted-repo-report-1.png) 
>


Not a trick question. Not even a hard question. Just the kind of operational query that should be answered with calm confidence, in minutes, without derailing the conversation.

I knew we had an automated report. It used to run weekly. We changed it to a manual trigger more recently to conserve Azure DevOps service load.

The traditional path was clear: go find the automation, trigger it, wait for output, and then format something presentable.

And then my brain offered a better option:

>
> **“Let me ask Agent Ubuntu.”**
>

So, instead of locating and using our existing automation and rebuilding an up-to-date report, I asked Agent Ubuntu to create a script that produced:

- A summary table
- A complete repository list
- Something I could share immediately

### Agent Ubuntu (powered by GitHub Copilot) responded

Agent Ubuntu delivered exactly what I needed. A PowerShell script that connects to our Azure DevOps organisation and produces (1) a summary table showing the number of repositories per project, and (2) a detailed list of every repository with its project, name, and estimated size.

The script was sitting in front of me before my “human follow-through” had even finished warming up.

My next command was beautifully uncomplicated:

> 
> **“Run it.”**
>

And that was it. I had a report with the requested information, and more.

**This is not a hypothetical. This is today's reality.** The pull request description clarified that the script was created because a question triggered the need, and asking Agent Ubuntu to create the script and generate the report was faster than finding the existing automated report and triggering it.

### The Agent Ubuntu generated magic

The script is not a “throwaway” today, although I am starting to question why we are version controlling both our instructions and source code.

Let us take a sneak peek at the generated code:

- It uses a Personal Access Token (PAT) (a scoped credential) via an environment variable ($env:pat).
- It generates both a Comma-Separated Values (CSV) export and a Markdown report file.
- It stamps the output with Coordinated Universal Time (UTC) plus local time for Vancouver, which makes sharing and audit conversations far less painful.
- The Markdown output includes a clear heading, a generated time, the organisation name, and the total repository count (calculated by the script).

It produces something that answers the question, and something that can be attached to an email or dropped into a working session chat without embarrassment.

``` powershell
<#
    .DESCRIPTION
        Connects to the wcbbc Azure DevOps organisation and produces:
          1. A summary table showing the number of repos in each project.
          2. A detailed list of every repo with its project, name, and estimated size.

        Size is returned directly from the Azure DevOps Git Repositories API (bytes).
        The script formats output to the console and exports CSV and Markdown files.
#>

#region params
[CmdletBinding()]
param (
    [Parameter(Mandatory = $false)]
    [String]
    $Organisation = "<organisation>",
    [Parameter(Mandatory = $false)]
    [String]
    $PAT = $env:pat,
    [String]
    $FilePath = "$Home\Downloads"
)
#endregion params


#region bootstrap
$FileName = 'bootstrap.ps1'
$FoundFlag = $false
$Path = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition

do {
    try {
        if (Test-Path -Path "$Path\$FileName") {
            $FoundFlag = $true
            Write-Output "Bootstrap found – importing modules"
            . "$Path\$FileName"
        }
        else {
            $Path = Split-Path -Parent -Path $Path
        }
    }
    catch {
        $_
        Write-Output "$FileName not found – bootstrap cannot load modules. Exiting."
        exit
    }
} Until ($FoundFlag -eq $true)
#endregion bootstrap

#region helpers
function Format-RepoSize {
    param ([long]$Bytes)

    if ($Bytes -ge 1GB) {
        return "{0:N2} GB" -f ($Bytes / 1GB)
    }
    elseif ($Bytes -ge 1MB) {
        return "{0:N2} MB" -f ($Bytes / 1MB)
    }
    elseif ($Bytes -ge 1KB) {
        return "{0:N2} KB" -f ($Bytes / 1KB)
    }
    else {
        return "$Bytes B"
    }
}
#endregion helpers

#region setup
Write-Debug "$($MyInvocation.MyCommand): Begin"

if (-not (Test-Path -Path $FilePath)) {
    Write-Host "Creating output folder: $FilePath"
    New-Item -Path $FilePath -ItemType Directory -Force | Out-Null
}

$FileTimeStamp      = Get-Date -Format "ddMMyyyy-HHmm"
$CSVFilePath        = "$FilePath\Repo-Size-Report-$FileTimeStamp.csv"
$MDFilePath         = "$FilePath\Repo-Size-Report-$FileTimeStamp.md"

Set-DevOpsScriptVariables -DevOpsOrganisation $Organisation -PAT $PAT -DevOpsProject "Common-Engineering-System"

$AllRepos           = [System.Collections.Generic.List[PSCustomObject]]::new()
#endregion setup

#region collect data
$Projects = Get-DevOpsProjects -Organisation $Organisation | Sort-Object name

foreach ($Project in $Projects) {
    $ProjectName = $Project.name
    Write-Host "  Processing project: $ProjectName"

    Set-DevOpsScriptVariables -DevOpsOrganisation $Organisation -DevOpsProject $ProjectName -PAT $PAT

    $Repos = Get-DevOpsRepo -Organisation $Organisation -ProjectName $ProjectName

    foreach ($Repo in ($Repos | Sort-Object name)) {
        $AllRepos.Add([PSCustomObject]@{
            ProjectName    = $ProjectName
            RepoName       = $Repo.name
            SizeBytes      = [long]$Repo.size
            SizeFormatted  = Format-RepoSize -Bytes ([long]$Repo.size)
            IsDisabled     = $Repo.isDisabled
            WebUrl         = $Repo.webUrl
        })
    }
}
#endregion collect data

#region summary table (console)
Write-Host ""
Write-Host "=== Repos per Project ===" -ForegroundColor Cyan

$SummaryTable = $AllRepos |
    Group-Object -Property ProjectName |
    Select-Object @{Name = 'Project'; Expression = { $_.Name }},
                  @{Name = 'RepoCount'; Expression = { $_.Count }} |
    Sort-Object Project

$SummaryTable | Format-Table -AutoSize
#endregion summary table (console)

#region detail list (console)
Write-Host "=== All Repositories ===" -ForegroundColor Cyan

$AllRepos |
    Select-Object ProjectName, RepoName, SizeFormatted, IsDisabled |
    Format-Table -AutoSize
#endregion detail list (console)

#region CSV export
$AllRepos | Export-Csv -Path $CSVFilePath -NoTypeInformation -Encoding UTF8
Write-Host "CSV saved: $CSVFilePath"
#endregion CSV export

#region Markdown report
$UTCTime      = (Get-Date).ToUniversalTime()
$TimeZone     = "Pacific Standard Time"
$LocalTime    = [System.TimeZoneInfo]::ConvertTimeBySystemTimeZoneId($UTCTime, $TimeZone)

$MD = [System.Text.StringBuilder]::new()
[void]$MD.AppendLine("# Azure DevOps Repository Report")
[void]$MD.AppendLine("")
[void]$MD.AppendLine("<font size='2'>Generated: $UTCTime UTC &nbsp;|&nbsp; $LocalTime Vancouver Time</font>")
[void]$MD.AppendLine("")
[void]$MD.AppendLine("**Organisation:** $Organisation")
[void]$MD.AppendLine("")
[void]$MD.AppendLine("**Total repositories:** $($AllRepos.Count)")
[void]$MD.AppendLine("")

# Summary section
[void]$MD.AppendLine("## Repos per Project")
[void]$MD.AppendLine("")
[void]$MD.AppendLine("| Project | Repo Count |")
[void]$MD.AppendLine("|:--------|----------:|")

foreach ($Row in $SummaryTable) {
    [void]$MD.AppendLine("| $($Row.Project) | $($Row.RepoCount) |")
}

[void]$MD.AppendLine("")

# Detail section
[void]$MD.AppendLine("## All Repositories")
[void]$MD.AppendLine("")
[void]$MD.AppendLine("| Project | Repository | Estimated Size | Disabled |")
[void]$MD.AppendLine("|:--------|:-----------|---------------:|:--------:|")

foreach ($Repo in $AllRepos) {
    [void]$MD.AppendLine("| $($Repo.ProjectName) | [$($Repo.RepoName)]($($Repo.WebUrl)) | $($Repo.SizeFormatted) | $($Repo.IsDisabled) |")
}

$MD.ToString() | Set-Content -Path $MDFilePath -Encoding UTF8
Write-Host "Markdown saved: $MDFilePath"
#endregion Markdown report
```

### Back to the Future

Let me be honest ... twelve months ago I would likely have:

- Dug through the Azure DevOps REST API documentation, which is not always the most straightforward experience.
- Written and refined code.
- Tweaked pagination, filtering, and output formatting.
- Burned time validating the result set.
- Lost the thread of the working group conversation.

Today, the work shifts from **construction to instruction**.

I can focus on what matters:

- The people in the working session.
- The decision we need to make.
- The “burning platform” of the day.

This is not laziness. That is efficiency.

We are amplifying, not abandoning engineering discipline..

**We are shifting our focus from writing code to writing instructions**, in a way that improves stakeholder experience, reduces risk, and avoids cost.

>
> ![agent ubuntu](../images/agent-ubuntu-mini.png)
>
> What is next? q;-)
> 