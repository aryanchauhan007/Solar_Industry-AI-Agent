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

    # All HTML in one block to maintain structure
    st.markdown("""
        <style>
            .card {
                background-color: #ffffff;
                border: 1px solid #e0e0e0;
                border-radius: 10px;
                box-shadow: 4px 4px 15px rgba(0,0,0,0.1);
                padding: 20px;
                min-height: 250px;
                margin-bottom: 20px;
            }
            .card h4 {
                margin-bottom: 15px;
            }
            .card ul {
                list-style-type: disc;
                padding-left: 20px;
            }
            .card ul li {
                margin-bottom: 10px;
                color: #333;
            }
            .card-container {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
            }
        </style>
        
        <div class="card-container">

            <div class="card">
                <h4>✅ Basic Questions</h4>
                <ul>
                    <li>How do solar panels generate electricity?</li>
                    <li>What are the benefits of using solar energy?</li>
                    <li>How long do solar panels last?</li>
                </ul>
            </div>

            <div class="card">
                <h4>⚙ Technical Questions</h4>
                <ul>
                    <li>What is the efficiency of modern solar panels?</li>
                    <li>What are the different types of solar panels?</li>
                    <li>How does net metering work in solar energy systems?</li>
                    <li>What is the best angle to install solar panels?</li>
                    <li>Can solar panels work on cloudy days?</li>
                </ul>
            </div>

            <div class="card">
                <h4>💰 Financial & ROI Questions</h4>
                <ul>
                    <li>How much does it cost to install a solar panel system?</li>
                    <li>What is the average payback period for solar panels?</li>
                    <li>Are there government subsidies for solar energy?</li>
                    <li>What factors affect the ROI of solar panel installation?</li>
                </ul>
            </div>

            <div class="card">
                <h4>📈 Industry & Market Trends</h4>
                <ul>
                    <li>What are the latest trends in the solar energy industry?</li>
                    <li>Which country produces the most solar energy?</li>
                    <li>What is the future of solar energy?</li>
                    <li>How is AI being used in the solar energy industry?</li>
                </ul>
            </div>

            <div class="card">
                <h4>🔧 Maintenance & Troubleshooting</h4>
                <ul>
                    <li>How often do solar panels need maintenance?</li>
                    <li>What are common problems in solar panel systems?</li>
                    <li>Can dust and dirt reduce solar panel efficiency?</li>
                    <li>How to clean and maintain solar panels for maximum efficiency?</li>
                </ul>
            </div>

        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
