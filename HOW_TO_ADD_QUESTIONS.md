# How to Add More Math Questions

## 🎯 New System: Question Banks

Instead of generating from templates, we now use **JSON question banks** for unlimited variety.

## 📁 Location

```
question_generator/data/question_banks/
├── matrices_bank.json
├── logarithm_bank.json
└── (add more here)
```

## ✏️ How to Add Questions

### Step 1: Open the JSON file

```bash
nano question_generator/data/question_banks/matrices_bank.json
```

### Step 2: Add questions to appropriate difficulty

```json
{
  "easy": [
    {
      "question": "Your question here",
      "answer": "Answer",
      "solution": "Step by step solution",
      "type": "determinant"
    }
  ],
  "medium": [...],
  "hard": [...]
}
```

### Step 3: Save and test

```bash
python -c "from question_generator.generators.math_bank_generator import MatricesBankGenerator; print(MatricesBankGenerator().generate('easy', 1))"
```

## 📝 Example: Adding 100 Questions

You can add as many as you want to each difficulty level:

```json
{
  "easy": [
    {"question": "Q1...", "answer": "A1", "solution": "S1", "type": "det"},
    {"question": "Q2...", "answer": "A2", "solution": "S2", "type": "add"},
    ...
    // Add 100 questions here
  ],
  "medium": [...],
  "hard": [...]
}
```

## 🔥 Advantages vs Templates

| Template Generators | Question Banks |
|---------------------|----------------|
| Limited patterns | **Unlimited variety** |
| Repetitive questions | **Each question unique** |
| Hard to make complex | **Any complexity** |
| Code changes needed | **Just edit JSON** |

## 🚀 Create New Question Bank

### For any new topic:

1. **Create JSON file**:
```bash
nano question_generator/data/question_banks/calculus_bank.json
```

2. **Add questions**:
```json
{
  "easy": [...],
  "medium": [...],
  "hard": [...]
}
```

3. **Create generator** (copy from `math_bank_generator.py`):
```python
class CalculusBankGenerator(QuestionBankGenerator):
    def __init__(self):
        super().__init__(
            "Mathematics",
            "Calculus",
            "Derivatives",
            "calculus_bank.json"
        )
```

4. **Add to CLI** in `cli_interface.py`

## 💡 Where to Get Questions

- Past DDCET papers
- JEE practice books
- NCERT textbooks
- Online question banks
- Exam preparation websites

## ✅ Quality Checklist

- [ ] Question is clear and well-formatted
- [ ] Answer is correct
- [ ] Solution shows steps
- [ ] Type is specified (determinant, equation, etc.)
- [ ] Difficulty is appropriate

---

**TIP**: Start with 10-20 questions per difficulty, then gradually add more. Even 30 questions per topic gives 90 total questions!

