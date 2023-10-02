package aula11_poo;
public /*final*/class Aluno extends Pessoa {
    //final indica que a classe é a última não podendo ter herdeiros(extends)
    private int matricula;
    private String curso;
    
    public /*final*/void pagarMensalidade(){
        //final indica que não pode haver sobreposição
        System.out.println("Pagando mensalidade de aluno "+this.nome);
    }

    public int getMatricula() {
        return matricula;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

    public String getCurso() {
        return curso;
    }

    public void setCurso(String curso) {
        this.curso = curso;
    }
}
