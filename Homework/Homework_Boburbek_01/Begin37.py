V_1,V_2=map(int,input("Birinchi va ikkinchi mashina tezliklarini kiriting(V1,V2): ").split(','))
S=int(input("Ular orasidagi masofani kiriting: "))
T=int(input("Ular bir-biriga harakatlangan vaqt: "))
New_S=S-(V_1+V_2)*T
print("Ular orasidagi masofa:",New_S)
