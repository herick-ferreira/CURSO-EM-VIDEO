package aula11_poo;
public class Tecnico extends Aluno {
    private int registroProfissional;
    
    public void praticar(){
        System.out.println(this.nome+" irá praticar "+this.getCurso());
    }

    public int getRegistroProfissional() {
        return registroProfissional;
    }

    public void setRegistroProfissional(int registroProfissional) {
        this.registroProfissional = registroProfissional;
    }
    
}
