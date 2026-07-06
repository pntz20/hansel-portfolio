# Multi-Platform Sync — Flow / Rules

## High-level flow
1. Event emitted from source
2. Normalize to master schema
3. Dedupe by external ID or composite key
4. Write to master store
5. Push change to CRM + notify Slack/email
6. Log success/failure

## Routing logic
- Source = form → create contact → notify owner
- Source = crm status change → update owner + notify ops
- Source = internal system → audit log + reconciliation flag

## Error behavior
- On failure: queue retry, send ops alert
- After 3 failures: pause queue, notify ops to review schema drift

## Monitoring signals
- Events processed/min
- Failure rate
- P95 latency from trigger to master write
