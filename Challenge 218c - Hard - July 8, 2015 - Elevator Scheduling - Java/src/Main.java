import java.io.BufferedReader;
import java.io.FileReader;
import java.util.*;


public class Main {

	public static void main(String[] args) {
		Elevator[] elevators = null;
		ArrayList<Passenger> passengers = new ArrayList<>();
		try{
			BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
		    String line;
		    
		    //Get Elevators
		    int numElevators = Integer.parseInt(reader.readLine());
		    String[] elevator;
		    elevators = new Elevator[numElevators];
		    for(int i = 0; i<numElevators;i++){
		    	line = reader.readLine();
		    	elevator = line.split(" ");
		    	elevators[i] = new Elevator(elevator[0],Integer.parseInt(elevator[1]),Float.parseFloat(elevator[2]),Integer.parseInt(elevator[3]));
		    }
		    
		    //Get passengers
		    int numPassengers = Integer.parseInt(reader.readLine());
		    String[] passenger;
		    for(int i = 0; i<numPassengers; i++){
		    	line = reader.readLine();
		    	passenger = line.split(" ");
		    	passengers.add(new Passenger(passenger[0],Integer.parseInt(passenger[1]),Integer.parseInt(passenger[2]),Integer.parseInt(passenger[3])));
		    }
		    
		    while ((line = reader.readLine()) != null){
		    }
		    reader.close();
		}
		catch (Exception e){
		    System.err.format("Exception occurred trying to read '%s'.", "input.txt");
		    e.printStackTrace();
		}

		long startTime = System.currentTimeMillis();
		ArrayList<Passenger> waitingPassengers = new ArrayList<>();
		boolean done = false;
		while(!done && (System.currentTimeMillis() - startTime <1100000)){
			for(Passenger passenger : passengers){
				done = true;
				long passengerTime = passenger.requestTime*1000;
				long currentTime = System.currentTimeMillis() - startTime;
				if(!passenger.arrived){
					done = false;
				}
				if(passengerTime <= currentTime){ 
					if(!passenger.arrived && !passenger.inTransit && !passenger.waiting){
						waitingPassengers.add(passenger);
						passenger.waiting = true;
					}
				}
				else{
					break;
				}
			}
			for(int i = 0; i<elevators.length;i++){
				Elevator elevator = elevators[i];
				waitingPassengers = sortPassengers(waitingPassengers,elevator);
				for(int j = 0; j<waitingPassengers.size();j++){
					Passenger passenger = waitingPassengers.get(j);
					if(elevator.direction >= 0 && passenger.direction >= 0 && !elevator.full /*&& elevator.destinationFloors.size()<12/*/){
						elevator.pickUpRequest(passenger);
						waitingPassengers.remove(passenger);
					}
				}
			}
		}
		
		System.out.println("Done");
	}
	
	public static ArrayList<Passenger> sortPassengers(ArrayList<Passenger> waitingPassengers, Elevator elevator){
		ArrayList<Passenger> orderedPassengers = new ArrayList<>();
		ArrayList<Passenger> tempList = waitingPassengers;
		while(tempList.size()>0){
			Passenger currentClosest = findClosest(tempList,elevator.currentFloor);
			tempList.remove(currentClosest);
			orderedPassengers.add(currentClosest);
		}
		return orderedPassengers;
	}
	
	public static Passenger findClosest(ArrayList<Passenger> passengers, int value){
		Passenger closest = passengers.get(0);
		int minDistance = Math.abs(closest.startFloor - value);
		for(Passenger passenger : passengers){
			int currentDistance = Math.abs(passenger.startFloor - value);
			if(currentDistance<minDistance){
				minDistance = currentDistance;
				closest = passenger;
			}
		}
		return closest;
	}
	
	   public void run() {
		   System.out.println("timer working");      
	   } 
}
