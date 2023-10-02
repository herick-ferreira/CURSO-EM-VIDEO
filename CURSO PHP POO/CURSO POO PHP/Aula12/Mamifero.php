<?php
require_once 'Animal.php';
class Mamifero extends Animal {
    private $corPelo;
    
    public function locomover(){
        echo "<p>Correndo</p>";
    }
    public function alimentar(){
        echo "<p>Mamanado</p>";
    }
    public function emitirSom(){
        echo "<p>Som de Mamífero</p>";
    }
    function getCorPelo() {
        return $this->corPelo;
    }

    function setCorPelo($corPelo) {
        $this->corPelo = $corPelo;
    }


}
