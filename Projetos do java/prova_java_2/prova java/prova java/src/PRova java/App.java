import java.util.ArrayList;
import java.util.Scanner;
public class App {

    public static void main(String[] args) throws Exception {


        ArrayList <Empresa> list = new ArrayList<>();
        System.out.println("Quantas empresas vamos gerar? ");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 0; i < n; i++){
            Empresa a;
            if (i%2 == 0){
                a = new Industria("1233", "dfsdaf", "unisc", Industria.EIndustria.CONSUMO);
            }
            else{
                a = new Comercio("12345", "MOttinha's", "Ramiro ramos chaves", Comercio.EComercio.ATACADO);
            }
            list.add(a);
        

        for (int j = 0; j < 3; j++){
            
            a.efetuarVenda(2,9.99);
        }
    }
        double totalGeralVendas = 0;
        double totalGeralImpostos =0;

        for (int x = 0; x < list.size(); x++){
            Empresa e = list.get(x);
            System.out.println(e);

            totalGeralVendas += e.getTotalVendas();
            totalGeralImpostos += e.getTotalImpostos();
        }
        System.out.printf("Total Geral de vendas: %.2f\n", totalGeralVendas);
        System.out.printf("Total Geral de impostos: %.2f\n", totalGeralImpostos);
    
    }
}

/* 
 * public class App {
    public static void main(String[] args) throws Exception {
    
    ArrayList < Empresa> empresas = new ArrayList<>();
   
    Comercio c2 = new Comercio("def", "Matheus", "drews", tipoComercio.ATACADO);
    Comercio c1 = new Comercio("abc", "Gustavo", "pv", tipoComercio.VAREJO);
    Industria a1 = new Industria("abc", "Gustavo", "Ramiro ramos chaves",tipoIndustria.INTERMEDIARIA);
    Industria a2 = new Industria("abc", "Gustavo", "Ramiro ramos chaves",tipoIndustria.PRODUCAO);

    empresas.add(a1);
    empresas.add(c1);
    empresas.add(c2);
    empresas.add(a2);

    for (int i = 0; i < empresas.size(); i++){

        Empresa a = empresas.get(i);
        System.out.println(a);
    }


}
}

*/
