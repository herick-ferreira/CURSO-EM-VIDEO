package aula12_poo;
public class Peixe extends Animal{
   private String corEscama; 

    @Override
    public void locomover() {
        System.out.println("Nadando");
    }

    @Override
    public void alimentar() {
        System.out.println("Comendo Substâncias");
    }

    @Override
    public void emitirSom() {
        System.out.println("Peixe não faz Som");
    }
    
    public void soltarBolha(){
        System.out.println("Soutou uma Bolha°°°°°0000");
    }

    public String getCorEscama() {
        return corEscama;
    }

    public void setCorEscama(String corEscama) {
        this.corEscama = corEscama;
    }
    
}
