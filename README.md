# Python Programming Practical -- Project Audit

## Student Details

  Field                           Details
  ------------------------------- ----------------------------------------------------------------------
  Student Name                    ummadisetti bhargav siva sankar
  Roll Number / Register Number   26001358\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Department                      csm
  Class / Year / Semester         \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Subject                         \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Subject Code                    \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Institution / College           \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Faculty Name                    \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Date of Submission              \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

------------------------------------------------------------------------

## Project Overview

This project contains **10 Python programming cases**. Each case
demonstrates the use of Python data structures, loops, conditional
statements, calculations, and validation techniques to solve a practical
problem.

### Objectives

-   Practise Python programming using lists, tuples, and dictionaries.
-   Apply conditional statements and loops to real-world scenarios.
-   Validate input data and identify invalid or duplicate records.
-   Perform calculations and generate meaningful summaries.
-   Develop logical thinking and problem-solving skills.

------------------------------------------------------------------------

# Case 1 -- Bank Transaction Validation

### Objective

Validate a list of bank transactions by identifying duplicate
transaction IDs and invalid transaction amounts. The program also checks
for suspicious transaction sequences.

### Input Data

Each transaction is represented as a tuple containing:

`(Transaction ID, Amount, Transaction Type)`

Example data:

``` python
transactions = [
    (101, 500, "Deposit"),
    (102, 200, "Withdraw"),
    (101, 300, "Deposit"),
    (103, -100, "Withdraw"),
    (104, 700, "Deposit")
]
```

### Logic and Python Concepts

1.  Store transaction IDs already encountered in a list.
2.  Check whether the current transaction ID has appeared before.
3.  Display a duplicate warning when an ID is repeated.
4.  Check whether the transaction amount is less than or equal to zero.
5.  Examine consecutive transactions for suspicious sequences.

**Concepts used:** Lists, tuples, `for` loops, `if-else`, membership
testing, and validation.

### Observed Output

``` text
101 Duplicate transaction ID
103 Invalid amount
Suspicious sequences:
```

No suspicious sequence was reported in the displayed execution.

### Audit Notes

-   The duplicate transaction ID `101` is correctly identified.
-   Transaction `103` is correctly flagged because its amount is
    negative.
-   The displayed output does not show any suspicious sequence.
-   Consider using a `set` for faster duplicate-ID checks.
-   In a real banking application, transaction types, IDs, and amounts
    should all be validated, and suspicious-sequence rules should be
    clearly defined.

**Audit status:** Basic duplicate and amount validation demonstrated.

------------------------------------------------------------------------

# Case 2 -- Balanced Student Score Grouping

### Objective

Divide student scores into groups of a fixed size while attempting to
balance the total scores of each group.

### Input Data

``` python
scores = [80, 60, 90, 70, 85, 65]
group_size = 2
```

### Logic and Python Concepts

1.  Sort the scores in descending order.
2.  Create the required number of empty groups.
3.  Maintain a running total for each group.
4.  Assign each score to the group with the smallest current total,
    provided that the group has space.
5.  Display each group and its total score.

**Concepts used:** Lists, nested lists, sorting, loops, `min()`,
`index()`, and list methods.

### Observed Output

``` text
Group 1 : [90, 60]
Total score: 150

Group 2 : [85, 65]
Total score: 150

Group 3 : [80, 70]
Total score: 150
```

### Audit Notes

-   All six scores are allocated.
-   Each group contains two scores.
-   All groups have an equal total of 150.
-   The program demonstrates a greedy balancing strategy.
-   This strategy is useful for basic grouping, but it does not
    guarantee an optimal solution for every possible score list.
-   Validate that `group_size` is greater than zero and that the input
    list is not empty.

**Audit status:** All groups are filled and balanced for the supplied
data.

------------------------------------------------------------------------

# Case 3 -- Shop Inventory and Sales Management

### Objective

Process customer orders, check available stock, calculate bills, update
inventory, and calculate total sales.

### Input Data

``` python
stock = {
    "Burger": 10,
    "Pizza": 5,
    "Juice": 8
}

price = {
    "Burger": 50,
    "Pizza": 100,
    "Juice": 30
}

orders = [
    ("Burger", 2),
    ("Pizza", 1),
    ("Juice", 3),
    ("Pizza", 6)
]
```

### Logic and Python Concepts

1.  Read each item and its requested quantity.
2.  Check whether the item exists in the stock dictionary.
3.  Ensure that the quantity is positive and does not exceed available
    stock.
4.  Calculate the bill using price multiplied by quantity.
5.  Reduce the stock after a successful order.
6.  Add the bill to total sales.
7.  Reject invalid or unavailable orders.

**Concepts used:** Dictionaries, tuples, loops, conditional statements,
arithmetic operations, and dictionary updates.

### Observed Output

``` text
Burger Bill: 100
Pizza Bill: 100
Juice Bill: 90
Pizza Order rejected

Total sales: 290
Remaining stock: {'Burger': 8, 'Pizza': 4, 'Juice': 5}
```

### Audit Notes

-   The first three orders are processed successfully.
-   The final Pizza order is rejected because six units were requested
    while only four remained.
-   Total sales of 290 are correct.
-   Inventory is updated after each successful order.
-   Consider handling unknown products and invalid quantities with
    clearer error messages.
-   For real applications, also validate that prices and stock
    quantities are non-negative.

**Audit status:** Order validation, billing, and stock updates work
correctly for the supplied data.

------------------------------------------------------------------------

# Case 4 -- Library Book Fine Calculation

### Objective

Calculate overdue fines for returned library books and track the number
of available books.

### Input Data

``` python
books = [
    ("B101", 5, 8),
    ("B102", 7, 7),
    ("B103", 4, 10),
    ("B104", 6, 9)
]

available = 4
fine_per_day = 5
total_fine = 0
```

Each tuple contains:

-   Book ID
-   Allowed borrowing period
-   Actual return period

### Logic and Python Concepts

1.  Calculate the delay by subtracting the allowed period from the
    actual return period.
2.  If the delay is greater than zero, calculate the fine.
3.  Add the fine to the total fine.
4.  Display whether the book was returned on time or late.
5.  Increase the available book count for each returned book.

**Concepts used:** Lists, tuples, loops, conditional statements,
arithmetic operations, and accumulators.

### Observed Output

``` text
B101 Overdue days: 3 Fine: 15
B102 Returned on time
B103 Overdue days: 6 Fine: 30
B104 Overdue days: 3 Fine: 15

Total fine: 60
Available books: 8
```

### Audit Notes

-   The fine for each overdue book is calculated correctly.
-   The total fine is 60.
-   Book B102 is correctly identified as returned on time.
-   The available count increases from 4 to 8.
-   The program assumes that all four records represent books that have
    been returned. A real library system should track each book's
    checkout and return status to prevent double-counting.
-   Consider handling negative or invalid borrowing periods.

**Audit status:** Fine calculation and basic availability tracking
demonstrated.

------------------------------------------------------------------------

# Case 5 -- Bus Requirement and Passenger Allocation

### Objective

Calculate the number of buses required for different routes based on
passenger counts and fixed bus capacity.

### Input Data

``` python
routes = [
    ("Route A", 120),
    ("Route B", 85),
    ("Route C", 200)
]

capacity = 50
```

### Logic and Python Concepts

1.  Calculate the initial number of buses using integer division.
2.  Check whether any passengers remain after allocating full buses.
3.  Add one additional bus if there is a remainder.
4.  Calculate the number of passengers served.
5.  Calculate unserved passengers.
6.  Maintain totals for all routes.

**Concepts used:** Lists, tuples, loops, integer division (`//`), modulo
(`%`), conditional statements, and accumulators.

### Observed Output

``` text
Route A Buses needed: 3
Unserved passengers: 0

Route B Buses needed: 2
Unserved passengers: 0

Route C Buses needed: 4
Unserved passengers: 0

Total buses: 9
Total unserved: 0
```

### Audit Notes

-   Route A requires three buses.
-   Route B requires two buses.
-   Route C requires four buses.
-   All passengers can be accommodated.
-   The total requirement is nine buses.
-   The calculation correctly accounts for partially filled final buses.
-   Validate that bus capacity is greater than zero and passenger counts
    are non-negative.

**Audit status:** Bus allocation calculations are correct for the
supplied data.

------------------------------------------------------------------------

# Case 6 -- Production Quality and Defect Analysis

### Objective

Calculate defect percentages for different products and identify whether
each product exceeds the permitted quality threshold.

### Input Data

``` python
products = ["Product A", "Product B", "Product C"]

production = [
    [100, 200, 150],
    [5, 30, 10]
]

threshold = 10
```

The first row contains production quantities, and the second row
contains defective units.

### Logic and Python Concepts

1.  Iterate through the product list using its index.

2.  Retrieve the total production and defective units.

3.  Calculate the defect percentage.

    `Defect Percentage = (Defective Units / Total Production) * 100`

4.  Round the percentage to two decimal places.

5.  Compare the result with the threshold.

6.  Display whether the quality threshold has been exceeded.

**Concepts used:** Lists, nested lists, indexing, loops, arithmetic
operations, `round()`, and conditional statements.

### Observed Output

``` text
Product A
Production: 100
Defective units: 5
Defect percentage: 5.0 %
Quality acceptable

Product B
Production: 200
Defective units: 30
Defect percentage: 15.0 %
Quality threshold exceeded

Product C
Production: 150
Defective units: 10
Defect percentage: 6.67 %
Quality acceptable
```

### Audit Notes

-   Product A has a defect rate of 5%.
-   Product B has a defect rate of 15% and exceeds the threshold.
-   Product C has a defect rate of 6.67%.
-   The calculations are correct.
-   The program uses `>` for threshold comparison, meaning a defect
    percentage exactly equal to 10% is considered acceptable.
-   Validate that production is greater than zero and defective units
    are not greater than total production.

**Audit status:** Defect calculations and threshold classification work
correctly for the supplied data.

------------------------------------------------------------------------

# Case 7 -- Seat Allocation Validation

### Objective

Validate seat or student roll-number allocations by identifying empty
seats, reserved seats, invalid allocations, and duplicate roll numbers.

### Input Data

``` python
seats = [
    [101, 102, 0],
    [103, 104, 105],
    [101, -1, 106]
]

reserved = [-1]
```

### Logic and Python Concepts

1.  Iterate through each row of the seat allocation list.
2.  Check whether a seat is empty (`0`).
3.  Identify reserved seats (`-1`).
4.  Identify invalid negative allocations.
5.  Check whether a roll number already exists.
6.  Count valid unique student allocations.

**Concepts used:** Nested lists, nested loops, membership testing,
conditional statements, and counters.

### Observed Output

``` text
Duplicate roll number: 101
Reserved seat

Empty seats: 1
Invalid allocations: 1
Valid students: 6
```

### Audit Notes

-   Roll number 101 is correctly identified as a duplicate.
-   The reserved seat is identified.
-   One empty seat is counted.
-   One invalid allocation is counted.
-   Six unique valid student roll numbers are identified.
-   Ensure that reserved seats and other invalid negative values are
    treated separately.
-   A set can be used to track unique roll numbers more efficiently.

**Audit status:** Duplicate, empty, reserved, and invalid allocation
checks are demonstrated.

------------------------------------------------------------------------

# Case 8 -- Area-wise Demand and Supply Shortage

### Objective

Compare demand and supply across different areas, calculate shortages,
and identify the most underserved area.

### Input Data

``` python
areas = ["Area A", "Area B", "Area C"]

demand = [
    [100, 120, 110],
    [150, 130, 140],
    [90, 100, 95]
]

supply = [
    [90, 100, 100],
    [120, 100, 120],
    [90, 90, 80]
]
```

### Logic and Python Concepts

1.  Iterate through each area.
2.  Calculate total demand using `sum()`.
3.  Calculate total supply using `sum()`.
4.  Find the shortage by subtracting supply from demand.
5.  Set negative shortages to zero because surplus is not a shortage.
6.  Store or compare the shortage values.
7.  Identify the area with the highest shortage.

**Concepts used:** Lists, nested lists, loops, `sum()`, conditional
statements, and maximum-value comparison.

### Observed Output

``` text
Area A
Demand: 330
Supply: 290
Shortage: 40

Area B
Demand: 420
Supply: 340
Shortage: 80

Area C
Demand: 285
Supply: 260
Shortage: 25

Most underserved area: Area B
```

### Audit Notes

-   Area A has a shortage of 40.
-   Area B has a shortage of 80.
-   Area C has a shortage of 25.
-   Area B is correctly identified as the most underserved area.
-   The program prevents negative shortage values.
-   Consider displaying surplus separately rather than simply converting
    it to zero.
-   Validate that demand and supply lists have matching dimensions.

**Audit status:** Area-wise shortage calculations and comparison are
correct for the supplied data.

------------------------------------------------------------------------

# Case 9 -- Product Price Fluctuation Analysis

### Objective

Calculate percentage changes in product prices and identify products
that exceed a specified fluctuation threshold.

### Input Data

``` python
products = ["Pen", "Book", "Bag"]

prices = [
    [10, 50, 500],
    [12, 45, 600],
    [15, 60, 550]
]

threshold = 20
```

The first row represents the old prices, and the last row represents the
latest prices.

### Logic and Python Concepts

1.  Iterate through each product.

2.  Retrieve its old and latest prices.

3.  Calculate the percentage change.

    `Percentage Change = ((New Price - Old Price) / Old Price) * 100`

4.  Store the absolute percentage change for comparison.

5.  Display the price change.

6.  Identify whether the absolute change exceeds the threshold.

7.  Find the product with the maximum fluctuation.

**Concepts used:** Lists, nested lists, indexing, loops, arithmetic
operations, `abs()`, `round()`, and maximum-value comparison.

### Observed Output

``` text
Pen
Price change: 50.0 %
Threshold exceeded

Book
Price change: 20.0 %
Within threshold

Bag
Price change: 10.0 %
Within threshold

Maximum fluctuation: Pen
```

### Audit Notes

-   Pen has a 50% price increase.
-   Book has a 20% price increase.
-   Bag has a 10% price increase.
-   Pen has the maximum fluctuation.
-   The threshold condition uses `>`; therefore, a change exactly equal
    to 20% is considered within the threshold.
-   Using the absolute percentage change correctly considers both
    increases and decreases.
-   Validate that the old price is greater than zero to avoid division
    by zero.

**Audit status:** Price-change calculations and maximum fluctuation
identification are correct.

------------------------------------------------------------------------

# Case 10 -- Student Course Registration Validation

### Objective

Validate student course registrations by identifying duplicate
registrations and invalid course names.

### Input Data

``` python
registrations = [
    ("S101", "Python"),
    ("S102", "Java"),
    ("S101", "Python"),
    ("S103", "Advanced Python"),
    ("S104", "Java")
]

valid_courses = ["Python", "Java", "Math"]
```

### Logic and Python Concepts

1.  Read each student ID and course name.
2.  Create a registration record as a tuple.
3.  Check whether the record already exists.
4.  Display a duplicate warning if the record is repeated.
5.  Add unique records to the list of seen registrations.
6.  Check whether the course exists in the valid course list.
7.  Display valid unique registrations.

**Concepts used:** Lists, tuples, loops, conditional statements,
membership testing, and duplicate validation.

### Observed Output

``` text
Duplicate registration: ('S101', 'Python')
Invalid course: S103 Advanced Python

Valid unique registrations:
S101 Python
S102 Java
S104 Java
```

### Audit Notes

-   The duplicate registration for S101 in Python is identified.
-   Advanced Python is correctly flagged because it is not in the valid
    course list.
-   Three valid unique registrations are displayed.
-   A student may register for different valid courses because duplicate
    checking is based on the combination of student ID and course.
-   Consider checking student ID validity and preventing duplicate
    course registrations for the same student.

**Audit status:** Duplicate registration and invalid course checks work
correctly for the supplied data.

------------------------------------------------------------------------

# Overall Project Audit Summary

  -----------------------------------------------------------------------
  Case                    Practical Area          Main Result
  ----------------------- ----------------------- -----------------------
  1                       Bank Transactions       Duplicate ID and
                                                  invalid amount detected

  2                       Student Score Grouping  Three groups balanced
                                                  to 150 each

  3                       Shop Inventory          Total sales of 290

  4                       Library Management      Total fine of 60

  5                       Bus Allocation          Nine buses required

  6                       Quality Control         Product B exceeds the
                                                  10% threshold

  7                       Seat Allocation         Duplicate, reserved,
                                                  empty, and invalid
                                                  seats detected

  8                       Demand and Supply       Area B has the highest
                                                  shortage of 80

  9                       Price Fluctuation       Pen has the highest
                                                  fluctuation at 50%

  10                      Course Registration     Duplicate and invalid
                                                  course detected
  -----------------------------------------------------------------------

## General Strengths

-   All ten cases use practical problem-solving scenarios.
-   Python lists, tuples, and dictionaries are applied appropriately.
-   Loops and conditional statements are used to process records.
-   Calculations and validation checks are demonstrated.
-   Output messages make the results understandable.

## General Recommendations

1.  Validate input data before processing.
2.  Handle empty lists and invalid values.
3.  Use sets where efficient duplicate checking is required.
4.  Use meaningful variable names and comments.
5.  Separate business logic from output statements in larger programs.
6.  Test boundary cases, including zero, negative values, and empty
    data.
7.  Add exception handling where user input or external data is
    involved.

## Final Conclusion

The project demonstrates ten practical applications of Python
programming. It covers transaction validation, score grouping, inventory
management, library fines, transportation planning, quality control,
seat allocation, supply-demand analysis, price fluctuation, and course
registration.

The displayed outputs support the expected calculations and validation
results for the supplied sample data. Some additional input validation
and real-world business rules would make the programs more robust.

Overall, these exercises provide a useful foundation in Python
programming, logical reasoning, data handling, and problem-solving.

------------------------------------------------------------------------

## Faculty / Evaluation Details

  Field               Details
  ------------------- ----------------------------------------------------------------------------------------------
  Faculty Remarks     \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Marks Obtained      \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Maximum Marks       \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Faculty Signature   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Date                \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

------------------------------------------------------------------------

*End of README*
