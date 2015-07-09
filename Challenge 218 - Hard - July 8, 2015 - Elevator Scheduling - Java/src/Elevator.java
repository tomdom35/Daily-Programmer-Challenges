import java.util.*;

public class Elevator {
	float speed;
	String name;
	int capacity;
	int currentFloor;
	ArrayList<Integer> destinationFloors = new ArrayList<>();
	int numStops = 0;
	boolean full = false;
	ArrayList<Passenger> currentPassengers = new ArrayList<>();
	ArrayList<Passenger> inRoutPassengers = new ArrayList<>();
	int direction = 0;
	Timer timer = new Timer();
	TimerTask task = new elevatorTimeTask(this);
	
	public Elevator(String name, int capacity, float speed, int currentFloor){
		this.speed = speed;
		this.name = name;
		this.capacity = capacity;
		this.currentFloor = currentFloor;
	}
	
	public void pickUpRequest(Passenger passenger){
		if(!destinationFloors.contains(passenger.startFloor)){
			destinationFloors.add(passenger.startFloor);
		}
		inRoutPassengers.add(passenger);
		System.out.println("\nPick up request from: " + passenger.name + "\n");
		if(/*direction==0*/destinationFloors.size()==1){
			move();
		}
	}
	
	public void move(){
		timer.cancel();
		timer.purge();
		if(destinationFloors.size()>0){
			if(destinationFloors.contains(currentFloor)){
				direction = 0;
				pickUp();
				dropOff();
			}
			else if(destinationFloors.get(0)>currentFloor){
				direction = 1;
				Timer timer = new Timer();
				TimerTask task = new elevatorTimeTask(this);
				timer.schedule(task, (long) ((1/speed) * 1000));
			}
			else if(destinationFloors.get(0)<currentFloor){
				direction = -1;
				Timer timer = new Timer();
				TimerTask task = new elevatorTimeTask(this);
				timer.schedule(task, (long) ((1/speed) * 1000));
			}
			/*else{
				direction = 0;
				pickUp();
				dropOff();
			}*/
		}
		else{
			System.out.println("No current destination");
		}
	}
	
	public void pickUp(){
		for(int i = 0; i<inRoutPassengers.size();i++){
			Passenger passenger = inRoutPassengers.get(i);
			if(passenger.startFloor == currentFloor){
				System.out.println("\nElevator " + name + " picked up passenger " + passenger.name + " on floor " + currentFloor + "\n");
				currentPassengers.add(passenger);
				inRoutPassengers.remove(i);
				if(destinationFloors.contains(currentFloor)){
					int index = destinationFloors.indexOf(currentFloor);
					destinationFloors.remove(index);
				}
				destinationFloors.add(passenger.endFloor);
				passenger.waiting = false;
				passenger.inTransit = true;
				full = currentPassengers.size()>=12;
			}
			//else{
				//i++;
			//}
		}
	}
	
	public void dropOff(){
		for(int i = 0; i<currentPassengers.size();i++){
			Passenger passenger = currentPassengers.get(i);
			if(passenger.endFloor == currentFloor){
				System.out.println("\nElevator " + name + " dropped off passenger " + passenger.name + " on floor " + currentFloor + "\n");
				currentPassengers.remove(i);
				passenger.arrived = true;
				passenger.inTransit = false;
				passenger.destinationFloor = currentFloor;
				if(destinationFloors.contains(currentFloor)){
					int index = destinationFloors.indexOf(currentFloor);
					destinationFloors.remove(index);
				}
				full = currentPassengers.size()>=12;
			}
			//else{
				//i++;
			//}
		}
		move();
	}
	
	public void printStats(){
		System.out.println("Name: " + name);
		System.out.println("Capacity: " + capacity);
		System.out.println("Speed: " + speed);
		System.out.println("Current Floor: " + currentFloor);
		System.out.print("Destination Floors:");
		for(int i = 0; i<numStops; i++){
			System.out.print(" "+destinationFloors.get(i));
		}
		System.out.println("\n");
	}
	
	public class elevatorTimeTask extends TimerTask{
		public Elevator elevator;
		public elevatorTimeTask(Elevator elevator){
			this.elevator = elevator;
		}
		public void run(){

			if(elevator.direction==1){
				elevator.currentFloor++;
			}
			else if(elevator.direction == -1){
				elevator.currentFloor--;
			}
			System.out.println("Elevator" + elevator.name + " is on floor: " + elevator.currentFloor);
			elevator.move();
		}
		
	}
}
