package aula12_poo;
public class Cachorro extends Mamifero {
    @Override
    public void emitirSom() {
        System.out.println("Latido");
    }
    public void enterrarOsso(){
        System.out.println("Enterrando Osso");
    }
    public void abanarRabo(){
        System.out.println("Abanando o Rabo");
    }
}
