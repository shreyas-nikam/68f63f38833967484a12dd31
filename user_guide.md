id: 68f63f38833967484a12dd31_user_guide
summary: AI-Readiness score - gemini-2.5-pro User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Navigating Your AI Career with the AI-Readiness Score

## Introduction to the AI Career Navigator
Duration: 3:00

Welcome to the AI Career Navigator & Pathway Planner! In an era where Artificial Intelligence is transforming industries, understanding your preparedness for an AI-driven career is more important than ever. This application is designed to help you quantify your readiness, explore potential career paths, and plan your professional development strategically.

The core of this application is the **AI-Readiness Score (AI-R)**, a comprehensive metric that evaluates your professional profile against the demands of the modern job market. The score is calculated using a sophisticated formula that balances your individual strengths with market opportunities.

The AI-R score is defined as:

$$ AI-R_{i,t} = \alpha \cdot V^R_i(t) + (1-\alpha) \cdot H^R_i(t) + \beta \cdot \text{Synergy}\%(V^R, H^R) $$

Let's break down what this means in simple terms:

*   **$V^R$ (Idiosyncratic Readiness):** This represents **your personal capabilities**. It includes your AI skills, your expertise in your specific domain, and your ability to adapt to new challenges. Think of this as "what you bring to the table."
*   **$H^R$ (Systematic Opportunity):** This represents the **job market opportunity**. It looks at factors like job growth, salary potential, and the demand for AI skills in a specific career. This is "what the market is looking for."
*   **Synergy:** This is a bonus that reflects how well **your skills align with a specific job's requirements**. A high synergy score means you are a great fit for a particular role, amplifying your overall readiness.
*   **$\alpha$ (alpha) and $\beta$ (beta):** These are weighting factors that you can adjust to customize the calculation based on what you feel is more important—your personal skills or the market demand.

This codelab will guide you through the three main sections of the application, accessible from the **Navigation** dropdown in the sidebar:

1.  **AI-Readiness Score:** Calculate your baseline score.
2.  **Pathway Simulation:** See how learning new skills can improve your score.
3.  **Data Explorer:** Look at the sample data that powers the application.

Let's get started!

## Calculating Your AI-Readiness Score
Duration: 10:00

In this step, you will input information about your skills, experience, and career goals to generate your personalized AI-Readiness Score.

First, ensure you are on the **AI-Readiness Score** page, selected from the sidebar navigation. The page is divided into three main columns: your personal inputs ($V^R$), market inputs ($H^R$), and the final calculation and results.

### Global Parameters (Sidebar)

Before diving into the main inputs, look at the sidebar. Here you can adjust the **Global Parameters**:

*   **Weight on Individual Factors ($\alpha$):** This slider lets you decide the importance of your personal skills ($V^R$) versus the market opportunity ($H^R$). A higher alpha means your personal readiness has a bigger impact on the final score.
*   **Synergy Coefficient ($\beta$):** This slider controls the "bonus" you get when your skills perfectly match a job's requirements. A higher beta gives a bigger boost for strong alignment.

For now, you can leave these at their default values.

### Column 1: Idiosyncratic Readiness ($V^R$) Inputs

This first column is all about you. It's broken down into three key areas that define your personal readiness.

1.  **AI-Fluency:** This measures how proficient you are with AI tools and concepts. Use the sliders to rate your skills in areas like prompt engineering, using AI tools, understanding AI principles, and data literacy. You'll also input metrics on how AI impacts your productivity and judgment.
2.  **Domain-Expertise:** This section captures your knowledge and experience in your professional field. Select your education level, enter your years of experience, and rate your portfolio, industry recognition, and credentials.
3.  **Adaptive-Capacity:** This evaluates your "soft skills" that are crucial for thriving in a changing world. Rate your cognitive flexibility, emotional intelligence, and strategic career management skills.

Fill out these sections to the best of your ability. The more accurate your inputs, the more meaningful your score will be.

### Column 2: Systematic Opportunity ($H^R$) & Synergy Inputs

This second column focuses on the job market and how you fit into it.

1.  **Systematic Opportunity ($H^R$) Inputs:**
    *   Use the **Target Occupation** dropdown to select a career you are interested in. The application will automatically pull market data for that role, such as its potential for AI enhancement, projected job growth, and wage premium.
    *   The **Market Multiplier Parameters** ($\lambda$ and $\gamma$) are advanced settings that help adjust for market volatility and regional demand differences. You can leave them at their defaults.

2.  **Synergy Inputs:**
    *   In the **Individual Skills Data** table, list your key professional skills and rate your proficiency (score) for each. You can add or remove rows as needed. This data will be compared against the required skills for your chosen Target Occupation to calculate the alignment.

### Column 3: Calculation and Results

Once you have filled in all your information, click the **Calculate AI-Readiness Score** button in the third column.

The **Results** section will immediately update to show you four key metrics:
*   **AI-Readiness Score:** Your final, overall score.
*   **Idiosyncratic Readiness ($V^R$):** Your score based purely on your personal capabilities.
*   **Systematic Opportunity ($H^R$):** The score for your chosen career's market potential.
*   **Synergy %:** The bonus reflecting your skill alignment with the job.

Below the metrics, you will see two charts:
*   A **pie chart** breaking down your $V^R$ score into its components (AI-Fluency, Domain-Expertise, Adaptive-Capacity).
*   A **bar chart** showing the factors contributing to the market opportunity ($H^R$) score.

Take a moment to analyze your results. Which areas are your strongest? Where is there room for improvement?

## Simulating Future Pathways
Duration: 5:00

Now that you have your baseline AI-Readiness Score, you can explore how to improve it. The **Pathway Simulation** page lets you perform a "what-if" analysis to see how completing a learning program could boost your profile.

Navigate to the **Pathway Simulation** page using the sidebar dropdown.

<aside class="positive">
<b>Note:</b> You must calculate an initial score on the "AI-Readiness Score" page before you can use the simulation tool.
</aside>

### Simulating Your Growth

On this page, you can model the impact of professional development.

1.  **Select Learning Pathway:** Choose a sample learning pathway from the dropdown. Each pathway is designed to improve a different aspect of your profile. For example, "Prompt Engineering Fundamentals" primarily boosts AI-Fluency, while "AI for Financial Analysis" enhances both AI-Fluency and Domain-Expertise.
2.  **Pathway Completion Score:** Use this slider to indicate how much of the course you plan to complete. A score of 1.0 means full completion.
3.  **Pathway Mastery Score:** This slider represents how well you expect to learn and master the material. A score of 1.0 indicates perfect mastery.

Once you've made your selections, click the **Simulate Pathway Impact** button.

### Analyzing the Simulation Results

The page will display a comparison of your current scores versus your projected scores after completing the selected pathway.

*   You will see your **Current** AI-R, $V^R$, and $H^R$ scores on the left.
*   On the right, you will see the **Projected** scores. Notice the green "delta" value next to the projected scores, which shows you the exact increase.

<aside class="positive">
Your Systematic Opportunity ($H^R$) score will remain the same. This is because undertaking a learning pathway improves <b>your</b> skills ($V^R$), not the external job market ($H^R$).
</aside>

The bar chart at the bottom provides a clear visual comparison between your current and projected scores, helping you understand the potential return on your investment in learning. Feel free to experiment with different pathways to find the one that gives you the biggest boost.

## Exploring the Underlying Data
Duration: 3:00

Transparency is key to understanding how the AI-R score is calculated. The **Data Explorer** page allows you to view the sample datasets used by the application.

Navigate to the **Data Explorer** page from the sidebar.

This page contains several expandable sections, each showing a different piece of the data puzzle:

*   **Individual Profiles Data:** This table contains the default input values for a sample user profile on the main calculation page.
*   **Occupational Data:** Here you can see all the market data for the different job roles available in the "Target Occupation" dropdown. This includes metrics like job growth rates, salaries, and required experience.
*   **Learning Pathways Data:** This table defines the learning pathways available on the simulation page, including how much they impact AI-Fluency, Domain-Expertise, and Adaptive-Capacity.
*   **Occupation Required Skills Data:** This dataset lists the specific skills and proficiency levels required for each occupation, which is used to calculate your Synergy score.
*   **Individual Skills Data:** This shows the sample skills for a user, which you can edit on the main page.

By exploring these tables, you can gain a deeper understanding of the factors that influence your AI-Readiness Score.

<aside class="negative">
Please note that all data in this application is <b>synthetic and for demonstration purposes only</b>. It does not represent real-time market data.
</aside>

## Conclusion
Duration: 1:00

Congratulations on completing this guide!

You have learned how to use the AI Career Navigator to:
*   **Calculate** your personal AI-Readiness Score based on your skills, experience, and the current job market.
*   **Analyze** the components of your score to identify your strengths and areas for development.
*   **Simulate** the impact of various learning pathways to plan your career growth strategically.
*   **Explore** the underlying data to understand how the application works.

This tool is a powerful resource for anyone looking to navigate their career in the age of AI. By periodically reassessing your score and exploring different pathways, you can make informed decisions to stay ahead of the curve and achieve your professional goals.
