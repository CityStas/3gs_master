---
title: "Risk levels"
url: /docs/en-us/cloud/reference/risk-levels
last_updated: 2026-10-30T19:55:39Z
description: "Explains the risk level classifications for Open Cloud API endpoints and their behavior in the \"try it out\" feature."
---

# Risk levels

Risk levels classify Open Cloud endpoints based on the potential impact of their operations. These classifications apply to the OAuth 2.0 authorization flow and the "try it out" feature here in the API documentation.

Risk levels help protect your data and account when testing API endpoints in the documentation. Always review an endpoint's functionality and potential impact before testing, particularly for medium and high risk operations that can modify your data.

## Try it out risk levels

The "try it out" feature uses four risk levels, which control the warnings and restrictions that you encounter when testing endpoints directly from the documentation.

| Risk level | "Try it out" allowed | Warning dialog | Warning banner | Cookie attachment |
| --- | --- | --- | --- | --- |
| Low | ✅ | No | Yes | Yes |
| Medium | ✅ | Yes (per endpoint, per session) | Yes | Yes |
| High | ✅ | Yes (per endpoint, per session) | Yes | Yes (after accepting second warning dialog) |
| Critical | ❌ | N/A | N/A | N/A |

- **Low risk** endpoints primarily retrieve publicly available information and have minimal impact on your data or games. These endpoints show a simple informational banner when using "try it out."
- **Medium risk** endpoints can create, update, or access private information. Most changes you make from these endpoints can be reversed using other available endpoints. These endpoints have the following "try it out" safety measures:
  - They display a confirmation dialog before you send a request. This dialog appears once per endpoint per browser session.
  - They show a warning banner to remind you of the risk level.
- **High risk** endpoints can modify or delete private information in ways that may be difficult or impossible to reverse. This category includes most DELETE operations and other potentially destructive actions. In addition to the confirmation dialog and warning banner from medium risk endpoints, a second confirmation dialog is required to send the first request (enforced only per session, not per endpoint).
- **Critical risk** endpoints access or modify highly sensitive data that could compromise account security or privacy. "Try it out" is disabled for these endpoints.
