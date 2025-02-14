class App:
    minimal_sum_of_delivery = 400

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def logError(self, message):
        print(message)

    def logWarning(self, message):
        print(message)

    def run(self):
        pass

    # desctination distance - calculated in km
    def define_cost_by_distance(self, destination_distance, fragile):
        cost = 0
        max_distance = 30
        if (destination_distance > max_distance) and not(fragile) :
            cost += 300
        elif destination_distance > 10 and destination_distance <= max_distance :
            cost += 200
        elif destination_distance > 2 and destination_distance <= 10:
            cost += 100
        elif destination_distance <= 2 and destination_distance >= 0:
            cost += 50
        elif fragile:
            self.logError(f"Fragile items can not travel more than {max_distance} km!")
        else:
            self.logError("Incorrect destination_distance value: " + destination_distance) 
        return cost
    
    def define_cost_by_volume(self, big: bool):
        if big:
            return 200
        else:
            return 100
        
    def define_fragility(self, fragile: bool):
        if fragile:
            return 300
        else:
            return 0
        
    def multiply_by_delivery_business(self, cost, business: str):
        if business == "very high":
            return cost * 1.6
        elif business == "high":
            return cost * 1.4
        elif business == "close to high":
            return cost * 1.2
        else:
            return cost
        
    def make_cost_to_be_greater_than_minimal(self, cost):
        if cost < 400:
            return 400
        else:
            return cost

    def calculate_cost_of_delivery(
            self,
            destination_distance,
            parcel_volume,
            parcel_fragility,
            delivery_business: str
                                   ):
        cost = 0
        cost += self.define_cost_by_distance(destination_distance, parcel_fragility)
        cost += self.define_cost_by_volume(parcel_volume)
        print(cost)
        cost += self.define_fragility(parcel_fragility)
        print(cost)

        cost = self.multiply_by_delivery_business(cost, delivery_business)
        print(cost)
        cost = self.make_cost_to_be_greater_than_minimal(cost)
        return cost



if __name__=="__main__":
    app = App()
    import sys
    # destination_distance, parcel_volume, parcel_fragility, delivery_business = sys.argv
    
    cost = 0
    if len(sys.argv) != 5:
        print("Please provide system args: destination_distance  parcel_volume  parcel_fragility  delivery_business")
        print("delivery_business can be: very high, high, close to high, or normal")
        print(sys.argv)
    else:
        destination_distance = float(sys.argv[1])
        parcel_volume = bool(sys.argv[2])
        parcel_fragility = bool(sys.argv[3])
        delivery_business = str(sys.argv[4])
        cost = app.calculate_cost_of_delivery(
            destination_distance=destination_distance,
            parcel_volume=parcel_volume,
            parcel_fragility=parcel_fragility,
            delivery_business=delivery_business
            )
        print("The cost is: " + str(cost))