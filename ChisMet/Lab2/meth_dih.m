function [root] = meth_dih(otr)
    
    x1 = otr(1); x2 = otr(2);x = 0;c = 0;eps = 10^-16;
    
    if (lab_2_1(x1)*lab_2_1(x2) > 0)
        print('Некорректный отрезок')
    else
        while(abs(lab_2_1(x)) >= eps)
            x = (x1 + x2)/2;
            if (lab_2_1(x1)*lab_2_1(x) > 0)
                x1 = x;
            else
                x2 = x;
            end
            c = c + 1;
        end
        root = x;
        c
    end
 
end