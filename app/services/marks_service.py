from data.loader import load_data


def get_student_marks(student_id):

    datasets = load_data()

    marks = datasets["marks"].copy()
    courses = datasets["courses"]
    subjects = datasets["subjects"]

    marks = marks[
        marks["Student_ID"] == student_id
    ]

    marks = marks.merge(
        courses[
            ["Course_ID", "Subject_ID"]
        ],
        on="Course_ID",
        how="left"
    )

    marks = marks.merge(
        subjects[
            ["Subject_ID", "Subject_Name"]
        ],
        on="Subject_ID",
        how="left"
    )

    return marks