# 50k Row Migration — SOP

- Project: CRM Data Migration + Cleanup
- Status: implemented
- Owner: Hansel Davis
- Contact: hansel.davis62@gmail.com

## Problem
Client CSV had inconsistent formats, duplicate contacts, missing fields, and the new CRM rejected bulk import.

## Outcome
Produced CSV that passed CRM import in under 48 hours.

## Quantitative outcome
- Migration went from estimated 2 weeks → 48 hours
- Duplicate records resolved through candidate surfacing
- Data accuracy: 99.8%

## Recurrence / cadence
- One-time migration with post-import validation pass
- Ongoing: repeat cleanup on each weekly export

## Platforms / tools
- Source: CSV export from old system
- Processing pipeline: CSV normalization + fuzzy matching + rules
- Destination: CRM import + staging validation file

## Triggers
- Source CSV export available
- CRM import error feedback
- Operator validation signoff

## Fallback behavior
- Unresolved rows exported to quarantine file
- Quarantine rows reviewed by operator before second pass
- Import rollback plan documented

## Handoff
- Quarantine workflow in repo
- Validation checklist in `checks.md`
- Operator handles exceptions, not automation

## Proof
- See: `logic.md`
- See: `checks.md`
- See demo: `/projects/migration/index.html#demo`
