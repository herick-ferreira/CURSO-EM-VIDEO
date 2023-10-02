package aula12_poo;
public class Aula12_POO {
    public static void main(String[] args) {
     //Classe abstrata
     //Animal a = new Animal();
     
     Mamifero m = new Mamifero();
     Reptil r = new Reptil();
     Peixe p = new Peixe();
     Ave a = new Ave();
     
     Canguru c = new Canguru();
     Cachorro k = new Cachorro();
     Cobra co = new Cobra();
     Tartaruga t = new Tartaruga();
     GoldFish g = new GoldFish();
     Arara ar = new Arara();
     /*m.setPeso(35.3f);
     m.setCorPelo("Marrom");
     m.alimentar();
     m.locomover();
     m.emitirSom();*/
     
     /*a.locomover();
     p.locomover();
     r.locomover();*/
     
     c.locomover();
     k.emitirSom();
     k.enterrarOsso();
    }
    
}
