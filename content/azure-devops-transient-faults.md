Title: Azure DevOps Transient Faults
Date: 2023.02.17
Category: Posts 
Tags: azure-devops, tips
Slug: azure-devops-transient-faults
Author: Willy-Peter Schaub
Summary: Be careful not to annoy Azure DevOps with your automated maintenance jobs!

When you automate your operational support and maintenance of [Azure DevOps](https://azure.microsoft.com/en-us/products/devops/), such as updating the pre- and post-approvers of 2500 Azure Pipelines, or creating a detailed report of all Azure Pipelines in your Azure DevOps Organization, you may come across ad-hoc exceptions, "429 Too Many Requests Error", "503 Service Unavailable", or a "_last time it 100% worked for sure with no issues_" call for help.

```
Service Unavailable
Service Unavailable
HTTP Error 503. The service is unavailable.
```

# Transient fault

You probably triggered a **throttling** or **circuit breaker** pattern, which Azure DevOps uses to protect itself against excessive load or potential ```denial of service``` attacks. If you do not deal with the transient fault you will end up with failed automation, wasted time, and **manual** intervention - more **WASTE**.

---

# Dealing with transient fault

Here is a simple **retry pattern** that allows you to retry the operation after going to sleep for a while. You may have to play with and increase the ```$retryValue``` default value, depending on the REST API you are calling. 

1.13 has worked for me and my automation scripts to date.

```
$retryCount = 3
$retrySleep = 1.13
$retryCheck = $retryCount - 1

for ( $failureCount = 0; $failureCount -lt $retryCount; $failureCount++ ) 
{
    try 
    {
        # call Azure DevOps REST API
        $result = Invoke-RestMethod -Uri $url -ContentType "application/json" -Headers $headers
        
        # processing
        # ...
    }
    catch 
    {
        # retry logic
        if ( $failureCount -eq $retryCheck )
        {
            # ensure that pipeline shows a warning
            Write-Output "##vso[task.complete result=SucceededWithIssues;]SUCCEEDED WITH ISSUES"
            break;
        }
        else 
        {
            # Logging
            Write-Output "Sleep and then retry processing loop. Count: " $failureCount " Sleep: " $retrySleep
            Write-Output $_.Exception.Message

            # retry
            $retrySleep = $retrySleep * ( $failureCount + 1 );
            Start-Sleep -Seconds $retrySleep
        }
    }
}   
```

Simple, yet effective.

---

Read [3 ways to handle transient faults for DevOps](https://opensource.com/article/19/9/transient-faults-devops) for more details on transient faults.

