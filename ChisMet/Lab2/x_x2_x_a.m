function result = x_x2_x_a(a, x0)
    % Функция, соответствующая уравнению x = x^2 + x - a
    g = @(x) x^2 + x - a;
    eps = 10^-16;
    % Итерационный процесс
    x = x0;
    for i = 1:100
        x_new = g(x);
        if abs(x_new - x) < eps
            result = x_new;
            return;
        end
        x = x_new;
    end
    error('Метод не сошелся');
end