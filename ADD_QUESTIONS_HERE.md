# 📝 HOW TO ADD REAL QUESTIONS

## You're Right - Generated Questions Suck!

Instead of fake AI-generated questions, ADD YOUR OWN from:
- JEE Mains papers
- GUJCET papers  
- DDCET papers
- Your coaching material
- Textbooks

---

## 🎯 Super Easy Method

### Step 1: Open a question bank file
```bash
nano question_generator/data/question_banks/trigonometry.json
```

### Step 2: Copy-paste this template for each question

```json
{
  "id": 2,
  "question": "YOUR QUESTION TEXT HERE",
  "answer": "ANSWER HERE",
  "solution": "SOLUTION STEPS HERE",
  "source": "JEE Mains 2023 or GUJCET 2024 etc"
}
```

### Step 3: Add comma after previous question, paste new one

Example:
```json
{
  "chapter": "Trigonometry",
  "questions": [
    {
      "id": 1,
      "question": "Example question",
      "answer": "1/2",
      "solution": "Steps",
      "source": "Example"
    },
    {
      "id": 2,
      "question": "YOUR NEW QUESTION",
      "answer": "YOUR ANSWER",
      "solution": "YOUR SOLUTION",
      "source": "JEE Mains 2023"
    },
    {
      "id": 3,
      "question": "ANOTHER QUESTION",
      "answer": "ANSWER",
      "solution": "SOLUTION",
      "source": "GUJCET 2024"
    }
  ]
}
```

### Step 4: Save (Ctrl+O, Enter, Ctrl+X)

---

## 📚 Create New Topic

```bash
cp question_generator/data/question_banks/trigonometry.json question_generator/data/question_banks/calculus.json
```

Then edit and add questions!

---

## 🚀 Bulk Add from PDF

1. Open your PDF (JEE/GUJCET paper)
2. Copy questions
3. Format like above
4. Paste into JSON
5. Done!

**PRO TIP:** Start with 10-20 questions per topic, add more as you go.

---

## ✅ Quality Over Quantity

- 50 REAL questions > 1000 fake ones
- Mix JEE Mains, GUJCET, DDCET
- Include good solutions
- Mark the source

---

## 🎯 Topics to Create

Create these files in `question_generator/data/question_banks/`:

**MATH:**
- trigonometry.json
- calculus.json (limits, differentiation, integration)
- algebra.json
- vectors.json
- coordinate_geometry.json
- matrices.json
- probability.json

**PHYSICS:**
- mechanics.json
- electromagnetism.json
- thermodynamics.json
- waves.json
- modern_physics.json

---

## 🔥 This Way:

✅ **REAL** questions from actual exams  
✅ **YOUR** control over quality  
✅ **EASY** to add (just copy-paste)  
✅ **NO** fake generated crap  

Start small, build big! 💪

