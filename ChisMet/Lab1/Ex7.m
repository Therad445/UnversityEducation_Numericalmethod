function [res]=Ex7(x)
res = 0; i = 0;
while (x^(2*i + 1) /factorial(2*i + 1) > 10^-17)
    res = res + (-1)^i*x^(2*i+1)/factorial(2*i + 1);
    i = i + 1;
end
end