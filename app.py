import streamlit as st
import pandas as pd

# Mock database
results = {
    "101": {
        "name": "Ali Khan",
        "father_name": "Tariq Khan",
        "registration": "REG-2024-001",
        "subjects": {
            "English": 75,
            "Urdu": 68,
            "Math": 90,
            "Physics": 88,
            "Chemistry": 85,
            "Biology": 78,
            "Pak Studies": 65,
            "Islamiat": 70,
            "Computer": 82,
        },
    },
    "102": {
        "name": "Sara Ahmed",
        "father_name": "Ahmed Raza",
        "registration": "REG-2024-002",
        "subjects": {
            "English": 45,
            "Urdu": 38,
            "Math": 55,
            "Physics": 30,
            "Chemistry": 25,
            "Biology": 40,
            "Pak Studies": 50,
            "Islamiat": 42,
            "Computer": 35,
        },
    },
}

# App title
st.title("🎓 Board Result Checker")
st.subheader("Enter your roll number to view detailed marksheet")

roll_no = st.text_input("Enter Roll Number")

if st.button("Check Result"):
    student = results.get(roll_no.strip())

    if student:
        st.success("✅ Result Found")

        st.markdown(f"**Name:** {student['name']}")
        st.markdown(f"**Father Name:** {student['father_name']}")
        st.markdown(f"**Registration No:** {student['registration']}")
        st.markdown(f"**Roll No:** {roll_no}")

        # Create DataFrame for subjects
        subjects = student["subjects"]
        df = pd.DataFrame({
            "Subject": list(subjects.keys()),
            "Marks Obtained": list(subjects.values()),
            "Total Marks": [100]*len(subjects),
        })

        # Calculate grade per subject
        def get_grade(marks):
            if marks >= 80: return "A+"
            elif marks >= 70: return "A"
            elif marks >= 60: return "B"
            elif marks >= 50: return "C"
            elif marks >= 40: return "D"
            else: return "F"

        df["Grade"] = df["Marks Obtained"].apply(get_grade)
        st.dataframe(df, hide_index=True)

        # Total marks calculation
        total = sum(subjects.values())
        failed = any(m < 40 for m in subjects.values())

        if failed:
            st.error("❌ Result: Clear Your Supply")
        else:
            st.success("🎉 Result: Passed")

        st.markdown(f"**Total Marks:** {total} / 1100")

    else:
        st.error("No record found for this roll number.")
