def MultiplyMatrix(m1,m2):
  #Create lists for vertical columns in m2
  vertical=[]
  #make new matrix
  matrix=[]
  for i in range(len(m1)):
    matrix.append([])
    for k in range(len(m2[0])):
      matrix[i].append(0)

  #dot product each list by each column
  for i in range(len(m1)):
    for k in range(len(m2[0])):  ##Which column youre at
      for j in range(len(m2)): #which row youre at
        vertical.append(m2[j][k])
      matrix[i][k]=dotproduct(m1[i],vertical)
      vertical=[]
  
  return matrix
