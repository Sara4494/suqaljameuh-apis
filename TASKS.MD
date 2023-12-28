# Sarah's Task (15 Sept)

---

# Create the following models:

> Please NOTE that all the schemas can be found here: https://drawsql.app/teams/progo/diagrams/suqaljameuh except ReportProblem is exactly like ReportAd but the only difference is that it doesn't contain ad field

## - ReportAd

## - ReportProblem

## - Favorites

# Create the following APIs

# - Making ReportAd

## Permission: User Must be authenticated

## There should be an endpoint named "make-reports" and this will take from the user the content of the report "report_content"

## then we'll create a new ReportAd instance which will take the Ad and will be associated with the user

## after completing the report successfully, please make sure to send a real-time notification to the ADMINS to inform them that a report was made by a user

> ReportProblem's schema is exactly like ReportAd but the difference is that it doesn't accept Ad

# - Retrieve Reports

## Permission: Admin-Only Endpoint

## Endpoint that gets all the latest reports (ReportAd)

# - Retrieve single report

## Permission: Admin-Only Endpoint

## Endpoint that gets a certain report based on the ID

# - Discard Report

## API's Method: PUT

## Permission: Admin-Only Endpoint

## Reports can be discarded which indicates that this report is useless or sensless

## in this endpoint will flag the report to "discard=True"

## NOTE: after flagging a report as discarded make sure to send the reporter (the user who made the report) a real-time notification informs him by that

# - Flag Report To Be In-Progress

## API's Method: PUT

## Permission: Admin-Only Endpoint

## Reports can be flagged to be in-progress which indicates that this reported was noticed by the admins

## in this endpoint will flag the report to "in_progress=True"

## NOTE: after flagging a report as in_progress make sure to send the reporter (the user who made the report) a real-time notification informs him by that

# - Flag Report To Be Finalized

## API's Method: PUT

## Permission: Admin-Only Endpoint

## Reports can be flagged to be finalized which indicates that this reported was finalized and the admins took a decision about it

## in this endpoint will flag the report to "finalized=True"

## NOTE: after flagging a report as finalized make sure to send the reporter (the user who made the report) a real-time notification informs him by that

# Report Problem APIs

## They're identical to Report Ad APIs but the only difference is that there's no Ad will be accepted and also we'll be working with ReportProblem model not ReportAd

# Favorites

# User should be able to store things he likes and get back to them later on

## Add To Favorite

## This endpoint should accept the ad which user wanna store and also and it will create a new favorite for this ad and will associate it with the user

## Retrieve Favorites

## This endpoint should get all the favorites that belongs ot that user

## Delete Favorite

## This endpoint should first get the favorite item based on the user and the ad then delete it

# TASK duration:

# The expected period is within 2 days at most
