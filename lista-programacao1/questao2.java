import java.util.Scanner;

public class questao2 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int n;

        n = sc.nextInt();

        System.out.printf("Resultado: %.2f", permutacoesCaoticas(n));

        sc.close();
    }

    public static double permutacoesCaoticas(int n) {

        double somatorio = 0;

        for (int k = 0; k <= n; k++) {
            somatorio += Math.pow(-1, k) / fatorial(k);
        }

        return fatorial(n) * somatorio;
    }

    public static int fatorial(int x) {

        if (x == 0) {
            return 1;
        }

        return x * fatorial(x - 1); // Utilizando função recurisva para calcular o fatorial
    }
}
