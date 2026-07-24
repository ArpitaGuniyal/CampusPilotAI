import streamlit as st

from services.student_service import (
    get_student,
    get_student_statistics,
)

from services.attendance_service import get_student_attendance

from services.timetable_service import get_student_timetable

from services.marks_service import get_student_marks

from services.fee_service import get_student_fees

from data.loader import load_data

def show():

    st.title("🎓 Student Portal")

    stats = get_student_statistics()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Students", stats["Total Students"])
    c2.metric("Departments", stats["Departments"])
    c3.metric("Sections", stats["Sections"])
    c4.metric("Avg CGPA", stats["Average CGPA"])

    st.divider()

    roll = st.text_input(
        "Enter Student Roll Number"
    )

    if st.button("Search"):

        student = get_student(roll)

        if student is None:

            st.error("Student not found.")

            return

        st.success("Student Found")

        st.divider()

        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "👤 Profile",
            "📅 Attendance",
            "📝 Marks",
            "🗓 Timetable",
            "💳 Fees"
        ])

        with tab1:

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("Basic Information")

                st.write("**Name:**", student["Full_Name"])
                st.write("**Roll Number:**", student["Roll_Number"])
                st.write("**Gender:**", student["Gender"])
                st.write("**Department:**", student["Department_ID"])

            with col2:

                st.subheader("Academic Information")

                st.write("**Program:**", student["Program"])
                st.write("**Year:**", student["Year"])
                st.write("**Section:**", student["Section_ID"])
                st.write("**CGPA:**", student["CGPA"])

            st.divider()

            st.subheader("Contact Information")

            st.write("📧", student["Email"])
            st.write("📞", student["Phone"])


        with tab2:

            attendance = get_student_attendance(
                student["Student_ID"]
            )

            overall = round(
                attendance["Attendance_Percentage"].mean(),
                2
            )

            st.metric(
                "Overall Attendance",
                f"{overall}%"
            )

            st.progress(overall / 100)

            st.divider()

            st.subheader("Subject-wise Attendance")

            display = attendance[
                [
                    "Subject_Name",
                    "Classes_Conducted",
                    "Classes_Attended",
                    "Attendance_Percentage"
                ]
            ]

            st.dataframe(
                display,
                use_container_width=True
            )

        with tab3:

            marks = get_student_marks(
                student["Student_ID"]
            )

            avg_marks = round(
                marks["Total"].mean(),
                2
            )

            avg_gp = round(
                marks["Grade_Point"].mean(),
                2
            )

            c1, c2 = st.columns(2)

            c1.metric(
                "Average Marks",
                avg_marks
            )

            c2.metric(
                "Average Grade Point",
                avg_gp
            )

            st.divider()

            st.subheader("Subject-wise Performance")

            display = marks[
                [
                    "Subject_Name",
                    "Assignment",
                    "Quiz",
                    "Mid_Sem",
                    "End_Sem",
                    "Total",
                    "Grade"
                ]
            ]

            display.columns = [
                "Subject",
                "Assignment",
                "Quiz",
                "Mid Sem",
                "End Sem",
                "Total",
                "Grade"
            ]

            st.dataframe(
                display,
                use_container_width=True,
                hide_index=True
            )

            st.bar_chart(
                marks.set_index("Subject_Name")["Total"]
            )


        with tab4:

            timetable = get_student_timetable(
                student["Section_ID"]
            )

            display = timetable[
                [
                    "Day",
                    "Period",
                    "Time_Slot",
                    "Subject_Name",
                    "Full_Name",
                    "Room_ID"
                ]
            ]

            display.columns = [
                "Day",
                "Period",
                "Time Slot",
                "Subject",
                "Faculty",
                "Room"
            ]

            st.dataframe(
                display,
                use_container_width=True,
                hide_index=True
            )


        with tab5:

            fees = get_student_fees(
                student["Student_ID"]
            )

            latest_fee = fees.iloc[-1]

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Total Fee",
                f"₹ {latest_fee['Total_Fee']:,.0f}"
            )

            c2.metric(
                "Amount Paid",
                f"₹ {latest_fee['Amount_Paid']:,.0f}"
            )

            c3.metric(
                "Balance",
                f"₹ {latest_fee['Balance']:,.0f}"
            )

            st.divider()

            status = latest_fee["Status"]

            if status == "Paid":

                st.success("✅ Fee Status : Paid")

            elif status == "Partial":

                st.warning("🟡 Fee Status : Partial")

            else:

                st.error("🔴 Fee Status : Pending")

            st.divider()

            st.subheader("Fee History")

            display = fees[
                [
                    "Semester",
                    "Tuition_Fee",
                    "Library_Fee",
                    "Exam_Fee",
                    "Total_Fee",
                    "Amount_Paid",
                    "Balance",
                    "Status"
                ]
            ]

            display.columns = [
                "Semester",
                "Tuition Fee",
                "Library Fee",
                "Exam Fee",
                "Total Fee",
                "Amount Paid",
                "Balance",
                "Status"
            ]

            st.dataframe(
                display,
                use_container_width=True,
                hide_index=True
            )