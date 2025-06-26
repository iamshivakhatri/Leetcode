class ParkingSpot:
  def __init__(self, spot_number, spot_type):
    self.spot_number = spot_number
    self.spot_type = spot_type
    self.occupied = False
    self.vehicle = None
  
  def assign(self, vehicle:vehicle):
    self.occupied = True 
    self.vehicle = vehicle
  
  def release(self):
    self.occupied = False
    self.vehicle = None

class ParkingLot:
  def __init__(self):
    self.spots:Dict[int, ParkingLot] = {}
    self.available:Dict[str, List[int]] = {
      "car":[],
      "bike":[],
      "truck":[]
    }
    self.tickets:Dict[str,ParkingSpot] = {}
    
    def add_spot(self, spot_number:int, spot_type:str):
      spot = ParkingSpot(spot_number, spot_type)
      self.spots[spot_number] = spot 
      if spot_type in self.available:
        heapq.heappush(self.available[spot_type],spot_number)
    
    def park(self, vehicle:Vehicle) -> Optional[str]:
      heap = self.available.get(vehicle.vehicle_type)
      while heap:
        spot_number = heapq.heappop(heap)
        spot = self.spots[spot_number]
        spot.assign(vehicle)
        ticket_id = str(uuid.uuid4())
        self.tickets[ticket_id] = spot 
        return ticket_id 
        
    def unpark(self, ticket_id:str) -> bool:
      spot = self.spots.get(ticket_id)
      if not spot: 
        return False 
      spot.release()
      spot_number = spot.spot_number
      spot_type = spot.spot_type
      heapq.heappush(self.available[spot_type], spot_number)
      return True
        
      
      
      
      

