from data.loader import load_data


def get_student_attendance(student_id):

    datasets = load_data()

    attendance_df = datasets["attendance"]
    courses_df = datasets["courses"]
    subjects_df = datasets["subjects"]

    attendance = attendance_df[
        attendance_df["Student_ID"] == student_id
    ].copy()

    attendance = attendance.merge(
        courses_df[
            ["Course_ID", "Subject_ID"]
        ],
        on="Course_ID",
        how="left"
    )

    attendance = attendance.merge(
        subjects_df[
            ["Subject_ID", "Subject_Name"]
        ],
        on="Subject_ID",
        how="left"
    )

    return attendance