# Существующий класс (старая система) с несовместимым интерфейсом
class LegacyOrderSystem:
    def get_order_info(self, order_id):
        # Возвращает базовую информацию о заказе
        return f"Basic info for order {order_id}"


# Новый интерфейс, который ожидает клиент
class ModernOrderSystem:
    def get_full_order_info(self, order_id):
        pass


# Адаптер для перехода от старого к новому интерфейсу
class LegacyToModernAdapter(ModernOrderSystem):
    def __init__(self, legacy_system):
        self.legacy_system = legacy_system

    def get_full_order_info(self, order_id):
        basic_info = self.legacy_system.get_order_info(order_id)
        # Дополнительная логика для получения дополнительной информации из старой системы
        full_info = f"{basic_info}, Additional info from the legacy system"
        return full_info


# Клиентский код, который ожидает работу с ModernOrderSystem
def client_code(modern_system):
    return modern_system.get_full_order_info("123")


# Использование адаптера для интеграции старой системы в новый код
legacy_system = LegacyOrderSystem()
adapter = LegacyToModernAdapter(legacy_system)

result = client_code(adapter)
print(result)
