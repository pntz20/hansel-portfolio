# AI Ticket Classifier — SOP

- Project: AI Support Triage + Routing
- Status: implemented
- Owner: Hansel Davis
- Contact: hansel.davis62@gmail.com

## Problem
Support team manually spent 10+ hours/week tagging and routing customer emails.

## Outcome
Faster, consistent triage with human review for sensitive or low-confidence tickets.

## Quantitative outcome
- Saved: ~12 hours/week to strategic work
- First-response accuracy improved
- Human review load: reduced ~50%

## Recurrence / cadence
- Every incoming email/system event
- Weekly review of false positives/negatives
- Monthly prompt/rule calibration

## Platforms / tools
- Intake: email feed / system form
- Classification: AI classifier API
- Action layer: automation platform / webhook
- Task tool: project management tool
- Optional: customer-facing auto-reply for low-priority cases

## Triggers
- New support message
- Escalation keywords detected
- Threshold confidence change

## Fallback behavior
- Low confidence → human review queue
- High severity → notify owner regardless of confidence
- API failure → treat as unclassified; default to human queue

## Handoff
- Prompt/rules owned by operator
- Calibration examples logged per week
- Support agent can override classification in task tool

## Proof
- See: `logic.md`
- See: `checks.md`
- See demo: `/projects/aiclassifier/index.html#demo`
