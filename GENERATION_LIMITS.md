# Question Generation Limits & Spam Prevention

## 🔒 Anti-Spam Features

### 1. Generation Cooldown
- **2 second cooldown** between generations
- Prevents rapid spam clicking
- User sees countdown if they try too fast

### 2. Question Limit
- **Maximum 100 questions** per generation
- Prevents server overload
- Still enough for practice sets

### 3. Two Modes for Math

#### Mode 1: Question Bank (Recommended)
- Uses pre-written questions from JSON files
- **All difficulties available**: easy, medium, hard
- **Better quality**: Real exam questions
- **Topics**: Matrices, Logarithm (more coming soon)

#### Mode 2: Auto Generate
- Generates questions on-the-fly
- **Only easy difficulty** (templates are limited)
- **Good for**: Quick practice
- **Topics**: Trigonometry, Limits, Differentiation, Integration, Vectors, Coordinate Geometry

## 📊 Usage Example

### Math with Question Bank:
```
1. Select: "Matrices & Determinants"
2. Mode: Uses question bank automatically
3. Difficulty: easy/medium/hard (your choice)
4. Count: 1-100 questions
```

### Math with Generators:
```
1. Select: "Trigonometry (50+ formulas)"
2. Mode: 
   - "Question Bank" → Select difficulty
   - "Auto Generate" → Easy only
3. Count: 1-100 questions
```

### Physics (Templates work fine):
```
1. Select: "Kinematics"
2. Difficulty: easy/medium/hard
3. Count: 1-100 questions
```

## ⏱️ Cooldown Behavior

```
User generates 10 questions
→ Success! Generated in 0.5s

User immediately clicks generate again
→ "Please wait 1.5 seconds before generating again..."
→ Auto-waits and then proceeds

After 2 seconds
→ Can generate again freely
```

## �� Best Practices

1. **For exams**: Use Question Bank mode (real questions)
2. **For quick practice**: Use Auto Generate mode
3. **Large sets**: Generate 50-100 at once, export to PDF
4. **Variety**: Mix different topics and difficulties

## 🚫 What's Prevented

- ❌ Infinite rapid clicking
- ❌ Generating 1000s of questions instantly
- ❌ Server overload
- ❌ Poor quality from templates at hard difficulty

## ✅ What's Allowed

- ✅ Generate up to 100 questions at once
- ✅ Multiple topics in same session
- ✅ Export unlimited times
- ✅ Preview all questions before export

---

**Note**: These limits are for the web version to prevent abuse. CLI version has same limits for consistency.
