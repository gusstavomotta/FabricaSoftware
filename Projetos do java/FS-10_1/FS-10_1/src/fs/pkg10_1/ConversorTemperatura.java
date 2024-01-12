
package fs.pkg10_1;

/**
 *
 * @author supti
 */
public class ConversorTemperatura {
    private float tempC;   
    
    /**
     * Inicializar o conversor com a temperatura em º Célcius
     * @param tempC 
     */
    public ConversorTemperatura(float tempC){
        this.tempC = tempC;
    }
    
    public float converter(String escala){
        return converter(Escala.valueOf(escala.toUpperCase()));
    }
    
    public float converter(Escala escala){
        switch (escala) {
            case CELCIUS:
                return tempC;
            case FAHRENHEIT:
                return 1.8f * tempC + 32;
            default://KELVIN
                return tempC + 273;
        }
    }

    @Override
    public String toString() {
        return super.toString() +  "\nConversorTemperatura{" + "tempC=" + tempC + '}';
    }
    
    
    
}
