# Reading Binary Files
import pickle
st = " "

with open("Resources/myfile.info", "rb") as fh:
    st = pickle.load(fh)
    lst = st.split("o")
    print(lst[0], lst[1])
