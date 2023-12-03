function result = x2_a(a, x0)
    % Инициализация
    x = x0;
    eps = 10^-16;
    % Итерации
    for i = 1:100
        x_new = 0.5 * (a/x + x);
        % Проверка на сходимость
        if abs(x_new - x) < eps
            result = x_new;
            return;
        end
        x = x_new;
    end
    error('Метод не сошелся');
end