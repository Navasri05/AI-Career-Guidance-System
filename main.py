import streamlit as st

st.set_page_config(
    page_title="AI Career Guidance System",
    page_icon="🎓",
    layout="centered"
)

# Career database
careers = {
    "Software Developer": {
        "interests": ["Programming", "Technology", "Problem Solving"],
        "skills": ["Python", "Java", "C", "Data Structures", "Git"],
        "description": "Develops software applications, websites and systems."
    },
    "Data Scientist": {
        "interests": ["Data Analysis", "Mathematics", "Technology"],
        "skills": ["Python", "SQL", "Statistics", "Machine Learning", "Pandas"],
        "description": "Analyzes data and builds machine learning models."
    },
    "AI/ML Engineer": {
        "interests": ["Artificial Intelligence", "Programming", "Mathematics"],
        "skills": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "SQL"],
        "description": "Builds AI and machine learning based applications."
    },
    "Web Developer": {
        "interests": ["Web Development", "Design", "Programming"],
        "skills": ["HTML", "CSS", "JavaScript", "React", "Git"],
        "description": "Creates and maintains websites and web applications."
    },
    "Cybersecurity Analyst": {
        "interests": ["Cybersecurity", "Technology", "Problem Solving"],
        "skills": ["Networking", "Linux", "Python", "Ethical Hacking", "Security"],
        "description": "Protects systems, networks and data from cyber threats."
    },
    "Cloud Engineer": {
        "interests": ["Cloud Computing", "Technology", "Networking"],
        "skills": ["AWS", "Azure", "Linux", "Docker", "Networking"],
        "description": "Designs and manages cloud-based infrastructure."
    }
}

st.title("🎓 AI-Based Career Guidance & Skill Recommendation System")

st.write(
    "Find suitable career paths and recommended skills based on your "
    "interests, education and existing skills."
)

st.divider()

# User information
name = st.text_input("👤 Enter your name")

education = st.selectbox(
    "🎓 Select your education",
    [
        "B.Tech",
        "B.Sc",
        "BCA",
        "MCA",
        "M.Tech",
        "Diploma",
        "Intermediate"
    ]
)

interests = st.multiselect(
    "💡 Select your interests",
    [
        "Programming",
        "Technology",
        "Problem Solving",
        "Data Analysis",
        "Mathematics",
        "Artificial Intelligence",
        "Web Development",
        "Design",
        "Cybersecurity",
        "Cloud Computing",
        "Networking"
    ]
)

skills = st.multiselect(
    "🛠️ Select your existing skills",
    [
        "Python",
        "Java",
        "C",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Git",
        "Data Structures",
        "Statistics",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "Pandas",
        "Networking",
        "Linux",
        "AWS",
        "Azure",
        "Docker",
        "Ethical Hacking",
        "Security"
    ]
)

experience = st.slider(
    "💼 Years of experience",
    0,
    10,
    0
)

st.divider()

if st.button("🚀 Get Career Recommendation", use_container_width=True):

    if not interests:
        st.warning("Please select at least one interest.")
    else:

        results = []

        # Calculate career scores
        for career, details in careers.items():

            interest_score = len(
                set(interests) & set(details["interests"])
            )

            skill_score = len(
                set(skills) & set(details["skills"])
            )

            total_score = (interest_score * 2) + skill_score

            results.append(
                (career, total_score, details)
            )

        # Sort by score
        results.sort(
            key=lambda x: x[1],
            reverse=True
        )

        st.success(f"Career recommendations for {name or 'Student'}")

        # Display top 3 careers
        for i, (career, score, details) in enumerate(results[:3], 1):

            st.subheader(f"{i}. {career}")

            st.write(details["description"])

            st.write(f"**Match Score:** {score}")

            # Recommended skills
            missing_skills = [
                skill
                for skill in details["skills"]
                if skill not in skills
            ]

            if missing_skills:
                st.write("📚 **Recommended Skills:**")

                for skill in missing_skills:
                    st.write(f"• {skill}")

            else:
                st.write(
                    "✅ You already have the important skills for this career!"
                )

            st.divider()

        # Overall skill recommendations
        best_career = results[0][2]

        recommended = [
            skill
            for skill in best_career["skills"]
            if skill not in skills
        ]

        st.subheader("📈 Your Skill Development Plan")

        if recommended:
            for skill in recommended:
                st.write(f"➡️ Learn **{skill}**")
        else:
            st.write(
                "🎉 Your current skills match the recommended career very well!"
            )

        st.info(
            "💡 Tip: Build projects, practice coding regularly, "
            "and create a strong GitHub/portfolio profile."
        )