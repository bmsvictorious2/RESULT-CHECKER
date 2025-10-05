import streamlit as st

# Mock database (dictionary of student results)
results = {
    "101": {"name": "Ali Khan", "marks": 85, "grade": "A"},
    "102": {"name": "Sara Ahmed", "marks": 72, "grade": "B"},
    "103": {"name": "Usman Tariq", "marks": 90, "grade": "A+"},
    "104": {"name": "Hina Iqbal", "marks": 60, "grade": "C"},
}

st.title("🎓 Student Result Checker")
st.write("Enter your roll number below to check your result:")

roll_no = st.text_input("Roll Number")

if st.button("Check Result"):
    student = results.get(roll_no.strip())
    if student:
        st.success("✅ Result Found!")
        st.write(f"**Roll No:** {roll_no}")
        st.write(f"**Name:** {student['name']}")
        st.write(f"**Marks:** {student['marks']}")
        st.write(f"**Grade:** {student['grade']}")
    else:
        st.error("❌ No result found for this roll number.")
