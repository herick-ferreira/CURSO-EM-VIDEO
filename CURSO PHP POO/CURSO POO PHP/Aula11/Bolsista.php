<?php
require_once 'Aluno.php';
class Bolsista extends Aluno{
    private $bolsa;
    
    public function renovarBolsa() {
        echo "<p>Bolsa Renovada</p>";
    }
    
    public function pagarMensalidade() {
        echo "<p>$this->nome é bolsista! Então paga com desconto!</p>".$this->nome;
    }
    
    function getBolsa() {
        return $this->bolsa;
    }

    function setBolsa($bolsa) {
        $this->bolsa = $bolsa;
    }


}
