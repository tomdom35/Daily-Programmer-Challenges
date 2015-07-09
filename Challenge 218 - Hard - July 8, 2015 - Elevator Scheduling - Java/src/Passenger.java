
public class Passenger {
	String name;
	int requestTime;
	int startFloor;
	int endFloor;
	boolean waiting = false;
	int direction;
	boolean inTransit = false;
	boolean arrived = false;
	int destinationFloor = 0;
	
	public Passenger(String name, int requestTime, int startFloor, int endFloor){
		this.name = name;
		this.requestTime = requestTime;
		this.startFloor = startFloor;
		this.endFloor = endFloor;
		if(endFloor>startFloor){
			this.direction = 1;
		}
		else if(startFloor>endFloor){
			this.direction = -1;
		}
		else{
			this.direction = 0;
		}
	}
	
	public void printStats(){
		System.out.println("Name: " + name);
		System.out.println("Request Time: " + requestTime);
		System.out.println("Start Floor: " + startFloor);
		System.out.println("End Floor: " + endFloor + "\n");
	}
}
