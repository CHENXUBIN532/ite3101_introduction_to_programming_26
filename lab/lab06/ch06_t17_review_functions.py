def shut_down(s:str) ：
    if s =="yes":
       return "Shutting down"
    elif s=="no":
        return shut_down("shutdown aborted")
    else:
        return shut_down("sorry")