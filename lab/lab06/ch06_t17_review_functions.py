def shut_down(s:str) ：
    if s ==yes:
       return shut_down("shutting down")
    elif s==no:
        return shut_down("shutdown aborted")
    else:
        return shut_down("sorry")