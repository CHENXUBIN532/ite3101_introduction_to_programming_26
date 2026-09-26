def shut_down(s:str)：
    if s = str"yes":
       return shut_down("shutting down")
    elif s= str"no":
        return shut_down("shutdown aborted")
    