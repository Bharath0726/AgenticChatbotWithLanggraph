import streamlit as st
import os
from ..uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        # Enhanced page configuration with custom theme
        st.set_page_config(
            page_title= "🤖 " + self.config.get_page_title(), 
            layout="wide",
            initial_sidebar_state="expanded",
            page_icon="🤖"
        )
        
        # Advanced custom CSS for better theming
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        .stApp {
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
            font-family: 'Inter', sans-serif;
        }
        
        .main-header {
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 35%, #06b6d4 100%);
            padding: 3rem 2rem;
            border-radius: 20px;
            margin-bottom: 2.5rem;
            text-align: center;
            color: white;
            font-size: 3rem;
            font-weight: 700;
            box-shadow: 0 20px 40px rgba(99, 102, 241, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.02); }
            100% { transform: scale(1); }
        }
        
        .subtitle {
            background: linear-gradient(90deg, #f472b6, #06b6d4, #10b981);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradientShift 3s ease infinite;
            font-size: 1.2rem;
            font-weight: 500;
            margin-top: 1rem;
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .sidebar-section {
            background: linear-gradient(145deg, #1e293b 0%, #334155 100%);
            padding: 1.5rem;
            border-radius: 15px;
            margin-bottom: 1.5rem;
            border: 1px solid rgba(148, 163, 184, 0.2);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
        }
        
        .sidebar-section:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4);
        }
        
        .config-title {
            color: #f1f5f9;
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .section-icon {
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            border-radius: 50%;
            width: 2rem;
            height: 2rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
        }
        
        .warning-box {
            background: linear-gradient(135deg, #f59e0b 0%, #ef4444 100%);
            padding: 1.5rem;
            border-radius: 12px;
            border-left: 4px solid #dc2626;
            box-shadow: 0 8px 25px rgba(239, 68, 68, 0.3);
            color: white;
            margin-top: 1rem;
        }
        
        .success-tip {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            padding: 1rem;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-top: 1rem;
            box-shadow: 0 6px 20px rgba(16, 185, 129, 0.3);
        }
        
        .stSelectbox > div > div {
            background: rgba(30, 41, 59, 0.8);
            border: 1px solid rgba(148, 163, 184, 0.3);
            border-radius: 8px;
            color: white;
        }
        
        .stTextInput > div > div > input {
            background: rgba(30, 41, 59, 0.8);
            border: 1px solid rgba(148, 163, 184, 0.3);
            border-radius: 8px;
            color: white;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #6366f1;
            box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2);
        }
        
        .sidebar .sidebar-content {
            background: rgba(15, 15, 35, 0.9);
            backdrop-filter: blur(10px);
        }
        
        .feature-highlight {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem 0;
        }
        
        .status-indicator {
            width: 10px;
            height: 10px;
            background: #10b981;
            border-radius: 50%;
            display: inline-block;
            margin-right: 0.5rem;
            animation: blink 1.5s infinite;
        }
        
        @keyframes blink {
            0%, 50% { opacity: 1; }
            51%, 100% { opacity: 0.3; }
        }
        
        .footer-brand {
            text-align: center;
            padding: 1rem;
            color: #64748b;
            font-size: 0.9rem;
            border-top: 1px solid rgba(148, 163, 184, 0.2);
            margin-top: 2rem;
        }
        </style>
        """, unsafe_allow_html=True)

        # Enhanced main header with subtitle
        st.markdown(f'''
        <div class="main-header">
            🤖 {self.config.get_page_title()}
            <div class="subtitle">
                ✨ Powered by Advanced AI • Built with LangGraph • Experience the Future
            </div>
        </div>
        ''', unsafe_allow_html=True)

        with st.sidebar:
            st.markdown("""
            <div style="text-align: center; padding: 1rem 0;">
                <span class="status-indicator"></span>
                <span style="color: #f1f5f9; font-weight: 600;">AI Configuration Panel</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # LLM Selection Section
            st.markdown('''
            <div class="sidebar-section">
                <div class="config-title">
                    <div class="section-icon">🧠</div>
                    Language Model Selection
                </div>
            ''', unsafe_allow_html=True)
            
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox(
                "🎯 Choose your AI Engine", 
                llm_options,
                help="Select the language model that will power your AI assistant"
            )
            st.markdown('</div>', unsafe_allow_html=True)

            if self.user_controls["selected_llm"] == 'Groq':
                # Model Configuration Section
                st.markdown('''
                <div class="sidebar-section">
                    <div class="config-title">
                        <div class="section-icon">⚙️</div>
                        Advanced Model Settings
                    </div>
                ''', unsafe_allow_html=True)
                
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox(
                    "🚀 Model Variant", 
                    model_options,
                    help="Choose the specific Groq model for optimal performance"
                )
                
                # API Key input with enhanced styling
                st.markdown('''
                <div class="feature-highlight">
                    <strong>🔐 Secure API Authentication</strong><br>
                    <small>Your API key is encrypted and never stored</small>
                </div>
                ''', unsafe_allow_html=True)
                
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input(
                    "🔑 Enter API Key",
                    type="password",
                    help="Paste your Groq API key for secure authentication",
                    placeholder="gsk_..."
                )
                
                # Enhanced warning message
                if not self.user_controls["GROQ_API_KEY"]:
                    st.markdown("""
                    <div class="warning-box">
                        <strong>⚠️ API Key Required</strong><br>
                        Please enter your GROQ API key to unlock AI capabilities.<br><br>
                        <a href="https://console.groq.com/keys" target="_blank" 
                           style="color: white; text-decoration: none; background: rgba(255,255,255,0.2); 
                           padding: 0.5rem 1rem; border-radius: 6px; display: inline-block; margin-top: 0.5rem;">
                            🔗 Get Free API Key
                        </a>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="success-tip">
                        ✅ API Key Configured Successfully!
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
            
            # Use Case Selection Section
            st.markdown('''
            <div class="sidebar-section">
                <div class="config-title">
                    <div class="section-icon">🎯</div>
                    AI Use Case Selection
                </div>
            ''', unsafe_allow_html=True)
            
            ## Usecase selection
            self.user_controls["selected_usecase"] = st.selectbox(
                "💡 Choose Your AI Application",
                usecase_options,
                help="Select the type of AI task you want to perform"
            )
            
            # Show use case description
            usecase_descriptions = {
                "Basic Chatbot": "💬 Interactive conversational AI for general queries and assistance",
                # Add more descriptions as you expand
            }
            
            if self.user_controls["selected_usecase"] in usecase_descriptions:
                st.markdown(f'''
                <div class="feature-highlight">
                    {usecase_descriptions[self.user_controls["selected_usecase"]]}
                </div>
                ''', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Footer in sidebar
            st.markdown("""
            <div class="footer-brand">
                <strong>🚀 LangGraph AgenticAI</strong><br>
                <small>Next-generation AI assistant</small>
            </div>
            """, unsafe_allow_html=True)

        return self.user_controls
        


