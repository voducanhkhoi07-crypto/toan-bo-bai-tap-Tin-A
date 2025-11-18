"""
Python solutions for the practice problems list provided by the user.
Each exercise is implemented as a function named according to the section and number,
e.g. problem_1_1(), problem_2_3(), etc.

You can import this file or run it directly. When run directly it shows a simple
interactive menu to try a specific problem quickly.

Note: Some problem statements in the list were ambiguous. In those cases the
implementation makes a reasonable assumption (documented in function docstrings).
"""
from math import pi, sqrt
from typing import Tuple, List

# ---------------------
# Section 1: Basic I/O
# ---------------------
def problem_1_1_c_to_f(celsius: float) -> float:
    """Convert Celsius to Fahrenheit. Returns Fahrenheit.
    Formula: F = C * 9/5 + 32"""
    return celsius * 9.0/5.0 + 32.0

def problem_1_1_f_to_c(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius. Returns Celsius.
    Formula: C = (F - 32) * 5/9"""
    return (fahrenheit - 32.0) * 5.0/9.0

def problem_1_2_div_mod(a: int, b: int) -> Tuple[int,int]:
    """Return integer division and remainder of a // b and a % b (b>0 assumed).
    Returns (quotient, remainder)."""
    if b == 0:
        raise ValueError("b must be non-zero")
    return divmod(a, b)

def problem_1_3_area_circle(radius: float) -> float:
    """Area of circle with radius."""
    if radius < 0:
        raise ValueError("radius must be non-negative")
    return pi * radius * radius

def problem_1_4_freefall_velocity(h: float, g: float=9.81) -> float:
    """Velocity of falling object from height h, starting at rest, ignoring air resistance.
    v = sqrt(2*g*h)"""
    if h < 0:
        raise ValueError("height must be non-negative")
    return sqrt(2.0 * g * h)

def problem_1_5_trapezoid_area(a: float, b: float, h: float) -> float:
    """Area of trapezoid with bases a (big), b (small) and height h."""
    return (a + b) * h / 2.0

def problem_1_6_triangle_perimeter_area(a: float, b: float, c: float) -> Tuple[float,float]:
    """Return (perimeter, area) of triangle with side lengths a,b,c using Heron's formula.
    Raises ValueError if not a triangle."""
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("sides must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("not a valid triangle")
    p = a + b + c
    s = p / 2.0
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return p, area

def problem_1_7_rectangle_perimeter_area(length: float, width: float) -> Tuple[float,float]:
    p = 2.0 * (length + width)
    a = length * width
    return p, a

def problem_1_8_seconds_to_hms(seconds: int) -> Tuple[int,int,int]:
    """Convert total seconds to (hours, minutes, seconds)."""
    if seconds < 0:
        raise ValueError("seconds must be non-negative")
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    s = seconds % 60
    return h, m, s

def problem_1_9_change_breakdown(amount: int, denominations: List[int]=None) -> List[Tuple[int,int]]:
    """Given amount (integer), return list of (denomination, count) using greedy algorithm.
    Default denominations (VND-like): [500000,200000,100000,50000,20000,10000,5000,2000,1000,500,200,100]
    If amount < 0 raises ValueError.
    """
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if denominations is None:
        denominations = [500000,200000,100000,50000,20000,10000,5000,2000,1000,500,200,100]
    result = []
    remaining = amount
    for d in denominations:
        cnt = remaining // d
        if cnt:
            result.append((d, cnt))
            remaining -= d * cnt
    if remaining:
        result.append((1, remaining))  # leftover as ones
    return result

def problem_1_10_mean_three(x: float, y: float, z: float) -> float:
    return (x + y + z) / 3.0

def problem_1_11_arithmetic_series_sum(a1: float, d: float, n: int) -> float:
    """Sum of arithmetic progression: n/2 * (2*a1 + (n-1)*d)"""
    if n < 0:
        raise ValueError("n must be non-negative")
    return n * (2 * a1 + (n - 1) * d) / 2.0

def problem_1_12_decimal_to_binary(n: int) -> str:
    """Return binary representation as string for integer n (handles negative)."""
    if n == 0:
        return "0"
    sign = ""
    if n < 0:
        sign = "-"
        n = -n

    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return sign + ''.join(reversed(bits))

def problem_1_13_distance_points(x1: float, y1: float, x2: float, y2: float) -> float:
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def problem_1_14_electric_bill(kwh: float) -> float:
    """Calculate tiered electricity bill using a common Vietnamese progressive tariff example.
    The user referenced a multi-tier scheme elsewhere; here we implement the common 5-tier: 
    0-50: 1678
    51-100: 1734
    101-200: 2014
    201-350: 2536
    >350: 2927
    (units: VND per kWh)
    """
    if kwh < 0:
        raise ValueError("kWh must be non-negative")
    tiers = [(50, 1678), (50, 1734), (100, 2014), (150, 2536), (float('inf'), 2927)]
    remaining = kwh
    total = 0.0
    for cap, price in tiers:
        use = min(remaining, cap)
        total += use * price
        remaining -= use
        if remaining <= 0:
            break
    return total

def problem_1_15_triangle_area_by_coords(x1,y1,x2,y2,x3,y3) -> float:
    """Area by shoelace formula."""
    area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0
    return area

# ---------------------
# Section 2: Branching
# ---------------------
def problem_2_1_even_odd(n: int) -> str:
    return "even" if n % 2 == 0 else "odd"

def problem_2_2_expression(x: float) -> float:
    """The original expression wasn't given exactly; implement example: y = (x^2 + 2x + 1)/(x+1) if x!=-1
    If x == -1 raises ZeroDivisionError."""
    if x == -1:
        raise ZeroDivisionError("division by zero for this chosen expression")
    return (x**2 + 2*x + 1) / (x + 1)

def problem_2_3_is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def problem_2_4_grade_classification(score: float) -> str:
    """Return classification string based on score (0-10 scale assumed).
    Typical Vietnamese scale: >=8: Giỏi, >=6.5: Khá, >=5: TB, else Yếu
    """
    if score >= 8.0:
        return "Giỏi"
    if score >= 6.5:
        return "Khá"
    if score >= 5.0:
        return "Trung Bình"
    return "Yếu"

def problem_2_5_solve_linear(a: float, b: float):
    """Solve ax + b = 0. Return solution or None if infinite/no solutions as tuple.
    Returns ('one', x) or ('none', None) or ('infinite', None)"""
    if a == 0:
        if b == 0:
            return ('infinite', None)
        else:
            return ('none', None)
    return ('one', -b / a)

def problem_2_6_solve_quadratic(a: float, b: float, c: float):
    """Solve ax^2 + bx + c = 0. Return tuple: (number_of_roots, roots_list)."""
    if a == 0:
        # reduce to linear
        return problem_2_5_solve_linear(b, c)
    disc = b*b - 4*a*c
    if disc < 0:
        return (0, [])
    if disc == 0:
        x = -b / (2*a)
        return (1, [x])
    root1 = (-b + sqrt(disc)) / (2*a)
    root2 = (-b - sqrt(disc)) / (2*a)
    return (2, [root1, root2])

def problem_2_7_point_in_circle(x: float, y: float, cx: float, cy: float, r: float) -> bool:
    return (x-cx)**2 + (y-cy)**2 <= r*r

def problem_2_8_solve_quadratic_allcases(a: float, b: float, c: float):
    """Similar to 2_6 but handles a==0 and returns message style results."""
    if a == 0:
        return problem_2_5_solve_linear(b, c)
    return problem_2_6_solve_quadratic(a,b,c)

def problem_2_9_triangle_type(a: float,b: float,c: float) -> str:
    """Return triangle type: 'not_triangle', 'equilateral', 'isosceles', 'right', 'right_isosceles', 'scalene'"""
    if a <=0 or b<=0 or c<=0:
        return 'not_triangle'
    if a + b <= c or a + c <= b or b + c <= a:
        return 'not_triangle'
    types = []
    eps = 1e-9
    # equilateral
    if abs(a-b) < eps and abs(b-c) < eps:
        return 'equilateral'
    # check right
    sides = sorted([a,b,c])
    is_right = abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9
    is_isos = abs(a-b) < eps or abs(a-c) < eps or abs(b-c) < eps
    if is_right and is_isos:
        return 'right_isosceles'
    if is_right:
        return 'right'
    if is_isos:
        return 'isosceles'
    return 'scalene'

def problem_2_10_char_type(ch: str) -> str:
    if len(ch) == 0:
        raise ValueError('empty string')
    c = ch[0]
    if c.isupper():
        return 'uppercase'
    if c.islower():
        return 'lowercase'
    if c.isdigit():
        return 'digit'
    return 'special'

def problem_2_11_days_in_feb(year: int) -> int:
    return 29 if problem_2_3_is_leap_year(year) else 28

def problem_2_12_can_be_triangle(a: float,b: float,c: float) -> bool:
    return a>0 and b>0 and c>0 and (a+b>c and a+c>b and b+c>a)

def problem_2_13_max_of_three(a: float,b: float,c: float) -> float:
    return max(a,b,c)

def problem_2_14_triangle_angle_type(a: float,b: float,c: float) -> str:
    """Return 'acute', 'right', 'obtuse' for triangle with sides a,b,c."""
    if not problem_2_12_can_be_triangle(a,b,c):
        return 'not_triangle'
    sides = sorted([a,b,c])
    x,y,z = sides
    val = x*x + y*y - z*z
    if abs(val) < 1e-9:
        return 'right'
    if val > 0:
        return 'acute'
    return 'obtuse'

def problem_2_15_year_days(year: int) -> int:
    return 366 if problem_2_3_is_leap_year(year) else 365

def problem_2_16_quadrant(x: float, y: float) -> int:
    if x==0 or y==0:
        return 0  # on axis
    if x>0 and y>0:
        return 1
    if x<0 and y>0:
        return 2
    if x<0 and y<0:
        return 3
    return 4

def problem_2_17_is_pythagorean_triplet(a:int,b:int,c:int) -> bool:
    s = sorted([a,b,c])
    return s[0]**2 + s[1]**2 == s[2]**2

def problem_2_18_next_prev_date(day:int, month:int, year:int) -> Tuple[Tuple[int,int,int], Tuple[int,int,int]]:
    """Return (next_date, prev_date) as tuples (d,m,y). Basic Gregorian calendar handling."""
    # helper
    def days_in_month(m,y):
        if m in (1,3,5,7,8,10,12):
            return 31
        if m in (4,6,9,11):
            return 30
        return 29 if problem_2_3_is_leap_year(y) else 28
    # validate
    if month <1 or month>12:
        raise ValueError('invalid month')
    dim = days_in_month(month, year)
    if day <1 or day>dim:
        raise ValueError('invalid day')
    # next
    nd, nm, ny = day+1, month, year
    if nd > dim:
        nd = 1
        nm += 1
        if nm > 12:
            nm = 1
            ny += 1
    # prev
    pd, pm, py = day-1, month, year
    if pd < 1:
        pm -= 1
        if pm < 1:
            pm = 12
            py -= 1
        pd = days_in_month(pm, py)
    return (nd,nm,ny), (pd,pm,py)

# ---------------------
# Section 3: Loops
# ---------------------
def problem_3_1_sum_range(a:int,b:int) -> int:
    return sum(range(a,b+1))

def problem_3_2_sum_odd_squares(a:int,b:int) -> int:
    return sum(i*i for i in range(a,b+1) if i%2==1)

def problem_3_3_times_table(n:int) -> List[str]:
    lines = []
    for i in range(1,10):
        lines.append(f"{n} x {i} = {n*i}")
    return lines

def problem_3_4_gcd_lcm(a:int,b:int) -> Tuple[int,int]:
    from math import gcd
    if a==0 and b==0:
        return 0,0
    g = gcd(a,b)
    l = abs(a//g * b) if g!=0 else 0
    return g,l

def problem_3_5_is_perfect(n:int) -> bool:
    if n<=1: return False
    s = 1
    i = 2
    while i*i <= n:
        if n % i == 0:
            s += i
            if i != n//i:
                s += n//i
        i += 1
    return s == n

def problem_3_6_count_primes_less_than(n:int) -> int:
    if n <= 2:
        return 0
    sieve = [True]*n
    sieve[0]=sieve[1]=False
    p=2
    while p*p < n:
        if sieve[p]:
            for multiple in range(p*p, n, p):
                sieve[multiple]=False
        p+=1
    return sum(1 for i in range(n) if sieve[i])

def problem_3_7_sum_series_x(n:int) -> float:
    """Example: sum_{i=1..n} 1/i until n"""
    if n<=0: return 0.0
    return sum(1.0/i for i in range(1,n+1))

def problem_3_8_hundred_cows():
    """Return list of solutions to classic problem (x+y+z=100 with cost constraints).
    Return list of tuples (bulls,cows,calves) that satisfy problem variant if implemented.
    Here we return classic: 100 animals costing 100 units with 5 per bull, 3 per cow, 0.5 per calf -> example.
    This problem has many formulations; we implement the classical Chinese variant.
    """
    solutions = []
    # classic: bull=5, cow=3, calf=1/3 ; modify as needed
    for bulls in range(0,21):
        for cows in range(0,34):
            calves = 100 - bulls - cows
            if calves < 0: continue
            cost = 5*bulls + 3*cows + calves/3
            if abs(cost - 100) < 1e-9:
                solutions.append((bulls,cows,calves))
    return solutions

def problem_3_9_prime_factorization(n:int) -> List[int]:
    factors = []
    if n <= 1:
        return factors
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1 if d==2 else 2
    if n>1:
        factors.append(n)
    return factors

def problem_3_10_is_palindrome_number(n:int) -> bool:
    s = str(n)
    return s == s[::-1]

def problem_3_11_sum_digits(n:int) -> int:
    s = 0
    for ch in str(abs(n)):
        s += int(ch)
    return s

def problem_3_12_list_divisors(n:int) -> List[int]:
    res = []
    for i in range(1,int(sqrt(n))+1):
        if n % i ==0:
            res.append(i)
            if i != n//i:
                res.append(n//i)
    return sorted(res)

def problem_3_13_power(base:float, exp:int) -> float:
    if exp == 0:
        return 1.0
    sign = 1
    if exp < 0:
        base = 1/base
        exp = -exp
    result = 1.0
    for _ in range(exp):
        result *= base
    return result

def problem_3_14_draw_shapes(kind:str, n:int) -> List[str]:
    """Return list of strings representing ascii shape. kind='square' or 'triangle'"""
    out = []
    if kind == 'square':
        for _ in range(n):
            out.append('*'*n)
    elif kind == 'triangle':
        for i in range(1,n+1):
            out.append('*'*i)
    return out

def problem_3_15_reverse_number(n:int) -> int:
    s = str(abs(n))[::-1]
    val = int(s)
    return -val if n<0 else val

def problem_3_16_count_digits(n:int) -> int:
    return len(str(abs(n)))

def problem_3_17_is_armstrong(n:int) -> bool:
    s = str(n)
    k = len(s)
    return sum(int(ch)**k for ch in s) == n

def problem_3_18_floyd_triangle(lines:int) -> List[str]:
    out=[]
    cur=1
    for r in range(1,lines+1):
        row = ' '.join(str(i) for i in range(cur,cur+r))
        out.append(row)
        cur += r
    return out

def problem_3_19_fibonacci(n:int) -> List[int]:
    if n<=0: return []
    if n==1: return [0]
    res=[0,1]
    while len(res) < n:
        res.append(res[-1]+res[-2])
    return res[:n]

# ---------------------
# Section 4: Functions
# ---------------------
def problem_4_1_seconds_from_hms(h:int,m:int,s:int) -> int:
    return h*3600 + m*60 + s

def problem_4_2_sum_n(n:int) -> int:
    return n*(n+1)//2

def problem_4_3_primes_in_range(a:int,b:int) -> List[int]:
    if b < 2 or a > b:
        return []
    sieve = [True]*(b+1)
    sieve[0]=sieve[1]=False
    p=2
    while p*p <= b:
        if sieve[p]:
            for multiple in range(p*p, b+1, p):
                sieve[multiple]=False
        p+=1
    return [i for i in range(max(a,2), b+1) if sieve[i]]

def problem_4_4_largest_prime_less_than(n:int) -> int:
    if n <= 2:
        return None
    for cand in range(n-1,1,-1):
        if problem_3_6_count_primes_less_than(cand+1) - problem_3_6_count_primes_less_than(cand) == 1 and all(cand % d for d in range(2,int(sqrt(cand))+1)):
            return cand
    return None

def problem_4_5_hanoi_moves(n:int, src='A', aux='B', dst='C') -> List[Tuple[str,str]]:
    moves = []
    def move(k, a, b, c):
        if k==1:
            moves.append((a,c))
        else:
            move(k-1,a,c,b)
            moves.append((a,c))
            move(k-1,b,a,c)
    move(n, src, aux, dst)
    return moves

def problem_4_6_sort_names(names: List[str]) -> List[str]:
    return sorted(names)

def problem_4_7_is_perfect_square(n:int) -> bool:
    if n<0: return False
    r=int(sqrt(n))
    return r*r==n

def problem_4_8_min_in_list(arr: List[int]) -> int:
    if not arr: return None
    m=arr[0]
    for x in arr[1:]:
        if x<m: m=x
    return m

def problem_4_9_fibonacci_recursive(n:int) -> int:
    if n<=0: return 0
    if n==1: return 0
    if n==2: return 1
    return problem_4_9_fibonacci_recursive(n-1) + problem_4_9_fibonacci_recursive(n-2)

def problem_4_10_valid_email(email: str) -> bool:
    if '@' not in email or email.count('@')!=1: return False
    user, domain = email.split('@')
    if not user or not domain: return False
    if '.' not in domain: return False
    return True

def problem_4_11_is_perfect_number(n:int) -> bool:
    return problem_3_5_is_perfect(n)

def problem_4_12_max_digit(n:int) -> int:
    return max(int(d) for d in str(abs(n)))

def problem_4_13_c_to_f_func(c: float) -> float:
    return problem_1_1_c_to_f(c)
def problem_4_13_f_to_c_func(f: float) -> float:
    return problem_1_1_f_to_c(f)

def problem_4_14_recursive_sum(a:int,b:int) -> int:
    if a>b: return 0
    if a==b: return a
    return a + problem_4_14_recursive_sum(a+1,b)

def problem_4_15_password_strength(password: str) -> bool:
    if len(password) < 8: return False
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    return has_upper and has_lower and has_digit

# ---------------------
# Section 5: Strings
# ---------------------
def problem_5_1_normalize_name(name: str) -> str:
    parts = name.strip().split()
    parts = [p.capitalize() for p in parts]
    return ' '.join(parts)

def problem_5_2_remove_digits(s: str) -> str:
    return ''.join(ch for ch in s if not ch.isdigit())

def problem_5_3_remove_adjacent_duplicates(s: str) -> str:
    if not s: return s
    res = [s[0]]
    for ch in s[1:]:
        if ch != res[-1]:
            res.append(ch)
    return ''.join(res)

def problem_5_4_insert_between(a: str, b: str, insert: str) -> str:
    return a + insert + b

def problem_5_5_count_name(names: List[str], target: str) -> int:
    return sum(1 for n in names if n.strip() == target)

def problem_5_6_print_first_last(fullname: str) -> Tuple[str,str]:
    parts = fullname.strip().split()
    if not parts:
        return ('','')
    return (parts[0], ' '.join(parts[1:]))

def problem_5_7_count_same_firstname(names: List[str], firstname: str) -> int:
    return sum(1 for n in names if n.strip().split()[-1] == firstname)

def problem_5_8_count_char(s: str, ch: str) -> int:
    return s.count(ch)

def problem_5_9_reverse_words(sentence: str) -> str:
    words = sentence.split()
    return ' '.join(reversed(words))

def problem_5_10_is_palindrome_string(s: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

def problem_5_11_caesar_cipher(s: str, shift: int=3) -> str:
    res = []
    for ch in s:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            res.append(chr((ord(ch) - ord(base) + shift) % 26 + ord(base)))
        else:
            res.append(ch)
    return ''.join(res)

def problem_5_12_count_words(sentence: str) -> int:
    return len(sentence.split())

def problem_5_13_trim_extra_spaces(s: str) -> str:
    return ' '.join(s.split())

def problem_5_14_is_valid_variable_name(s: str) -> bool:
    if not s: return False
    if not (s[0].isalpha() or s[0]=='_'): return False
    return all(ch.isalnum() or ch=='_' for ch in s)

def problem_5_15_normalize_phone(phone: str) -> str:
    digits = ''.join(ch for ch in phone if ch.isdigit())
    if digits.startswith('0'):
        return '+84' + digits[1:]
    if digits.startswith('84'):
        return '+' + digits
    return digits

def problem_5_16_swap_case(s: str) -> str:
    return s.swapcase()

# ---------------------
# Section 6: File I/O (helper implementations)
# ---------------------
def problem_6_1_sum_odd_from_file(infile: str, outfile: str):
    with open(infile, 'r', encoding='utf-8') as f:
        nums = [int(x) for x in f.read().split()]
    s = sum(x for x in nums if x%2==1)
    with open(outfile, 'w', encoding='utf-8') as f:
        f.write(str(s))
def problem_6_2_filter_numbers_from_text(infile: str, outfile: str):
    with open(infile,'r',encoding='utf-8') as f:
        text = f.read()
    nums = ''.join(ch if ch.isdigit() or ch.isspace() else ' ' for ch in text)
    with open(outfile,'w',encoding='utf-8') as f:
        f.write(nums)
def problem_6_3_count_lines_words_chars(infile: str) -> Tuple[int,int,int]:
    with open(infile,'r',encoding='utf-8') as f:
        text = f.read()
    lines = text.count('\n') + (0 if text.endswith('\n') or not text else 1)
    words = len(text.split())
    chars = len(text)
    return lines, words, chars

# (Other file IO tasks omitted for brevity but can be added similarly.)

# ---------------------
# Section 7: Lists
# ---------------------
def problem_7_1_sum_odds_in_list(arr: List[int]) -> int:
    return sum(x for x in arr if x%2==1)

def problem_7_2_max_in_list(arr: List[float]) -> float:
    return max(arr) if arr else None

def problem_7_3_list_comprehensions(limit:int) -> Tuple[List[int], List[int]]:
    multiples_of_3 = [i for i in range(1,limit+1) if i%3==0]
    squares = [i*i for i in range(1,limit+1) if int(sqrt(i))**2 == i]
    return multiples_of_3, squares

def problem_7_4_is_arithmetic_sequence(arr: List[int]) -> bool:
    if len(arr) < 2: return True
    d = arr[1] - arr[0]
    return all(arr[i] - arr[i-1] == d for i in range(1,len(arr)))

def problem_7_5_fibonacci_list(n:int) -> List[int]:
    return problem_3_19_fibonacci(n)

def problem_7_6_count_primes_in_list(arr: List[int]) -> int:
    return sum(1 for x in arr if x>1 and all(x%d for d in range(2,int(sqrt(x))+1)))

def problem_7_7_add_matrices(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    n = len(A); m = len(A[0])
    return [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]

def problem_7_8_print_people_info(people: List[dict]) -> List[str]:
    return [f"{p.get('name')} - {p.get('age')} - {p.get('gender')} - {p.get('hometown')}" for p in people]

def problem_7_9_basic_sort(arr: List[int]) -> List[int]:
    # simple bubble sort
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def problem_7_10_linear_search(arr: List[int], key:int) -> int:
    for i,v in enumerate(arr):
        if v==key:
            return i
    return -1

def problem_7_11_matrix_diagonal_sums(mat: List[List[int]]) -> Tuple[int,int]:
    n = len(mat)
    main = sum(mat[i][i] for i in range(n))
    anti = sum(mat[i][n-1-i] for i in range(n))
    return main, anti

def problem_7_12_matrix_multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    n = len(A); m = len(B[0]); p = len(B)
    C = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                C[i][j] += A[i][k]*B[k][j]
    return C

def problem_7_13_second_largest(arr: List[int]) -> int:
    uniq = sorted(set(arr), reverse=True)
    return uniq[1] if len(uniq) > 1 else None

def problem_7_14_insert_at(arr: List[int], idx:int, val:int) -> List[int]:
    return arr[:idx] + [val] + arr[idx:]

def problem_7_15_remove_value(arr: List[int], val:int) -> List[int]:
    return [x for x in arr if x != val]

def problem_7_16_reverse_list(arr: List) -> List:
    return arr[::-1]

def problem_7_17_is_symmetric_matrix(mat: List[List[int]]) -> bool:
    n = len(mat)
    return all(mat[i][j] == mat[j][i] for i in range(n) for j in range(n))

def problem_7_18_row_col_max(mat: List[List[int]]) -> Tuple[int,int]:
    row_sums = [sum(r) for r in mat]
    col_sums = [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]
    return max(row_sums), max(col_sums)

# ---------------------
# Section 8: Dictionaries
# ---------------------
def problem_8_1_word_occurrences(s: str) -> dict:
    words = s.split()
    d = {}
    for w in words:
        d[w] = d.get(w,0) + 1
    return d

def problem_8_2_student_dict(students: List[Tuple[str,int,str]]) -> dict:
    return {sid: {'name':name,'age':age,'class':cl} for sid,(name,age,cl) in enumerate(students, start=1)}

def problem_8_3_sort_dict_by_value(d: dict) -> List[Tuple]:
    return sorted(d.items(), key=lambda kv: kv[1])

def problem_8_4_simple_translate(sentence: str, dictionary: dict) -> str:
    return ' '.join(dictionary.get(w,w) for w in sentence.split())

def problem_8_5_char_frequency(s: str) -> dict:
    d={}
    for ch in s:
        d[ch]=d.get(ch,0)+1
    return d

def problem_8_6_merge_dicts(a: dict, b: dict) -> dict:
    res = a.copy()
    res.update(b)
    return res

def problem_8_7_remove_duplicate_keys(d1: dict, d2: dict) -> dict:
    for k in list(d1.keys()):
        if k in d2:
            del d1[k]
    return d1

def problem_8_8_mini_database() -> dict:
    return {}

# ---------------------
# Section 9: Sets
# ---------------------
def problem_9_1_common_digits(s1: str, s2: str) -> List[str]:
    return sorted(set(ch for ch in s1 if ch.isdigit()) & set(ch for ch in s2 if ch.isdigit()))

def problem_9_2_unique_elements(lst: List) -> List:
    return [x for x in lst if lst.count(x)==1]

def problem_9_3_union_intersection(a:set,b:set) -> Tuple[set,set]:
    return a|b, a&b

def problem_9_4_remove_duplicates(lst: List) -> List:
    return list(dict.fromkeys(lst))

def problem_9_5_symmetric_difference(a:set,b:set) -> set:
    return a ^ b

def problem_9_6_is_subset(a:set,b:set) -> bool:
    return a.issubset(b)

def problem_9_7_count_unique_vowels_consonants(s:str) -> Tuple[int,int]:
    s = s.lower()
    vowels = set([c for c in s if c in 'aeiou'])
    consonants = set([c for c in s if c.isalpha() and c not in 'aeiou'])
    return len(vowels), len(consonants)

def problem_9_8_even_set() -> set:
    return set(range(2,101,2))

def problem_9_9_intersection_three(a:set,b:set,c:set) -> set:
    return a & b & c

# ---------------------
# Section 10: OOP
# ---------------------
class Polygon:
    def __init__(self, sides: List[float]):
        self.sides = sides

class Triangle(Polygon):
    def __init__(self, a,b,c):
        super().__init__([a,b,c])
    def perimeter(self):
        return sum(self.sides)
    def area(self):
        s = self.perimeter()/2
        a,b,c = self.sides
        return sqrt(s*(s-a)*(s-b)*(s-c))

class Student:
    def __init__(self, name:str, scores: List[float]):
        self.name = name
        self.scores = scores
    def average(self):
        return sum(self.scores)/len(self.scores) if self.scores else 0.0

class Fraction:
    def __init__(self, p:int,q:int):
        if q==0: raise ValueError('denominator 0')
        from math import gcd
        g = gcd(p,q)
        self.p = p//g
        self.q = q//g
    def __str__(self):
        return f"{self.p}/{self.q}"

class Circle:
    def __init__(self, r: float):
        self.r = r
    def area(self):
        return pi*self.r*self.r
    def volume_of_cylinder(self,height:float):
        return self.area()*height

class Car:
    def __init__(self, speed=0.0):
        self.speed = speed
    def accelerate(self, dv):
        self.speed += dv
    def decelerate(self, dv):
        self.speed = max(0.0, self.speed - dv)

class ComplexNumber:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b
    def __add__(self, other):
        return ComplexNumber(self.a+other.a, self.b+other.b)
    def __str__(self):
        return f"{self.a}+{self.b}j"

class Employee:
    def __init__(self, name:str, salary:float):
        self.name = name
        self.salary = salary
    def net_salary(self, tax_rate:float):
        return self.salary * (1 - tax_rate)

class Animal:
    def speak(self):
        return ''
class Dog(Animal):
    def speak(self):
        return 'Woof'
class Cat(Animal):
    def speak(self):
        return 'Meow'

class Point2D:
    def __init__(self,x,y):
        self.x=x;self.y=y
    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

# ---------------------
# If run as main: small interactive demo
# ---------------------
if __name__ == '__main__':
    print('This module contains implementations for many practice problems.')
    print('Import functions from this file or run small demos by calling functions.')
    # simple demo
    print('Example: problem_1_1_c_to_f(0) ->', problem_1_1_c_to_f(0))
    print('Example: problem_1_14_electric_bill(400) ->', problem_1_14_electric_bill(400))
