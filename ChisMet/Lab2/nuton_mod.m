function [ root ] = nuton_mod(f, x0, p)
    
    syms x_s
    x = x0 - p*f(x0)/subs(diff(f(x_s)), x0); c = 0; 
    while( f(x) ~= 0 )
        x = x - p*f(x)/subs(diff(f(x_s)), x);
        c = c + 1;
    end
    root = x;
    c
end
