package aula11_poo;
public class Professor extends Pessoa{
    private String especialidade;
    private float salario;
    
    public void receberAumento(){
        System.out.printf(this.nome+" recebeu um aumento de 15%, passando de R$" + this.salario+ " para R$");
        System.out.println(this.salario+=this.salario*.15);       
    }

    public String getEspecialidade() {
        return especialidade;
    }

    public void setEspecialidade(String especialidade) {
        this.especialidade = especialidade;
    }

    public float getSalario() {
        return salario;
    }

    public void setSalario(float salario) {
        this.salario = salario;
    }
    
}
