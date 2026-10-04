# Idempotent consumer

Message brokers and outbox relays deliver at least once, so a consumer can see the same message twice. An idempotent consumer records the IDs of processed messages (in the same transaction as its own state change) and discards duplicates.

Source: microservices.io, "Pattern: Idempotent Consumer".
