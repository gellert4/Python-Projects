P = round(float(input("Price: ")))
Z = int(input("Payment: "))

V = Z - P

A = V//1000
B = V%1000//500
C = V%1000%500//200
D = V%1000%500%200//100
E = V%1000%500%200%100//50
F = V%1000%500%200%100%50//20
G = V%1000%500%200%100%50%20//10
H = V%1000%500%200%100%50%20%10//5
I = V%1000%500%200%100%50%20%10%5//2
J = V%1000%500%200%100%50%20%10%5%2//1

print("\nChange:",V,"kr\n"+
"1000kr bills:",A,"\n"+
" 500kr bills:",B,"\n"+
" 200kr bills:",C,"\n"+
" 100kr bills:",D,"\n"+
"  50kr bills:",E,"\n"+
"  20kr bills:",F,"\n"+
"  10kr coins:",G,"\n"+
"   5kr coins:",H,"\n"+
"   2kr coins:",I,"\n"+
"   1kr coins:",J,"\n")