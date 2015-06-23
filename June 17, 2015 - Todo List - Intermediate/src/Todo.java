import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class Todo {
	
	public static void main(String[] args) {
		CompleteList list = new CompleteList();
		list.addCatagory("Names");
		list.addItem("Tommy", "Names");
		list.addItem("Ben", "Names");
		list.addItem("Joe", "Names");
		list.addCatagory("Colors");
		list.addItem("Red", "Colors");
		list.addItem("Green", "Colors");
		list.addItem("Blue", "Colors");
		list.addItem("Yellow", "Colors");
		list.viewList();
		list.deleteItem("Ben");
		list.deleteItem("Blue");
		list.deleteItem("asfd");
		list.viewList();
		list.addItem("Dog", "Animals");
		list.updateItem("Tommy", "Tom");
		list.addItem("Cat", "Animals");
		list.viewCatagory("Animals");
	}
}
class CompleteList{
	ArrayList<List> list = new ArrayList<List>();
    Scanner sc = new Scanner(System.in);
    String response = "";
	public void addItem(String item, String subList){
		boolean found = false;
		for(Iterator<List> it = list.iterator();it.hasNext();){
			List curList = it.next();
			if(curList.name == subList){
				found = true;
				if(curList.exists(item)){
					System.out.println("'" +item+ "' already exists in the list. No modifications have been made.");
				}
				else{
					curList.addItem(item);
					System.out.println(item +" has been added to " + subList);
				}
			}
		}
		if(!found){
			do{
				System.out.println("The catagory '"+ subList + "' does not exist, woud you like to create it? (Y/N): ");
			     response = sc.next();
			     if(response.equalsIgnoreCase("y")){
			    	 this.addCatagory(subList);
			    	 this.addItem(item, subList);
			     }
			     else if(response.equalsIgnoreCase("n")){
			    	 System.out.println("No new entry as been added to the list");
			     }
		     }while(response.equalsIgnoreCase("n") && response.equalsIgnoreCase("y"));
		}
	}
	
	public void deleteItem(String item){
		boolean removed = false;
		for(Iterator<List> it = list.iterator();it.hasNext() && !removed;){
			if(it.next().deleteItem(item)){
				removed = true;
				System.out.println(item +" has been removed from the list");
			}	
		}
		if(!removed){
			System.out.println("No such item exists");
		}
	}
	
	public void addCatagory(String catagory){
		list.add(new List(catagory));
	}
	
	public void updateItem(String originalStr, String newStr){
		boolean found = false;
		for(Iterator<List> it = list.iterator();it.hasNext() && !found;){
			if(it.next().updateItem(originalStr, newStr)!=-1){
				found = true;
				System.out.println("'" + originalStr + "' has been changed to '" + newStr + "'");
			}
		}
		if(!found){
			System.out.println("'"+originalStr+"'"+" does not exist in the list. No modifications have been made.");
		}
	}
	
	public void viewList(){
		for(Iterator<List> it = list.iterator();it.hasNext();){
			it.next().viewList();
		}
	}
	
	public void viewCatagory(String subList){
		boolean found = false;
		for(Iterator<List> it = list.iterator();it.hasNext() && !found;){
			List curList = it.next();
			if(curList.name.equalsIgnoreCase(subList)){
				curList.viewList();
				found = true;
			}
		}
		if(!found){
			System.out.println("The catagory '" + subList + "' does not exist.");
		}
	}
}

class List{
	ArrayList<String> list = new ArrayList<String>();
	String name;
	
	public List(String name){
		this.name = name;
	}
	
	public boolean addItem(String item){
		return list.add(item);
	}
	
	public boolean deleteItem(String item){
		return list.remove(item);
	}
	
	public boolean contains(String item){
		return list.contains(item);
	}
	
	public int updateItem(String originalStr, String newStr){
		int index = list.indexOf(originalStr);
		if(index != -1){
			list.set(index, newStr);
		}
		return index;
	}
	
	public boolean exists(String item){
		if(list.indexOf(item)!=-1){
			return true;
		}
		else return false;
	}
	
	public void viewList(){
		System.out.println("==="+name.toUpperCase()+"===");
		for (Iterator<String> it = list.iterator();it.hasNext();){
			System.out.println(it.next());
		}
		System.out.println();
	}
}