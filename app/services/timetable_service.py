from data.loader import load_data


def get_student_timetable(section_id):

    datasets = load_data()

    timetable = datasets["timetable"].copy()
    subjects = datasets["subjects"]
    faculty = datasets["faculty"]

    # Only this student's section
    timetable = timetable[
        timetable["Section_ID"] == section_id
    ]

    # Subject names
    timetable = timetable.merge(
        subjects[
            ["Subject_ID", "Subject_Name"]
        ],
        on="Subject_ID",
        how="left"
    )

    # Faculty names
    timetable = timetable.merge(
        faculty[
            ["Faculty_ID", "Full_Name"]
        ],
        on="Faculty_ID",
        how="left"
    )

    timetable = timetable.sort_values(
        ["Day", "Period"]
    )

    return timetable