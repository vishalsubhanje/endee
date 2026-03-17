documents = [
    "Common symptoms of heart disease include chest pain, shortness of breath, dizziness, nausea, fatigue, and discomfort in the arms, neck, jaw, or back.",
    "Major risk factors include smoking, high blood pressure, diabetes, obesity, lack of physical activity, unhealthy diet, stress, and family history of heart disease.",
    "Heart disease can be prevented by regular exercise, maintaining a healthy diet, controlling blood pressure, reducing salt intake, avoiding smoking, and managing diabetes.",
    "Healthy lifestyle habits include daily walking, balanced nutrition, proper sleep, reducing alcohol consumption, maintaining a healthy weight, and stress management.",
    "Emergency signs of a heart attack include severe chest pain, pain spreading to the arm or jaw, difficulty breathing, fainting, and sudden sweating."
]

def retrieve_relevant_context(question):
    question = question.lower()

    matched_docs = []

    for doc in documents:
        doc_lower = doc.lower()
        score = 0

        for word in question.split():
            if word in doc_lower:
                score += 1

        matched_docs.append((doc, score))

    matched_docs.sort(key=lambda x: x[1], reverse=True)

    top_docs = [doc for doc, score in matched_docs[:2]]

    return "\n".join(top_docs)