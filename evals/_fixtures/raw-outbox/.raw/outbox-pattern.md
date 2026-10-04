# The transactional outbox pattern

Problem: a service must update its database and publish a message, but a distributed transaction across the database and the broker is not available.

Solution: write the message into an OUTBOX table in the same local transaction as the business change. A separate relay (polling publisher or change data capture on the outbox table) reads new rows and publishes them to the broker, then marks them sent.

Consequences:
- At-least-once delivery: consumers must be idempotent (see the idempotent consumer pattern).
- Ordering is preserved per aggregate if the relay publishes in commit order.
- Often combined with sagas, where each saga step emits its event through the outbox.

Source: Chris Richardson, microservices.io, "Pattern: Transactional outbox".
