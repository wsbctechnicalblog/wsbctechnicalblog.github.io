Title: Find the capabilities and IP addresses of an Azure DevOps agent
Date: 2021-03-12
Category: Posts
Tags: azure-devops, pipelines, tips
Slug: azure-devops-agent-capabilities
Author: Willy-Peter Schaub
Summary: How to find more information on hosted Azure DevOps agents, such as capabilities and IP addresses.

# Why should we care about an Azure DevOps Agent?

To use our [Azure Pipelines](https://wsbctechnicalblog.github.io/index.html), we need the agents. Every time one of our pipelines is triggered, it comes to life on one or more jobs, which are hosted and run an agent.

Azure DevOps offers two types of agents. **Microsoft-hosted** agents are a software as a service (SaaS) offering, where maintenance and upgrades are taken care of for you. Our recommended type of agents!

**Self-hosted agents** give you more control of access and installed software needed for special builds and deployments. For example, we have a self-hosted pool to service our good old **Cobol** builds.

---

# How to determine the capabilities of an Azure DevOps Agent

We often get the question: "What software is installed on the agent?" In other words, how do we determine the capabilities of each Azure DevOPs agent.

For self-hosted agents you can go to your Azure DevOps **organizational** setting, Agent pools, select **pool**, select **Agents**, select an **agent**, and finally, select **Capabilities**. You will be presented with the agent's system capabilities, variables, paths, and installed software, as shown below.

> Capabilities of a **self-hosted** agent
>
> ![AzDO Agent Details](/images/azuredevops-agent-info-1.png)

When you select a Microsoft-hosted agent and pool, the presented capabilities are less exciting.

> Capabilities of a **Microsoft-hosted** agent
>
> ![AzDO Agent LAck of Details](/images/azuredevops-agent-info-2.png)

You need to visit the [Microsoft-hosted Agents](https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/hosted) documentation and scroll down to the **Software** section. Peruse a list of hosted agents, classic pipeline editor specifications, YAML image labels, and links to software available on each type of agent.

> Azure DevOps Agent Documentation
>
> ![AzDO Agent Documentation](/images/azuredevops-agent-info-3.png)

Select your agent, click on the included software hyperlink, and voila, you have a detailed report of the agent's capabilities.

> Azure DevOps Agent Capabilities Documentation
>
> ![AzDO Agent Capabilties Documentation](/images/azuredevops-agent-info-4.png)

---

# How to determine the IP addresses of an Azure DevOps Agent

The [Microsoft-hosted Agents](https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/hosted) documentation also gives you information on how to identify possible IP ranges for Microsoft-hosted agents. This information is pivotal if you need to allow the agents to make their way from the public internet, through your firewall, to collaborate with one of your services.

Unfortunately, you will also find some small print ... well, it is the same sized font and the note is placed on a prominent Indigo background. It is easy to miss the highlighted part, as shown below, that mentions that the IP addresses for the macOS agents are not included.

> macOS Addresses are a mystery
>
> ![macOS Address Mystery](/images/azuredevops-agent-info-5.png)

First thought is to queue a investigative pipeline on one of the macOS agents and run the **ipconfig getifaddr en0** command. That only returns the private IP address of the agent, which is interesting, but not very useful to the firewall engineers.

Try this:

```yml
- task: PowerShell@2
  inputs:
    targetType: 'inline'
    script: 'curl ipecho.net'
    errorActionPreference: 'continue'
    pwsh: true
```

It reveals the public IP address:

```html
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  2090  100  2090    0     0  32656      0 --:--:-- --:--:-- --:--:-- 32153
100  2090  100  2090    0     0  32656      0 --:--:-- --:--:-- --:--:-- 32153

... SNIPPED FOR BLOG POST ...

<main>
<div style="text-align: center; flex: 1; ">
    <h1>Your IP is 13.105.49.13</h1>

...SNIPPED FOR BLOG POST...
```

Lastly, who owns the IP address we just found?

Visit [13.105.49.13 IP Address Details - IPinfo.io](https://ipinfo.io/13.105.49.13) for the answer:


> IP address "BINGO!"
>
> ![IPinfo.io](/images/azuredevops-agent-info-6.png)

---

A big thank you to [Lukas Wilson](https://www.linkedin.com/in/lukas-wilson-8792ba172/), one of our resident Azure gurus, who helped with the IP address exploration. 

# Reference Information

- [Microsoft-hosted agents](https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/hosted)
- [Part 1: Pipelines - Why bother and what are our nightmares and options?](https://wsbctechnicalblog.github.io/index.html)