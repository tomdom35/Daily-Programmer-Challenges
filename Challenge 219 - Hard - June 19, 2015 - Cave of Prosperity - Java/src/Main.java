

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.FileReader;
import java.io.BufferedReader;

public class Main {

	public static void main(String[] args) {
		String path = "C:\\Users\\1020071\\Desktop\\info.txt";
		float[] nuggets = null;
		float backpackSize = 0;
		FileReader fr;
		BufferedReader br;
		try {
			fr = new FileReader(path);
			br = new BufferedReader(fr);
			try {
				backpackSize = Float.valueOf(br.readLine());
				nuggets = new float[Integer.valueOf(br.readLine())];
				for(int i = 0;i<nuggets.length;i++){
					nuggets[i] = Float.valueOf(br.readLine());
				}
				runWithAverage(nuggets,backpackSize);
			} catch (NumberFormatException e){
				e.printStackTrace();
			} catch (IOException e){
				e.printStackTrace();
			}
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		if(backpackSize != 0 && nuggets != null){
			
		}
	}
	
	public static void runWithAverage(float[] nuggets, float backpackSize){
		float total = sum(nuggets);
		float average = 0;
		float[] backpackContents = new float[0];
		float[] distanceFromAverage = new float[0];
		float[] invalidEntries = new float[0];
		displayContents(nuggets);
		System.out.println();
		System.out.println("Back Pack Size: " + backpackSize);
		System.out.println("Total: " + total);
		average = (total/nuggets.length);
		System.out.println("Average: " + average);
		distanceFromAverage = distanceFromAverage(nuggets, average);
		System.out.println();
		for(int i = 0; i<nuggets.length && sum(backpackContents)<backpackSize;i++){
			if(findMinIndex(distanceFromAverage,invalidEntries,nuggets)!=-1){
				float nugget = nuggets[findMinIndex(distanceFromAverage,invalidEntries,nuggets)];
				if(sum(backpackContents) + nugget<=backpackSize){
					backpackContents = add(backpackContents,nugget);
				}
				invalidEntries = add(invalidEntries,nugget);
			}
		}
		displayContents(backpackContents);
		System.out.println();
		System.out.println(sum(backpackContents));
	}
	
	public static float[] add(float[] list, float newItem){
		float[] newList = new float[list.length+1];
		for(int i = 0; i<list.length;i++){
			newList[i] = list[i];
		}
		newList[list.length] = newItem;
		return newList;
	}
	
	public static float[] distanceFromAverage(float[] list, float average){
		float[] newList = new float[list.length];
		for(int i=0;i<list.length;i++){
			newList[i] = Math.abs(list[i] - average);
		}
		return newList;
	}
	
	public static int findMinIndex(float[] list, float[] backpackContents, float[] nuggets){
		int minIndex = 0;
		boolean found = false;
		for(int i=0;i<list.length;i++){
			if(list[i]<=list[minIndex] && !contains(backpackContents, nuggets[i])){
				minIndex = i;
				found=true;
			}
		}
		if(found){
			return minIndex;
		}
		else
			return -1;
	}
	
	public static float sum(float[] list){
		float total = 0;
		for(int i=1;i<list.length;i++){
			total+=list[i];
		}
		return total;
	}
	
	public static boolean contains(float[] list, float index){
		for(int i = 0; i<list.length;i++){
			if(list[i] == index){
				return true;
			}
		}
		return false;
	}
	
	public static void displayContents(float[] list){
		for(int i=0;i<list.length;i++){
			System.out.println(list[i]);
		}
	}
}