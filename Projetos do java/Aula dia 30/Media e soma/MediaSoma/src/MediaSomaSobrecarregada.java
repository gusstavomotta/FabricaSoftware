//EXERCÍCIOS JAVA / J4.6, J4.7
//GUSTAVO OLIVEIRA DA MOTTA
//DATA DE MODIFICAÇÃO: 30/03/2023

package media;

public class MediaSomaSobrecarregada {
    public static int soma(int a, int b){
        return a+b;
    }
    public static int soma(int a, int b, int c){
        return a+b+c;
    }     
    public static int soma(int a, int b, int c, int d){
        return a+b+c+d;
    }       
    public static int soma(int a, int b, int c, int d, int e){
        return a+b+c+d+e;
    }  
    
    public static double soma(double a, double b){
        return a+b;
    }
    public static double soma(double a, double b, double c){
        return a+b+c;
    }     
    public static double soma(double a, double b, double c, double d){
        return a+b+c+d;
    }       
    public static double soma(double a, double b, double c, double d, double e){
        return a+b+c+d+e;
    }
    
    public static int media(int a, int b){
        return a+b;
    }
    public static int media(int a, int b, int c){
        return a+b+c;
    }     
    public static int media(int a, int b, int c, int d){
        return a+b+c+d;
    }       
    public static int media(int a, int b, int c, int d, int e){
        return a+b+c+d+e;
    }  
    
    public static double media(double a, double b){
        return (a+b)/2;
    }
    public static double media(double a, double b, double c){
        return (a+b+c)/3;
    }     
    public static double media(double a, double b, double c, double d){
        return (a+b+c+d)/4;
    }       
    public static double media(double a, double b, double c, double d, double e){
        return (a+b+c+d+e)/5;
    }       
}
