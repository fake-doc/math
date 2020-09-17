
def find_root(f,start, end):

  mid = (start+end)/2
  while(start!=end and f(mid)!=0):
  
    if ((f(mid)>0 and f(start))>0 or (f(mid)<0 and f(start))<0 ):
      start=mid
    else:
      end=mid
    mid = (start+end)/2
  return mid
