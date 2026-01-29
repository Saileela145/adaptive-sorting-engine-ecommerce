# Sorting Strategy Decision Logic

## 1. Introduction
The decision logic is responsible for selecting the most suitable sorting
strategy based on real-time data characteristics.
Instead of hardcoding a single algorithm, the system uses a rule-based
decision process.

This approach makes the system adaptive and efficient.

---

## 2. Inputs to the Decision Logic
The decision logic receives the following inputs from the data analyzer:

- Data size (small, medium, large)
- Degree of sortedness (unsorted, partially sorted, nearly sorted)
- Duplicate value density (low or high)
- Sorting key type (price, rating, date)
- Frequency of updates (low or high)

---

## 3. Rule-Based Decision Approach
The system follows a set of predefined rules to select the sorting strategy.

### Rule 1: Small Dataset
If the data size is small, the system selects a simple comparison-based
sorting strategy due to low overhead.

---

### Rule 2: Large Dataset
If the data size is large and the data is mostly unsorted, the system selects
an efficient comparison-based strategy to ensure good performance.

---

### Rule 3: Nearly Sorted Data
If the data is already partially or nearly sorted, the system selects an
adaptive sorting strategy that takes advantage of existing order.

---

### Rule 4: High Duplicate Values
If many products share the same price or rating, the system selects a
duplicate-aware strategy to handle repeated values efficiently.

---

### Rule 5: Frequently Updated Data
If the data changes frequently due to new products or price updates, the
system selects an incremental or update-friendly strategy to avoid full
re-sorting.

---

## 4. Conflict Resolution
In cases where multiple rules apply, the system prioritizes:
1. Data size
2. Degree of sortedness
3. Update frequency

This ensures stable and predictable decision-making.

---

## 5. Output of Decision Logic
The output of this step is the selected sorting strategy, which is passed
to the sorting execution module.
