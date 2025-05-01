import java.io.*;

public class Main{
    static int check(String word, char c){
        for(int i = 0; i<word.length(); i++){
            if(word.charAt(i)==c)
                return i;
        }
        return -1;
    }
    public static void main(String[]args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String word = br.readLine();
        int[] characters = new int[26];
        for(int i = 0; i<26;i++){
            System.out.print(check(word, (char)(i+97))+" ");
        }
        
    }
}