# 50k Row Migration — Validation / QA Checklist

## Setup
- [ ] Raw export preserved as archive before processing
- [ ] CRM import spec confirmed (headers, required fields, max row count)
- [ ] Thresholds set: phone min length, name min length, required fields

## Behavior checks
- [ ] Clean output row count equals normalized unique count
- [ ] No duplicate keys in output
- [ ] No invalid phone length rows in clean output
- [ ] Quarantine file created when source contains errors

## Import checks
- [ ] Sample first import accepted
- [ ] Full import accepted
- [ ] Post-import sample checked for content fidelity

## Rollback / safety
- [ ] Archive of raw and clean files kept for verification
- [ ] Import confirmation saved
