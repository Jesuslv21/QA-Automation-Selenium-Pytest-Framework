# 🚀 QA Automation Framework - Selenium & Pytest

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green.svg)
![Pytest](https://img.shields.io/badge/Pytest-Testing-orange.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

---

## 📌 Project Overview

End-to-end QA automation framework built using **Python**, **Selenium**, and **Pytest**.

This project implements industry best practices such as:

- Page Object Model (POM)
- Explicit waits (stable tests)
- Automated screenshots on failure

Focused on creating a scalable, maintainable, and professional QA automation solution.

---

## 🎯 Key Features

- ✅ End-to-End Testing (E2E)
- ✅ Page Object Model (POM)
- ✅ Explicit Waits (no flaky tests)
- ✅ Automatic screenshots on test failure
- ✅ Modular architecture
- ✅ Clean and maintainable code

---

## 🧪 Test Coverage

### 🔐 Authentication
- ✔️ Successful login
- ✔️ Invalid credentials
- ✔️ Empty fields validation

### 📦 Inventory
- ✔️ Products load validation
- ✔️ Sorting by price (low to high)

### 🛒 Cart
- ✔️ Add product
- ✔️ Add multiple products
- ✔️ Remove product

### 🧭 Navigation
- ✔️ Logout functionality

---

## 📁 Project Structure

qa-automation-selenium/
│
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_navigation.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│
├── data/
│   ├── test_data.py
│
├── screenshots/
├── conftest.py
├── requirements.txt
├── README.md

---

## ⚙️ Tech Stack

- Python
- Selenium WebDriver
- Pytest

---

## ▶️ How to Run the Project

### 1. Clone the repository

git clone https://github.com/TU-USUARIO/qa-automation-selenium-pytest-framework.git
cd qa-automation-selenium-pytest-framework

### 2. Install dependencies
pip install -r requirements.txt

---

## 📸 Screenshots on Failure

This framework automatically captures screenshots when a test fails.

All screenshots are stored in:

<img width="2880" height="1370" alt="test_login_empty_fields__20260415_171222" src="https://github.com/user-attachments/assets/163db8ca-cbdc-48d4-92c8-0195338de68b" />

<img width="2880" height="1368" alt="test_logout_20260416_154302" src="https://github.com/user-attachments/assets/82dbfd1b-ba04-49fd-83ca-65a51c53516a" />

<img width="2880" height="1370" alt="test_remove_product_20260416_114314" src="https://github.com/user-attachments/assets/5effe4a6-3ce3-4dac-b668-18569d72e808" />


🧠 Best Practices Implemented

* Page Object Model (POM)
* Explicit waits instead of sleep
* Separation of concerns (tests / pages / data)
* Reusable methods
* Clean assertions
⸻

👨‍💻 Author

Jesus Lopez
QA Automation Engineer Jr 
⸻

⭐ Why this project matters

This project demonstrates:

* Real QA automation framework structure
* Test design and coverage strategy
* Debugging with screenshots evidence
* Maintainable and scalable automation practices

⸻

🚀 Open to Opportunities

Currently transitioning into QA Automation.
Open to Junior QA / QA Automation roles
