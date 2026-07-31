
## 🔑 Common Dunder Methods (Magic Methods)

### 1. Arithmetic Operators
| Operator | Dunder Method |
|----------|---------------|
| `+` (addition) | `__add__(self, other)` |
| `-` (subtraction) | `__sub__(self, other)` |
| `*` (multiplication) | `__mul__(self, other)` |
| `/` (division) | `__truediv__(self, other)` |
| `//` (floor division) | `__floordiv__(self, other)` |
| `%` (modulus) | `__mod__(self, other)` |
| `**` (power) | `__pow__(self, other)` |

---

### 2. Comparison Operators
| Operator | Dunder Method |
|----------|---------------|
| `<` | `__lt__(self, other)` |
| `<=` | `__le__(self, other)` |
| `>` | `__gt__(self, other)` |
| `>=` | `__ge__(self, other)` |
| `==` | `__eq__(self, other)` |
| `!=` | `__ne__(self, other)` |

---

### 3. Unary Operators
| Operator | Dunder Method |
|----------|---------------|
| `-obj` (negation) | `__neg__(self)` |
| `+obj` (positive) | `__pos__(self)` |
| `abs(obj)` | `__abs__(self)` |
| `~obj` (bitwise NOT) | `__invert__(self)` |

---

### 4. Container / Sequence Methods
| Action | Dunder Method |
|--------|---------------|
| `len(obj)` | `__len__(self)` |
| `obj[i]` (indexing) | `__getitem__(self, i)` |
| `obj[i] = val` | `__setitem__(self, i, val)` |
| `del obj[i]` | `__delitem__(self, i)` |
| `for x in obj` | `__iter__(self)` + `__next__(self)` |
| `in` operator | `__contains__(self, item)` |

---

### 5. Object Representation
| Action | Dunder Method |
|--------|---------------|
| `str(obj)` → user-friendly | `__str__(self)` |
| `repr(obj)` → developer-friendly | `__repr__(self)` |
| `format(obj)` | `__format__(self, format_spec)` |

---

### 6. Object Lifecycle
| Action | Dunder Method |
|--------|---------------|
| Constructor | `__init__(self, …)` |
| Destructor | `__del__(self)` |
| Copy | `__copy__`, `__deepcopy__` |

---

### 7. Callable & Context Manager
| Action | Dunder Method |
|--------|---------------|
| `obj()` (function call) | `__call__(self, …)` |
| `with obj:` | `__enter__(self)` + `__exit__(self, exc_type, exc_val, exc_tb)` |

---

### 8. Attribute Access
| Action | Dunder Method |
|--------|---------------|
| `obj.attr` | `__getattr__(self, name)` / `__getattribute__(self, name)` |
| `obj.attr = val` | `__setattr__(self, name, val)` |
| `del obj.attr` | `__delattr__(self, name)` |

---

## ✅ Summary
- Arithmetic → `__add__`, `__sub__`, `__mul__`, etc.  
- Comparison → `__eq__`, `__lt__`, etc.  
- Sequence/Container → `__getitem__`, `__setitem__`, `__len__`, etc.  
- Representation → `__str__`, `__repr__`.  
- Lifecycle → `__init__`, `__del__`.  
- Callable/Context → `__call__`, `__enter__`, `__exit__`.  
- Attribute access → `__getattr__`, `__setattr__`.  
