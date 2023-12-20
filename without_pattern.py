# Существующий класс (старая система) с несовместимым интерфейсом
class LegacyOrderSystem:
    def get_order_info(self, order_id):
        # Возвращает базовую информацию о заказе
        return f"Basic info for order {order_id}"


# Новый интерфейс, который ожидает клиент
class ModernOrderSystem:
    def get_full_order_info(self, order_id):
        # В старой системе получаем базовую информацию
        legacy_system = LegacyOrderSystem()
        basic_info = legacy_system.get_order_info(order_id)

        # Дополнительная логика для получения дополнительной информации из старой системы
        full_info = f"{basic_info}, Additional info from the legacy system"
        return full_info


# Клиентский код, который ожидает работу с ModernOrderSystem
def client_code(modern_system):
    return modern_system.get_full_order_info("123")


# Использование нового интерфейса в клиентском коде
modern_system = ModernOrderSystem()
result = client_code(modern_system)
print(result)
