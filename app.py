import streamlit as st
from backend import get_ai_response

def main():
    st.set_page_config(page_title="Solar AI Assistant", page_icon="☀️")
    st.title("☀️ Solar Industry AI Assistant")
    st.write("Ask me anything about solar energy, and I'll provide insights!")

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

    # Suggested Questions Below Search Bar
    st.markdown("---")
    st.subheader("💡 Suggested Questions")

    # Function to display question cards in a clean style
    def display_card(title, questions, icon):
        st.markdown(f"""
            <div style="
                background-color: #f9f9f9; 
                padding: 20px; 
                border-radius: 10px; 
                box-shadow: 2px 2px 10px rgba(0,0,0,0.1); 
                min-height: 200px;
            ">
                <h4 style="margin-bottom: 10px;">{icon} {title}</h4>
                <ul style="padding-left: 20px; margin-top: 10px;">
        """, unsafe_allow_html=True)
        
        for question in questions:
            st.markdown(f"<li>{question}</li>", unsafe_allow_html=True)
        
        st.markdown("""
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # Displaying in 2 Columns
    col1, col2 = st.columns(2)

    with col1:
        display_card(
            "Basic Questions",
            [
                "How do solar panels generate electricity?",
                "What are the benefits of using solar energy?",
                "How long do solar panels last?"
            ],
            "✅"
        )

        display_card(
            "Financial & ROI Questions",
            [
                "How much does it cost to install a solar panel system?",
                "What is the average payback period for solar panels?",
                "Are there government subsidies for solar energy?",
                "What factors affect the ROI of solar panel installation?"
            ],
            "💰"
        )

        display_card(
            "Maintenance & Troubleshooting",
            [
                "How often do solar panels need maintenance?",
                "What are common problems in solar panel systems?",
                "Can dust and dirt reduce solar panel efficiency?",
                "How to clean and maintain solar panels for maximum efficiency?"
            ],
            "🔧"
        )

    with col2:
        display_card(
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

        display_card(
            "Industry & Market Trends",
            [
                "What are the latest trends in the solar energy industry?",
                "Which country produces the most solar energy?",
                "What is the future of solar energy?",
                "How is AI being used in the solar energy industry?"
            ],
            "📈"
        )

if __name__ == "__main__":
    main()
