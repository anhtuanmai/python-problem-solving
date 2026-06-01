# 🎯 Domain Design Challenge: Event Ticketing Platform

**Duration:** 3 hours
**Language:** Kotlin

---

## 🧭 Context

A ticketing company wants to digitise the management of live events.
They need a system that handles venues, events, seat reservations, and booking lifecycles.
Your job is to design and implement the core domain from scratch.

> **Ubiquitous Language:** *Event*, *Venue*, *Seat*, *Booking*, *Customer*, *Reservation*, *Capacity*

---

## 📋 Business Requirements

### Venues
- A venue has a name and a fixed seating capacity.
- A venue with zero or negative capacity is not valid.

### Events
- An event takes place in a venue on a specific date, has a title and a ticket price.
- An event starts as a **Draft** and must be explicitly **Published** before any booking can happen.
- An event that has no available seats cannot be published.
- When all seats are taken, the event automatically becomes **Sold Out**.
- An event can be **Cancelled** at any time, regardless of its current state.
- Once cancelled, an event cannot transition to any other state.

### Customers
- A customer has a name and an email address.
- An email address must be valid.

### Seats
- Each seat is identified by a row letter and a seat number (e.g. `A12`, `C3`).
- Seat numbers range from 1 to 50.

### Bookings
- A booking associates a customer with a specific seat at a specific event.
- A booking can only be made for a **Published** event.
- Only available seats can be booked.
- A new booking starts as **Pending**.
- A pending booking can be **Confirmed**.
- A booking can be **Cancelled** with a reason:
    - A pending booking can be cancelled at any time.
    - A confirmed booking can only be cancelled within **24 hours** of its creation.
- When a booking is cancelled on a **Sold Out** event, that seat becomes available again
  and the event returns to **Published**.

### Money
- Prices are represented with an amount and a currency (e.g. `EUR`, `USD`).
- Amounts cannot be negative.
- Adding two amounts in different currencies is not allowed.

---

## ✅ Expected Deliverables

1. A **domain model** with all relevant entities, value objects, and aggregate roots.
2. **Repository interfaces** (no implementation technology required — in-memory is fine).
3. An **application service** exposing at minimum two use cases:
    - Book a seat for a customer.
    - Cancel an existing booking.
4. **Unit tests** covering the business rules above, including all edge cases and invalid states.

---

## 🏆 Evaluation Criteria

| Criterion         | Weight | Description                                                       |
|-------------------|--------|-------------------------------------------------------------------|
| **Correctness**   | 35%    | All business rules are enforced, no silent failures               |
| **Domain purity** | 20%    | Domain layer has no infrastructure or framework dependencies      |
| **Kotlin idioms** | 20%    | Idiomatic use of the Kotlin type system to express domain concepts |
| **Test coverage** | 15%    | Edge cases and invalid states are tested                          |
| **Code clarity**  | 10%    | Naming reflects the ubiquitous language                           |

---

## ⚡ Bonus (if you finish early)

- **Bonus A:** Customers can join a waiting list for a Sold Out event and are automatically
  offered a seat when a booking is cancelled.
- **Bonus B:** Support pluggable pricing policies, such as early-bird discounts or
  last-minute surcharges.
