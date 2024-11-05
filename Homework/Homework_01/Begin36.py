V_1,V_2=map(int,input("Birinchi va ikkinchi mashina tezliklarini kiriting(V1,V2): ").split(','))
S=int(input("Ular orasidagi masofani kiriting: "))
T=int(input("Ular qarama-qarshi tomonga harakatlangan vaqt: "))
New_S=(V_1+V_2)*T+S
print("Ular orasidagi masofa:",New_S)
