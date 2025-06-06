import streamlit as st
from pathlib import Path
from resume_parser import extract_resume_text
from utils import extract_text_from_jd
from ranker import rank_resumes
from report_generator import generate_pdf_report




st.set_page_config(page_title="AI Resume Ranker", layout="centered")

st.title("📄 AI‑Driven Resume Ranker")
st.markdown("Upload resumes and a job description. Get ranked results instantly.")

# Upload multiple resumes
uploaded_resumes = st.file_uploader("📎 Upload Resumes (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

# Upload job description
uploaded_jd = st.file_uploader("📄 Upload Job Description (PDF or TXT)", type=["pdf", "txt"])

# Just a test button
if st.button("🔍 Rank Resumes"):
    if uploaded_resumes and uploaded_jd:
        # Extract JD text
        jd_text = extract_text_from_jd(uploaded_jd)

        # Extract all resume texts
        resume_names = []
        resume_texts = []
        for file in uploaded_resumes:
            text = extract_resume_text(file)
            resume_names.append(file.name)
            resume_texts.append(text)

        # Rank resumes using TF-IDF
        ranking = rank_resumes(jd_text, resume_texts)

        # Display ranking results
        st.subheader("🏆 Resume Rankings by JD Match")
        for idx, score in ranking:
            name = resume_names[idx]
            percent = round(score * 100, 2)
            st.markdown(f"**{name}** — Match Score: 🔥 `{percent}%`")
        # Generate downloadable PDF report
        pdf_path = generate_pdf_report(ranking, resume_names)

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📥 Download PDF Report",
                data=f,
                file_name="resume_rank_report.pdf",
                mime="application/pdf"
            )


    else:
        st.warning("⚠️ Please upload both resumes and a job description.")
