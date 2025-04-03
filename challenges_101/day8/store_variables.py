from typing import Optional

# Template expected:
# For sale: A superb semi-detached house located on Turing Street, London. 
# This house contains 3 bedrooms and 2 reception rooms and is organised across 2 floors. 
# It is for sale at £1,000,000.

def store_variables(
    streetName: Optional[str] = "Turing Street", 
    town: Optional[str] = "London", 
    typeOfHouse: Optional[str] = "semi-detached", 
    numberOfBedrooms: Optional[int] = 3, 
    numberReceptionRooms: Optional[int] = 2, 
    numberOfFloors: Optional[int] = 1, 
    price: Optional[float] = 1000000.00):

    beds = f"{numberOfBedrooms} bedrooms" if numberOfBedrooms is not None else ""
    receptions = f"{numberReceptionRooms} reception rooms" if numberReceptionRooms is not None else ""
    floors = f"is organised across {numberOfFloors} floors" if numberOfFloors is not None else ""

    contains = ""

    # if numberOfBedrooms is not None and numberReceptionRooms is not None:
    #     contains = "This house contains"
        
    print(f"""
        For sale: A superb {typeOfHouse} house located on {streetName}, {town}.
        This house contains {beds} and {receptions} and {floors}.
        It is for sale at £{price:,.2f}.
    """)



if __name__ == "__main__":
    store_variables()
