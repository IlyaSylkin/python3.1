while (st := input()) != "":
    if st[-3:] != "@@@":
        print(st.lstrip("#"))
