function result = x2_a(a, x0)
    % �������������
    x = x0;
    eps = 10^-16;
    % ��������
    for i = 1:100
        x_new = 0.5 * (a/x + x);
        % �������� �� ����������
        if abs(x_new - x) < eps
            result = x_new;
            return;
        end
        x = x_new;
    end
    error('����� �� �������');
end