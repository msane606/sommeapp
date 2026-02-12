import streamlit as st

with st.sidebar:
    st.header("Methodes de calcul")
    st.info("Addition")
    st.info("Soustraction")
    st.info("Multiplication")
    st.info("Division")



st.title("Calculatrice")

st.header("Calcul d'addition")
st.subheader("Calculer la somme de deux nombre")
a=st.number_input("saisir a")
b=st.number_input("saisir b")
somme=a+b
if st.button("Somme"):
    st.info(somme)

    st.header("Calcul de soustraction")
st.subheader("Calculer la difference de deux nombre")
X=st.number_input("saisir X")
Y=st.number_input("saisir Y")
difference=X-Y
if st.button("difference"):
    st.info(difference)

st.header("Calcul de multiplication")
st.subheader("Calculer le produit de deux nombre")
s=st.number_input("saisir s")
d=st.number_input("saisir d")
produit=s*d
if st.button("produit"):
    st.info(produit)

st.header("Calcul de division")
st.subheader("Calculer la division de deux nombre")
m=st.number_input("m")
n=st.number_input("n")
if n==0:
    st.warning("error")
else:
    division=m/n
if st.button("division"):
        st.info(division)