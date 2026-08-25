# -*- coding: utf-8 -*-
# Exact verbatim text from the live FYW 1323 site. Compact, consistent
# heading treatment throughout — same sections packed onto the same page
# wherever they fit.
import sys
sys.path.insert(0, "/private/tmp/claude-504/-Users-vmontrose-Desktop-FYW-1323-What-is-a-cult-syllabus-website/b73c8ee0-12b2-4b38-8bba-44ab21e5fc8f/scratchpad/syllabus-pdfs")
from gen_schedule import sched_table
from fyw_data import rows as sched_rows

OUT = "/private/tmp/claude-504/-Users-vmontrose-Desktop-FYW-1323-What-is-a-cult-syllabus-website/b73c8ee0-12b2-4b38-8bba-44ab21e5fc8f/scratchpad/syllabus-pdfs/fyw-syllabus.html"

TOKENS = """
:root {
  --paper: #ffffff;
  --ink: #100a26;
  --ink-soft: #5a5178;
  --dark: #100a26;
  --on-dark: #ffffff;
  --on-dark-soft: #cbc3ec;
  --accent-a: #0d9488;
  --accent-strong: #0f766e;
  --accent-b: #6d28d9;
  --line: #ddd7ee;
  --callout-bg: #f4f2fb;
  --photo-bg: #f6f4fc;
  --accent-mark: #5eead4;
  --font-display: "Space Grotesk", sans-serif;
  --font-body: "Work Sans", sans-serif;
}
body { background: #ffffff; }
mark { color: #100a26 !important; }
a { color: var(--accent-a); }
"""

HEAD = f"""<!doctype html>
<html><head><meta charset="utf-8">
<title>FYW 1323 Syllabus</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Work+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="print-system.css">
<style>{TOKENS}</style>
</head><body>
"""

RUNHEAD = '<div class="runhead">Fall 2026 &middot; First-Year Writing &middot; FYW 1323</div>'

def photo_ph(label, height="2.3in"):
    return f'<div class="photo-ph" style="height:{height};">' \
           f'<span class="cap">PHOTO PLACEHOLDER<br>{label}</span></div>'

def item(heading, body_html):
    return f'<div class="item"><h4>{heading}</h4><div class="prose">{body_html}</div></div>'

pages = []

# ---------------- PAGE 1: COVER ----------------
pages.append(f"""
<div class="page">
  <div class="cover-hero">
    <div class="cover-eyebrow">Fall 2026 &middot; Furman University &middot; First-Year Writing</div>
    <h1 class="cover-title">WHAT IS<br>A CULT?</h1>
    <p class="cover-subtitle">Reading, writing, and researching persuasion, belief, and belonging &mdash; FYW 1323</p>
  </div>
  <div class="pad" style="margin-top:0.35in;">
    <div style="height:2.6in; overflow:hidden;"><img src="cover-photo.png" style="width:100%; height:100%; object-fit:cover; display:block;"></div>
    <div class="cols2" style="margin-top:0.28in;">
      <div class="side-head" style="grid-template-columns:1.1in 3px 1fr;">
        <div class="label" style="font-size:16px;">Course<br>Info</div>
        <div class="rule"></div>
        <div class="body prose">
          <p><strong>Meets:</strong> Mon / Wed / Fri, 1:30&ndash;2:20 PM &middot; Furman Hall 121</p>
          <p><strong>Instructor:</strong> Dr. Tori Montrose<br>victoria.montrose@furman.edu</p>
          <p><strong>Office:</strong> Furman Hall 206J &middot; Office hours by appointment</p>
          <p><strong>Librarian:</strong> Patricia Sasser<br>patricia.sasser@furman.edu</p>
        </div>
      </div>
      <div class="prose">
        <h4 class="block-title" style="font-size:16px;">Course Description</h4>
        <p>In this first-year writing course, we will learn and employ effective reading, writing, critical thinking, and academic research in an exploration of the question &ldquo;what is a cult?&rdquo; While this term has typically been used to pejoratively describe fringe religious movements, it has also been used to describe secular fanaticism for works of art, political movements, and even brands. We will examine historical and current use of this word&mdash;and the movements it is used to describe&mdash;in art, politics, business, and pop culture, all while learning effective writing strategies and skills that will prepare you to write well in future academic and professional endeavors.</p>
      </div>
    </div>
  </div>
</div>
""")

# ---------------- PAGE 2: OBJECTIVES + GRADING ----------------
pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.3in;">
    <div class="sec-title">Learning Objectives</div>
    <div class="sec-kicker">By the end of the semester, you will be able to:</div>
    <div class="cols2">
      <div class="prose">
        <p><strong>Read and analyze diverse genres and sources</strong> &mdash; identify how texts about &ldquo;cults&rdquo; and mass movements differ across genre (news, scholarship, memoir, polemic) and apply X-ray reading strategies to uncover structure, purpose, and audience.</p>
        <p><strong>Locate and evaluate evidence-based arguments</strong> &mdash; find credible sources and use research- or data-derived evidence to support claims about how the &ldquo;cult&rdquo; label functions in religion, politics, business, and pop culture.</p>
      </div>
      <div class="prose">
        <p><strong>Use writing as a tool for critical thinking and scholarly conversation</strong> &mdash; draft to develop ideas, engage sources as a &ldquo;scholarly dinner table&rdquo; of voices, and cite/quote effectively to demonstrate the significance of an argument about group identity and fanaticism.</p>
        <p><strong>Write clearly and purposefully for an audience</strong> &mdash; apply precise language and word choice, and shape prose for the reader's needs, when making arguments about contested terms like &ldquo;cult.&rdquo;</p>
      </div>
    </div>

    <div class="sec-title" id="graded" style="margin-top:0.3in;">Graded Elements &amp; Assignments</div>
    <div class="sec-kicker">How your final grade is calculated, and what each assignment involves.</div>
    <table class="weights">
      <thead><tr><th>Component</th><th class="num">Weight</th></tr></thead>
      <tbody>
        <tr><td>Attendance and In-class Engagement</td><td class="num">20%</td></tr>
        <tr><td>Engagement with Readings on Perusall</td><td class="num">10%</td></tr>
        <tr><td>In-class Reflective Writing Assignments</td><td class="num">10%</td></tr>
        <tr><td>Research Proposal (Midterm Assignment)</td><td class="num">30%</td></tr>
        <tr><td>Final Paper</td><td class="num">30%</td></tr>
      </tbody>
    </table>
    <h4 class="block-title" style="margin-top:0.15in;">Grading Scale</h4>
    <div class="grade-scale">
      <div class="cell"><span class="letter">A</span><span class="pct">93&ndash;100</span></div>
      <div class="cell"><span class="letter">A&minus;</span><span class="pct">90&ndash;92</span></div>
      <div class="cell"><span class="letter">B+</span><span class="pct">87&ndash;89</span></div>
      <div class="cell"><span class="letter">B</span><span class="pct">83&ndash;86</span></div>
      <div class="cell"><span class="letter">B&minus;</span><span class="pct">80&ndash;82</span></div>
      <div class="cell"><span class="letter">C+</span><span class="pct">77&ndash;79</span></div>
      <div class="cell"><span class="letter">C</span><span class="pct">73&ndash;76</span></div>
      <div class="cell"><span class="letter">C&minus;</span><span class="pct">70&ndash;72</span></div>
      <div class="cell"><span class="letter">D+</span><span class="pct">67&ndash;69</span></div>
      <div class="cell"><span class="letter">D</span><span class="pct">63&ndash;66</span></div>
      <div class="cell"><span class="letter">D&minus;</span><span class="pct">60&ndash;62</span></div>
      <div class="cell"><span class="letter">F</span><span class="pct">Below 60</span></div>
    </div>
  </div>
</div>
""")

# ---------------- PAGE 3: ASSIGNMENT DESCRIPTIONS (all 5, compact) ----------------
attendance = item("Attendance and In-class Engagement &mdash; 20%",
  '<p>Every version of this course is unique to the combination of students that comprise it. Your presence is an essential part of the learning experience for yourself and all of us in the room with you. This course requires you to come prepared to share your questions, struggles, and ideas surrounding the readings and content we cover. Each student is expected to actively participate in all activities and discussions. There are several ways to demonstrate engagement including small group discussions, taking notes, large group discussions, polls. See <a href="#rubrics">Engagement Rubric</a>. See also <a href="#policy-absences">Policies on Absences and Late Submissions</a>.</p>')

perusall = item("Engagement with Readings on Perusall &mdash; 10%",
  '<p>Readings will be posted to Perusall, which can be accessed through the link on course Moodle page. Prior to class, you will annotate the day&rsquo;s assigned reading with your comments, questions, observations, and reflections. Perusall comments are time stamped and must be made by 10am the day of class to receive full credit. I value the quality of the annotation more than the quantity of annotations you make. Thoughtful responses to classmates&rsquo; comments or questions are also welcomed.</p>')

inclass = item("In-class Reflective Writing Assignments &mdash; 10%",
  '<p>Throughout the semester, you will complete short, low-stakes writing exercises during class time &mdash; diagnostic reflections (e.g., &ldquo;What do you think a cult is?&rdquo;), structured analyses using tools like Stasis Theory or X-Ray Reading, and reflective writing tied to your research proposal&rsquo;s progress. These are handwritten or in-class exercises, not take-home essays, and they are assessed for thoughtful engagement rather than polish.</p>'
  '<p>The emphasis here is <strong>process over product</strong>: this is writing-to-think, one of the &ldquo;Ten College Writing Skills&rdquo; this course is built around. These exercises give you low-pressure space to test ideas, work through confusion, and discover what you actually think before you have to argue it formally &mdash; skills that directly feed your Research Proposal and Final Paper. Because they happen in the moment, missed in-class writing generally cannot be made up, but you are allowed to miss 2 without impacting your grade.</p>')

proposal = item("Research Proposal (Midterm Assignment) &mdash; 30%",
  '<p>For your midterm project, you will develop a research proposal investigating a specific cult or cult-related phenomenon. This project builds across several weeks and includes: research question (<mark>due Wed. 9/16 in class</mark>), annotated bibliography (<mark>due Fri. 9/25 by 11:59pm</mark>), background (<mark>due Fri. 10/2 by 11:59pm</mark>), methodology and significance (<mark>due Fri. 10/9 by 11:59pm</mark>), and abstract and compiled first draft of the full proposal (<mark>due Fri. 10/16 by 11:59pm</mark>).</p>'
  '<p>By Friday 10/16, you are submitting more than just the abstract &mdash; you will compile your background, methodology, and significance sections together with the new abstract into a single, complete first draft of your proposal.</p>'
  '<p>You will receive feedback at multiple stages and have opportunities for revision. Keep in mind that your research question and abstract may change as you progress &mdash; that is normal and a healthy sign that you are carefully considering your sources.</p>'
  '<p>The Peer Review Form (5%) contributes to the assignment grade for this proposal.</p>'
  '<p>Peer Review: In class, Mon. Oct. 19. Final drafts <mark>due Fri. Oct. 23 by 11:59pm to Moodle</mark>.</p>')

final_paper = item("Final Paper &mdash; 30%",
  '<p><strong>Due:</strong> <mark>Tue. 12/15 at 12:00 PM</mark>.</p>'
  '<p>For your final project, you will write an argumentative essay using a specific &ldquo;cult&rdquo; case study to make a broader argument about how we define and understand cults. Your essay should:</p>'
  '<ul><li>Analyze a specific cult case in depth</li><li>Engage with scholarly definitions and frameworks</li><li>Make an original argument about cult definitions, boundaries, or characteristics</li><li>Incorporate evidence from multiple scholarly sources</li><li>Address counterarguments and acknowledge complexity</li></ul>'
  '<p>This essay will go through multiple drafts with peer review and instructor feedback. A completed <strong>AI Consultation Log</strong> must be submitted as an appendix to your final essay.</p>')

ai_log = item("AI Consultation Log &mdash; 5% of Final Essay Grade",
  '<p>Your AI Consultation Log is a 1&ndash;2 page document demonstrating your thoughtful, critical engagement with AI as a thought partner during the development of your final essay. Required components:</p>'
  '<ol><li><strong>Documentation of AI Interactions:</strong> Specific prompts used, summaries of AI responses, and any additional consultations conducted independently</li>'
  '<li><strong>Critical Evaluation:</strong> Which suggestions did you pursue or reject, and why? Where did you misunderstand your argument?</li>'
  '<li><strong>Reflection on AI&rsquo;s Role:</strong> What did AI help you see? What are its limitations? How did you ensure your essay remained authentically yours?</li></ol>'
  '<p>Both the AI Consultation Log (5%) and Peer Review Form (5%) contribute to the assignment grade for this paper.</p>')

pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.32in;">
    <div class="sec-title">Assignment Descriptions</div>
    <div class="sec-kicker">Every graded element on the Grade Breakdown table, in full.</div>
    {attendance}
    {perusall}
    {inclass}
  </div>
</div>
""")

pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.32in;">
    {proposal}
    {final_paper}
    {ai_log}
  </div>
</div>
""")

# ---------------- SCHEDULE PAGES ----------------
headers = ["#", "Date", "Topic", "Pre-class Activity / Assignment", "Campus Calendar/Notes"]
widths = ["0.28in", "0.72in", "1.1in", None, "1.3in"]

def sched_page(title, rows_slice, first=False):
    tb = sched_table(headers, rows_slice, ["topic", "pre", "notes"], widths)
    tbar = f'<div class="title-bar" id="schedule">{title}</div>' if first else RUNHEAD
    return f"""
<div class="page">
  {tbar}
  <div class="pad" style="margin-top:0.18in;">{tb}</div>
</div>
"""

chunk1 = sched_rows[0:19]
chunk2 = sched_rows[19:]

pages.append(sched_page("CLASS SCHEDULE", chunk1, first=True))
pages.append(sched_page("", chunk2))

# ---------------- PAGE 5: POLICIES I ----------------
accessibility = item("Statement on Accessibility and Inclusivity",
  '<p>In the spirit of Universal Design for Learning, I will strive to provide an environment that is equitable and conducive to achievement and learning for all students. I recognize and value the many perspectives students bring to the classroom. Many factors&mdash;social identities, visible and invisible disabilities, family circumstances, physical location, mental health, access to the internet&mdash;all influence the experiences that every individual can have in this course. I am committed to building an environment to support your learning. I ask that we all be respectful of diverse opinions and of all class members, regardless of personal attribute, and that we all use inclusive language in written and oral work. I encourage persons with Student Office for Accessibility Resources (SOAR) accommodations or other needs that may impact your performance to meet with me promptly to make a plan for the semester.</p>')

pronoun = item("Name/Pronoun Use",
  '<p>I am committed to an environment that affirms people of all gender expressions and gender identities. I will gladly honor the name or gender pronouns that are correct for you. I will never require you to disclose this information, as I view it as your choice to share if and when you desire. If you choose to share this information, please advise me early in the semester so that I may make appropriate changes to my records.</p>')

absences = item('<span id="policy-absences">Policies on Absences and Late Submissions</span>',
  '<p>Students are allowed <strong>4 free absences</strong> (roughly 10% of the total number of classes) regardless of the reason. I do not need you to email me or provide an explanation for these absences. These include absences due to illnesses, personal loss, athletics, religious observances, or any other reason. After 4 absences, your attendance and participation grade will be negatively impacted.</p>'
  '<p>Late submissions following absences must be submitted on the day of return to class. Otherwise late submissions of assignments may be accepted for partial credit depending on the circumstances.</p>'
  '<p>Meeting deadlines is part of what this course is teaching: staying on schedule and managing your time across multiple due dates are skills that matter well beyond this class, and I want you to build those habits here. If a deadline is coming and something has gotten in the way, reach out to me before it passes &mdash; a short email is often enough to work out a brief extension. Assignments submitted late without any communication beforehand may receive reduced feedback and a grade deduction, but my goal is always to help you finish the work well, not to penalize you for asking.</p>')

integrity = item("Statement on Academic Integrity",
  '<p>Per <a href="https://policies.furman.edu//view.php?policy=584">Section 121.5 of Furman&rsquo;s University Policy</a>, &ldquo;All forms of academic misconduct including cheating, plagiarism, misrepresentation, and unacceptable collaboration are violations of Furman&rsquo;s academic integrity standard. Examples and explanations may be found elsewhere in official university documents (e.g., The Student Handbook and the academic integrity portion of the Furman University website).&rdquo;</p>'
  '<p>Please note: Students who are suspected of submitting writing produced in any part by an AI system will be subjected to review by the Academic Discipline Committee. For more information on Generative Artificial Intelligence use in this class, see the Use of Generative Artificial Intelligence (AI) policy below.</p>'
  '<p>It is always better to get a zero on an assignment rather than submitting something that violates the university&rsquo;s academic integrity policy, which usually results in far worse consequences.</p>')

nondiscrim = item("Nondiscrimination Policy and Sexual Misconduct",
  '<p>Furman University and its faculty are committed to supporting our students and seeking an environment that is free of bias, discrimination, and harassment. Furman does not unlawfully discriminate on the basis of race, color, national origin, sex, sexual orientation, gender identity, pregnancy, disability, age, religion, veteran status, or any other characteristic or status protected by applicable local, state, or federal law in admission, treatment, or access to, or employment in, its programs and activities.</p>'
  '<p>If you have encountered any form of discrimination or harassment, including sexual misconduct (e.g. sexual assault, sexual harassment or gender-based harassment, sexual exploitation or intimidation, stalking, intimate partner violence), we encourage you to report this to the institution. If you wish to report such an incident of misconduct, you may contact Furman&rsquo;s Title IX Coordinator, Melissa Nichols (Trone Center, Suite 215; Melissa.nichols@furman.edu; 864.294.2221).</p>'
  '<p>If you would like to speak with someone who can advise you but maintain complete confidentiality, you can talk with a counselor, a professional in the Student Health Center, or someone in the Office of Spiritual Life. If you speak with a faculty member, understand that as a mandated reporter of the University, the faculty member MUST report to the University&rsquo;s Title IX Coordinator what you share to help ensure that your safety and welfare are being addressed, consistent with the requirements of the law. However, unless there is an ongoing safety risk to you or to the Furman community, you will determine whether the university initiates any formal process. You are entitled to supportive measures (such as a no contact order or academic accommodations) regardless of whether you decide to initiate a formal process.</p>'
  '<p>Additional information about Furman&rsquo;s Sexual Misconduct Policy, how to report sexual misconduct, and your rights can be found at the Furman Title IX webpage at <a href="https://www.furman.edu/titleix">www.furman.edu/titleix</a>. You do not have to go through the experience alone.</p>')

pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.32in;">
    <div class="sec-title" id="policies">Course Policies</div>
    <div class="sec-kicker">Please read these carefully &mdash; they explain how the class runs day to day.</div>
    {accessibility}
    {pronoun}
    {absences}
    {nondiscrim}
  </div>
</div>
""")

ai_policy = item("Use of Generative Artificial Intelligence (AI)",
  '<p>This is a &ldquo;No, But&rdquo; course. This means that generative AI tools are <strong>generally prohibited</strong> unless explicitly permitted for specific assignments or activities.</p>'
  '<ul>'
  '<li>AI tools cannot be used to generate anything, in part or in whole, that is submitted with a student&rsquo;s name on it for credit, unless the instructor explicitly permits it for an assignment.</li>'
  '<li>Specific assignments may incorporate AI tools for specific learning objectives.</li>'
  '<li>When AI use is allowed, assignment instructions will identify which tools are allowed and to what extent they may be used.</li>'
  '<li>In cases of uncertainty, students should assume that no AI tool is allowed.</li>'
  '</ul>'
  '<p><strong>When AI is NOT Permitted:</strong> A key learning goal in this course is engaging in reflection on your own development. Reflective exercises require you to think about what you have experienced, critically evaluate that experience, and articulate your learning from that experience. Generative AI tools that write text for you (such as ChatGPT, Microsoft Copilot, and Canva) are prohibited for these assignments. Violations will be considered academic misconduct.</p>'
  '<p><strong>When AI IS Permitted:</strong> If AI use is permitted for a specific assignment or activity, it will be clearly stated in the assignment or activity instructions. These instructions will specify:</p>'
  '<ul><li>What AI tools you may use</li><li>How you may use them</li><li>How you must acknowledge your use</li></ul>'
  '<p>Even when AI is permitted:</p>'
  '<ul>'
  '<li>You are responsible for verifying the accuracy of any AI-generated content</li>'
  '<li>You must acknowledge your use of AI as instructed</li>'
  '<li>You cannot upload copyrighted materials (textbooks, instructor notes, slides) to AI without express permission</li>'
  '</ul>'
  '<p><strong>Grammar and Spell Check Tools:</strong></p>'
  '<ul>'
  '<li>You may use your word processor&rsquo;s native spelling and grammar checker (e.g., built-in tools in Word or Google Docs that are not LLM-based) only to identify sentence-level issues. Allowing these tools to rewrite parts of sentences, whole sentences, or paragraphs is not acceptable. You do not need to cite the use of these standard tools.</li>'
  '<li>You may not use Grammarly or similar third-party writing assistants, as these tools often provide more intervention than is appropriate for this course.</li>'
  '</ul>'
  '<p><strong>When in Doubt, Ask!</strong> If you are uncertain whether AI use is permitted for a specific assignment or activity, ask me before you use it. If you have questions about what constitutes plagiarism or academic misconduct, consult me before it&rsquo;s too late! The penalty for academic integrity violations is an F for the assignment or, in case of multiple violations, an F for the course.</p>')

recordings = item("Course Activity Recordings",
  '<p>Furman University prohibits the recording of classes by students without obtaining prior, written permission of the instructor, except in cases where Furman permits a qualified student with a documented disability to record classes as a reasonable accommodation. Students are advised of this policy in the Student Handbook. Under no circumstances should recorded classes be used in any way that denigrates and/or decontextualizes the instructor or any student whose class remarks are recorded. Unauthorized dissemination of any recorded classroom proceedings, including distribution for compensation, is strictly prohibited. The improper sharing of recorded material by students or others may constitute a violation of U.S. copyright law and is a violation of campus policy.</p>')

pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.32in;">
    {integrity}
    {ai_policy}
    {recordings}
  </div>
</div>
""")

# ---------------- RUBRICS PAGE (all three levels together) ----------------
pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.32in;">
    <div class="sec-title" id="rubrics">Engagement Rubric</div>
    <div class="sec-kicker">Each class, your engagement will be assessed using the following scale.</div>
    <div class="cols3">
      <div class="prose">
        <h4 class="block-title">A-level</h4>
        <ul>
          <li>Prepared to ask and answer questions, in writing or orally, based on assigned readings;</li>
          <li>Prepared with any required assignments;</li>
          <li>Focused on classroom discussions and activities (i.e., not using technology unless it aids in classroom discussion or activities, not conducting side conversations, not engaging in behaviors that disrupt the focus of others);</li>
          <li>Fully engaged in all in-class activities;</li>
          <li>Fully attentive when others are speaking; and</li>
          <li>Fully attentive to your own contributions, which includes&hellip;
            <ul>
              <li>giving others the space and time to contribute;</li>
              <li>understanding that others come to our classroom with different experiences than your own; and</li>
              <li>being open to learning, including learning from your own mistakes.</li>
            </ul>
          </li>
        </ul>
      </div>
      <div class="prose">
        <h4 class="block-title">B-level</h4>
        <ul>
          <li>Mostly prepared to ask and answer questions, in writing or orally, based on assigned readings;</li>
          <li>Prepared with any required assignments;</li>
          <li>Mostly focused on classroom discussions and activities (i.e., not using technology unless it aids in classroom discussion or activities, not conducting side conversations, not engaging in behaviors that disrupt the focus of others);</li>
          <li>Mostly engaged in all in-class activities;</li>
          <li>Mostly attentive when others are speaking; and</li>
          <li>Mostly attentive to your own contributions, which includes&hellip;
            <ul>
              <li>giving others the space and time to contribute;</li>
              <li>understanding that others come to our classroom with different experiences than your own; and</li>
              <li>being open to learning, including learning from your own mistakes.</li>
            </ul>
          </li>
        </ul>
      </div>
      <div class="prose">
        <h4 class="block-title">C&ndash;D level</h4>
        <ul>
          <li>Arrived more than 5 minutes late and/or left before the end of class;</li>
          <li>Not prepared to ask and answer questions, in writing or orally, based on assigned readings;</li>
          <li>Not prepared with some or any required assignments;</li>
          <li>Not focused on classroom discussions and activities (i.e., using technology in ways other than for use in classroom discussion or activities, conducting side conversations, engaging in behaviors that disrupt the focus of others);</li>
          <li>Not engaged in all in-class activities;</li>
          <li>Not attentive when others are speaking; OR</li>
          <li>Not attentive to your own contributions, which includes&hellip;
            <ul>
              <li>Not giving others the space and time to contribute;</li>
              <li>Not understanding that others come to our classroom with different experiences than your own; and</li>
              <li>Not being open to learning, including learning from your own mistakes.</li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
    <div class="callout" style="margin-top:0.3in;">
      <p>Rubrics for the Research Proposal and Final Paper will be added here later.</p>
    </div>
  </div>
</div>
""")

with open(OUT, "w") as f:
    f.write(HEAD)
    f.write("\n".join(pages))
    f.write("</body></html>")

print("wrote", OUT, "pages:", len(pages))
