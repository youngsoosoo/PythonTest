import java.util.*;

public class Main {
    public static boolean isPrime(int num){
        if(num < 2) return false;
        for(int i=2; i*i<=num; i++){
            if(num % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int min = sc.nextInt();
        int max = sc.nextInt();
        sc.close();

        for(int i = min; i <= max; i++){
            if(isPrime(i)){
                System.out.println(i);
            }
        }
    }
}