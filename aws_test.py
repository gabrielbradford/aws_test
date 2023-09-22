import streamlit as st

#make interface fill screen
st.set_page_config(layout="wide")


    
def main():
    tab1, tab2 = st.tabs(['Page1','page2'])

    with tab1:
        col1, col2 = st.columns([2,3])

        with col1:
            # create file uploader button. Store uploaded files that aren't already in DB in all_files
            st.header('Test App')
            
            input1 = st.text_input('Enter your name')
            st.write(input1)

                            

        
if __name__ == '__main__':
    main()