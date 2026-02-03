import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="Pinpoint Multi-Collection Search",
    layout="centered"
)

st.title("Search Across Epstein Files Pinpoint Collections")
st.markdown("Launch the same query across multiple Google Pinpoint collections")

query = st.text_input(
    "Search query",
    placeholder='e.g. "Palm Beach"'
)

COLLECTIONS = {
    "Data Sets 1-8 & 12": "ea371fdea7a785c0",
    "Data Set 9 (1 of 2)": "3a62693c54a6b908",
    "Data Set 9 (2 of 2)": "2c41b44764b7e5fe",
    "Data Set 10 (1 of 3)": "9048f6067cfe6177",
    "Data Set 10 (2 of 3)": "24065f82a453c46f",
    "Data Set 10 (3 of 3)": "0feaee37455f425b",
    "Data Set 11 (1 of 2)": "25ab125b2a2a01ee",
    "Data Set 11 (2 of 2)": "d99f1d9ce4eb747d",
}

if query:
    encoded_query = urllib.parse.quote(query)

    st.subheader("Open results in Pinpoint")
    st.markdown(f'Search results for <span style="color:green;">{query}</span>', unsafe_allow_html=True)
    
    for name, collection_id in COLLECTIONS.items():
        url = (
            "https://journaliststudio.google.com/pinpoint/search"
            f"?collection={collection_id}&q={encoded_query}"
        )

        st.link_button(
            f"{name}",
            url=url,
            use_container_width=True
        )
else:
    st.info("Enter a search term to enable links.")