company_db = {

"python": ["Google", "Amazon", "Microsoft", "Flipkart"],

"sql": ["Accenture", "TCS", "Infosys"],

"machine learning": ["Google AI", "Meta AI", "OpenAI"],

"data analysis": ["Deloitte", "KPMG", "EY"],

"html": ["Wipro", "Capgemini"],

"javascript": ["Adobe", "PayPal"]

}

def recommend_companies(skills):

    companies = []

    for skill in skills:

        skill = skill.lower()   # important fix

        if skill in company_db:

            companies.extend(company_db[skill])

    return list(set(companies))