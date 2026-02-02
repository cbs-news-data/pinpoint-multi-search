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
    "Data Set 9": "3a62693c54a6b908",
    "Data Set 10": "9048f6067cfe6177",
    "Data Set 11": "25ab125b2a2a01ee",
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