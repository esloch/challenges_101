def school_username(username):
    """
    If the username is less than 6 characters long the program should ask the user to enter a valid username.
    If the username does not contain the character “_” it should also ask the user to enter a valid username.
    If the username is valid, the program should decide if the user is a member of staff or a student.
    If they are a student the programme should find out their year group.
    The program should also display the initial of the student as well as their lastname.
    Finally the program should display whether the user is a Student, a Teacher or an Admin member of staff.
    """

    school_years = {"07": "Year 7", "11": "Year 11", "00": "Staff"}
    role_codes = {"_S": "Student", "_T": "Teacher", "_A": "Admin Staff"}

    if len(username) < 6 or "_" not in username:
        return "Invalid username. Please enter a valid format."

    try:
        name_part, role_code = username.split("_")
        print(name_part, role_code)
    except ValueError:
        return "Invalid username format. Please include exactly one underscore (_) before the role."

    # Validate role
    role_code = f"_{role_code.upper()}"
    if role_code not in role_codes:
        return "Invalid role code. Use _S for Student, _T for Teacher, or _A for Admin."

    # Extract year, initial, and last name
    year = name_part[:2]
    if year not in school_years:
        return f"Invalid year group: {year}."

    initial = name_part[2:3]
    last_name = name_part[3:]

    if not initial.isalpha() or not last_name:
        return "Invalid format for name. Please include initial and last name."

    result = [
        "Valid username!",
        f"Year group: {school_years[year]}",
        f"Initial: {initial}",
        f"Last name: {last_name}",
        f"User type: {role_codes[role_code]}"
    ]

    return "\n > ".join(result)


if __name__ == "__main__":
    username = "07sLoch_T" #input("Enter your username: ")
    print(school_username(username))