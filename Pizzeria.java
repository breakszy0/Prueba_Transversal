//Programa principal main
package pizzeria;

public class Pizzeria {

    public static void main(String[] args) {
        System.out.println("Bienvenido");
        System.out.println("Bienenido 2");
        
        //instanciar a la clase, para crear un objeto
        //NombeClase + nombreObjeto = new Nombreclase
        Pizza pizza1 = new Pizza("pepperoni","grande","gruesa");
        Pizza pizza2 = new Pizza("vegetariana","familiar","delgada");
        
        //Obtener el dato con get
        String nombreGet = pizza1.getNombre();
        System.out.println("El nombre de la pizza es: " + nombreGet);
        
        String nombreGet2 = pizza2.getNombre();
        System.out.println("El nombre de la pizza es: " + nombreGet2);
        
        
        //setear cualquier dato del objeto SET
        pizza1.setMasa(" Extra queso");
        // Almacenamos el dato cambiado en una variable
        String masaSet = pizza1.getMasa();
        //Imprimimos el dato seteado
            System.out.println("Ahora el tipo de masa es " + masaSet);
            
        
        
        
    }
    
}
