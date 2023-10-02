/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package programaidade;

import java.util.Scanner;

/**
 *
 * @author HericK
 */
public class ProgramaIdade {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner t = new Scanner(System.in);
        System.out.print("Em que ano você nasceu?");
        int nasc = t.nextInt();
        int i = 2020 - nasc;
        System.out.println("Sua idade é "+i+" anos");
        if (i>=18){
            System.out.println("Você é Maior de Idade");
        } else {
            System.out.println("Você é Menor de Idade");
        }
    }
    
}
