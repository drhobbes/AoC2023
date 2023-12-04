import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.io.File;
import java.io.IOException;

public class day1 {
  
  public static ArrayList<String> words = new ArrayList<String>(Arrays.asList(
      "zero","one","two","three","four","five","six","seven","eight","nine"));
  
  private static int[] getFirstWord(String line) {
    int minInd = line.length();
    int value = -1;
    
    for (int i=0; i<words.size(); i++) {
      int index = line.indexOf(words.get(i));
      if (index != -1 && index < minInd) {
        value = i;
        minInd = index;
      }
    }
    return new int[] {value, minInd};
  }
  
  private static int[] getFirstDigit(String line) {
    int index = 0;
    while (index < line.length() && !Character.isDigit(line.charAt(index))) {
      index++;
    }
    if (index == line.length()) return new int[] {-1,-1}; //  not sure if this will happen
    return new int[] {line.charAt(index)-'0', index};
  }
  
  private static int[] getLastWord(String line) {
    int maxInd = -1;
    int value = -1;
    
    for (int i=0; i<words.size(); i++) {
      int index = line.lastIndexOf(words.get(i));
      if (index != -1 && index > maxInd) {
        value = i;
        maxInd = index;
      }
    }
    return new int[] {value, maxInd};
  }
  
  private static int[] getLastDigit(String line) {
    int index = line.length()-1;
    while (index >= 0 && !Character.isDigit(line.charAt(index))) {
      index--;
    }
    if (index < 0) return new int[] {-1, -1};
    return new int[] {line.charAt(index)-'0', index};
  }
  
  public static void main(String[] args) throws IOException{
    int total = 0;
    
    Scanner in = new Scanner(new File("input.txt"));
    while (in.hasNextLine()) {
      String line = in.nextLine();
    
      int[] digit = getFirstDigit(line); // [value, index]
      int[] word = getFirstWord(line);
      int firstDigit = 10;
      if (digit[0] == -1 && word[0] == -1) firstDigit = 0;
      else if (digit[0] == -1) firstDigit *= word[0];
      else if (word[0] == -1) firstDigit *= digit[0];
      else firstDigit *= (digit[1] < word[1]) ? digit[0] : word[0];
      
      digit = getLastDigit(line);
      word = getLastWord(line);
      int lastDigit = 1;
      if (digit[0] == -1 && word[0] == -1) lastDigit = 0;
      else if (digit[0] == -1) lastDigit *= word[0];
      else if (word[0] == -1) lastDigit *= digit[0];
      else lastDigit *= (digit[1] > word[1]) ? digit[0] : word[0];
      
      total += firstDigit + lastDigit;
      
      System.out.println(line+": "+(firstDigit+lastDigit));
    }
    in.close();
    
    System.out.println(total);
  }

}
