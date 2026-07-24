from data.loader import load_data


def get_student_fees(student_id):

    datasets = load_data()

    fees = datasets["fees"]

    fees = fees[
        fees["Student_ID"] == student_id
    ]

    return fees