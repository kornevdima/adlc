# Choreography-based sagas

Each service publishes a domain event when its local transaction completes; other services subscribe and run their own step. There is no central coordinator. Compensation is triggered by failure events. Events must be published reliably, which is why choreography is usually built on the transactional outbox.

Source: microservices.io, "Pattern: Saga".
