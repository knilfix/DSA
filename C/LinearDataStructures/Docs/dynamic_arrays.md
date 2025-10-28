
# 📚 Dynamic Array Documentation

## 🎯 Core Concept

**Dynamic Array** = Array that automatically resizes when full, providing O(1) amortized insertion while maintaining random access.

## 🔑 Key Mechanisms

### 1. **Automatic Resizing**

- **When**: Array reaches capacity during append
- **How**: Double capacity (growth factor of 2)
- **Why**: Amortized O(1) cost for appends
- **Trade-off**: Memory vs Performance

### 2. **Memory Management**

- **Structure**: `data` pointer + `size` + `capacity`
- **Creation**: Allocate initial capacity
- **Destruction**: Free both structure AND data
- **Resize**: Allocate new, copy old, free old
-

### 3. **Operation Complexities**

- **Append**: O(1) amortized (resizing cost spread)
- **Random Access**: O(1)
- **Remove from end**: O(1)
- **Remove from middle**: O(n) (requires shifting)
- **Insert middle**: O(n) (requires shifting)

### 💡 Implementation Insights

#### **Critical Functions**

```c
// Growth strategy: double when full
if (arr->size >= arr->capacity) {
    resize_array(arr, arr->capacity * 2);
}

// Removal strategy: shift elements left
for (int i = index; i < arr->size - 1; i++) {
    arr->data[i] = arr->data[i + 1];
}
```

#### **Design Decisions**

1. **Growth Factor**: 2x (common trade-off between memory and performance)
2. **No Shrink**: Capacity doesn't reduce on removal (simplicity)
3. **Error Handling**: Return -1 for invalid operations
4. **Index Validation**: Bounds checking on access/modification

### 🚀 Usage Patterns

- **Ideal for**: Frequent appends + random access
- **Avoid**: Frequent insertions/deletions in middle
- **Watch for**: Memory usage with large capacities
