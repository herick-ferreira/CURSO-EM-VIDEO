package aula11_poo;
public class Aula11_POO {
    public static void main(String[] args) {
       //Classe abstrata só pode ser usada para heranças e não objetos
        //Pessoa p1 = new Pessoa();
       
        //Herança Pobre herda tudo não tem nada próprio
        /*Visitante v1 = new Visitante();
        v1.setNome("Juvenal");
        v1.setIdade(22);
        v1.setSexo("M");
        System.out.println(v1.toString());*/
        
        /*Aluno a1 = new Aluno();
        a1.setNome("Cláudio");
        a1.setMatricula(11111);
        a1.setCurso("Informática");
        a1.setIdade(16);
        a1.setSexo("M");
        a1.pagarMensalidade();
        
        Bolsista b1 = new Bolsista();
        b1.setMatricula(1112);
        b1.setNome("Jubileu");
        b1.setBolsa(12.5f);
        b1.setSexo("M");
        b1.pagarMensalidade();*/
        
        Tecnico t1 = new Tecnico();
        t1.setNome("Godofredo");
        t1.setIdade(21);
        t1.setCurso("TI");
        t1.setRegistroProfissional(11111);
        t1.praticar();
        
        Professor p1 = new Professor();
        p1.setNome("Rodinei");
        p1.setSalario(3222);
        p1.setEspecialidade("IA");
        System.out.println(p1);
        p1.receberAumento();
    }
    
}
