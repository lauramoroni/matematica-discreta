import java.util.Scanner;

public class questao1 {
    public static void main(String[] args) throws Exception {
        
        Scanner sc = new Scanner(System.in);

        int n;
        double a;

        a = sc.nextInt();
        n = sc.nextInt();

        System.out.printf("Somatório: %.4f%n", somatorio(a, n));

        System.out.printf("Fórmula: %.4f", formula(a, n));

        sc.close();
    }

    public static double somatorio(double a, int n) {
        
        double somatorio = 0;

        for (int k = 1; k <= n; k++) {
            somatorio += Math.sin(Math.toRadians(k * a));
        }

        return somatorio;
    }

    public static double formula(double a, int n) {
        
        double x = a/2;

        double ans = Math.sin(Math.toRadians(n * x)) * Math.sin(Math.toRadians((n + 1) * x)) / Math.sin(Math.toRadians(x));

        return ans;
    }
}
