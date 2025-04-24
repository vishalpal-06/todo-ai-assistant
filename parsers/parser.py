
from pydantic import BaseModel, Field, validator
from typing import Optional


# Define the output structure
class TaskIdentification(BaseModel):
    task: str = Field(description="The identified task", enum=["create_todo", "update_todo", "delete_todo", "other"])


# Model for delete_todo: Extract title
class DeleteTodoDetails(BaseModel):
    title: str = Field(description="The title of the todo to delete")


# Model for create_todo: Extract title, description, status, priority
class CreateTodoDetails(BaseModel):
    title: str = Field(description="The title of the todo")
    description: str = Field(description="The description of the todo")
    status: Optional[str] = Field(description="The status of the todo", enum=["Completed", "Pending"], default="Pending")
    priority: Optional[str] = Field(description="The priority of the todo", enum=["Low", "Medium", "High"], default="Low")


class UpdateTodoDetails(BaseModel):
    title: str = Field(description="The title of the todo", min_length=1, max_length=100)
    description: Optional[str] = Field(description="The description of the todo if mention to update", min_length=1, max_length=500, default=None)
    status: Optional[str] = Field(description="The status of the todo if mention to update", enum=["Completed", "Pending"], default=None)
    priority: Optional[str] = Field(description="The priority of the todo if mention to update", enum=["Low", "Medium", "High"], default=None)
