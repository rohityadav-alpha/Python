**Python interpreter errors are mainly of two types: *Syntax Errors* (detected before execution) and *Exceptions* (runtime errors). Common built‑in exceptions include `TypeError`, `ZeroDivisionError`, `NameError`, `IndexError`, `KeyError`, `ValueError`, `FileNotFoundError`, and more. Each occurs due to specific mistakes in code.**  

---

## 🟢 Types of Errors in Python

### 1. Syntax Errors (Parsing Errors)
- **Raised before execution starts** when code violates Python grammar rules.  
- Examples:
  - Missing colon → `if x > 5 print("Hi")` → **SyntaxError**  
  - Wrong indentation → **IndentationError**  

👉 These stop the program immediately, even before running.

---

### 2. Exceptions (Runtime Errors)
- **Raised during execution** when operations fail.  
- Examples and causes:

| Error Type | When It Occurs | Example |
|------------|----------------|---------|
| **TypeError** | Wrong data type in operation | `"2" + 2` → cannot add str + int |
| **ZeroDivisionError** | Division by zero | `10 / 0` |
| **NameError** | Variable/function not defined | `print(x)` when `x` not declared |
| **IndexError** | Accessing list index out of range | `nums = [1,2]; nums[5]` |
| **KeyError** | Accessing missing dictionary key | `data = {"a":1}; data["b"]` |
| **ValueError** | Wrong value for correct type | `int("abc")` |
| **AttributeError** | Accessing undefined attribute | `"hello".append("!")` |
| **ImportError / ModuleNotFoundError** | Importing missing module | `import nonexist` |
| **FileNotFoundError** | File not found | `open("abc.txt")` when file missing |
| **OverflowError** | Result too large for data type | `math.exp(1000)` |
| **MemoryError** | Operation exceeds memory | Creating huge list |
| **KeyboardInterrupt** | User interrupts program (Ctrl+C) | Long loop stopped manually |

---

## ⚖️ Errors vs Exceptions
- **Errors (SyntaxError, IndentationError):** Prevent program from starting.  
- **Exceptions (TypeError, ZeroDivisionError, etc.):** Occur during execution, can be handled with `try-except`.  

---

## 🛑 Common Mistakes That Trigger Errors
- Forgetting colon/indentation → **SyntaxError / IndentationError**  
- Using undefined variable → **NameError**  
- Mixing incompatible types → **TypeError**  
- Wrong index/key → **IndexError / KeyError**  
- Wrong value conversion → **ValueError**  
- Dividing by zero → **ZeroDivisionError**  
- Importing wrong module → **ImportError**  
- Accessing missing file → **FileNotFoundError**  

---

## ✅ Summary for Exams
- **Two main categories:** Syntax Errors & Exceptions.  
- **Syntax Errors:** detected before execution.  
- **Exceptions:** runtime problems like `TypeError`, `ZeroDivisionError`, `NameError`, etc.  
- **Handling:** use `try-except-finally`.  

---

👉 Rohit, chaho to main tumhare liye ek **Day‑25 notes file (Python Errors & Exceptions)** bana kar exam‑style likh du?  [Python](https://docs.python.org/3.12//tutorial/errors.html)  [GeeksForGeeks](https://www.geeksforgeeks.org/python/errors-and-exceptions-in-python/)  [letshired.com](https://www.letshired.com/tutorials/python/python-error-types)