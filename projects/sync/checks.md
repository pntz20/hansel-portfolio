# Multi-Platform Sync — Validation / QA Checklist

## Setup
- [ ] Each source has mapped event schema
- [ ] Composite key chosen: avoids false dedupe
- [ ] Idempotency key set for retries

## Behavior checks
- [ ] Form submit creates master record
- [ ] CRM update overwrites same record
- [ ] Failed sync does not create duplicates
- [ ] Retry succeeds within 3 attempts
- [ ] Ops alert received on failure

## Data checks
- [ ] 7-day sample: zero duplicate master records
- [ ] All required fields populated for CRM import
- [ ] Timestamps monotonic

## Handoff completeness
- [ ] Operator has read access to logs
- [ ] On-call knows retry queue location
- [ ] Revert plan documented
