/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package vetor02;

import java.util.Scanner;

/**
 *
 * @author HericK
 */
public class Vetor02 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner teclado = new Scanner(System.in);
        System.out.print("Ano atual: ");
        int ano = teclado.nextInt();
        if (ano%4==0 && ano%100!=0 || ano%400==0){
            System.out.println("O ano de "+ano+" é \033[0;31mBISSEXTO\033[m");
            System.out.println(" ");
            String mes[] = {"Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"};
            int tot[] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
            for (int c = 0; c < mes.length; c++) {
                System.out.println("O mês de " + mes[c] + " tem " + tot[c] + " dias ao todo");
            }
        } else {
            System.out.println("O ano de "+ano+" NÃO é \033[0;31mBISSEXTO\033[m");
            System.out.println(" ");
            String mes[] = {"Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"};
            int tot[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
            for (int c = 0; c < mes.length; c++) {
                System.out.println("O mês de " + mes[c] + " tem " + tot[c] + " dias ao todo");
        }
    }

}
}