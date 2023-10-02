function clicou(){
          let pan = Number(window.prompt('Qual era o preço anterior do produto?'))
          
          let pat = Number(window.prompt('Qual é o preço atual do produto?'))
          
          
          let panR = pan.toLocaleString('pt-BR', {style: 'currency',currency:'BRL'})
          
          let patR = pat.toLocaleString('pt-BR', {style: 'currency',currency:'BRL'})
          
          res.innerHTML = '<h2><strong>Analisando os valores informados</strong></h2>'
          
          res.innerHTML += `O produto custava ${panR} e agora custa ${patR}.<br>`
          
          if (pan > pat){
              let valor = pan - pat
          
              let valorR = valor.toLocaleString('pt-BR', {style: 'currency',currency:'BRL'})
              
              let vari = ((pat/pan)-1)*-100
              
              
              res.innerHTML += `Hoje o produto está mais barato <br> O produto diminuiu ${valorR} em relação ao preço anterior.<br>Uma variação de ${vari.toFixed(1)}% para baixo.`
            } else if (pan < pat){
              let valor = (pan - pat)*-1
          
              let valorR = valor.toLocaleString('pt-BR', {style: 'currency',currency:'BRL'})
              
              let vari = (((pat/pan)-1) * 100)
              
              
              res.innerHTML += `Hoje o produto está mais caro <br> O produto aumentou ${valorR} em relação ao preço anterior.<br>Uma variação de ${vari.toFixed(1)}% para cima.`
              
          } else {
              res.innerHTML += `O produto permanece o mesmo valor.`
        }
          
}
        
        
