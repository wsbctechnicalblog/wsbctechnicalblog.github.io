Title: A Friday AI Prompt Epiphany
Date: 2026-04-24
Category: Posts
Tags: ai, engineering, prompts
Slug: ai-fundamentals-a-prompt-epiphany
Author: Willy-Peter Schaub
Summary: The Night I Stopped Checking In Code and Started Checking In Intent.

Last night I had a small epiphany that I want to take to our next team huddle: I solved the right problem… in the wrong way.

> ![EPIHANY](../images/ai-fundemantels-a-prompt-epiphany-1.png) 

**It started with a simple Azure DevOps query result**. 202 work items, and only one was linked to a parent. The backlog was real, the gap in traceability was real, and the cost of leaving it as-is was evident too. Weaker portfolio visibility, messier reporting, and more time burned later when someone inevitably asked, “Which feature does this belong to?”

## The obvious “engineering” move

I did what most of us do when we see toil and feel urgency ... I automated.

The challenge had a twist. Within the same Azure DevOps project, parenting work items is easy. Across projects, the intentional isolation between Azure DevOps projects adds a spice of complexity. So I asked our digital companion, [Agent Ubuntu](/zero-or-one-not-fault-lines-2029-ubuntu-vision.html) (powered by GitHub Copilot), to write a PowerShell script.

It delivered. I ran it. In under three minutes, every work item returned by the query was parented to the right portfolio item. Job done. I even checked the script into our scripts repository for future reuse.

And then… the epiphany landed.

>
> The epiphany: **I checked in the wrong artefact!**
>
> The script is not the asset.
>
> The instruction is the asset.
>
> The source code is a by-product: interesting to review, sometimes worth keeping, but frequently not worth preserving as a first-class artefact. What matters most is the intent — the prompt that captures:
>

The instruction can be reused, improved, and re-applied across similar situations, even when the implementation changes (PowerShell today, Azure DevOps CLI tomorrow, a pipeline task next month). This aligns strongly with what we are learning across our AI adoption journey: **Prompt precision and human validation are where the durable value sits.**

Take it one step further and ask the agent to check in the prompt

After the epiphany, I restarted my laptop, opened GitHub Copilot chat, and gave it a crisp and simple instruction:

> 
> _Find the most efficient way to securely parent all work items returned by query <URL>, re-parent as needed, and validate._
> 

**And then it hit me.** I could have gone one step further and asked Agent Ubuntu to improve and check in the instruction once the task completed successfully. That is how we reduce repeated effort, reduce risk, and avoid cost over time: we keep the recipe, not only the dish.

This is consistent with how we already talk about reusable instructions and prompts as shareable organisational assets (not tribal memory)!

You can find the script referenced in this post and an improved instruction from [Agent Ubuntu](/zero-or-one-not-fault-lines-2029-ubuntu-vision.html) for your reference. Remember, the real asset is the instruction itself. The script is just one implementation of that instruction, and it may not even be the best one. The instruction can be adapted and improved over time, while the script may become obsolete as tools and APIs evolve.

---

### Reference script:

```powershell
# Configuration
$organization = "<ORG>"
$project = "<AzDO PROJECT>"
$queryId = "<QUERY ID>"
$parentWorkItemId = "<PARENT WORK ITEM ID>"
$baseUrl = "https://dev.azure.com/$organization/$project"

# Get PAT from environment or prompt
$pat = $env:AZURE_DEVOPS_PAT
if (-not $pat) {
    $pat = Read-Host -Prompt "Enter your Azure DevOps PAT" -AsSecureString
    $pat = [Runtime.InteropServices.Marshal]::PtrToStringAuto(
        [Runtime.InteropServices.Marshal]::SecureStringToBSTR($pat)
    )
}

$base64Auth = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(":$pat"))
$headers = @{
    Authorization  = "Basic $base64Auth"
    "Content-Type" = "application/json"
}

# Execute the query to get work item IDs
Write-Host "Fetching work items from query..."
$queryUrl = "https://dev.azure.com/$organization/$project/_apis/wit/wiql/$queryId`?api-version=7.1"
$queryResult = Invoke-RestMethod -Uri $queryUrl -Headers $headers -Method Get

$workItemIds = $queryResult.workItems | Select-Object -ExpandProperty id

if (-not $workItemIds) {
    Write-Host "No work items found in query."
    exit
}

Write-Host "Found $($workItemIds.Count) work item(s): $($workItemIds -join ', ')"

# Get the URL of the parent work item
$parentUrl = "https://dev.azure.com/$organization/_apis/wit/workItems/$parentWorkItemId"

# Add parent link to each work item
foreach ($id in $workItemIds) {
    Write-Host "Processing work item $id..."

    # Check existing relations to avoid duplicate parent
    $wiUrl = "https://dev.azure.com/$organization/$project/_apis/wit/workItems/$id`?`$expand=relations&api-version=7.1"
    $wi = Invoke-RestMethod -Uri $wiUrl -Headers $headers -Method Get

    $existingParent = $wi.relations | Where-Object { $_.rel -eq "System.LinkTypes.Hierarchy-Reverse" }
    if ($existingParent) {
        Write-Host "  Work item $id already has a parent. Skipping."
        continue
    }

    $patchUrl = "https://dev.azure.com/$organization/$project/_apis/wit/workItems/$id`?api-version=7.1"
    $patchHeaders = $headers.Clone()
    $patchHeaders["Content-Type"] = "application/json-patch+json"

    $body = ConvertTo-Json -InputObject @(
        @{
            op    = "add"
            path  = "/relations/-"
            value = @{
                rel        = "System.LinkTypes.Hierarchy-Reverse"
                url        = $parentUrl
                attributes = @{ comment = "Parent set by automation script" }
            }
        }
    ) -Depth 5

    try {
        Invoke-RestMethod -Uri $patchUrl -Headers $patchHeaders -Method Patch -Body $body | Out-Null
        Write-Host "  Successfully set parent for work item $id."
    }
    catch {
        Write-Warning "  Failed to update work item $id`: $_"
    }
}

Write-Host "Done."
```

---

### Reference Instruction

Here is an example prompt template you can check in as a markdown file.

```markdown
# Prompt: Securely parent work items from an Azure DevOps query

## Goal
Parent all work items returned by Azure DevOps query <URL> to portfolio parent work item <PARENT_ID>.

## Guardrails (non-negotiable)
- Do not expose secrets. Use a Personal Access Token (PAT) from a secure source (environment variable or secret store), never hard-code it.
- Use least privilege: token must have only the Work Items permissions required.
- Do not modify unrelated work items.
- If a work item already has a parent, do not overwrite unless explicitly instructed.
- Log actions and produce a summary of changes.

## Steps
1. Retrieve work item IDs from the query.
2. For each work item:
   - Fetch existing relations.
   - If a parent exists, skip (or re-parent only if instructed).
   - Add the parent relation to <PARENT_ID>.
3. Validate:
   - Re-fetch each updated work item and confirm the parent relation exists.
   - Produce a report: updated, skipped (already parented), failed (with reason).

## Output
- Implementation approach recommendation (best option and why).
- A safe script or command sequence (PowerShell or Azure DevOps CLI).
- A validation report format (markdown table or JSON).
```

That all for today folks. I am going to enjoy my day off. If you have any questions or want to chat about AI, prompts, or anything else, feel free to reach out. See you soon!

