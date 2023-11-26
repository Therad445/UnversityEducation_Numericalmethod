format long e
n=1;
f=@(x,n)x^n*exp(x-1);
syms x
for n=1:30
    n=n+1; 
    subs(int(f(x,n),x,0,1))
end
