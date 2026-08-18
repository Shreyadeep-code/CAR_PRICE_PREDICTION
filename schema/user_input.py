from pydantic import BaseModel,Field
from typing import Annotated,Literal
from config.companies import companies

class UserInput(BaseModel):
    company:Annotated[str,Field(...,description=f"Name of Car company {','.join(companies)}")]
    name:Annotated[str,Field(...,description='car model name')]
    year:Annotated[int,Field(...,gt=1900,description=' in the year purchased')]
    kms_driven:Annotated[int,Field(...,description='kilometers the car driven')]
    fuel_type:Annotated[Literal['Petrol','Diesel','LPG'],Field(...,description='fuel_type')]
