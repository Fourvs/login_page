from database.skills import skills_list

def extract_skills(tokens):

    extracted = []

    for skill in skills_list:
        if skill in tokens:
            extracted.append(skill)

    return list(set(extracted))