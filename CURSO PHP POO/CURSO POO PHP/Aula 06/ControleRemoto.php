<pre>
    <?php
    require_once("Controlador.php");
    class ControleRemoto implements Controlador {
         //Atributos
        private $volume;
        private $ligado;
        private $tocando;
        
        //Métodos Especiais
        
        public function __construct() {
            $this->volume = 50;
            $this->ligado = false;
            $this->tocando = false;
          }
          private function getVolume() {
              return $this->volume;
          }
          private function getLigado() {
              return $this->ligado;
          }
          private function getTocando() {
              return $this->tocando;
          }
          
          
          private function setVolume($volume){
              $this->volume= $volume;
          }
          private function setLigado($ligado){
              $this->ligado = $ligado;
          }
          private function setTocando($tocando){
              $this->tocando = $tocando;
          }
          
          
          
          
          public function abrirMenu(){
              if ($this->getLigado()){
                  echo "<p>---------- MENU ------------</p>";
              echo "<br>Está ligado? ".($this->getLigado()?"SIM":"NÃO");
              echo "<br>Está tocando?: ".($this->getTocando()?"SIM":"NÃO");
              echo "<br>Volume: ".$this->getVolume();
              for ($i=0; $i<=$this->getVolume(); $i+=10){
                  echo "|";
              }
              echo "<br/>";
              }else {
                  echo "<p>ERRO! Não Posso abrir o Menu com a TV desligada.</p>";
              }
          }
          
          public function desligar(){
              $this->setLigado(false);
              echo "<br>Desligando</br>";
          }
          public function desligarMudo(){
              if ($this->getLigado() && $this->getVolume()==0){
                  $this->setVolume(50);
              }
          }
          public function fecharMenu(){
              if ($this->getLigado()) {
                  echo "<br>Fechando Menu...";
          } else {
              echo "<p>ERRO! Não posso fechar menu com a TV desligada</p>";
              }
          }
          public function ligar(){
              $this->setLigado(true);
          }
          public function ligarMudo(){
              if ($this->getLigado() && $this->getVolume()>0){
                  $this->setVolume(0);
              }
          }
          public function maisVolume(){
              if ($this->getLigado()){
                  $this->setVolume($this->getVolume()+10);
              }else{
                  echo "<p>Erro! Não posso aumentar o volume<p/>";
              }
          }
          public function menosVolume(){
              if ($this->getLigado()){
              $this->setLigado($this->getVolume()-10);
              }else {
                  echo "<p>ERRO! Não posso diminuir o volume<p/>";
              }
          }
          public function pause(){
              if ($this->getLigado() && $this->getTocando()){
                  $this->setTocando(false);
              }
          }
          public function play(){
              if ($this->getLigado() && ! ($this->getTocando())){
                  $this->setTocando(true);
              }
          }
        }
    ?>
</pre>

 