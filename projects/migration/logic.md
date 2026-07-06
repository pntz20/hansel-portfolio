# 50k Row Migration — Flow / Rules

## High-level flow
1. Load raw export
2. Normalize per-field:
   - Name: trim, collapse spaces, title case
   - Phone: digits only, E.164 candidate
   - State/region: uppercase, short form
3. Build composite key for identity
4. Fuzzy match against existing CRM contacts
5. Route:
   - unique → insert candidate
   - probable match → operator review queue
   - invalid → quarantine
6. Validate required fields before export

## De-dup logic
- Candidate: normalized name + phone
- False-positive risk: shared household phones
- Mitigation: operator review for high-similarity matches

## Validation rules
- Required: name, phone OR email
- Phone length rule: if numeric digits < 7, quarantine
- State length rule: max 2 chars after normalization

## Export format
- Clean CSV headers match CRM import spec
- Quarantine file has review columns: reason, original row, normalized row
