def stop_ascending(numlst):
    if numlst == []:
        return None
    for i in range(1, len(numlst)):
        if numlst[i] <= numlst[i-1]:
            return i
    
    return len(numlst)
        
