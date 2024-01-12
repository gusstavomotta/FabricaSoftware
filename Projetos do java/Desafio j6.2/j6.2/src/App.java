public class App {
    public static void main(String[] args) throws Exception {

        int matriz[][] = { { 1, 2, 3, 4, 5, 6 }, { 7, 8, 9, 10, 11, 12 }, { 13, 14, 15, 16, 17, 18 },
                { 19, 20, 21, 22, 23, 24 } };
        int maiorNum = 0;

        for (int i = 0; i < matriz.length; i++) {
            for (int k = 0; k < matriz[i].length; k++) {

                if (matriz[i][k] > maiorNum) {
                    maiorNum = matriz[i][k];
                }
                System.out.println(matriz[i][k] + " ");
            }
            System.out.println();
        }
        for (int i = 0; i < matriz.length; i++) {
            for (int k = 0; k < matriz[i].length; k++) {

                matriz[i][k] *= maiorNum;
                System.out.println(matriz[i][k]);
            }
            System.out.println();
        }

        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                matriz[i][j] = i * matriz[i].length + j + 1;

                System.out.println(matriz[i][j]);
            }
            System.out.println();
        }

    }

}