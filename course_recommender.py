def recommend_courses(missing_skills):

    course_map = {
        "python": "Python for Everybody - Coursera",
        "data analysis": "Google Data Analytics - Coursera",
        "excel": "Excel Skills for Business - Coursera",
        "sql": "SQL for Data Science - Coursera",
        "machine learning": "Machine Learning by Andrew Ng - Coursera"
    }

    courses = []

    for skill in missing_skills:
        if skill.lower() in course_map:
            courses.append((skill, course_map[skill.lower()]))

    return courses