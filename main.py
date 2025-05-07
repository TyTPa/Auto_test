def modulo(a, b):
    """
    Вычисляет остаток от деления a на b.

    Args:
        a (int): Делимое
        b (int): Делитель

    Returns:
        int: Остаток от деления a на b

    Raises:
        ZeroDivisionError: Если b равно 0
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a % b
