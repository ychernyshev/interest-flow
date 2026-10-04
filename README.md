[україномовна версія](README.UK-ua.md)

# Interest Flow 💰📈

> A modern personal deposit tracker and financial growth visualizer designed to track bank accounts, manage interest rates, and watch capital grow in real-time.

## 🔧 Tech Stack & Badges

![Python](https://img.shields.io/badge/python-3.14-blue.svg)
![Django](https://img.shields.io/badge/django-6.1.1-green.svg)
![Vue.js](https://img.shields.io/badge/vue.js-3.5.43-4FC08D.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

* **Backend:** Python, Django 6.1.1 (Django Templates, ORM, Auth, SQLite/PostgreSQL)
* **Frontend:** Vue.js 3.5.43 (via CDN), Bootstrap CSS
* **Interactivity:** Real-time client-side calculations, animations, and charts

---

## 🚀 Core Features

- **Deposit Cards:** Management of individual deposits and banks with custom interest rates and tax percentages.
- **Dynamic Controls:** Flexible interface to adjust deposit amounts and parameters on the fly.
- **Real-Time Counters:** Live capital growth ticker on each card and a global summary counter.
- **Replenishment History:** Detailed logs of all deposit additions and transactions.
- **Growth Visualization:** Interactive charts forecasting capital accumulation over time.
- **User Authentication:** Secure personal dashboard for every user.

---

## 📁 Project Architecture & Plan

1. **Backend Layer (Django):**
   - Models for Users, Banks, Deposits, and Transactions (History).
   - Views & Forms for handling CRUD operations on deposits.
   - REST endpoints or JSON context for dynamic frontend updates where needed.

2. **Frontend Layer (Django Templates + Vue 3 CDN):**
   - **Django Templates:** Renders the core HTML structure, layout, sidebars, and server-side data initializations.
   - **Vue.js CDN:** Powers the reactive UI layers (real-time interest increments, card states, dynamic filters, and interactive animations).

3. **Styling & UI:**
   - Bootstrap CSS framework integrated with custom components for a clean, modern dashboard look.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).