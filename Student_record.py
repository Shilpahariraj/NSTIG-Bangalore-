import streamlit as st
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="student_report_db"
)
cursor = conn.cursor()

# ------------------- Add Student -----------------------
st.title("🎓 Student Report Card System")

menu = st.sidebar.selectbox("Select Option", ["Add Student", "Add/Update Marks", "View Report Card"])

if menu == "Add Student":
    st.header("➕ Add Student")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    email = st.text_input("Email")
    if st.button("Add"):
        cursor.execute("INSERT INTO Students (name, age, email) VALUES (%s, %s, %s)", (name, age, email))
        conn.commit()
        st.success("✅ Student added successfully!")

# ---------------- Add or Update Marks -----------------
elif menu == "Add/Update Marks":
    st.header("📝 Add or Update Marks")
    student_id = st.number_input("Student ID", min_value=1)
    subject_name = st.text_input("Subject Name")
    marks = st.number_input("Marks", min_value=0.0, max_value=100.0)

    if st.button("Save Marks"):
        # Check subject
        cursor.execute("SELECT id FROM Subjects WHERE subject_name = %s", (subject_name,))
        subject = cursor.fetchone()
        if subject:
            subject_id = subject[0]
        else:
            cursor.execute("INSERT INTO Subjects (subject_name) VALUES (%s)", (subject_name,))
            conn.commit()
            subject_id = cursor.lastrowid

        # Check if marks exist
        cursor.execute("SELECT id FROM Marks WHERE student_id = %s AND subject_id = %s", (student_id, subject_id))
        exists = cursor.fetchone()
        if exists:
            cursor.execute("UPDATE Marks SET marks_obtained = %s WHERE student_id = %s AND subject_id = %s",
                           (marks, student_id, subject_id))
            st.info("🔄 Marks updated!")
        else:
            cursor.execute("INSERT INTO Marks (student_id, subject_id, marks_obtained) VALUES (%s, %s, %s)",
                           (student_id, subject_id, marks))
            st.success("✅ Marks added!")
        conn.commit()

# ---------------- View Report Card --------------------
elif menu == "View Report Card":
    st.header("📄 View Report Card")
    sid = st.number_input("Enter Student ID", min_value=1)
    if st.button("Show Report"):
        cursor.execute("SELECT name, age, email FROM Students WHERE id = %s", (sid,))
        student = cursor.fetchone()

        if student:
            st.subheader(f"Student Info: {student[0]} (Age: {student[1]}, Email: {student[2]})")

            cursor.execute("""
                SELECT sub.subject_name, m.marks_obtained
                FROM Marks m
                JOIN Subjects sub ON m.subject_id = sub.id
                WHERE m.student_id = %s
            """, (sid,))
            results = cursor.fetchall()

            if results:
                total = 0
                for sub in results:
                    st.write(f"📘 {sub[0]}: {sub[1]}")
                    total += sub[1]

                avg = total / len(results)
                if avg >= 90:
                    grade = "A+"
                elif avg >= 80:
                    grade = "A"
                elif avg >= 70:
                    grade = "B"
                elif avg >= 60:
                    grade = "C"
                else:
                    grade = "F"

                st.write(f"**Average Marks**: {avg:.2f}")
                st.write(f"**Grade**: 🏅 {grade}")
            else:
                st.warning("No marks found for this student.")
        else:
            st.error("Student not found.")