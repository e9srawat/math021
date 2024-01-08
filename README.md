# Problem No. 21

## Amicable Numbers

Let $d(n)$ be defined as the sum of proper divisors of $n$ (numbers less than $n$ which divide evenly into $n$).

If $d(a) = b$ and $d(b) = a$, where $a \ne b$, then $a$ and $b$ are an amicable pair and each of $a$ and $b$ are called amicable numbers.

For example, the proper divisors of $220$ are $1, 2, 4, 5, 10, 11, 20, 22, 44, 55$ and $110$; therefore $d(220) = 284$. The proper divisors of $284$ are $1$, $2$, $4$, $71$ and $142$; so $d(284) = 220$.

## Part A

Evaluate the sum of all the amicable numbers under $10000$.

Update the function `answer()` in `solution.py` with your solution.

## Part B

Generalize the solution in Part A to evaluate the sum of all amicable numbers that lie inside the range `p` and `q`, inclusive.

Update the function `solver()` in `solution.py` with your generalized solution.

```python
solver(n: int)
```

## Instructions

Create a new directory in your math problem repo (math) called `math021`

Copy README.md and solution.py into `math021`

Share your solution by updating `answer()` and `solver()` in solution.py.

```
math021
├── README.md
└── solution.py
``` 

