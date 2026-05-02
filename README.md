# 🎓 Student Management System

## 📌 Project Overview

This is a **menu-driven Student Management System** built using **Python**.
The program allows users to manage student records, including personal details, courses, marks, and grades.

This project was developed as part of **B.Tech 2nd Semester (Python Programming)**.

---

## 🚀 Features

### ✅ 1. Add New Student

* Stores:

  * Roll Number (unique)
  * Name
  * Branch
  * Semester
  * Courses enrolled

### ✅ 2. Record Marks

* Enter marks for each course (0–100)
* Automatically calculates:

  * Average marks
  * Grade (A+, A, B+, etc.)

### ✅ 3. Display All Students

* Shows all students in **tabular format**
* Includes:

  * Roll No
  * Name
  * Branch
  * Average
  * Grade

### ✅ 4. Display Individual Student

* Search by roll number
* Shows:

  * Full details
  * Courses + marks
  * Average + grade

### ✅ 5. Update Student Information

* Update:

  * Name, Branch, Semester
  * Add/remove courses
  * Update marks

### ✅ 6. Delete Student Record

* Delete student by roll number
* Confirmation before deletion

### ✅ 7. Search by Branch

* Filter students by branch
* Displays total count

---

## 🛠️ Technologies Used

* Python (Core concepts only)
* Data Structures:

  * Lists
  * Dictionaries
  * Sets

❌ No external libraries used

---

## 🗂️ Data Structure Used

```python
students = {
    "roll_no": {
        "name": "",
        "branch": "",
        "semester": "",
        "courses": [],
        "marks": {}
    }
}
```

---

## ▶️ How to Run

1. Install Python (3.x)
2. Download or clone this repository
3. Open terminal in project folder
4. Run:

```bash
python code.py
```

---

## 📋 Menu System

```
1. Add New Student
2. Record Marks
3. Display All Students
4. Display Individual Student
5. Update Student Information
6. Delete Student Record
7. Search by Branch
8. Exit
```

---

## 🧪 Sample Test Data

| Roll No | Name         | Branch           | Semester |
| ------- | ------------ | ---------------- | -------- |
| 2023001 | Rahul Sharma | Computer Science | 2        |
| 2023002 | Priya Singh  | Electrical Engg  | 2        |
| 2023003 | Amit Kumar   | Computer Science | 2        |

---

## ⚠️ Validations Implemented

* Unique roll number check
* Marks must be between 0–100
* Student existence validation
* Menu input validation
* Error handling for invalid inputs

---

## 📸 Output (Recommended)

Add screenshots of:

* Adding students
* Recording marks
* Display table
* Search & update
* Delete operation

---

## 👨‍💻 Author

* Name: Pushpank kumar
* Course: B.Tech (2nd Semester)
* Subject: Python Programming

---

## 📌 Notes

* Program runs in loop until exit
* Clean and formatted output
* Beginner-friendly logic
* Fully menu-driven CLI application

---

⭐ If you like this project, consider giving it a star on GitHub!
