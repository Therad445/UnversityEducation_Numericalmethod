function [ root ] = nuton(f, x0)
    
    syms x_s
    x = x0 - f(x0)/subs(diff(f(x_s)), x0); c = 0; 
    while( f(x) ~= 0 )
        x = x - f(x)/subs(diff(f(x_s)), x);
        x
        c = c + 1;
        c
    end
    root = x;
    c
end
