# SEC-305: Optimize N+1 Queries in Product Catalog

**Status:** In Progress · **Priority:** Medium
**Sprint:** Sprint 32 · **Story Points:** 5
**Reporter:** Performance Team · **Assignee:** You (Intern)
**Labels:** `performance`, `sql`, `python`, `maintenance`
**Task Type:** Maintenance

---

## Description

The product catalog page takes 6 seconds to load because of N+1 query problems.
For each of 100 products, it makes a separate query to get reviews and a separate
query to get the category. That's 201 queries instead of 3.

Fix the code to use JOINs or batch queries instead.

## Acceptance Criteria

- [ ] Uses 3 or fewer queries (not 201)
- [ ] Same output as before
- [ ] Response time under 100ms
- [ ] All tests pass
