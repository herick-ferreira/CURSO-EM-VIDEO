/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exerciciorepita;

import javax.swing.JOptionPane;

/**
 *
 * @author HericK
 */
public class ExercicioRepita {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int n = 0;
        int s = 0;
        int cp = 0;
        int ci = 0;
        int mc = 0;
        int cont = 0;
        int m = 0;
        do {
            n = Integer.parseInt(JOptionPane.showInputDialog(null, 
                  "<html>Informe um Número: <br><em>(valor 0 interrompe)</em></html> "));
            s+=n;
            cont+=1;
            if (n%2==0){
                cp += 1;
            }else {
                ci +=1;
            }if (n>100){
                mc += 1;
            }
        } while(n != 0);
        m = s/(cont-1);
        JOptionPane.showMessageDialog(null, "<html>Resultado final <hr>"+
                "<br>Total de valores: " + (cont-1) +"</html>"
                        + "\nTotal de Pares: " + (cp-1)
                        +"\nTotal de Ímpares: " + (ci)
                        +"\nAcima de 100: " + (mc)
                        +"\nMédia de valores: " + (m));
    }
}