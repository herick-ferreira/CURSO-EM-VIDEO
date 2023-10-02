package aula04;
public class Aula04 {
    public static void main(String[] args) {
        Caneta c1 = new Caneta("BIC", "Amarela", 0.4f);
        c1.status();
        System.out.println(" ");
        Caneta c2 = new Caneta("Faber Castell", "Roxa", 0.8f);
        c2.status();
        /*c1.setModelo("BIC");
        c1.setPonta(.5f);
        //c1.status();
        System.out.println("Tenho uma caneta " + c1.getModelo() + " de ponta " + c1.getPonta());*/
    }
    
}
