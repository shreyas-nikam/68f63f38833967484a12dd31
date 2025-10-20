import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from .page1 import (
    calculate_technical_ai_skills, calculate_ai_augmented_productivity, calculate_critical_ai_judgment,
    calculate_ai_learning_velocity, calculate_ai_fluency, calculate_education_foundation,
    calculate_practical_experience, calculate_specialization_depth, calculate_domain_expertise,
    calculate_adaptive_capacity, calculate_idiosyncratic_readiness, calculate_job_growth_projection,
    calculate_wage_premium, calculate_entry_accessibility, calculate_base_opportunity_score,
    calculate_growth_multiplier, calculate_regional_multiplier, calculate_systematic_opportunity,
    calculate_skills_match_score, calculate_timing_factor, calculate_alignment_factor,
    calculate_synergy_percentage, calculate_ai_readiness_score
)

def simulate_pathway_impact(current_ai_fluency, current_domain_expertise, current_adaptive_capacity,
                           pathway_type, impact_ai_fluency, impact_domain_expertise,
                           impact_adaptive_capacity, completion_score=1.0, mastery_score=1.0):
    ai_fluency = current_ai_fluency + impact_ai_fluency * completion_score * mastery_score
    domain_expertise = current_domain_expertise + impact_domain_expertise * completion_score * mastery_score
    adaptive_capacity = current_adaptive_capacity + impact_adaptive_capacity * completion_score * mastery_score
    ai_fluency = min(ai_fluency, 1.0)
    domain_expertise = min(domain_expertise, 1.0)
    adaptive_capacity = min(adaptive_capacity, 1.0)
    return ai_fluency, domain_expertise, adaptive_capacity

def run_page2():
    st.header("What-If Scenario Analysis")

    learning_pathways_df = pd.DataFrame({
        'pathway_id': [1, 2, 3], 'pathway_name': ['Prompt Engineering Fundamentals', 'AI for Financial Analysis', 'Human-AI Collaboration'],
        'pathway_type': ['AI-Fluency', 'Domain+AI Integration', 'Adaptive Capacity'],
        'impact_ai_fluency': [0.2, 0.1, 0.05], 'impact_domain_expertise': [0.05, 0.2, 0.1],
        'impact_adaptive_capacity': [0.1, 0.05, 0.2]
    })
    selected_pathway = st.selectbox("Select Learning Pathway", learning_pathways_df['pathway_name'])
    pathway_completion_score = st.slider("Pathway Completion Score", 0.0, 1.0, 1.0)
    pathway_mastery_score = st.slider("Pathway Mastery Score", 0.0, 1.0, 1.0)

    if st.button("Simulate Pathway Impact"):
        # This is a simplified example. In a real app, you'd get the current scores from the session state or re-calculate them.
        # For simplicity, we'll use some default values here.
        current_ai_fluency = 0.5
        current_domain_expertise = 0.6
        current_adaptive_capacity = 0.7
        current_vr_score = calculate_idiosyncratic_readiness(current_ai_fluency, current_domain_expertise, current_adaptive_capacity)
        current_hr_score = 0.8 # Placeholder
        current_synergy = 10 # Placeholder
        current_ai_r_score = calculate_ai_readiness_score(current_vr_score, current_hr_score, current_synergy, 0.6, 0.15)

        pathway_data = learning_pathways_df[learning_pathways_df['pathway_name'] == selected_pathway].iloc[0]

        new_ai_fluency, new_domain_expertise, new_adaptive_capacity = simulate_pathway_impact(
            current_ai_fluency, current_domain_expertise, current_adaptive_capacity,
            pathway_data['pathway_type'], pathway_data['impact_ai_fluency'],
            pathway_data['impact_domain_expertise'], pathway_data['impact_adaptive_capacity'],
            pathway_completion_score, pathway_mastery_score
        )

        new_vr_score = calculate_idiosyncratic_readiness(new_ai_fluency, new_domain_expertise, new_adaptive_capacity)
        # For this example, we assume HR and Synergy don't change. In a real app, they might.
        new_hr_score = current_hr_score
        new_synergy = current_synergy
        new_ai_r_score = calculate_ai_readiness_score(new_vr_score, new_hr_score, new_synergy, 0.6, 0.15)


        st.subheader("Simulation Results")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Current AI-R Score", f"{current_ai_r_score:.2f}")
            st.metric("Current VR Score", f"{current_vr_score:.2f}")
            st.metric("Current HR Score", f"{current_hr_score:.2f}")
        with col2:
            st.metric("Projected AI-R Score", f"{new_ai_r_score:.2f}")
            st.metric("Projected VR Score", f"{new_vr_score:.2f}")
            st.metric("Projected HR Score", f"{new_hr_score:.2f}")

        # Comparison Chart
        fig = go.Figure(data=[
            go.Bar(name='Current', x=['AI-R', 'VR', 'HR'], y=[current_ai_r_score, current_vr_score, current_hr_score]),
            go.Bar(name='Projected', x=['AI-R', 'VR', 'HR'], y=[new_ai_r_score, new_vr_score, new_hr_score])
        ])
        fig.update_layout(barmode='group', title_text='Current vs. Projected Scores')
        st.plotly_chart(fig, use_container_width=True)