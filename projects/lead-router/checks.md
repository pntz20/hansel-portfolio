# Lead Router — Validation / QA Checklist

## Setup
- [ ] Routing map documented per region
- [ ] Backup owner defined per route
- [ ] Notification templates reviewed
- [ ] Escalation path documented

## Behavior checks
- [ ] New lead routes instantly
- [ ] High-priority uses expected channel
- [ ] Standard route respects business hours if configured
- [ ] Fallback/retry counts visible in logs

## Reporting checks
- [ ] Weekly lead count matches CRM intake
- [ ] Response percentile matches notification latency
- [ ] Escalation log reviewed for false alerts
