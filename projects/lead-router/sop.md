# Lead Router — SOP

- Project: Lead Response Router
- Status: implemented
- Owner: Hansel Davis
- Contact: hansel.davis62@gmail.com

## Problem
Incoming form entries sat in email until someone manually triaged and assigned.

## Outcome
Automatic routing with instant notification and no dropped leads.

## Quantitative outcome
- Response from 5 hours → ~90 seconds
- Saved: ~15 min daily per agent
- Lead miss rate: 0%

## Recurrence / cadence
- Real-time on every form submit
- Weekly routing rule review
- Monthly channel audit

## Platforms / tools
- Intake: form
- Rules engine: dedicated automation platform
- Notify: Slack, SMS, email
- Fallback: delayed channel + escalation rule

## Triggers
- New form entry
- Priority field change
- Assignment override by operator

## Fallback behavior
- If owner unavailable in 60s: route to backup owner
- If both unavailable: queue for urgent review + send ops alert

## Handoff
- Operator owns routing table
- Channel maps live in logic.md
- On-call knows escalation path

## Proof
- See: `logic.md`
- See: `checks.md`
- See demo: `/projects/lead-router/index.html#demo`
