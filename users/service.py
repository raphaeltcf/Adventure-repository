from typing import Any, Dict, List, Optional, Union
from users.models import User, Address

class UserService:
    def list_users(self) -> List[User]:
        return User.objects.all().order_by('-created_at')
    
    def get_user(self, user_id: str) -> User:
        return User.objects.get(id=user_id)
    
    def create_user(self, user_data: Dict[str, Any]) -> User:
        return User.objects.create(**user_data)
    
    def update_user(self, user_id: str, user_data: Dict[str, Any]) -> User:
        user = self.get_user(user_id)
        for key, value in user_data.items():
            setattr(user, key, value)
        user.save()
        return user
    
    def delete_user(self, user_id: str) -> None:
        user = self.get_user(user_id)
        user.delete()
        return user
    
   