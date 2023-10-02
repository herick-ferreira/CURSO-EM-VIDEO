<?php
require_once 'Pessoa.php';
class Professor extends Pessoa{
    private $especialidade;
    private $salario;
    
    public function receberAumento() {
        echo "<p>$this->nome recebeu um aumento de 25% passando de $this->salario para ".$this->salario += $this->salario *.25;
        echo "</br>";
        echo "</br>";
    }
    function getEspecialidade() {
        return $this->especialidade;
    }

    function getSalario() {
        return $this->salario;
    }

    function setEspecialidade($especialidade) {
        $this->especialidade = $especialidade;
    }

    function setSalario($salario) {
        $this->salario = $salario;
    }

}
