<?php
require_once 'Pessoa.php';
/*Final*/class Aluno extends Pessoa{
    //Final não deixa essa classe ser herdada
    private $matricula;
    private $curso;
    
    public /*Final*/function pagarMensalidade() {
        //Final não deixa ser sobreposto
        echo "<p>Pagando Mensalidade do aluno </p>".$this->nome;
    }
    function getMatricula() {
        return $this->matricula;
    }

    function getCurso() {
        return $this->curso;
    }

    function setMatricula($matricula) {
        $this->matricula = $matricula;
    }

    function setCurso($curso) {
        $this->curso = $curso;
    }


}
