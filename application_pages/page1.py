
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
    if total_ai_errors == 0 or total_decisions == 0:
        return 0
    return 1 - ((errors_caught / total_ai_errors) + (appropriate_trust_decisions / total_decisions)) / 2

def calculate_ai_learning_velocity(delta_proficiency, delta_t_hours_invested):
    if delta_t_hours_invested == 0:
        return 0
    return delta_proficiency / delta_t_hours_invested

def calculate_ai_fluency(s1, s2, s3, s4):
    return 0.1 * s1 + 0.2 * s2 + 0.3 * s3 + 0.4 * s4

def calculate_education_foundation(education_level):
    education_map = {
        "PhD": 1.0,
        "Master's": 0.8,
        "Bachelor's": 0.6,
        "Associate's/Certificate": 0.4,
        "HS + significant coursework": 0.2,
        "Some College": 0.3,
        "Other": 0.0,
    }
    return education_map.get(education_level, 0.0)

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
    return int(max(0, min(score, 100)))

def calculate_wage_premium(ai_skilled_wage, median_wage):
    if median_wage == 0:
        return 0
    return (ai_skilled_wage - median_wage) / median_wage

def calculate_entry_accessibility(education_years_required, experience_years_required):
    return 1 / (1 + 0.1 * (education_years_required + experience_years_required))

def calculate_base_opportunity_score(ai_enhancement, job_growth_normalized, wage_premium, entry_accessibility, w1=0.30, w2=0.30, w3=0.25, w4=0.15):
    return (w1 * ai_enhancement + w2 * job_growth_normalized + w3 * wage_premium + w4 * entry_accessibility)

def calculate_growth_multiplier(current_job_postings, previous_job_postings, lambda_val=0.3):
    if previous_job_postings == 0:
        return 1.0
    return (current_job_postings / previous_job_postings) ** lambda_val

def calculate_regional_multiplier(local_demand, national_avg_demand, remote_work_factor, gamma=0.2):
    if national_avg_demand == 0:
        return 1.0
    return 1 + gamma * (local_demand / national_avg_demand + remote_work_factor - 1)

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
    return 1 + (years_experience / 5)

def calculate_alignment_factor(skills_match_score, max_possible_match, timing_factor):
    if max_possible_match == 0:
        return 0
    return (skills_match_score / max_possible_match) * timing_factor

def calculate_synergy_percentage(vr_score, hr_score, alignment_factor):
    return (vr_score * hr_score * alignment_factor) / 100.0

def calculate_ai_readiness_score(vr_score, hr_score, synergy_percentage, alpha, beta):
    return alpha * vr_score + (1 - alpha) * hr_score + beta * synergy_percentage

def run_page1():
    st.header("AI-Readiness Score Calculator")

    st.sidebar.header("Global Parameters")
    alpha = st.sidebar.slider("Weight on Individual Factors (α)", 0.0, 1.0, 0.6, help="Weight allocated to individual readiness ($V^R$) vs. market opportunity ($H^R$) in the overall AI-Readiness Score.")
    beta = st.sidebar.slider("Synergy Coefficient (β)", 0.0, 1.0, 0.15, help="Coefficient for the Synergy component, amplifying the AI-Readiness Score when individual readiness aligns with market opportunity.")

    st.subheader("Idiosyncratic Readiness ($V^R$) Inputs")
    with st.expander("AI-Fluency Sub-Components"):
        prompting_score = st.slider("Prompting Score", 0.0, 1.0, 0.75)
        tools_score = st.slider("Tools Score", 0.0, 1.0, 0.6)
        understanding_score = st.slider("Understanding Score", 0.0, 1.0, 0.8)
        datalit_score = st.slider("Datalit Score", 0.0, 1.0, 0.9)
        output_quality_with_ai = st.slider("Output Quality with AI", 0, 100, 90)
        output_quality_without_ai = st.slider("Output Quality without AI", 0, 100, 60)
        time_without_ai = st.slider("Time without AI (hours)", 1, 10, 4)
        time_with_ai = st.slider("Time with AI (hours)", 1, 10, 1)
        errors_caught = st.slider("Errors Caught", 0, 50, 15)
        total_ai_errors = st.slider("Total AI Errors", 0, 50, 20)
        appropriate_trust_decisions = st.slider("Appropriate Trust Decisions", 0, 50, 25)
        total_decisions = st.slider("Total Decisions", 0, 50, 30)
        delta_proficiency = st.slider("Delta Proficiency", 0.0, 1.0, 0.3)
        delta_t_hours_invested = st.slider("Delta T Hours Invested", 1, 20, 10)

    with st.expander("Domain-Expertise Sub-Components"):
        education_level = st.selectbox("Education Level", ["PhD", "Master's", "Bachelor's", "Associate's/Certificate", "HS + significant coursework", "Some College", "Other"], index=1)
        years_experience = st.slider("Years Experience", 0, 30, 5)
        portfolio_score = st.slider("Portfolio Score", 0.0, 1.0, 0.85)
        recognition_score = st.slider("Recognition Score", 0.0, 1.0, 0.7)
        credentials_score = st.slider("Credentials Score", 0.0, 1.0, 0.9)

    with st.expander("Adaptive-Capacity Sub-Components"):
        cognitive_flexibility = st.slider("Cognitive Flexibility", 0, 100, 85)
        social_emotional_intelligence = st.slider("Social-Emotional Intelligence", 0, 100, 90)
        strategic_career_management = st.slider("Strategic Career Management", 0, 100, 75)
    
    st.subheader("Systematic Opportunity ($H^R$) Inputs")
    occupational_data = {
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
    }
    occupational_data_df = pd.DataFrame(occupational_data)
    
    target_occupation = st.selectbox("Target Occupation", occupational_data_df['occupation_name'], index=0)
    
    lambda_val = st.slider("Lambda value for Growth Multiplier (lambda)", 0.0, 1.0, 0.3)
    gamma_val = st.slider("Gamma value for Regional Multiplier (gamma)", 0.0, 1.0, 0.2)
    
    st.subheader("Synergy Inputs")
    with st.expander("Individual Skills Data"):
        individual_skills_data = {
            'user_id': [1] * 3,
            'skill_name': ['Python', 'Data Visualization', 'Machine Learning'],
            'individual_skill_score': [70, 60, 40]
        }
        individual_skills_df = pd.DataFrame(individual_skills_data)
        st.dataframe(individual_skills_df)
    
    with st.expander("Required Skills Data"):
        occupation_required_skills_data = {
            'occupation_name': ['Data Analyst with AI Skills'] * 3 + ['AI UX Researcher'] * 3,
            'skill_name': ['Python', 'Data Visualization', 'Machine Learning'] + ['User Research', 'UI Design', 'AI Ethics'],
            'required_skill_score': [80, 70, 60, 90, 80, 75],
            'skill_importance': [0.7, 0.8, 0.5, 0.9, 0.7, 0.6]
        }
        occupation_required_skills_df = pd.DataFrame(occupation_required_skills_data)
        st.dataframe(occupation_required_skills_df[occupation_required_skills_df['occupation_name'] == target_occupation])

    max_possible_match = st.number_input("Max Possible Skills Match", value=100)

    if st.button("Calculate AI-Readiness Score"):
        s1 = calculate_technical_ai_skills(prompting_score, tools_score, understanding_score, datalit_score)
        s2 = calculate_ai_augmented_productivity(output_quality_with_ai, output_quality_without_ai, time_without_ai, time_with_ai)
        s3 = calculate_critical_ai_judgment(errors_caught, total_ai_errors, appropriate_trust_decisions, total_decisions)
        s4 = calculate_ai_learning_velocity(delta_proficiency, delta_t_hours_invested)
        ai_fluency = calculate_ai_fluency(s1, s2, s3, s4)

        education_foundation = calculate_education_foundation(education_level)
        practical_experience = calculate_practical_experience(years_experience)
        specialization_depth = calculate_specialization_depth(portfolio_score, recognition_score, credentials_score)
        domain_expertise = calculate_domain_expertise(education_foundation, practical_experience, specialization_depth)

        adaptive_capacity = calculate_adaptive_capacity(cognitive_flexibility, social_emotional_intelligence, strategic_career_management)

        vr_score = calculate_idiosyncratic_readiness(ai_fluency, domain_expertise, adaptive_capacity)

        occupation_row = occupational_data_df[occupational_data_df['occupation_name'] == target_occupation].iloc[0]
        ai_enhancement = calculate_ai_enhancement_potential(occupation_row['ai_enhancement_score'])
        job_growth_projection = calculate_job_growth_projection(occupation_row['job_growth_rate_g'])
        wage_premium = calculate_wage_premium(occupation_row['ai_skilled_wage'], occupation_row['median_wage'])
        entry_accessibility = calculate_entry_accessibility(occupation_row['education_years_required'], occupation_row['experience_years_required'])
        h_base = calculate_base_opportunity_score(ai_enhancement, job_growth_projection, wage_premium, entry_accessibility)

        growth_multiplier = calculate_growth_multiplier(occupation_row['current_job_postings'], occupation_row['previous_job_postings'], lambda_val)
        regional_multiplier = calculate_regional_multiplier(occupation_row['local_demand'], occupation_row['national_avg_demand'], occupation_row['remote_work_factor'], gamma_val)
        hr_score = calculate_systematic_opportunity(h_base, growth_multiplier, regional_multiplier)

        required_skills_df = occupation_required_skills_df[occupation_required_skills_df['occupation_name'] == target_occupation]
        skills_match_score = calculate_skills_match_score(individual_skills_df, required_skills_df)
        timing_factor = calculate_timing_factor(years_experience)
        alignment_factor = calculate_alignment_factor(skills_match_score, max_possible_match, timing_factor)

        synergy_percentage = calculate_synergy_percentage(vr_score, hr_score, alignment_factor)

        ai_r_score = calculate_ai_readiness_score(vr_score, hr_score, synergy_percentage, alpha, beta)

        st.session_state.vr_score = vr_score
        st.session_state.hr_score = hr_score
        st.session_state.synergy_percentage = synergy_percentage
        st.session_state.ai_r_score = ai_r_score

        st.subheader("AI-Readiness Score Calculation Results")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Idiosyncratic Readiness ($V^R$)", f"{vr_score:.2f}")
        col2.metric("Systematic Opportunity ($H^R$)", f"{hr_score:.2f}")
        col3.metric("Synergy %", f"{synergy_percentage:.2f}")
        col4.metric("AI-Readiness Score (AI-R)", f"{ai_r_score:.2f}")

        # Pie chart for VR components
        vr_components = pd.DataFrame({
            'Component': ['AI-Fluency', 'Domain-Expertise', 'Adaptive-Capacity'],
            'Value': [ai_fluency, domain_expertise, adaptive_capacity]
        })
        fig = go.Figure(data=[go.Pie(labels=vr_components['Component'], values=vr_components['Value'], title='Idiosyncratic Readiness ($V^R$) Breakdown')])
        st.plotly_chart(fig)
