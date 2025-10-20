
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- Data Generation ---
def generate_data():
    learning_pathways_data = {
        'pathway_id': [1, 2, 3],
        'pathway_name': ['Prompt Engineering Fundamentals', 'AI for Financial Analysis', 'Human-AI Collaboration'],
        'pathway_type': ['AI-Fluency', 'Domain+AI Integration', 'Adaptive Capacity'],
        'impact_ai_fluency': [0.2, 0.1, 0.05],
        'impact_domain_expertise': [0.05, 0.2, 0.1],
        'impact_adaptive_capacity': [0.1, 0.05, 0.2]
    }
    learning_pathways_df = pd.DataFrame(learning_pathways_data)
    return learning_pathways_df

# --- Calculation Functions ---
def simulate_pathway_impact(current_ai_fluency, current_domain_expertise, current_adaptive_capacity, pathway_type, impact_ai_fluency, impact_domain_expertise, impact_adaptive_capacity, completion_score=1.0, mastery_score=1.0):
    ai_fluency = current_ai_fluency + impact_ai_fluency * completion_score * mastery_score
    domain_expertise = current_domain_expertise + impact_domain_expertise * completion_score * mastery_score
    adaptive_capacity = current_adaptive_capacity + impact_adaptive_capacity * completion_score * mastery_score

    ai_fluency = min(ai_fluency, 1.0)
    domain_expertise = min(domain_expertise, 1.0)
    adaptive_capacity = min(adaptive_capacity, 1.0)

    return ai_fluency, domain_expertise, adaptive_capacity

def calculate_idiosyncratic_readiness(ai_fluency, domain_expertise, adaptive_capacity, w1=0.45, w2=0.35, w3=0.20):
    return (w1 * ai_fluency) + (w2 * domain_expertise) + (w3 * adaptive_capacity)

def calculate_synergy_percentage(vr_score, hr_score, alignment_factor):
    if 'alignment_factor' in st.session_state:
         return (vr_score * hr_score * st.session_state.alignment_factor) / 100.0
    return (vr_score * hr_score * 0.5) / 100.0

def calculate_ai_readiness_score(vr_score, hr_score, synergy_percentage, alpha, beta):
    return alpha * vr_score + (1-alpha) * hr_score + beta * synergy_percentage

def run_page2():
    st.header("What-If Scenario Analysis")
    
    learning_pathways_df = generate_data()

    if 'ai_r_score' not in st.session_state:
        st.warning("Please calculate your AI-Readiness Score on the 'AI-Readiness Score Calculator' page first.")
        return

    st.sidebar.title("Simulation Parameters")
    pathway_name = st.sidebar.selectbox("Select Learning Pathway", learning_pathways_df['pathway_name'].tolist())
    completion_score = st.sidebar.slider("Pathway Completion Score", 0.0, 1.0, 1.0)
    mastery_score = st.sidebar.slider("Pathway Mastery Score", 0.0, 1.0, 1.0)
    
    pathway_data = learning_pathways_df[learning_pathways_df['pathway_name'] == pathway_name].iloc[0]

    if st.sidebar.button("Simulate Pathway Impact"):
        new_ai_fluency, new_domain_expertise, new_adaptive_capacity = simulate_pathway_impact(
            st.session_state.ai_fluency,
            st.session_state.domain_expertise,
            st.session_state.adaptive_capacity,
            pathway_data['pathway_type'],
            pathway_data['impact_ai_fluency'],
            pathway_data['impact_domain_expertise'],
            pathway_data['impact_adaptive_capacity'],
            completion_score,
            mastery_score
        )
        
        new_vr_score = calculate_idiosyncratic_readiness(new_ai_fluency, new_domain_expertise, new_adaptive_capacity)
        
        new_hr_score = st.session_state.hr_score
        
        if 'alignment_factor' not in st.session_state:
            st.session_state.alignment_factor = 0.5
            
        new_synergy_percentage = calculate_synergy_percentage(new_vr_score, new_hr_score, st.session_state.alignment_factor)
        new_ai_r_score = calculate_ai_readiness_score(new_vr_score, new_hr_score, new_synergy_percentage, st.session_state.get('alpha', 0.6), st.session_state.get('beta', 0.15))

        st.session_state.new_vr_score = new_vr_score
        st.session_state.new_hr_score = new_hr_score
        st.session_state.new_synergy_percentage = new_synergy_percentage
        st.session_state.new_ai_r_score = new_ai_r_score
        
    st.subheader("Current Scores")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("$V^R$ Score", f"{st.session_state.vr_score:.2f}")
    with c2:
        st.metric("$H^R$ Score", f"{st.session_state.hr_score:.2f}")
    with c3:
        st.metric("Synergy %", f"{st.session_state.synergy_percentage:.2f}")
    with c4:
        st.metric("AI-R Score", f"{st.session_state.ai_r_score:.2f}")

    if 'new_ai_r_score' in st.session_state:
        st.subheader("Projected Scores After Pathway")
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric("New $V^R$ Score", f"{st.session_state.new_vr_score:.2f}", delta=f"{st.session_state.new_vr_score - st.session_state.vr_score:.2f}")
        with c2:
            st.metric("New $H^R$ Score", f"{st.session_state.new_hr_score:.2f}", delta=f"{st.session_state.new_hr_score - st.session_state.hr_score:.2f}")
        with c3:
            st.metric("New Synergy %", f"{st.session_state.new_synergy_percentage:.2f}", delta=f"{st.session_state.new_synergy_percentage - st.session_state.synergy_percentage:.2f}")
        with c4:
            st.metric("New AI-R Score", f"{st.session_state.new_ai_r_score:.2f}", delta=f"{st.session_state.new_ai_r_score - st.session_state.ai_r_score:.2f}")

        st.subheader("Comparison Chart")
        
        categories = ['$V^R$ Score', '$H^R$ Score', 'AI-R Score']
        current_scores = [st.session_state.vr_score, st.session_state.hr_score, st.session_state.ai_r_score]
        projected_scores = [st.session_state.new_vr_score, st.session_state.new_hr_score, st.session_state.new_ai_r_score]

        fig = go.Figure(data=[
            go.Bar(name='Current', x=categories, y=current_scores),
            go.Bar(name='Projected', x=categories, y=projected_scores)
        ])
        fig.update_layout(barmode='group', title_text='Current vs. Projected Scores')
        st.plotly_chart(fig)
