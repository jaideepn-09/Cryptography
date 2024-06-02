import streamlit as st
import hashlib

def sha256(text):
    hashed_text = hashlib.sha256(text.encode()).hexdigest()
    return hashed_text

def verify_sha256(text, expected_hash):
    hashed_text = sha256(text)
    return hashed_text == expected_hash

def main():
    st.title("SHA-256 Text Converter")
    st.write("Enter a text below to convert it to SHA-256 hash:")
    input_text = st.text_input("Enter text here:", "")

    if st.button("Convert"):
        if not input_text:
            st.warning("Please enter some text.")
        else:
            hashed_text = sha256(input_text)
            st.success("SHA-256 Hash:")
            st.write(hashed_text)
            
    st.write("\n---\n")
    st.write("Verify a SHA-256 hash:")
    input_hash = st.text_input("Enter a SHA-256 hash:", "")
    input_text_to_verify = st.text_input("Enter the text to verify:", "")
    
    if st.button("Verify"):
        if not input_hash or not input_text_to_verify:
            st.warning("Please enter both the hash and the text to verify.")
        else:
            if verify_sha256(input_text_to_verify, input_hash):
                st.success("The provided text matches the SHA-256 hash!")
            else:
                st.error("The provided text does not match the SHA-256 hash.")

if __name__ == "__main__":
    main()
