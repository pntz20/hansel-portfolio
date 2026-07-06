# Lead Router — Flow / Rules

## High-level flow
1. Form submitted
2. Read: source, location, priority, product interest
3. Match owner by region/rule map
4. Select main channel + fallback
5. Send notification with lead context
6. Track response latency

## Routing rules
- Priority = high → SMS + Slack → notify within 90 seconds
- Priority = standard → Slack channel → ~2 minutes
- Fallback: if owner unavailable in 60s → backup owner
- Final fallback: ops alert + queue

## Notification format
- Lead name, location, priority
- Key property or budget signal
- Quick reply template link

## Metrics
- Time to first response by lead
- Notify success/failure by channel
- Escalation rate
