package aula14_e_aula_15_poo_projetoyoutube;
public class Aula14_e_Aula_15_POO_ProjetoYoutube {
    public static void main(String[] args) {
        Video v[] = new Video[3];
        v[0] = new Video("Aula 1 de POO");
        v[1] = new Video("Aula 12 de PHP");
        v[2] = new Video("Aula 10 de HTML 5");
        
        //Classe Abstrata
        //Pessoa p = new Pessoa("Jubileu", 22, "M");
        
        Gafanhoto g[] = new Gafanhoto[2];
        g[0] = new Gafanhoto("Jubileu", 22, "M", "Juba");
        g[1] = new Gafanhoto("Creuza", 12, "F", "creuzita");
        
        
        //System.out.println(g[0].toString());
        //System.out.println(v[0].toString());
        
        Visualizacao vis[] = new Visualizacao[5];
        vis[0] = new Visualizacao(g[0], v[2]);//Jubileu assisti HTML 5
        vis[0].avaliar();
        System.out.println(vis[0].toString());
        
        vis[1] = new Visualizacao(g[0], v[1]);//Jubileu assisti PHP
        vis[0].avaliar(87.0f);
        System.out.println(vis[0].toString());
    }
    
}
