from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from decimal import Decimal
from typing import Optional

class OrderBase(BaseModel):
    customer_name: str = Field(..., min_length=2, max_length=100)
    product_name: str = Field(..., min_length=1, max_length=200)
    quantity: int = Field(..., gt=0)
    total_price: Decimal = Field(..., gt=0)
    status: str = Field(default="pending", pattern="^(pending|processing|completed|cancelled)$")
class OrderCreate(OrderBase):
    pass #так как идёт полное насследование атрибутов
class OrderUpdate(OrderBase):
    pass

class OrderPatch(BaseModel):
    customer_name: Optional[str] = Field(None, min_length=2, max_length=100)
    product_name: Optional[str] = Field(None, min_length=1, max_length=200)
    quantity: Optional[int] = Field(None, gt=0)
    total_price: Optional[Decimal] = Field(None, gr=0)
    status: Optional[str] = Field(None, pattern="^(pending|processing|completed|cancelled)$")

class OrderResponse(OrderBase):
    id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)