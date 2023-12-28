# Reports APIs Ref

---
# Get All Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/reports/all/

## Method: GET

## Description: Retrieves all report object

## Data: None

## NOTES:

 
# Report Details Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/reports/report/<int:report_id>/

## Data: None

## Description: Retrieves a specific report object by ID.

# Delete Ad Endpoint

> NOTE: Reported aren't deletable, but you can discard them, and the user will know about it

## Create Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/reports/make-report/

## Method: POST

## Description: Creates a new report object with the given content and ad ID.

## Data: content, ad

## Update Endpoint



## Endpoint: https://suqaljameuh-apis.up.railway.app/reports/discard/int:report_id/

## Method: PUT

## Description: Discards a specific report object by ID.

## Endpoint: https://suqaljameuh-apis.up.railway.app/reports/update/in-progress/int:report_id/

## Method: PUT

## Description: Flags a specific report object by ID as in progress.

## Endpoint: https://suqaljameuh-apis.up.railway.app/reports/update/finalized/int:report_id/

## Method: PUT

## Description: Flags a specific report object by ID as finalized.

## Data: None


# ReportProblem APIs Ref

---

## Get All Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/reports/problems/

## Method: GET

## Description: Retrieves all problem report objects.

## Data: None

## Report Details Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/reports/problems/int:problem_id/

## Method: GET

## Description: Retrieves a specific problem report object by ID.

## Data: None

# Delete Ad Endpoint

> NOTE: Reported aren't deletable, but you can discard them, and the user will know about it

## Update Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/reports/problems/int:problem_id/discard/

## Method: PUT

## Description: Discards a specific problem report object by ID.

## Endpoint: https://suqaljameuh-apis.up.railway.app/reports/problems/int:problem_id/in-progress/discard/

## Method: PUT

## Description: Flags a specific problem report object as in progress by ID.

## Endpoint: https://suqaljameuh-apis.up.railway.app/reports/problems/finalized/int:problem_id/

## Method: PUT

## Description: Flags a specific problem report object as finalized by ID.

## Create Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/reports/make-problem-reports/

## Method: POST

## Description: Creates a new problem report object with the given content and ad_id.

## Data: content, ad_id


# Favorites APIs Ref

---


## Get All Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/reports/favorites/

## Method: GET

## Description: Retrieves all favorite objects.

## Data: None

## Create Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/reports/favorites/add/

## Method: POST

## Description: Creates a new favorite object with the given name.

## Data: name

## Update Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/reports/favorites/delete/int:favorite_id/

## Method: DELETE

## Description: Deletes a specific favorite object by ID.

## Data: None

---