import streamlit as st

st.title("Moqta mini biblioteka")

if "books" not in st.session_state:
    st.session_state.books = []

st.header("Dobavi kniga")
title = st.text_input("Zaglavie")
author = st.text_input("Avtor")
price = st.number_input("Cena", min_value=0.0)

if st.button("Dobavi knigata"):
    if title and author:
        book = {
            "title": title,
            "author": author,
            "price": price
        }
        st.session_state.books.append(book)
        st.success("Knigata e dobavena!")
    else:
        st.error("Populnete vsichki poleta!")

if st.button("Pokaji vsichki knigi"):
    if len(st.session_state.books) == 0:
        st.write("Nqma dobaveni knigi")
    else:
        for book in st.session_state.books:
            st.write(f"Zaglavie: {book['title']}")
            st.write(f"Avtor: {book['author']}")
            st.write(f"Cena: {book['price']}")
            st.write("------------------")

st.header("Tursene na avtor")
search_author = st.text_input("Vuvedi ime na avtor")
if st.button("Tursi po avtor"):
    found = False
    for book in st.session_state.books:
        if book["author"].lower() == search_author.lower():
            st.write(book)
            found = True
    if not found:
        st.write("Nqma namereni knigi ot tozi avtor")

st.header("Tursene po zaglavie")
search_title = st.text_input("Vuvedi zaglavie")if st.button("Tursi po zaglavie"):
    found = False
    for book in st.session_state.books:
        if book["title"].lower() == search_title.lower():
            st.write(book)
            found = True
    if not found:
        st.write("Nqma namerena takava kniga.")

if st.button("Pokaji nai-evtina kniga"):
    if len(st.session_state.books) == 0:
        st.write("Bibliotekata e prazna")
    else:
        cheapest = st.session_state.books[0]
        for book in st.session_state.books:
            if book["price"] < cheapest["price"]:
                cheapest = book
        st.write("Nai-evtina kniga:")
        st.write(cheapest)
