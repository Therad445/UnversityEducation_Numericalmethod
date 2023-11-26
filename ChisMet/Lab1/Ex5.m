x=1;
for c=1:10^6
    x = x+10^-16;
end
disp(x)
x=1+(10^-16*10^17);
disp(x)