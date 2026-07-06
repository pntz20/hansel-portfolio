# AI Ticket Classifier — Flow / Rules

## High-level flow
1. Receive ticket text
2. Extract signals: urgency, topic, customer tier
3. Classify: category + priority
4. Create structured task in project tool
5. If allowed: send templated auto-reply
6. Log confidence + review outcome

## Category map
- auth, billing, incident, feature, general

## Priority map
- high: outage, payment failure, security signal
- standard: questions, requests, low urgency

## Human review conditions
- Confidence below configured threshold
- Sensitive keywords
- Customer tier VIP
