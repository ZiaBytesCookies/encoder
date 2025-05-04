# encoder

# 🧠 Categorical Feature Encoder (From Scratch)

This project demonstrates how to implement **Label Encoding** and **One-Hot Encoding** from scratch using only `pandas` and `numpy`, without relying on external libraries like `scikit-learn`.

It’s a great way to show off your **analytical thinking**, **data transformation skills**, and **understanding of how machine learning preprocessing works under the hood**.

---

## 🔍 What It Does

Given a simple dataset with categorical features like `"Color"` and `"Size"`, this script:

1. **Label Encodes** each category to a numeric value.
2. **One-Hot Encodes** each category into binary features.
3. Shows the mapping used for label encoding.
4. Combines the transformed data into a final encoded DataFrame.

---

## 🧾 Example Dataset

```plaintext
| Color | Size |
|-------|------|
| Red   | S    |
| Blue  | M    |
| Green | L    |
| Blue  | S    |
| Red   | M    |
| Green | L    |

## 📊 Output Preview

### ✅ Label Encoding

```plaintext
Color_Map: {'Blue': 0, 'Green': 1, 'Red': 2}
Size_Map: {'L': 0, 'M': 1, 'S': 2}
```

### ✅ One-Hot Encoding

```plaintext
| Color_Blue | Color_Green | Color_Red | Size_L | Size_M | Size_S |
|------------|-------------|-----------|--------|--------|--------|
|     0      |      0      |     1     |   0    |   0    |   1    |
|     1      |      0      |     0     |   0    |   1    |   0    |
...
```

---

## 🚀 How to Run

1. Clone this repo or copy the script into a `.py` or Jupyter Notebook file.
2. Run the script. It uses a hardcoded DataFrame—no setup or downloads needed.
3. View the printed maps and transformed DataFrame.

---

## 🛠 Tech Stack

- Python 3.x
- `pandas`
- `numpy`

---

## 📚 Learning Goals

- Understand the logic behind feature encoding.
- Translate categorical values into numerical form.
- Prepare data for machine learning models.
- Build intuition for ML preprocessing pipelines.

---

## 📦 Optional Extensions

- Turn the logic into reusable classes/functions.
- Add support for handling unknown categories during inference.
- Save encoders as pickle files for deployment.

---

## ✍️ Author

ZiaBytesCookies

---
