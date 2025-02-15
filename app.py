import streamlit as st
from backend import get_ai_response

def main():
    st.set_page_config(page_title="Solar AI Assistant", page_icon="☀️")
    st.title("☀️ Solar Industry AI Assistant")
    st.write("Ask me anything about solar energy, and I'll provide insights!")

    # Suggested Questions
    st.subheader("💡 Suggested Questions")

    with st.expander("Basic Questions"):
        if st.button("How do solar panels generate electricity?"):
            st.session_state.user_query = "How do solar panels generate electricity?"
        if st.button("What are the benefits of using solar energy?"):
            st.session_state.user_query = "What are the benefits of using solar energy?"
        if st.button("How long do solar panels last?"):
            st.session_state.user_query = "How long do solar panels last?"

    with st.expander("⚙ Technical Questions"):
        if st.button("What is the efficiency of modern solar panels?"):
            st.session_state.user_query = "What is the efficiency of modern solar panels?"
        if st.button("What are the different types of solar panels?"):
            st.session_state.user_query = "What are the different types of solar panels?"
        if st.button("How does net metering work in solar energy systems?"):
            st.session_state.user_query = "How does net metering work in solar energy systems?"
        if st.button("What is the best angle to install solar panels?"):
            st.session_state.user_query = "What is the best angle to install solar panels?"
        if st.button("Can solar panels work on cloudy days?"):
            st.session_state.user_query = "Can solar panels work on cloudy days?"

    with st.expander("💰 Financial & ROI Questions"):
        if st.button("How much does it cost to install a solar panel system?"):
            st.session_state.user_query = "How much does it cost to install a solar panel system?"
        if st.button("What is the average payback period for solar panels?"):
            st.session_state.user_query = "What is the average payback period for solar panels?"
        if st.button("Are there government subsidies for solar energy?"):
            st.session_state.user_query = "Are there government subsidies for solar energy?"
        if st.button("What factors affect the ROI of solar panel installation?"):
            st.session_state.user_query = "What factors affect the ROI of solar panel installation?"

    with st.expander("📈 Industry & Market Trends"):
        if st.button("What are the latest trends in the solar energy industry?"):
            st.session_state.user_query = "What are the latest trends in the solar energy industry?"
        if st.button("Which country produces the most solar energy?"):
            st.session_state.user_query = "Which country produces the most solar energy?"
        if st.button("What is the future of solar energy?"):
            st.session_state.user_query = "What is the future of solar energy?"
        if st.button("How is AI being used in the solar energy industry?"):
            st.session_state.user_query = "How is AI being used in the solar energy industry?"

    with st.expander("🔧 Maintenance & Troubleshooting"):
        if st.button("How often do solar panels need maintenance?"):
            st.session_state.user_query = "How often do solar panels need maintenance?"
        if st.button("What are common problems in solar panel systems?"):
            st.session_state.user_query = "What are common problems in solar panel systems?"
        if st.button("Can dust and dirt reduce solar panel efficiency?"):
            st.session_state.user_query = "Can dust and dirt reduce solar panel efficiency?"
        if st.button("How to clean and maintain solar panels for maximum efficiency?"):
            st.session_state.user_query = "How to clean and maintain solar panels for maximum efficiency?"

    # User Query Input
    user_query = st.text_area("Enter your question about solar energy:", value=st.session_state.get("user_query", ""))
    
    if st.button("Get Answer") and user_query:
        with st.spinner("Thinking..."):
            response = get_ai_response(user_query)
        
        if response.startswith("Error") or response.startswith("API Request Error"):
            st.error(response)
        else:
            st.success("Here's what I found:")
            st.write(response)

if __name__ == "__main__":
    main()
