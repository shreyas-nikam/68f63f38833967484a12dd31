
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def calculate_technical_ai_skills(prompting, tools, understanding, data_lit):
    return (prompting + tools + understanding + data_lit) / 4

def calculate_ai_augmented_productivity(output_quality_with_ai, output_quality_without_ai, time_without_ai, time_with_ai):
    if output_quality_without_ai == 0 or time_with_ai == 0:
        return 0
    return (output_quality_with_ai / output_quality_without_ai) * (time_without_ai / time_with_ai)

def calculate_critical_ai_judgment(errors_caught, total_ai_errors, appropriate_trust_decisions, total_decisions):
    if total_ai_errors == 0 and total_decisions == 0:
        return 0.0
    if total_ai_errors == 0:
        return 1 - (appropriate_trust_decisions / total_decisions) / 2
    if total_decisions == 0:
        return 1 - (errors_caught / total_ai_errors) / 2
    return 1 - (errors_caught / total_ai_errors + appropriate_trust_decisions / total_decisions) / 2

def calculate_ai_learning_velocity(delta_proficiency, delta_t_hours_invested):
    if delta_t_hours_invested == 0:
        return 0.0
    return delta_proficiency / delta_t_hours_invested

def calculate_ai_fluency(s1, s2, s3, s4):
    return 0.1 * s1 + 0.2 * s2 + 0.3 * s3 + 0.4 * s4

def calculate_education_foundation(education_level):
    if education_level == "PhD":
        return 1.0
    elif education_level == "Master's":
        return 0.8
    elif education_level == "Bachelor's":
        return 0.6
    elif education_level == "Associate's/Certificate":
        return 0.4
    elif education_level == "HS + significant coursework":
        return 0.2
    elif education_level == "Some College":
        return 0.3
    else:
        return 0.0

def calculate_practical_experience(years_experience, gamma=0.15):
    return years_experience / (years_experience + (1 / gamma))

def calculate_specialization_depth(portfolio_score, recognition_score, credentials_score):
    return (portfolio_score + recognition_score + credentials_score) / 3

def calculate_domain_expertise(education_foundation, practical_experience, specialization_depth):
    return 0.125 * education_foundation + 0.25 * practical_experience + 0.625 * specialization_depth

def calculate_adaptive_capacity(cognitive_flexibility, social_emotional_intelligence, strategic_career_management):
    return (cognitive_flexibility + social_emotional_intelligence + strategic_career_management) / 3

def calculate_idiosyncratic_readiness(ai_fluency, domain_expertise, adaptive_capacity, w1=0.45, w2=0.35, w3=0.20):
    return (w1 * ai_fluency) + (w2 * domain_expertise) + (w3 * adaptive_capacity)

def calculate_ai_enhancement_potential(ai_enhancement_score):
    return ai_enhancement_score

def calculate_job_growth_projection(growth_rate_g):
    score = 50 + (growth_rate_g * 100)
    score = max(0, min(score, 100))
    return int(score)

def calculate_wage_premium(ai_skilled_wage, median_wage):
    if median_wage == 0:
        return 0
    return (ai_skilled_wage - median_wage) / median_wage

def calculate_entry_accessibility(education_years_required, experience_years_required):
    return 1 / (1 + 0.1 * (education_years_required + experience_years_required))

def calculate_base_opportunity_score(ai_enhancement, job_growth_normalized, wage_premium, entry_accessibility, w1=0.30, w2=0.30, w3=0.25, w4=0.15):
    return (w1 * ai_enhancement +
            w2 * job_growth_normalized +
            w3 * wage_premium +
            w4 * entry_accessibility)

def calculate_growth_multiplier(current_job_postings, previous_job_postings, lambda_val=0.3):
    if previous_job_postings == 0:
        return 1.0
    return (current_job_postings / previous_job_postings)**lambda_val

def calculate_regional_multiplier(local_demand, national_avg_demand, remote_work_factor, gamma=0.2):
    if national_avg_demand == 0:
        return 1.0
    return 1 + gamma * (local_demand/national_avg_demand + remote_work_factor - 1)

def calculate_systematic_opportunity(h_base, growth_multiplier, regional_multiplier):
    return h_base * growth_multiplier * regional_multiplier

def calculate_skills_match_score(user_skills_df, required_skills_df):
    if user_skills_df.empty or required_skills_df.empty:
        return 0

    merged_df = pd.merge(user_skills_df, required_skills_df, on='skill_name', how='inner')

    if merged_df.empty:
        return 0

    weighted_sum = 0
    total_importance = required_skills_df['skill_importance'].sum()

    for _, row in merged_df.iterrows():
        weighted_sum += (min(row['individual_skill_score'], row['required_skill_score']) / 100) * row['skill_importance']

    if total_importance == 0:
        return 0

    return (weighted_sum / total_importance) * 100

def calculate_timing_factor(years_experience):
    if years_experience <= 0:
        return 1
    else:
        return 1 + (years_experience / 5)

def calculate_alignment_factor(skills_match_score, max_possible_match, timing_factor):
    if max_possible_match == 0:
        return 0
    return (skills_match_score / max_possible_match) * timing_factor

def calculate_synergy_percentage(vr_score, hr_score, alignment_factor):
    return (vr_score * hr_score * alignment_factor) / 100.0

def calculate_ai_readiness_score(vr_score, hr_score, synergy_percentage, alpha, beta):
    return alpha * vr_score + (1-alpha) * hr_score + beta * synergy_percentage

def run_page1():
    st.header("AI-Readiness Score Calculation")

    # Initialize session state
    if 'alpha' not in st.session_state:
        st.session_state.alpha = 0.6
    if 'beta' not in st.session_state:
        st.session_state.beta = 0.15
    if 'prompting_score' not in st.session_state:
        st.session_state.prompting_score = 0.75
    if 'tools_score' not in st.session_state:
        st.session_state.tools_score = 0.6
    if 'understanding_score' not in st.session_state:
        st.session_state.understanding_score = 0.8
    if 'datalit_score' not in st.session_state:
        st.session_state.datalit_score = 0.9
    if 'output_quality_with_ai' not in st.session_state:
        st.session_state.output_quality_with_ai = 90
    if 'output_quality_without_ai' not in st.session_state:
        st.session_state.output_quality_without_ai = 60
    if 'time_without_ai' not in st.session_state:
        st.session_state.time_without_ai = 4
    if 'time_with_ai' not in st.session_state:
        st.session_state.time_with_ai = 1
    if 'errors_caught' not in st.session_state:
        st.session_state.errors_caught = 15
    if 'total_ai_errors' not in st.session_state:
        st.session_state.total_ai_errors = 20
    if 'appropriate_trust_decisions' not in st.session_state:
        st.session_state.appropriate_trust_decisions = 25
    if 'total_decisions' not in st.session_state:
        st.session_state.total_decisions = 30
    if 'delta_proficiency' not in st.session_state:
        st.session_state.delta_proficiency = 0.3
    if 'delta_t_hours_invested' not in st.session_state:
        st.session_state.delta_t_hours_invested = 10
    if 'education_level' not in st.session_state:
        st.session_state.education_level = "Master's"
    if 'years_experience' not in st.session_state:
        st.session_state.years_experience = 5
    if 'portfolio_score' not in st.session_state:
        st.session_state.portfolio_score = 0.85
    if 'recognition_score' not in st.session_state:
        st.session_state.recognition_score = 0.7
    if 'credentials_score' not in st.session_state:
        st.session_state.credentials_score = 0.9
    if 'cognitive_flexibility' not in st.session_state:
        st.session_state.cognitive_flexibility = 85
    if 'social_emotional_intelligence' not in st.session_state:
        st.session_state.social_emotional_intelligence = 90
    if 'strategic_career_management' not in st.session_state:
        st.session_state.strategic_career_management = 75
    if 'target_occupation' not in st.session_state:
        st.session_state.target_occupation = 'Data Analyst with AI Skills'
    if 'lambda_val' not in st.session_state:
        st.session_state.lambda_val = 0.3
    if 'gamma_val' not in st.session_state:
        st.session_state.gamma_val = 0.2
    if 'max_possible_skills_match' not in st.session_state:
        st.session_state.max_possible_skills_match = 100
    if 'individual_skills' not in st.session_state:
        st.session_state.individual_skills = pd.DataFrame({
            'skill_name': ['Python', 'Data Visualization', 'Machine Learning'],
            'individual_skill_score': [70, 60, 40]
        })
    if 'vr_score' not in st.session_state:
        st.session_state.vr_score = 0
    if 'hr_score' not in st.session_state:
        st.session_state.hr_score = 0
    if 'synergy_percentage' not in st.session_state:
        st.session_state.synergy_percentage = 0
    if 'ai_r_score' not in st.session_state:
        st.session_state.ai_r_score = 0
    if 'h_base_components' not in st.session_state:
        st.session_state.h_base_components = {}
    if 'vr_components' not in st.session_state:
        st.session_state.vr_components = {}


    st.sidebar.header("Global Parameters")
    st.session_state.alpha = st.sidebar.slider("Weight on Individual Factors (\\\\alpha)", 0.0, 1.0, st.session_state.alpha, help="Weight allocated to individual readiness ($V^R$) vs. market opportunity ($H^R$) in the overall AI-Readiness Score.")
    st.session_state.beta = st.sidebar.slider("Synergy Coefficient (\\\\beta)", 0.0, 1.0, st.session_state.beta, help="Coefficient for the Synergy component, amplifying the AI-Readiness Score when individual readiness aligns with market opportunity.")

    st.subheader("Input Parameters")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.expander("Idiosyncratic Readiness ($V^R$) Inputs", expanded=True):
            st.markdown("**AI-Fluency**")
            st.session_state.prompting_score = st.slider("Prompting Score", 0.0, 1.0, st.session_state.prompting_score)
            st.session_state.tools_score = st.slider("Tools Score", 0.0, 1.0, st.session_state.tools_score)
            st.session_state.understanding_score = st.slider("Understanding Score", 0.0, 1.0, st.session_state.understanding_score)
            st.session_state.datalit_score = st.slider("Datalit Score", 0.0, 1.0, st.session_state.datalit_score)
            st.session_state.output_quality_with_ai = st.slider("Output Quality with AI", 0, 100, st.session_state.output_quality_with_ai)
            st.session_state.output_quality_without_ai = st.slider("Output Quality without AI", 0, 100, st.session_state.output_quality_without_ai)
            st.session_state.time_without_ai = st.number_input("Time without AI (hours)", value=st.session_state.time_without_ai)
            st.session_state.time_with_ai = st.number_input("Time with AI (hours)", value=st.session_state.time_with_ai)
            st.session_state.errors_caught = st.slider("Errors Caught", 0, 100, st.session_state.errors_caught)
            st.session_state.total_ai_errors = st.slider("Total AI Errors", 0, 100, st.session_state.total_ai_errors)
            st.session_state.appropriate_trust_decisions = st.slider("Appropriate Trust Decisions", 0, 100, st.session_state.appropriate_trust_decisions)
            st.session_state.total_decisions = st.slider("Total Decisions", 0, 100, st.session_state.total_decisions)
            st.session_state.delta_proficiency = st.slider("Delta Proficiency", 0.0, 1.0, st.session_state.delta_proficiency)
            st.session_state.delta_t_hours_invested = st.number_input("Delta T Hours Invested", value=st.session_state.delta_t_hours_invested)
            
            st.markdown("**Domain-Expertise**")
            st.session_state.education_level = st.selectbox("Education Level", ["PhD", "Master's", "Bachelor's", "Associate's/Certificate", "HS + significant coursework", "Some College", "Other"], index=1)
            st.session_state.years_experience = st.number_input("Years Experience", value=st.session_state.years_experience)
            st.session_state.portfolio_score = st.slider("Portfolio Score", 0.0, 1.0, st.session_state.portfolio_score)
            st.session_state.recognition_score = st.slider("Recognition Score", 0.0, 1.0, st.session_state.recognition_score)
            st.session_state.credentials_score = st.slider("Credentials Score", 0.0, 1.0, st.session_state.credentials_score)

            st.markdown("**Adaptive-Capacity**")
            st.session_state.cognitive_flexibility = st.slider("Cognitive Flexibility", 0, 100, st.session_state.cognitive_flexibility)
            st.session_state.social_emotional_intelligence = st.slider("Social-Emotional Intelligence", 0, 100, st.session_state.social_emotional_intelligence)
            st.session_state.strategic_career_management = st.slider("Strategic Career Management", 0, 100, st.session_state.strategic_career_management)

    with col2:
        with st.expander("Systematic Opportunity ($H^R$) Inputs", expanded=True):
            occupational_data_df = pd.DataFrame({
                'occupation_name': ['Data Analyst with AI Skills', 'AI UX Researcher', 'AI Prompt Engineer', 'Data Scientist', 'Nursing Informatics', 'Medical Coding'],
                'ai_enhancement_score': [0.8, 0.9, 0.7, 0.95, 0.75, 0.6],
                'job_growth_rate_g': [0.25, 0.35, 0.4, 0.3, 0.2, 0.15],
                'ai_skilled_wage': [120000, 130000, 140000, 150000, 110000, 90000],
                'median_wage': [90000, 95000, 100000, 110000, 85000, 70000],
                'education_years_required': [4, 4, 4, 4, 4, 2],
                'experience_years_required': [2, 3, 1, 3, 2, 0],
                'current_job_postings': [500, 400, 600, 700, 300, 200],
                'previous_job_postings': [400, 300, 450, 500, 250, 180],
                'remote_work_factor': [0.6, 0.7, 0.8, 0.5, 0.4, 0.3],
                'local_demand': [1.2, 1.1, 1.3, 1.4, 1.0, 0.9],
                'national_avg_demand': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            })
            st.session_state.target_occupation = st.selectbox("Target Occupation", occupational_data_df['occupation_name'].tolist(), index=0, help="Select a target occupation to calculate your market opportunity ($H^R$) based on its attributes.")
            
            st.markdown("**Market Multiplier Parameters**")
            st.session_state.lambda_val = st.slider("Lambda value for Growth Multiplier (lambda)", 0.0, 1.0, st.session_state.lambda_val, help="Adjust $\\\\lambda$ to dampen volatility in job posting growth.")
            st.session_state.gamma_val = st.slider("Gamma value for Regional Multiplier (gamma)", 0.0, 1.0, st.session_state.gamma_val, help="Adjust $\\\\gamma$ for regional market influence.")

        with st.expander("Synergy Inputs", expanded=True):
            st.markdown("**Individual Skills Data**")
            st.session_state.individual_skills = st.data_editor(st.session_state.individual_skills, num_rows="dynamic")
            st.session_state.max_possible_skills_match = st.number_input("Max Possible Skills Match", value=st.session_state.max_possible_skills_match)

    with col3:
        if st.button("Calculate AI-Readiness Score"):
            # VR Calculation
            s1 = calculate_technical_ai_skills(st.session_state.prompting_score, st.session_state.tools_score, st.session_state.understanding_score, st.session_state.datalit_score)
            s2 = calculate_ai_augmented_productivity(st.session_state.output_quality_with_ai, st.session_state.output_quality_without_ai, st.session_state.time_without_ai, st.session_state.time_with_ai)
            s3 = calculate_critical_ai_judgment(st.session_state.errors_caught, st.session_state.total_ai_errors, st.session_state.appropriate_trust_decisions, st.session_state.total_decisions)
            s4 = calculate_ai_learning_velocity(st.session_state.delta_proficiency, st.session_state.delta_t_hours_invested)
            ai_fluency = calculate_ai_fluency(s1, s2, s3, s4)
            
            education_foundation = calculate_education_foundation(st.session_state.education_level)
            practical_experience = calculate_practical_experience(st.session_state.years_experience)
            specialization_depth = calculate_specialization_depth(st.session_state.portfolio_score, st.session_state.recognition_score, st.session_state.credentials_score)
            domain_expertise = calculate_domain_expertise(education_foundation, practical_experience, specialization_depth)

            adaptive_capacity = calculate_adaptive_capacity(st.session_state.cognitive_flexibility, st.session_state.social_emotional_intelligence, st.session_state.strategic_career_management)

            st.session_state.vr_score = calculate_idiosyncratic_readiness(ai_fluency, domain_expertise, adaptive_capacity)
            st.session_state.vr_components = {'AI-Fluency': ai_fluency, 'Domain-Expertise': domain_expertise, 'Adaptive-Capacity': adaptive_capacity}

            # HR Calculation
            occupation_data = occupational_data_df[occupational_data_df['occupation_name'] == st.session_state.target_occupation].iloc[0]
            ai_enhancement = calculate_ai_enhancement_potential(occupation_data['ai_enhancement_score'])
            job_growth_projection = calculate_job_growth_projection(occupation_data['job_growth_rate_g'])
            wage_premium = calculate_wage_premium(occupation_data['ai_skilled_wage'], occupation_data['median_wage'])
            entry_accessibility = calculate_entry_accessibility(occupation_data['education_years_required'], occupation_data['experience_years_required'])
            h_base = calculate_base_opportunity_score(ai_enhancement, job_growth_projection, wage_premium, entry_accessibility)
            st.session_state.h_base_components = {'AI-Enhancement Potential': ai_enhancement, 'Job Growth Projection': job_growth_projection, 'Wage Premium': wage_premium, 'Entry Accessibility': entry_accessibility}

            growth_multiplier = calculate_growth_multiplier(occupation_data['current_job_postings'], occupation_data['previous_job_postings'], st.session_state.lambda_val)
            regional_multiplier = calculate_regional_multiplier(occupation_data['local_demand'], occupation_data['national_avg_demand'], occupation_data['remote_work_factor'], st.session_state.gamma_val)
            st.session_state.hr_score = calculate_systematic_opportunity(h_base, growth_multiplier, regional_multiplier)

            # Synergy Calculation
            occupation_required_skills_df = pd.DataFrame({
                'occupation_name': ['Data Analyst with AI Skills'] * 3 + ['AI UX Researcher'] * 3,
                'skill_name': ['Python', 'Data Visualization', 'Machine Learning'] + ['User Research', 'UI Design', 'AI Ethics'],
                'required_skill_score': [80, 70, 60, 90, 80, 75],
                'skill_importance': [0.7, 0.8, 0.5, 0.9, 0.7, 0.6]
            })
            required_skills = occupation_required_skills_df[occupation_required_skills_df['occupation_name'] == st.session_state.target_occupation]
            skills_match_score = calculate_skills_match_score(st.session_state.individual_skills, required_skills)
            timing_factor = calculate_timing_factor(st.session_state.years_experience)
            alignment_factor = calculate_alignment_factor(skills_match_score, st.session_state.max_possible_skills_match, timing_factor)
            st.session_state.synergy_percentage = calculate_synergy_percentage(st.session_state.vr_score, st.session_state.hr_score, alignment_factor)

            # AI-R Score
            st.session_state.ai_r_score = calculate_ai_readiness_score(st.session_state.vr_score, st.session_state.hr_score, st.session_state.synergy_percentage, st.session_state.alpha, st.session_state.beta)

        st.header("Results")
        st.metric("AI-Readiness Score", f"{st.session_state.ai_r_score:.2f}")
        st.metric("Idiosyncratic Readiness ($V^R$)", f"{st.session_state.vr_score:.2f}")
        st.metric("Systematic Opportunity ($H^R$)", f"{st.session_state.hr_score:.2f}")
        st.metric("Synergy %", f"{st.session_state.synergy_percentage:.2f}%")

        if st.session_state.vr_components:
            fig = go.Figure(data=[go.Pie(labels=list(st.session_state.vr_components.keys()), values=list(st.session_state.vr_components.values()), title='VR Components Contribution')])
            st.plotly_chart(fig, use_container_width=True)

        if st.session_state.h_base_components:
            fig = go.Figure(data=[go.Bar(x=list(st.session_state.h_base_components.keys()), y=list(st.session_state.h_base_components.values()))])
            fig.update_layout(title_text='H_base Components Breakdown')
            st.plotly_chart(fig, use_container_width=True)
