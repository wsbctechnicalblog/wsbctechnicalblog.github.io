Title: Privacy and Security
Date: 2021-04-17 10:37
Category: Links
Slug: privacy
Author: WorkSafeBC
Summary: WorkSafeBC Technical Blog has protected your privacy by disabling Google to collect the information for the Federated Learning of Cohorts

WorkSafeBC is above all concerned about the privacy and the security of all the parties visiting our Technical Blog. To that end we have diligently opted out of the controversial [Federated Learning of Cohorts (FLoC)](https://github.com/WICG/floc).

## How does WorkSafeBC Technical Blog ensure no FLoC data gets collected when visitors browse the blog?

We have configured the ```<head>``` section of our root index.html document with the follwong meta directive:

```
<meta http-equiv="Permissions-Policy" content="interest-cohort=()"/>
```