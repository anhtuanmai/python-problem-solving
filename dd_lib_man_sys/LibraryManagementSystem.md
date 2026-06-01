# Domain Design Challenge: Library Management System

## Context

A library manages a collection of books that members can borrow.
Each book can have multiple physical copies. A member can borrow up to
3 books at a time. A borrowed book must be returned within 14 days,
after which a daily late fee of €0.50 is applied. Members with unpaid
fees exceeding €5.00 are suspended and cannot borrow new books.

## Requirements

Model the domain to support the following operations:

1. Register a new member
2. Add a book (with one or more copies) to the library catalog
3. Borrow a book — find an available copy and assign it to a member
4. Return a book — mark the copy as available and calculate any late fee
5. Pay outstanding fees for a member
6. Query all currently borrowed books for a given member
7. Query all overdue loans across the entire library

## Constraints

- All business rules must be enforced within the domain model itself,
  not in a service or controller layer
- No frameworks, no persistence layer — pure domain logic only
- Use Kotlin idioms: data classes, sealed classes, value classes,
  and result/error handling as you see fit
- Side effects (e.g., sending notifications) must be represented in
  the return type, not executed directly
- The current date must be injected, not accessed via
  `System.currentTimeMillis()` or `LocalDate.now()`

## Deliverable

Provide the complete domain model with all entities, value objects,
domain rules, and use case logic. Include unit tests for at least
4 business rules.
