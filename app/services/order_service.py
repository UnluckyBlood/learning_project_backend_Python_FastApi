from sqlalchemy.orm import Session
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate, OrderPatch

# схемы управления бдшкой, передача данных бдшке коммит перезапуск бдшки, получение снова таблиц

# Получение списка заказов
def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Order).offset(skip).limit(limit).all()
# Получить какой-то конкретный заказ
def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()
# Создать заказ 
def create_order(db: Session, order: OrderCreate):
    db_order = Order(**order.model_dump()) #преобразует модель в словарь
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
# Полное обновлоение заказа
def update_order(db: Session, order_id: int, order_update: OrderUpdate):
    db_order = get_order(db, order_id)
    if not db_order:
        return None
    for key, value in order_update.model_dump().items():
        setattr(db_order, key, value)
    db.commit()
    db.refresh(db_order)
    return db_order
# часть какую-то обновляем 
def patch_order(db: Session, order_id: int, order_patch: OrderPatch):
    db_order = get_order(db, order_id)
    if not db_order:
        return None
    update_data = order_patch.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_order, key, value)
    db.commit()
    db.refresh(db_order)
    return db_order
# Удаление заказа
def delete_order(db: Session, order_id: int):
    db_order = get_order(db, order_id)
    if not db_order:
        return False
    db.delete(db_order)
    db.commit()
    return True
