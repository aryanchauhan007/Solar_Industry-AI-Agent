import streamlit as st
from backend import get_ai_response

def main():
    st.set_page_config(page_title="Solar AI Assistant", page_icon="☀️")
    st.title("☀️ Solar Industry AI Assistant")

    # Search Bar on Top
    st.markdown("---")
    st.subheader("🔍 Ask Your Question")
    user_query = st.text_area("Enter your question about solar energy:")

    if st.button("Get Answer") and user_query:
        with st.spinner("Thinking..."):
            response = get_ai_response(user_query)
        
        if response.startswith("Error") or response.startswith("API Request Error"):
            st.error(response)
        else:
            st.success("Here's what I found:")
            st.write(response)

    # Suggested Questions
    st.markdown("---")
    st.subheader("💡 Suggested Questions")

    # Custom CSS for Box Layout
    st.markdown("""
        <style>
            .card {
                background-color: #f9f9f9;
                border-radius: 10px;
                padding: 15px;
                box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
            }
            .card h4 {
                margin-bottom: 10px;
                font-size: 18px;
                color: #333;
            }
            .card ul {
                padding-left: 20px;
            }
            .card ul li {
                margin-bottom: 8px;
                color: #555;
            }
        </style>
    """, unsafe_allow_html=True)

    # Function to create cards
    def create_card(title, questions, icon):
        st.markdown(f"""
            <div class="card">
                <h4>{icon} {title}</h4>
                <ul>
        """, unsafe_allow_html=True)
        
        for question in questions:
            st.markdown(f"<li>{question}</li>", unsafe_allow_html=True)
        
        st.markdown("</ul></div>", unsafe_allow_html=True)

    # Grid Layout for Questions
    col1, col2 = st.columns(2)

    with col1:
        create_card(
            "Basic Questions",
            [
                "How do solar panels generate electricity?",
                "What are the benefits of using solar energy?",
                "How long do solar panels last?"
            ],
            "✅"
        )

        create_card(
            "Financial & ROI Questions",
            [
                "How much does it cost to install a solar panel system?",
                "What is the average payback period for solar panels?",
                "Are there government subsidies for solar energy?",
                "What factors affect the ROI of solar panel installation?"
            ],
            "💰"
        )

    with col2:
        create_card(
            "Technical Questions",
            [
                "What is the efficiency of modern solar panels?",
                "What are the different types of solar panels?",
                "How does net metering work in solar energy systems?",
                "What is the best angle to install solar panels?",
                "Can solar panels work on cloudy days?"
            ],
            "⚙"
        )

        create_card(
            "Industry & Market Trends",
            [
                "What are the latest trends in the solar energy industry?",
                "Which country produces the most solar energy?",
                "What is the future of solar energy?",
                "How is AI being used in the solar energy industry?"
            ],
            "📈"
        )

        create_card(
            "Maintenance & Troubleshooting",
            [
                "How often do solar panels need maintenance?",
                "What are common problems in solar panel systems?",
                "Can dust and dirt reduce solar panel efficiency?",
                "How to clean and maintain solar panels for maximum efficiency?"
            ],
            "🔧"
        )

if __name__ == "__main__":
    main()
