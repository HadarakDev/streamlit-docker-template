import streamlit as st


st.set_page_config(layout="wide")

def main():
    st.title("Welcome !")
    st.write("You can find a tutorial to Deploy this App on my website: https://www.hadarak.com/")
    return


if __name__ == "__main__":

    # Hide Streamlit footer and Settings Menu
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    main()