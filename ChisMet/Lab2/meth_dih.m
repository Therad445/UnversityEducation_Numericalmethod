function [root] = meth_dih(otr)
    
    x1 = otr(1); x2 = otr(2);x = 0;c = 0;eps = 10^-16; max_iter = 2000;
    
    if (lab_2_1(x1)*lab_2_1(x2) > 0)
        print('������������ �������')
    else
        while(abs(x2 - x1) >= eps && c<max_iter)
            x = (x1 + x2)/2;
            if lab_2_1(x) == 0 || abs(lab_2_1(x)) < eps
                break
            elseif (lab_2_1(x2)*lab_2_1(x) < 0)
                x1 = x;
            else
                x2 = x;
            end
            c = c + 1;
        end
        root = x;
        disp('c =');
        disp(c);
    end
end

otr = -10:20:10;
meth_dih(otr)

function [root] = meth_dih(otr)
    
    x1 = otr(1); x2 = otr(2);x = 0;c = 0;eps = 10^-16;
    
    if (lab_2_1(x1)*lab_2_1(x2) > 0)
        print('������������ �������')
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