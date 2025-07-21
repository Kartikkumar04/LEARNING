from fpdf import FPDF

# Create a custom PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Roadmap to Become Job-Ready by 7th Semester", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(3)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Data content for the PDF
content = {
    "Goal": "Job-Ready by 7th Semester (within 1 year)\nField: Python + AI/ML + Web Dev (Backup)",
    "Month 1–2 (Jul–Sep)": """
🎯 Focus: Python mastery + Projects + GitHub

✅ Complete:
- CodeWithHarry Python (10 hr video)
- 100 Days of Code – Python (use YouTube if Udemy paid)
- GitHub basics + upload 2 mini projects

✅ Tools to Learn:
- VS Code, GitHub, Jupyter Notebook
- Learn Markdown for GitHub README

✅ Project Ideas:
- Age calculator
- Weather app using API
- Expense tracker
- Chatbot with basic logic
""",
    "Month 3–4 (Sep–Nov)": """
🎯 Focus: AI/ML Foundation + Resume building

✅ Learn:
- NumPy, Pandas, Matplotlib
- Scikit-learn basics (classification, regression)
- 2 Mini AI projects: Iris flower classifier, House price predictor

✅ Resume + LinkedIn:
- Create 1-page resume with project links
- Optimize LinkedIn with keywords + profile photo

✅ Upload on:
- GitHub, LinkedIn, Personal Portfolio (optional)
""",
    "Month 5–6 (Nov–Jan)": """
🎯 Focus: Internships + Real-world Skills

✅ Apply for:
- Unpaid → Paid internships on: Internshala, LinkedIn Jobs, HelloIntern

✅ Also:
- Learn Flask or Streamlit to make ML projects web-based
- Make 1–2 AI apps with GUI or web
""",
    "Month 7–8 (Jan–March, Start of 7th Sem)": """
🎯 Focus: Internship convert to PPO (Pre-Placement Offer)

✅ Apply for:
- Internships from Tier 2/3 startups
- Hackathons / Coding events
- Open source contributions on GitHub

✅ Create:
- Final resume, Portfolio website (free templates)
""",
    "Tools to Learn by Nov": """
- GitHub: Showcase code & projects
- Google Colab: Run ML models online
- VS Code: Python coding
- Streamlit: Web app for ML models
- ChatGPT: Assistant & guide
""",
    "Bonus Tips": """
- Record yourself explaining a project (post on Insta/Reel)
- Learn English daily
- Start freelancing on Fiverr or Upwork with Python scripts
""",
    "Deliverables by 7th Sem": """
✅ Resume
✅ GitHub profile with 4–6 projects
✅ 1 personal project with good UI
✅ LinkedIn profile
✅ Internship certificate (even if unpaid)
"""
}

# Add content to the PDF
for section, text in content.items():
    pdf.chapter_title(section)
    pdf.chapter_body(text)

# Save the file
output_path = "/mnt/data/Kartik_AI_ML_Job_Ready_Roadmap.pdf"
pdf.output(output_path)

output_path
