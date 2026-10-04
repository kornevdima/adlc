# Exploring CQRS and Event Sourcing (notes)

Source: Microsoft patterns & practices, 2012.

The CQRS pattern and the event sourcing pattern are frequently combined, but neither requires the other. Several bounded contexts in the reference implementation use CQRS with a conventional relational store. Apply CQRS selectively, per bounded context, where read and write requirements diverge.
