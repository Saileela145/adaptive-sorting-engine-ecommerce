# System Architecture

## 1. Overview
The Adaptive Real-World Sorting Engine is designed to efficiently sort
e-commerce product listings such as price, rating, and date.
Instead of using a single fixed sorting algorithm, the system dynamically
selects the most suitable sorting strategy based on real-time data characteristics.

This approach improves performance and scalability for large and dynamic
e-commerce platforms.

---

## 2. High-Level Architecture Diagram

User Request  
↓  
Product Data Source  
↓  
Data Analyzer  
↓  
Sorting Strategy Selector  
↓  
Sorting Execution Engine  
↓  
Sorted Product List  

---

## 3. Module Description

### 3.1 User Request Module
This module handles user interactions such as selecting sorting options
(e.g., sort by price, rating, or newest products).

### 3.2 Product Data Module
This module stores and retrieves product information including price,
rating, and date of addition from the database or cache.

### 3.3 Data Analyzer Module
This module analyzes the product data before sorting.
It checks data size, level of sortedness, number of duplicate values,
and frequency of updates.

### 3.4 Sorting Strategy Selector
Based on the analysis results, this module decides which sorting strategy
is most suitable for the current data.

### 3.5 Sorting Execution Module
This module applies the selected sorting strategy and generates the
final sorted product list to be displayed to the user.
