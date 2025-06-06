# ranker.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(jd_text, resume_texts):
    documents = [jd_text] + resume_texts  # First: JD, then resumes
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(documents)

    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    ranked = sorted(
        zip(range(len(resume_texts)), similarity_scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked  # List of (index, score)
