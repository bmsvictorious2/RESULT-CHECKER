import streamlit as st
import pandas as pd

# 🎓 Mock database
results = {
    "101": {
        "name": "Ali Khan",
        "father_name": "Tariq Khan",
        "registration": "REG-2024-001",
        "subjects": {
            "English": {"9th": 75, "10th": 80},
            "Urdu": {"9th": 70, "10th": 75},
            "Math": {"9th": 90, "10th": 92},
            "Physics": {"9th": 85, "10th": 88},
            "Chemistry": {"9th": 82, "10th": 84},
            "Biology": {"9th": 78, "10th": 80},
            "Pak Studies": {"9th": 68, "10th": 70},
            "Islamiat": {"9th": 72, "10th": 74},
            "Computer": {"9th": 80, "10th": 85},
        },
    },
    "102": {
        "name": "Sara Ahmed",
        "father_name": "Ahmed Raza",
        "registration": "REG-2024-002",
        "subjects": {
            "English": {"9th": 40, "10th": 35},
            "Urdu": {"9th": 50, "10th": 45},
            "Math": {"9th": 30, "10th": 32},
            "Physics": {"9th": 25, "10th": 28},
            "Chemistry": {"9th": 33, "10th": 30},
            "Biology": {"9th": 38, "10th": 35},
            "Pak Studies": {"9th": 42, "10th": 44},
            "Islamiat": {"9th": 50, "10th": 48},
            "Computer": {"9th": 40, "10th": 38},
        },
    },
}

# 🎨 Custom CSS for attractive table
st.markdown("""
    <style>
        .result-table {
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
            font-family: 'Segoe UI';
        }
        .result-table th {
            background-color: #0A74DA;
            color: white;
            padding: 10px;
            text-align: center;
        }
        .result-table td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }
        .result-table tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        .result-table tr:hover {
            background-color: #d0e4ff;
        }
        .pass {
            color: green;
            font-weight: bold;
        }
        .fail {
            color: red;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# 🧾 App layout
st.title("🎓 Student Result Card")
st.write("Enter your roll number below to view your detailed marksheet:")

roll_no = st.text_input("Enter Roll Number")

if st.button("Check Result"):
    student = results.get(roll_no.strip())

    if student:
        st.success("✅ Result Found")

        st.markdown(f"**Name:** {student['name']}")
        st.markdown(f"**Father Name:** {student['father_name']}")
        st.markdown(f"**Registration No:** {student['registration']}")
        st.markdown(f"**Roll No:** {roll_no}")

        # 🧮 Process subjects
        subjects = student["subjects"]
        rows = []
        failed = False

        for subject, marks in subjects.items():
            total = marks["9th"] + marks["10th"]
            if marks["9th"] < 40 or marks["10th"] < 40:
                failed = True

            # Calculate grade
            avg = total / 2
            if avg >= 80:
                grade = "A+"
            elif avg >= 70:
                grade = "A"
            elif avg >= 60:
                grade = "B"
            elif avg >= 50:
                grade = "C"
            elif avg >= 40:
                grade = "D"
            else:
                grade = "F"

            rows.append(
                f"<tr><td>{subject}</td><td>{marks['9th']}</td><td>{marks['10th']}</td><td>{total}</td><td>{grade}</td></tr>"
            )

        # 🎯 Table HTML
        table_html = f"""
        <table class="result-table">
            <tr>
                <th>Subject</th>
                <th>9th Marks</th>
                <th>10th Marks</th>
                <th>Total Obtained</th>
                <th>Grade</th>
            </tr>
            {''.join(rows)}
        </table>
        """
        st.markdown(table_html, unsafe_allow_html=True)

        # 🔢 Total Marks
        total_obtained = sum(m["9th"] + m["10th"] for m in subjects.values())

        if failed:
            st.error(f"❌ Result: Clear Your Supply | Total Marks: {total_obtained} / 1100")
        else:
            st.success(f"🎉 Result: Passed | Total Marks: {total_obtained} / 1100")

    else:
        st.error("No record found for this roll number.")


