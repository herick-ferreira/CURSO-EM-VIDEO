package aula11_poo;
public class Bolsista extends Aluno {
    private float bolsa;
    
    public void renovarBolsa(){
        System.out.println("Renovando bolsa de "+this.nome);
    }
    @Override//@Override : Sobreposição a outro método
    public void pagarMensalidade(){
        System.out.println(this.nome+" é bolsista pagamento facilitado! ");
    }

    public float getBolsa() {
        return bolsa;
    }

    public void setBolsa(float bolsa) {
        this.bolsa = bolsa;
    }
    
}
