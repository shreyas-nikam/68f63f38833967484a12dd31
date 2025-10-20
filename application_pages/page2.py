
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
    elif education_level == "Master\\'s":
        return 0.8
    elif education_level == "Bachelor\\'s":
        return 0.6
    elif education_level == "Associate\\'s/Certificate":
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

def calculate_synergy_percentage(vr_score, hr_score, alignment_factor):
    return (vr_score * hr_score * alignment_factor) / 100.0

def calculate_ai_readiness_score(vr_score, hr_score, synergy_percentage, alpha, beta):
    return alpha * vr_score + (1-alpha) * hr_score + beta * synergy_percentage

def simulate_pathway_impact(current_ai_fluency, current_domain_expertise, current_adaptive_capacity, pathway_type, impact_ai_fluency, impact_domain_expertise, impact_adaptive_capacity, completion_score=1.0, mastery_score=1.0):
    ai_fluency = current_ai_fluency + impact_ai_fluency * completion_score * mastery_score
    domain_expertise = current_domain_expertise + impact_domain_expertise * completion_score * mastery_score
    adaptive_capacity = current_adaptive_capacity + impact_adaptive_capacity * completion_score * mastery_score

    ai_fluency = min(ai_fluency, 1.0)
    domain_expertise = min(domain_expertise, 1.0)
    adaptive_capacity = min(adaptive_capacity, 1.0)

    return ai_fluency, domain_expertise, adaptive_capacity

def run_page2():
    st.header("What-If Scenario Analysis")

    if 'vr_score' not in st.session_state or st.session_state.vr_score == 0:
        st.warning("Please calculate the AI-Readiness Score on the 'AI-Readiness Score' page first.")
        return

    learning_pathways_df = pd.DataFrame({
        'pathway_id': [1, 2, 3],
        'pathway_name': ['Prompt Engineering Fundamentals', 'AI for Financial Analysis', 'Human-AI Collaboration'],
        'pathway_type': ['AI-Fluency', 'Domain+AI Integration', 'Adaptive Capacity'],
        'impact_ai_fluency': [0.2, 0.1, 0.05],
        'impact_domain_expertise': [0.05, 0.2, 0.1],
        'impact_adaptive_capacity': [0.1, 0.05, 0.2]
    })

    st.session_state.pathway = st.selectbox("Select Learning Pathway", learning_pathways_df['pathway_name'].tolist(), index=0)
    st.session_state.completion_score = st.slider("Pathway Completion Score", 0.0, 1.0, 1.0)
    st.session_state.mastery_score = st.slider("Pathway Mastery Score", 0.0, 1.0, 1.0)

    if st.button("Simulate Pathway Impact"):
        selected_pathway = learning_pathways_df[learning_pathways_df['pathway_name'] == st.session_state.pathway].iloc[0]

        # Get current VR components
        current_ai_fluency = st.session_state.vr_components.get('AI-Fluency', 0)
        current_domain_expertise = st.session_state.vr_components.get('Domain-Expertise', 0)
        current_adaptive_capacity = st.session_state.vr_components.get('Adaptive-Capacity', 0)

        # Simulate impact
        new_ai_fluency, new_domain_expertise, new_adaptive_capacity = simulate_pathway_impact(
            current_ai_fluency, current_domain_expertise, current_adaptive_capacity,
            selected_pathway['pathway_type'],
            selected_pathway['impact_ai_fluency'],
            selected_pathway['impact_domain_expertise'],
            selected_pathway['impact_adaptive_capacity'],
            st.session_state.completion_score,
            st.session_state.mastery_score
        )

        # Calculate new VR score
        st.session_state.vr_score_new = calculate_idiosyncratic_readiness(new_ai_fluency, new_domain_expertise, new_adaptive_capacity)

        # HR score remains the same
        st.session_state.hr_score_new = st.session_state.hr_score

        # Recalculate Synergy and AI-R Score
        st.session_state.synergy_percentage_new = calculate_synergy_percentage(st.session_state.vr_score_new, st.session_state.hr_score_new, st.session_state.synergy_percentage / (st.session_state.vr_score * st.session_state.hr_score / 100) if st.session_state.vr_score * st.session_state.hr_score != 0 else 0)
        st.session_state.ai_r_score_new = calculate_ai_readiness_score(st.session_state.vr_score_new, st.session_state.hr_score_new, st.session_state.synergy_percentage_new, st.session_state.alpha, st.session_state.beta)

    st.header("Simulation Results")

    if 'ai_r_score_new' in st.session_state:
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Current AI-Readiness Score", f"{st.session_state.ai_r_score:.2f}")
            st.metric("Current Idiosyncratic Readiness ($V^R$)", f"{st.session_state.vr_score:.2f}")
            st.metric("Current Systematic Opportunity ($H^R$)", f"{st.session_state.hr_score:.2f}")

        with col2:
            st.metric("Projected AI-Readiness Score", f"{st.session_state.ai_r_score_new:.2f}", delta=f"{st.session_state.ai_r_score_new - st.session_state.ai_r_score:.2f}")
            st.metric("Projected Idiosyncratic Readiness ($V^R$)", f"{st.session_state.vr_score_new:.2f}", delta=f"{st.session_state.vr_score_new - st.session_state.vr_score:.2f}")
            st.metric("Projected Systematic Opportunity ($H^R$)", f"{st.session_state.hr_score_new:.2f}")

        fig = go.Figure(data=[
            go.Bar(name='Current', x=['AI-R', 'V^R', 'H^R'], y=[st.session_state.ai_r_score, st.session_state.vr_score, st.session_state.hr_score]),
            go.Bar(name='Projected', x=['AI-R', 'V^R', 'H^R'], y=[st.session_state.ai_r_score_new, st.session_state.vr_score_new, st.session_state.hr_score_new])
        ])
        fig.update_layout(barmode='group', title_text='Current vs. Projected Scores')
        st.plotly_chart(fig, use_container_width=True)
