import streamlit as st
st.title("My mini library app")
if books not in st.session_state:
  st.session_state.books = []
  st.header("Add book")
  title =  st.text_input("title")
  author = st.text_imput("Author")
  price = st.text_imput("Price", min_value=0.0)
  if st.button("Add book"):
    book = { "title" : title,
            "author" : author,
            "price" : price}
    st.sessipn_state.books.appened(book)
    st.success("The book is added")

if st.button("Show all books"):
  if len(st.session_state.books) == 0:
    st.write("No added books")
  else:
    for book in st.session_state.books:
      st.write("Tite", book["title"])
      st.write("Author", book["author"])
      st.write("Price", book["price"])
      st.write("--------------------")

st.header("Serch by author")
search_author = st.text_input("Enter Author name:")
if st.button("Serch by author"):
  found = False
for book in st.session_state.books:
  if book["author"] == search_author:
    st.write(book)
    found = true
  in found = False:
  st.write("There are no books from thi sauthor")
