import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content
from parse import parse

st.title("AI Web Scraper")
url = st.text_input("Enter your website url: ")

if st.button("Scrape Site"):
    if url:
        st.write("Scraping the website")
        dom_content = scrape_website(website=url)
        body_content = extract_body_content(html_content=dom_content)
        cleaned_content = clean_body_content(body_content=body_content)

        st.session_state.dom_content = cleaned_content

        with st.expander("View DOM content"):
            st.text_area("DOM Content", cleaned_content, height=300)
        
        print(cleaned_content)

if "dom_content" in st.session_state:
    parse_description = st.text_area("What information would you like to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse(dom_chunks, parse_description)
            st.write(parsed_result)