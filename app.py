import streamlit as st
from backend import get_ai_response

def main():
    st.set_page_config(page_title="Solar AI Assistant", page_icon="☀️")
    st.title("☀️ Solar Industry AI Assistant")
    st.write("Ask me anything about solar energy, and I'll provide insights!")

    # Suggested Questions
    st.subheader("💡 Suggested Questions")
    
    st.markdown("### Basic Questions:")
    st.markdown("""
    - How do solar panels generate electricity?  
    - What are the benefits of using solar energy?  
    - How long do solar panels last?  
    """)

    st.markdown("### ⚙ Technical Questions:")
    st.markdown("""
    - What is the efficiency of modern solar panels?  
    - What are the different types of solar panels?  
    - How does net metering work in solar energy systems?  
    - What is the best angle to install solar panels?  
    - Can solar panels work on cloudy days?  
    """)

    st.markdown("### 💰 Financial & ROI Questions:")
    st.markdown("""
    - How much does it cost to install a solar panel system?  
    - What is the average payback period for solar panels?  
    - Are there government subsidies for solar energy?  
    - What factors affect the ROI of solar panel installation?  
    """)

    st.markdown("### 📈 Industry & Market Trends:")
    st.markdown("""
    - What are the latest trends in the solar energy industry?  
    - Which country produces the most solar energy?  
    - What is the future of solar energy?  
    - How is AI being used in the solar energy industry?  
    """)

    st.markdown("### 🔧 Maintenance & Troubleshooting:")
    st.markdown("""
    - How often do solar panels need maintenance?  
    - What are common problems in solar panel systems?  
    - Can dust and dirt reduce solar panel efficiency?  
    - How to clean and maintain solar panels for maximum efficiency?  
    """)

    # User Query Input
    user_query = st.text_area("Enter your question about solar energy:")
    
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
