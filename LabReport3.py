import json
import streamlit as st

# ======================================================
#  LOAD RULES (exactly as given in the question)
# ======================================================

RULES = [
    {
        "name": "Top merit candidate",
        "priority": 100,
        "conditions": [
            ["cgpa", ">=", 3.7],
            ["co_curricular_score", ">=", 80],
            ["family_income", "<=", 8000],
            ["disciplinary_actions", "==", 0]
        ],
        "action": {
            "decision": "AWARD_FULL",
            "reason": "Excellent academic & co-curricular performance, with acceptable need"
        }
    },s
    {
        "name": "Good candidate - partial scholarship",
        "priority": 80,
        "conditions": [
            ["cgpa", ">=", 3.3],
            ["co_curricular_score", ">=", 60],
            ["family_income", "<=", 12000],
            ["disciplinary_actions", "<=", 1]
        ],
        "action": {
            "decision": "AWARD_PARTIAL",
            "reason": "Good academic & involvement record with moderate need"
        }
    },
    {
        "name": "Need-based review",
        "priority": 70,
        "conditions": [
            ["cgpa", ">=", 2.5],
            ["family_income", "<=", 4000]
        ],
        "action": {
            "decision": "REVIEW",
            "reason": "High need but borderline academic score"
        }
    },
    {
        "name": "Low CGPA – not eligible",
        "priority": 95,
        "conditions": [
            ["cgpa", "<", 2.5]
        ],
        "action": {
            "decision": "REJECT",
            "reason": "CGPA below minimum scholarship requirement"
        }
    },
    {
        "name": "Serious disciplinary record",
        "priority": 90,
        "conditions": [
            ["disciplinary_actions", ">=", 2]
        ],
        "action": {
            "decision": "REJECT",
            "reason": "Too many disciplinary records"
        }
    }
]


# ======================================================
#   RULE ENGINE
# ======================================================

def evaluate_conditions(applicant, conditions):
    for field, operator, value in conditions:
        applicant_value = applicant[field]

        if operator == ">=" and not applicant_value >= value:
            return False
        if operator == "<=" and not applicant_value <= value:
            return False
        if operator == ">" and not applicant_value > value:
            return False
        if operator == "<" and not applicant_value < value:
            return False
        if operator == "==" and not applicant_value == value:
            return False

    return True


def run_rule_engine(applicant):
    # Sort by priority (highest first)
    sorted_rules = sorted(RULES, key=lambda r: r["priority"], reverse=True)

    for rule in sorted_rules:
        if evaluate_conditions(applicant, rule["conditions"]):
            return rule["name"], rule["action"]["decision"], rule["action"]["reason"]

    return None, "NO_DECISION", "No rule matched"


# ======================================================
#   STREAMLIT APPLICATION UI
# ======================================================

st.title("Scholarship Advisory – Rule-Based System")
st.write("Enter applicant details:")

cgpa = st.number_input("CGPA", 0.0, 4.0, step=0.01)
income = st.number_input("Monthly Family Income (RM)", 0, 50000)
cocu = st.number_input("Co-curricular Score (0–100)", 0, 100)
community_hours = st.number_input("Community Service Hours", 0, 500)
semester = st.number_input("Current Semester", 1, 10)
disciplinary = st.number_input("Number of Disciplinary Actions", 0, 10)

if st.button("Evaluate"):
    applicant_data = {
        "cgpa": cgpa,
        "family_income": income,
        "co_curricular_score": cocu,
        "community_service": community_hours,
        "semester": semester,
        "disciplinary_actions": disciplinary
    }

    rule_name, decision, reason = run_rule_engine(applicant_data)

    st.subheader("Evaluation Result")
    st.write(f"**Rule matched:** {rule_name}")
    st.write(f"**Decision:** {decision}")
    st.write(f"**Reason:** {reason}")

    st.success("Evaluation completed successfully!")
