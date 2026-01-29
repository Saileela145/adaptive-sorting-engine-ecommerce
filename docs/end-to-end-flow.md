# End-to-End Flow of the Adaptive Sorting System

## 1. Scenario Description
Consider an e-commerce platform where a user searches for smartphones
and selects the option "Sort by Price: Low to High".

The system must display the sorted product list efficiently while
handling a large and dynamic dataset.

---

## 2. Step-by-Step Flow

### Step 1: User Request
The user selects a sorting option from the product listing page.
The request is sent to the sorting system.

Example:
- Sorting key: Price
- Order: Low to High

---

### Step 2: Product Data Retrieval
The system retrieves the relevant product data from the database or cache.
This includes prices, ratings, and other attributes.

---

### Step 3: Data Characteristics Analysis
The data analyzer examines the retrieved data and identifies:
- Large dataset size
- Mostly unsorted price values
- High number of duplicate prices
- Low frequency of updates

---

### Step 4: Strategy Selection
Based on the analyzed data, the decision logic applies its rules:
- Large dataset → efficient strategy
- High duplicates → duplicate-aware strategy

The system selects the most suitable sorting strategy.

---

### Step 5: Sorting Execution
The sorting execution module applies the selected strategy to the product data
and generates the sorted product list.

---

### Step 6: Display to User
The sorted product list is sent back to the user interface and displayed
in ascending order of price.

---

## 3. Outcome
The user receives a correctly sorted product list with minimal delay.
The system avoids unnecessary overhead by adapting to real-time data conditions.
