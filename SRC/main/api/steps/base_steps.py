from typing import Any, List



class BaseSteps:
    def __init__(self, created_obj: List[Any]):
        self.created_obj = created_obj
        # self.admin_steps = AdminSteps(created_obj)
        # self.user_steps = UserSteps(created_obj)

