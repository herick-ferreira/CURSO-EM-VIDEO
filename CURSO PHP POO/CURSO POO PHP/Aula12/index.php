<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Aula 12</title>
    </head>
    <body>
        <?php
        require_once 'Animal.php';
        require_once 'Mamifero.php';
        require_once 'Reptil.php';
        require_once 'Peixe.php';
        require_once 'Ave.php';
        require_once 'Cachorro.php';
        require_once 'Canguru.php';
        require_once 'Cobra.php';
        require_once 'Tartaruga.php';
        require_once 'GoldFish.php';
        require_once 'Arara.php';
        
        $m = new Mamifero();
        $a = new Ave();
        $r = new Reptil();
        $c = new Canguru();
        $k = new Cachorro();
        $t = new Tartaruga();
        
        /*$m->setPeso(33.5);
        $m->locomover();
        $a->locomover();
        $r->locomover();
        $c->locomover();
        $k->locomover();
        $t->locomover();*/
        
        $k->emitirSom();
        $m->emitirSom();
        
        $k->abanarRabo();
        
        
        
        ?>
    </body>
</html>
