function [Xk, Yk] = Newton(f,diap)
    a = diap(1);
    b = diap(2);
    df = char(diff(sym(f))); 
    ddf = char(diff(sym(df)));
    F = inline(f);
    F1 = inline(df);
    F2 = inline(ddf);
    c = 0;
    eps = 10^-16;
    if F(a)*F2(a) > 0
        Xk = b;
        X0 = a;
    else
        Xk = a;
        X0 = b;
    end
    while abs(Xk-X0) > eps
        c = c + 1;
        X0 = Xk;
        Xk =  X0 - (F1(X0)/(F2(X0))); 
        Yk = F(Xk);
    end
    c
    Xk
    Yk
end
