from data.loader import load_data


def get_student(roll_number):

    datasets = load_data()

    students_df = datasets["students"]

    student = students_df[
        students_df["Roll_Number"].str.upper()
        == roll_number.strip().upper()
    ]

    if student.empty:
        return None

    return student.iloc[0]


def get_student_statistics():

    datasets = load_data()

    students_df = datasets["students"]

    return {
        "Total Students": len(students_df),
        "Departments": students_df["Department_ID"].nunique(),
        "Sections": students_df["Section_ID"].nunique(),
        "Average CGPA": round(students_df["CGPA"].mean(), 2)
    }

