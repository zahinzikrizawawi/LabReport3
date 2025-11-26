# LabReport3
A rule-based expert system built with Python and Streamlit to automate university scholarship eligibility reviews. Developed for the BSD3513 Artificial Intelligence course (Lab 3).

# 🎓 Scholarship Advisory System (Rule-Based AI)

## 📌 Overview
This project is a **Rule-Based Expert System** developed as part of the **BSD3513 Artificial Intelligence** course (Lab 3: Knowledge Representation System).

The application assists a university scholarship committee by automating the initial screening process. It uses a **Forward Chaining** inference engine to evaluate applicants based on academic performance, financial need, and co-curricular involvement.

## 🚀 Live Demo
**[Click here to view the deployed App](https://labreport3.streamlit.app/)**

## 🛠️ Features
- **Interactive UI:** Built with [Streamlit](https://streamlit.io/) for easy data entry.
- **Rule Engine:** Implements specific logic for awarding, reviewing, or rejecting candidates.
- **Priority Handling:** Resolves conflicts by processing rules based on assigned priority levels (e.g., Disqualification rules take precedence over Award rules).

## 🧠 Knowledge Base (Rules)
The system evaluates the following criteria using a JSON-based rule structure:

1.  **Top Merit Candidate (Priority 100):**
    * CGPA ≥ 3.7, Income ≤ RM 8,000, Co-curriculum ≥ 80, No disciplinary issues.
    * *Decision:* AWARD FULL
2.  **Low CGPA (Priority 95):**
    * CGPA < 2.5.
    * *Decision:* REJECT
3.  **Serious Disciplinary Record (Priority 90):**
    * Disciplinary Actions ≥ 2.
    * *Decision:* REJECT
4.  **Good Candidate (Priority 80):**
    * CGPA ≥ 3.3, Income ≤ RM 12,000, Co-curriculum ≥ 60, Max 1 disciplinary action.
    * *Decision:* AWARD PARTIAL
5.  **Need-Based Review (Priority 70):**
    * CGPA ≥ 2.5, Income ≤ RM 4,000.
    * *Decision:* REVIEW

## 💻 Installation & Usage

### Prerequisites
* Python 3.8+
* Streamlit

